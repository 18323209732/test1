import re

import pytest
import requests
def test_token():
    #获取Token
    corpid = "wwdbf78b1014ed2f3b"
    corpsecret = 'iqlhZWi7pbDSfTd0gOP0NfV0iwkGf9VLCfINw-5JhIg'
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
    return res.json()['access_token']
    # 'YsK_E4zAnI8gEVJPCIZtANERigognp4WSx4LSTVl1b7aVpKy4mrviI_q3q1eQnKMmVH - cJkjmwR - 5
    # WzCN8737Oy9DFjuu - icYN - Qw285QLBb3PvGT5GHinNJqdfoo5C4_qwtl - G1cEGB5ZizTc1OcLC0EJX9RADK1jjQSDEym_i2dayKcSRsYHd64EP9y7MhPp - 8
    # ME_eJ2g0OEGMNMtBRw'

def test_get(userid):
    #获取成员信息
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token()}&userid={userid}')
    return res.json()

def test_create(userid,name,mobile):
    #创建成员
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department":[1]
    }
    res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token()}',json=data)
    return res.json()

def test_update(userid,name,mobile):
    #更新成员信息
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "position": "哈麻皮测试工程师",
        "address": "哈麻皮市哈麻皮区哈麻皮人"
    }
    res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token()}',json=data)
    return res.json()

def test_delete(userid):
    #删除成员
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token()}&userid={userid}')
    return res.json()

# def test_create_department():
#     #创建新部门
#     data = {
#         "name": "易强欢乐中心",
#         "parentid": 1,
#     }
#     res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_token()}',json=data)
#     print(res.json())
#
# def test_get_department():
#     #获取部门信息
#     id = 2
#     res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_token()}&id={id}')
#     print(res.json())
#
# def test_update_department():
#     #更新部门信息
#     data = {
#         "id": 2,
#         "name": "易二麻子装傻中心",
#         "name_en": "yqsz",
#         "parentid": 1,
#         "order": 1
#     }
#     res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_token()}",json=data)
#     print(res.json())
#
# def test_delete_department():
#     #删除部门
#     id = 2
#     res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_token()}&id={id}')
#     print(res.json())

@pytest.mark.parametrize("userid,name,mobile",[("zhangsan123456","小白","13815201548")])
def test_all(userid,name,mobile):
    try:
        #可能发生创建失败
        assert "created" == test_create(userid,name,mobile)["errmsg"]
    except AssertionError as e:
        if "mobile existed" in e.__str__():
            re_userid = re.findall(":(.*)'$",e.__str__())[0]
            assert 'deleted' == test_delete(re_userid)['errmsg']
            assert 60111 == test_get(re_userid)['errcode']
            assert "created" == test_create(userid, name, mobile)["errmsg"]

    # 可能出现userid不存在的异常
    assert name == test_get(userid)['name']
    assert "updated" == test_update(userid,'xxxxxx',mobile)["errmsg"]
    assert 'xxxxxx' == test_get(userid)['name']
    assert 'deleted' == test_delete(userid)['errmsg']
    assert 60111 == test_get(userid)['errcode']