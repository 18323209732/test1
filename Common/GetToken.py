import sqlite3
import sys
import re
import win32crypt
import os
import json
import base64
import sqlite3
from win32crypt import CryptUnprotectData
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import winreg, os
import time
from Common.ReadWriteIni import ReadWrite
from Common.ReadYaml import ConfigYaml
from Common.Login import Login


class Get_Cookies:
    def __init__(self):
        '''
        '''
        self.browser_type = ConfigYaml('browserName').base_config
        self.over_time = ConfigYaml('over_time').base_config
        self.host = ConfigYaml('website').base_config
        self.key = ConfigYaml('key').base_config
        self.local_state = os.environ['LOCALAPPDATA'] + r'\Google\Chrome\User Data\Local State'
        self.cookie_path = os.environ['LOCALAPPDATA'] + r"\Google\Chrome\User Data\Default\Cookies"
        self.sql = ConfigYaml('search_cookies').sql % self.host
        self.current_time = int(time.time())


    def get_path(self, main_value, sub_value):
        '''

        :param main_value:
        :param sub_value:
        :return:
        '''
        try:
            self.key = winreg.OpenKey(main_value, sub_value)
        except FileNotFoundError:
            return '未安装相关浏览器'
        value, data = winreg.QueryValueEx(self.key, "")
        full_file_name = value.split(',')[0]
        dir_name, file_name = os.path.split(full_file_name)
        return dir_name

    def get_browser(self):
        '''
        :return:
        '''
        if self.browser_type == 'chrome':
            browser_ico = "SOFTWARE\\Clients\\StartMenuInternet\\Google Chrome\\DefaultIcon"
        elif self.browser_type == 'ie':
            browser_ico = "SOFTWARE\\Clients\\StartMenuInternet\\IEXPLORE.EXE\\DefaultIcon"
        elif self.browser_type == 'firefox':
            browser_ico = "SOFTWARE\\Clients\\StartMenuInternet\\FIREFOX.EXE\\DefaultIcon"
        else:
            browser_ico = "SOFTWARE\\Clients\\StartMenuInternet\\360Chrome\\DefaultIcon"

        return self.get_path(winreg.HKEY_LOCAL_MACHINE, browser_ico)

    def get_string(self, local_state):
        '''

        :param local_state:
        :return:
        '''
        with open(local_state, 'r', encoding='utf-8') as f:
            content = json.load(f)['os_crypt']['encrypted_key']
        return content

    def pull_the_key(self, base64_encrypted_key):
        '''

        :param base64_encrypted_key:
        :return:
        '''
        encrypted_key_with_header = base64.b64decode(base64_encrypted_key)
        encrypted_key = encrypted_key_with_header[5:]
        key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
        return key

    def decrypt_string(self, key, data):
        '''

        :param key:
        :param data:
        :return:
        '''
        nonce, cipherbytes = data[3:15], data[15:]
        aesgcm = AESGCM(key)
        plainbytes = aesgcm.decrypt(nonce, cipherbytes, None)
        plaintext = plainbytes.decode('utf-8')
        return plaintext

    def get_cookie_from_chrome(self):
        '''

        :return:
        '''
        with sqlite3.connect(self.cookie_path) as conn:
            cursor = conn.cursor()
            res = cursor.execute(self.sql).fetchall()
            cursor.close()
            cookies = {}
            key = self.pull_the_key(self.get_string(self.local_state))
            for host_key, encrypted_value in res:
                if encrypted_value[0:3] == b'v10':
                    cookies[host_key] = self.decrypt_string(key, encrypted_value)
                else:
                    cookies[host_key] = CryptUnprotectData(encrypted_value)[1].decode()

            return cookies

    def write_cookies(self):
        '''
        :return:
        '''
        value = ReadWrite(time_sign='times', time_option="time").read_ini_time()
        session = self.cookies_value = ReadWrite(sign='session', option='cookies').read_ini_cookies()
        if session:
            authen = session.split("=")[1]
            if authen == "none":
                result = False
            else:
                result = True
        else:
            result = False
        if value and result:
            over_time = int(value) + int(self.over_time)
            if over_time < self.current_time:
                cookie = Login().get_cookie()
                ReadWrite(sign="session", option='cookies',
                          value=cookie,
                          time_sign='times', time_option='time',
                          time_value=str(self.current_time)).write_ini()
        else:
            cookie = Login().get_cookie()
            ReadWrite(sign="session", option='cookies',
                      value=cookie,
                      time_sign='times', time_option='time',
                      time_value=str(self.current_time)).write_ini()


# Get_Cookies().write_cookies()