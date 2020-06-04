# -*- coding: utf-8 -*-

import execjs

def get_js():
    # f = open("./../js/my.js", 'r', encoding='utf-8') # 打开JS文件
    f = open(r"D:\Portal_interface\Common\get_token.js", 'r', encoding='utf-8') # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr+line
        line = f.readline()
    return htmlstr

def get_des_psswd():
    js_str = get_js()
    ctx = execjs.compile(js_str,cwd=r'D:\nodes\node_modules') #加载JS文件
    return (ctx.call('get_token'))  #调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数

