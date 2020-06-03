# -*- coding: utf-8 -*-

import execjs

def get_js():
    # f = open("./../js/my.js", 'r', encoding='utf-8') # 打开JS文件
    f = open("tongchengJS.js", 'r', encoding='utf-8') # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr+line
        line = f.readline()
    return htmlstr


def get_des_psswd(e):
    js_str = get_js()
    ctx = execjs.compile(js_str) #加载JS文件
    return (ctx.call('antitoken', e))  #调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数


if __name__ == '__main__':
    print(get_des_psswd(e='1570243707293'))