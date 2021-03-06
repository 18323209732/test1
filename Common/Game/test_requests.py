import random
import re

import pytest
import requests
from filelock import FileLock


@pytest.fixture(scope="session")
def test_token():
    #获取Token
    while FileLock("session.lock"):
        corpid = "wwdbf78b1014ed2f3b"
        corpsecret = 'iqlhZWi7pbDSfTd0gOP0NfV0iwkGf9VLCfINw-5JhIg'
        res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
    print("get_token")
    return res.json()['access_token']
    # 'YsK_E4zAnI8gEVJPCIZtANERigognp4WSx4LSTVl1b7aVpKy4mrviI_q3q1eQnKMmVH - cJkjmwR - 5
    # WzCN8737Oy9DFjuu - icYN - Qw285QLBb3PvGT5GHinNJqdfoo5C4_qwtl - G1cEGB5ZizTc1OcLC0EJX9RADK1jjQSDEym_i2dayKcSRsYHd64EP9y7MhPp - 8
    # ME_eJ2g0OEGMNMtBRw'

def test_get(userid,test_token):
    #获取成员信息
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token}&userid={userid}')
    return res.json()

def test_create(userid,name,mobile,test_token):
    #创建成员
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department":[1]
    }
    res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token}',json=data)
    return res.json()

def test_update(userid,name,mobile,test_token):
    #更新成员信息
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "position": "哈麻皮测试工程师",
        "address": "哈麻皮市哈麻皮区哈麻皮人"
    }
    res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token}',json=data)
    return res.json()

def test_delete(userid,test_token):
    #删除成员
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid={userid}')
    return res.json()

# def test_create_department(test_token,name,parentid):
#     #创建新部门
#     data = {
#         "name": name,
#         "parentid": parentid,
#     }
#     res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_token}',json=data)
#     print(res.json())
#
# def test_get_department(id,test_token):
#     #获取部门信息
#     res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_token}&id={id}')
#     print(res.json())
#
# def test_update_department(test_token,id,name,name_en,parentid)
#     #更新部门信息
#     data = {
#         "id": id,
#         "name": name,
#         "name_en": name_en,
#         "parentid": parentid,
#     }
#     res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_token}",json=data)
#     print(res.json())
#
# def test_delete_department(id,test_token):
#     #删除部门
#     res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_token}&id={id}')
#     print(res.json())
#
# def test_create_data():
#     data = [("wu123fff" + str(x),"zhangsan","138%08d" % x) for x in range(10)]
#     #print(data)
#     return data

def test_data_department():
    pass

@pytest.mark.parametrize("userid,name,mobile",test_create_data())
def test_all(userid,name,mobile,test_token):
    try:
        #可能发生创建失败
        assert "created" == test_create(userid,name,mobile,test_token)["errmsg"]
    except AssertionError as e:
        if "mobile existed" in e.__str__():
            #如果手机号被使用了，找出使用手机号的 userid 进行删除
            re_userid = re.findall(":(.*)'$",e.__str__())[0]
            if re_userid.endswith("'") or re_userid.endswith('"'):
                re_userid = re_userid[:-1]
            assert 'deleted' == test_delete(re_userid,test_token)['errmsg']
            assert 60111 == test_get(re_userid,test_token)['errcode']
            assert "created" == test_create(userid, name, mobile,test_token)["errmsg"]

    # 可能出现userid不存在的异常
    assert name == test_get(userid,test_token)['name']
    assert "updated" == test_update(userid,'xxxxxx',mobile,test_token)["errmsg"]
    assert 'xxxxxx' == test_get(userid,test_token)['name']
    assert 'deleted' == test_delete(userid,test_token)['errmsg']
    assert 60111 == test_get(userid,test_token)['errcode']
# @pytest.mark.parametrize("id,name,name_en,parentid",test_data_department())
# def test_all_department(id,name,name_en,parentid):
#     try:
#         assert "created" == test_create_department(test_token,name,parentid)["errmsg"]
#     except AssertionError as e:
#         if "name existed" in e.__str__():
#             re_userid = re.findall(":(.*)'$",e.__str__())[0]
#     assert name ==test_get_department(id,test_token)['name']
#     assert name_en ==test_update_department(test_token,id,name,name_en,parentid)
#     assert "deleted" == test_delete_department(id,test_token)['errmsg']
#     assert 60111 == test_get_department(id,test_token)['errcode']