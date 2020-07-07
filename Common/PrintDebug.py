from datetime import *
import sys,os

def print_debug_info(o):
    """
    打印打印日期，文件名，行，函数名的方法
    :param o:
    :return:
    """
    try:
        raise Exception
    except :
        f = sys.exc_info()[2].tb_frame.f_back
    print('%s -- %s -- %d -- %s ' % (str(datetime.now()), os.path.basename(f.f_code.co_filename), f.f_lineno, f.f_code.co_name), end='')
    print(o)