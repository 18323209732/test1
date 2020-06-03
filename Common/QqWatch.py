import io
import urllib
from ctypes import windll
from urllib.request import urlopen
import PIL
import itchat
import win32con
import win32clipboard
import win32gui
import win32api
import traceback
from PIL import Image
from io import StringIO
from ctypes import *
from Common.ReadYaml import ConfigYaml
from time import sleep
from Common.Route import Any_Path
import os
import requests,json
from Common.FontColor import outcome


class QQ():
    def __init__(self,name,picture,msg):
        '''
        :param name: 窗口句柄名称
        '''
        self.name = name
        self.win = win32clipboard
        self.gwin = win32gui
        self.apiwin = win32api
        self.cwin = win32con
        self.user32 = windll.user32
        self.kernel32 = windll.kernel32
        self.picture = picture
        self.msg = msg
        self.QQ = ConfigYaml('QQ').base_config
        self.chat = ConfigYaml('chat').base_config

    def write_picture(self):
        '''
        将图片数据写入剪切板
        :return:
        '''
        self.win.OpenClipboard()
        try:
            self.win.EmptyClipboard()
            self.win.SetClipboardData(win32con.CF_BITMAP, self.picture)
        except:
            traceback.print_exc()
        finally:
            self.win.CloseClipboard()

    def write_text(self):
        '''
        写入文本数据到剪切板
        :param data:
        :return:
        '''

        self.user32.OpenClipboard(c_int(0))
        self.win.EmptyClipboard()
        alloc = self.kernel32.GlobalAlloc(0x2000, len(bytes(self.msg, encoding='gbk')) + 1)
        lock = self.kernel32.GlobalLock(alloc)
        cdll.msvcrt.strcpy(c_char_p(lock), bytes(self.msg, encoding='gbk'))
        self.kernel32.GlobalUnlock(alloc)
        self.user32.SetClipboardData(c_int(1), alloc)
        self.user32.CloseClipboard()

    def send_picture(self):
        '''
        :param image:
        :return:
        '''
        image = PIL.Image.open(("Img",self.picture)).convert("RGB")
        filename = self.picture.split(".")[0]+'.bmp'
        image.save(Any_Path("Img",filename))
        self.picture = windll.user32.LoadImageW(0, Any_Path("Img",filename), win32con.IMAGE_BITMAP, 0, 0, win32con.LR_LOADFROMFILE)
        self.write_picture()
        sleep(0.5)
        self.send_data()

    def clear(self):
        '''
        清空剪切板
        :return:
        '''
        self.user32.OpenClipboard(c_int(0))
        self.user32.EmptyClipboard()
        self.user32.CloseClipboard()


    def send_text(self):
        '''
        :return:
        '''
        sleep(0.5)
        window = self.gwin.FindWindow(None, self.name)
        if window > 0:
            self.gwin.SendMessage(window, 258, 22, 2080193)
            self.gwin.SendMessage(window, 770, 0, 0)
            self.gwin.SendMessage(window, self.cwin.WM_KEYDOWN, self.cwin.VK_RETURN, 0)
            self.gwin.SendMessage(window, self.cwin.WM_KEYUP, self.cwin.VK_RETURN, 0)
        else:
            print("请开启qq消息窗口")
            return False

    def send_data(self):
        '''
        发送文本信息
        :param msg:
        :return:
        '''
        try:
            window = self.gwin.FindWindow(None, self.name)  # 获取窗口句柄
            self.gwin.ShowWindow(window, self.cwin.SW_RESTORE)
            self.gwin.SetActiveWindow(window)
            self.gwin.SetForegroundWindow(window)
            rect = self.gwin.GetWindowRect(window)  # 获取窗口位置
            x = (rect[0] + rect[2]) / 2
            y = rect[3] - 50
            self.apiwin.SetCursorPos((int(x), int(y)))
            self.apiwin.mouse_event(0x0002, 0, 0, 0, 0)
            self.apiwin.mouse_event(0x0004, 0, 0, 0, 0)
            self.apiwin.keybd_event(self.cwin.VK_CONTROL, 0, 0, 0)
            self.apiwin.keybd_event(86, 0, 0, 0)
            self.apiwin.keybd_event(86, 0, self.cwin.KEYEVENTF_KEYUP, 0)
            self.apiwin.keybd_event(self.cwin.VK_CONTROL, 0, self.cwin.KEYEVENTF_KEYUP, 0)
            self.apiwin.keybd_event(13, 0, 0, 0)
            self.apiwin.keybd_event(13, 0, self.cwin.KEYEVENTF_KEYUP, 0)
        except Exception as info:
            print(info)

    def del_file(self):
        file_path = Any_Path("Img","")
        files = os.listdir(file_path)
        if len(files) > 4:
            for i in files:
                os.remove(Any_Path("Img",i))

    def send_qq_chat(self):
        self.write_text()
        if self.QQ:
            self.send_text()
        if self.chat:
            self.send_data()
        self.send_picture()
        self.del_file()


class Send_Wechat(object):

    def __init__(self):
        '''
        发送企业微信消息内容
        '''
        self.corp_id = ConfigYaml('corpid').wechat
        self.wechat_url = ConfigYaml('wechat_url').wechat
        self.token_url = ConfigYaml('access_token_url').wechat
        self.corp_secret = ConfigYaml('corpsecret').wechat
        self.toparty = ConfigYaml('toparty').wechat
        self.touser = ConfigYaml('touser').wechat
        self.agentid = ConfigYaml('agentid').wechat

    def get_access_token(self):
        '''
        获取企业微信登录token
        :return:
        '''
        params={'corpid': self.corp_id,
        'corpsecret': self.corp_secret}
        r = requests.get(url=self.wechat_url,params=params)
        if r.json().get('errcode') == 0:
            return r.json().get('access_token')
        else:
            return False

    def send_msg(self):
        '''
        发送文字消息内容
        :return:
        '''
        access_token = self.get_access_token()
        datas = {
            "toparty": self.toparty,
            "touser": self.touser,
            "agentid": self.agentid,
            "msgtype": "text",
            "text": {"content": ""},
        }
        data = json.dumps(datas, ensure_ascii=False).encode('utf-8')
        if access_token:
            r = requests.post(url=self.token_url.format(access_token),data=data)
            if r.json().get("errcode") == 0:
                outcome('green','企业微信消息发送成功....!')
            else:
                outcome('red', '企业微信消息发送失败....!')

    def send_picture(self, title, descrip, report, picurl):
        '''
        发送文字消息内容
        :return:
        '''
        access_token = self.get_access_token()
        header = {"accept":"application/json"}
        datas = {
           "touser": self.touser,
           "toparty": self.toparty,
           "msgtype": "news",
           "agentid": self.agentid,
           "news": {
               "articles": [
                   {
                       "title": title,
                       "description": descrip,
                       "url": report,
                       "picurl": picurl,
                   },
                ]
           }
        }
        data = json.dumps(datas, ensure_ascii=False).encode('utf-8')
        if access_token:
            r = requests.post(url=self.token_url.format(access_token), data=data, headers=header,stream=True)
            if r.json().get("errcode") == 0:
                outcome('green','企业微信消息发送成功....!')
            else:
                outcome('red', '企业微信消息发送失败....!')







if __name__ == '__main__':
    pass


