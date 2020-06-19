# -*- coding: utf-8 -*-
# author：baoshan
# 带参数的类装饰器（和不带参数的类装饰器有很大的不同）
# 类装饰器的实现，必须实现__call__和__init__两个内置函数。
# __init__：不再接收被装饰函数，而是接收传入参数；
# __call__：接收被装饰函数，实现装饰逻辑


class logger(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("[{level}]: the function {func}() is running...".format(level=self.level, func=func.__name__))
            func(*args, **kwargs)
        return wrapper


@logger(level="WARNING")
def say(something):
    print("say {}!".format(something))


say("hello")

