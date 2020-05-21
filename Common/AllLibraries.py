import re
from random import choice
from Common.FontColor import outcome


def Get_Regular(string,style,index=-1):
    '''
    获取任意数据，一个或者多个
    :param string: 传入字符串
    :param style: 匹配字符
    :param index:  取值条件，-1：全部，0:随机取值，任意正整数：取第几个值，0表示取第一个,以此类推
    :return:
    '''
    global all_data

    if string:
        newstr = str(string).replace("'", '"').replace(' ', '')
        all_data = re.findall(f'\"{style}\":\"(.*?)\"', newstr)

    if index == -1:
        value = all_data

    elif index == 0:
        value = choice(all_data)

    else:
        if index <= len(all_data):
            value = all_data[index]
        else:
            raise IndexError("你的取值已经超出列表范围....")

    return value


