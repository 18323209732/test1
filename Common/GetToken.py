import sqlite3
import sys
import re
import win32crypt

def getCookie(path,sql):
    '''
    获取token方法
    :return:
    '''
    # path = r'C:\Users\lenovo\AppData\Local\Google\Chrome\User Data\Default\Cookies'
    # sql = "select name ,encrypted_value from cookies WHERE host_key='1807050057.pre-pool1-site.make.yun300.cn'"
    conn = sqlite3.connect(path)
    data = {}
    cookie = ''
    for row in conn.execute(sql):
        if row[0] == "JSESSIONID" or row[0] == "_T" or row[0] == "bfp" or row[0] == "xag":
            value = row[1]
            ret = win32crypt.CryptUnprotectData(value)
            data[row[0]] = str(ret[1])[1:].replace("'","")
    for key,value in data.items():
        cookie+="{}={};".format(key,value)
    return cookie
