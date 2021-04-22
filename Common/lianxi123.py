#def method(a,b,c):
    #print(a)
    #b.append(a)
    #return b
    #print(a)
    #print(b)
   # print(c)
#method()
#print(method(1))
#print(method(2))
#dic1 = {"a":1,"b":2,"c":3}
#method(**dic1)
#y = lambda x,y,z:x+y+z
#print(y(1,2,3))
#list_biao = []
#list_biao.append(1)
#print(list_biao)
#a = [1,2,3]
#tuple_lianxi = (1,2,a)
#a[0] = "a"
#print(tuple_lianxi)
#print(tuple_lianxi.count(2))
#print(tuple_lianxi.index(2))
#a = {1}
#b = set()
#print(len(b))
#print(type(a))
#print(type(b))
#a = {1,2,3}
#b = {1,4,5}
#print(a.union(b))
#print(a.intersection(b))
#print(a.difference(b))
#a.add("a")
#print(a)
#a = "ewuhifhuifgiuergfuirgeuig"
#print(set(a))
#lianxi_dict1 = {"a":1,"b":2}
#lianxi_dict2 = dict(a=1,b=2)
#print(lianxi_dict1,lianxi_dict2)
#print(lianxi_dict1.keys())
#print(lianxi_dict1.values())
#lianxi_dict1.pop("a")
#print(lianxi_dict2.popitem())
#print(lianxi_dict2)
#lianxi_dict1 = lianxi_dict2.fromkeys((1,2,3),"a")
#print(lianxi_dict1)
#print({i: i ** 2 for i in range(1, 4)})
import _thread
import sys
import threading
import time
import json
#print(sys.argv)
#time.sleep(3)
#print("exit")
#name = 'yqsz'
#str = "my name is %s , my age is %d"%(name,20)
#print(str)
#print("pi = %.2f"%3.1415926)
#name1 = "tom"
#name = "jerry"
#print("two boy is {} and {}".format(name,name1))
#dic = {"name":"tom","age":"20"}
#print("this is boy {name} today {age}".format(**dic))
#name = "yqsz"
#print(f"my name is {name}")
#f = open(r'C:\Users\Administrator\AppData\Local\Programs\Python\Python38\Portal_interface\Common\text_File','rt')
#print(f.readlines())
#print(f.readable())
#f.close()
#with open(r'C:\Users\Administrator\AppData\Local\Programs\Python\Python38\Portal_interface\Common\text_File','rt') as f:
    #print(f.read())
    #while True:
        #line = f.readline()
       # if line :
           # print(line)
       # else:
           # break
# info = [{
#     "name":"tom",
#     "gender":"sale",
#     "other":None
# },
#     {
#     "name":"jerry",
#     "gender":"sale",
#     "other":None
#     }
# ]
# date = json.dumps(info,sort_keys=True,indent=4)
#print(date)
#print(type(date))
#json.dump(info,open(r'C:\Users\Administrator\AppData\Local\Programs\Python\Python38\Portal_interface\Common\json_dump','w'))
# try:
#     num1 = int(input("请输入一个除数:"))
#     num2 = int(input("请输入一个被除数:"))
#     print(num2/num1)
# except:
#     print("这是个异常！")
# #else:
#    # print("程序未发生异常！")
# finally:
#     print("无论发不发生异常都会执行！")
# x = 10
# if x > 5:
#     #raise Exception("抛出一个异常！")
#     print("神经病呀")
# class MyException(Exception):
#     def __init__(self,value1,value2):
#         self.value1 = value1
#         self.value2 = value2
# raise MyException("value1","value2")
# class Person():
#     name = "1111"
#     def get_name(self):
#         return self.name
# print(Person.name)
# p = Person()
# print(p.name)
# print(p.get_name())
# #p.name = "yqsz"
# p.name = "yqsz123"
# Person.name = "yqsz"
# print(p.name)
# p1 = Person()
# print(p1.name)
# class Person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def set_att(self,value):
#         self.value = value
#
#     def eat(self):
#         print(f"name : {self.name},age : {self.age},gender : {self.gender}   我在吃")
#
#     def drink(self):
#         print(f"name : {self.name},age : {self.age},gender : {self.gender}   我在喝")
#
#     def run(self):
#         print(f"name : {self.name},age : {self.age},gender : {self.gender}   我在跑")
#
# xiaoming = Person("xiaoming",10,"male")
# xiaohong = Person("xiaohong",15,"female")
# print(xiaoming.name)
# print(xiaoming.run())
# xiaoming.set_att("fit")
# print(xiaoming.value)

# class Game:
#
#     def __init__(self,hp,power):
#         self.hp = hp
#         self.power = power
#
#     def fight(self,enemy_hp,enemy_power):
#         final_hp = self.hp - enemy_power
#         enemy_final_hp = enemy_hp - self.power
#         if final_hp > enemy_final_hp:
#             print("我赢了！")
#         elif final_hp < enemy_final_hp:
#             print("敌人赢了！")
#         else:
#             print("平局")

# game = Game(1000,500)
# # game.fight(500,1000)

# class HouYi(Game):
#     ##如果在子类重新定义了_init__，那么父类的_init_将会被覆盖
#     def __init__(self):
#         super().__init__(1000,200)
#         self.defence = 100
#
#     def houyi_fight(self, enemy_hp, enemy_power):
#         final_hp = self.hp + self.defence - enemy_power
#         enemy_final_hp = enemy_hp - self.power
#         if final_hp > enemy_final_hp:
#             print("我赢了！")
#         elif final_hp < enemy_final_hp:
#             print("敌人赢了！")
#         else:
#             print("平局")
#
# hp = 1000
# power = 300
# houyi = HouYi()
# houyi.houyi_fight(hp,power)
import os
#os.mkdir("test")

# print(os.listdir("./"))
# #os.removedirs("test")
# print(os.getcwd())
#
# print(os.path.exists("b"))
#
# if not os.path.exists("b"):
#     os.mkdir("b")
# if not os.path.exists("b/test.txt"):
#     f = open("b/test.txt","w")
#     f.write("hello , os using")
#     f.close()

import time

# print(time.asctime())
#
# print(time.time())
#
# print(time.localtime())
#
# p = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
#
# print(p)

# now_timestamp = time.time()
# two_day_before = now_timestamp - 60*60*24*2
# time_tuple = time.localtime(two_day_before)
# print(time.strftime("%Y-%m-%d %H:%M:%S",time_tuple))

import urllib.request

# response = urllib.request.urlopen("https://www.baidu.com")
# print(response.status)
# print(response.read())
# print(response.headers)

import math

# print(math.ceil(10.1))
# print(math.floor(20.2))
# print(math.sqrt(9))

import logging
from time import sleep,ctime

from HTMLTestRunner import HTMLTestRunner

logging.basicConfig(level=logging.INFO)

loops  = [2,4]

# def loop(nloop,nsec,lock):
#     logging.info("start loop" +str(nloop)+ "at"+ ctime())
#     sleep(nsec)
#     logging.info("start loop"+str(nloop)+"at"+ ctime())
#     lock.release()

# def loop0():
#     logging.info("start loop0 at"+ ctime())
#     sleep(4)
#     logging.info("end loop0 at" + ctime())
#
# def loop1():
#     logging.info("start loop1 at"+ ctime())
#     sleep(2)
#     logging.info("end loop1 at" + ctime())

# def main():
#     logging.info("start all at"+ ctime())
#     locks = []
#     nloops  = range(len(loops))
#     for i in nloops:
#         lock = _thread.allocate_lock()
#         lock.acquire()
#         locks.append(lock)
#
#     for i  in nloops:
#         _thread.start_new_thread(loop,(i,loops[i],locks[i]))
#
#     for i in nloops:
#         while locks[i].locked():pass
#     # _thread.start_new_thread(loop0,())
#     # _thread.start_new_thread(loop1,())
#     #sleep(6)
#     logging.info("end all at"+ ctime())

# class MyThread(threading.Thread()):
#     def __init__(self,func,args,name = ''):
#         threading.Thread.__init__(self)
#         self.func = func
#         self.args = args
#         self.name = name
#
#     def run(self):
#         self.func(*self.args)
#
# def loop(nloop,nsec):
#     logging.info("start loop" +str(nloop)+ "at"+ ctime())
#     sleep(nsec)
#     logging.info("start loop"+str(nloop)+"at"+ ctime())
#
# def main():
#     logging.info("start all at"+ ctime())
#     threads = []
#     nloops  = range(len(loops))
#
#     for i  in nloops:
#         t = threading.Thread(target=loop,args=(i, loops[i]))
#         threads.append(t)
#
#     for i in nloops:
#         threads[i].start()
#
#     for i in nloops:
#         threads[i].join()
#
#     logging.info("end all at" + ctime())
#
# if  __name__ == "__main__":
#     main()
import requests

#r = requests.get("https://www.baidu.com")
# r = requests.post("https://www.baidu.com",data={"key":"value"})
# print(r.text)
# import yaml
# print(yaml.dump({'a':[1,2]}))
import unittest
from HTMLTestRunner_PY3.HTMLTestRunner_PY3 import HTMLTestRunner

# class demo(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print("setup class")
#     @classmethod
#     def tearDownClass(cls):
#         print("teardown class")
#
#     def setUp(self):
#         print("setUp")
#
#     def tearDown(self):
#         print("tearDown")
#
#     def test_case01(self):
#         print("testcase01")
#         self.assertEqual(2,2,"判断相等")
#         self.assertNotIn("q","this")
#
#     def test_case02(self):
#         print("testcase02")
#         self.assertEqual(2, 2, "判断相等")
#         self.assertNotIn("q", "this")
#
#     @unittest.skipIf(1+1==2,"跳过这条用例")
#     def test_case03(self):
#         print("testcase03")
#         self.assertEqual(2, 2, "判断相等")
#         self.assertNotIn("q", "this")
#
# class demo1(unittest.TestCase):
#
#     def test_case01(self):
#         print("testcase01")
#         self.assertEqual(2,2,"判断相等")
#         self.assertNotIn("q","this")
#
#     def test_case02(self):
#         print("testcase02")
#         self.assertEqual(2, 2, "判断相等")
#         self.assertNotIn("q", "this")


# if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(demo("test_case01"))
    # unittest.TextTestRunner().run(suite)
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    # suite = unittest.TestSuite([suite1,suite2])
    # unittest.TextTestRunner().run(suite)

    # report_title = "Example用例执行报告"
    # desc = "用于展示修改样式后的HTMLTestRunner"
    # report_file = "./ExampleReeport.html"
    # discover = unittest.defaultTestLoader.discover("./","lianxi*.py")
    # # unittest.TextTestRunner().run(discover)
    #
    # with open(report_file,"wb") as report:
    #     runner = HTMLTestRunner(stream = report,title = report_title,description = desc)
    #     runner.run(discover)

import pytest
# def func(x):
#     return x + 1
# def test_answer():
#     assert func(3) == 5
# def test_one():
#     print("开始执行test_one方法")
#     x = "this"
#     assert "h" in x
#
# def test_two():
#     print("开始执行test_two方法")
#     x = "hello"
#     assert "e" in x
#
# def test_three():
#     print("开始执行test_three方法")
#     a = "hello"
#     b = "hello word"
# #     assert a in b
# @pytest.fixture()
# def login():
#     print("这是一个登陆方法")
#
# def test_case1(login):
#     print("test_case1,需要登陆")
#     pass
#
# def test_case2():
#     print("test_case2，不需要登陆")
#     pass
#
# def test_case3(login):
#     print("test_case3,需要登陆")
#     pass
#
# if __name__ == '__main__':
#     pytest.main()
# @pytest.fixture(scope="module")
# def open_brower():
#     print("\n打开浏览器，打开百度首页")
#
#     yield
#
#     print('执行teardown')
#     print('最后关闭浏览器')
# @pytest.mark.parametrize("x",[1,2])
# @pytest.mark.parametrize("y",[8,10,11])
# def test_foo(x,y):
#     print(f"测试数据组合x:{x},y:{y}")
# test_user_data = ["Tome","Jerry"]
# @pytest.fixture(scope="module")
# def login_r(request):
#     user = request.param
#     print(f"\n 打开首页准备登陆, 登陆用户:{user}")
#     return user
#
# @pytest.mark.parametrize("login_r",test_user_data,indirect=True)
# def test_login(login_r):
#     a = login_r
#     print(f"测试用例中login的返回值:{a}")
#     assert a != ""

@pytest.mark.search
def test_search1():
    print("test_search1")
    raise NameError
    pass

@pytest.mark.search
def test_search2():
    print("test_search2")
    pass

@pytest.mark.search
def test_search3():
    print("test_search3")
    pass

@pytest.mark.login
def test_login1():
    print("test_login1")
    pass

@pytest.mark.login
def test_login2():
    print("test_login2")
    pass

if __name__ == '__main__':
    pytest.main()