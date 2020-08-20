
# coding=utf-8
import configparser
import urllib3
import traceback
import os,requests
import requests.packages.urllib3
from Common.FontColor import outcome
import yaml
from ruamel.yaml import RoundTripDumper
from Common.Route import Any_Path
from Common.ReadYaml import ReadPublic, ConfigYaml
from urllib3 import encode_multipart_formdata
from Door.companyFile import Public
projectName = ConfigYaml("projectName").base_config
Url = ConfigYaml(projectName).base_url



def readyaml(file=None, key=None):
    """
    1. 获取文件当前路劲+文件名称
    2. 打开yaml文件
    3. 转译文件内容获取对应key的值
    """
    path = Any_Path(file, "Public.yaml")

    try:
        with open(path, 'r', encoding='utf-8') as f:
            # yaml.warnings({'YAMLLoadWarning': False})
            value = yaml.load(f.read(), Loader=yaml.Loader)[key]
        return value
    except:
        pass


def readyaml_case(key=None):
    """
    1. 获取case.yaml的橱窗列表
    2. 转译文件内容获取对应test03_keywords_listShowcase的URL值
    """
    path = Any_Path("Door", "Case.yaml")

    try:
        with open(path, 'r', encoding='utf-8') as f:
            # yaml.warnings({'YAMLLoadWarning': False})
            # value = yaml.load(f.read(), Loader=yaml.Loader)[key]
            value = yaml.load(f.read())['Door']['listShowcase'][0]['funName'][0]['test03_keywords_listShowcase']['url']

        return value
    except:
        pass


def writeyaml(w_key=None, w_value=None, n=None, file=None):
    """
    1. 打开当前文件下的yaml文件，n传入写入方法（a 为追加方式写入，w 为清空后重写）
    2. 传入要写入的key：value
    3. 转译文件，传入参数，去重｛｝，方便yaml直接读取数据
    """
    path = Any_Path(file, "Public.yaml")
    with open(path, n, encoding="utf-8") as yaml_file:
        data = {w_key: w_value}
        if int(yaml.__version__[0]) >= 5:
            # yaml.warnings({'YAMLLoadWarning': False})
            yaml.dump(data, yaml_file, allow_unicode=True)
        else:
            yaml.dump(data, yaml_file, Dumper=RoundTripDumper, allow_unicode=True)


def readconfig_yaml(basekey='base_url', key='Door'):
    path = Any_Path("Config", "Config.yaml")
    # print(path)
    with open(path, 'r', encoding='utf-8') as f:
        # yaml.warnings({'YAMLLoadWarning': False})
        value = yaml.load(f.read(), Loader=yaml.Loader)[basekey][key]
    return value


def readconfig_ini(v=True):
    path = Any_Path("Door", "Config.ini")
    config = configparser.ConfigParser()
    config.read(path)
    cookies_value = config.get("session", "cookies")
    headers1 = {'Content-Type': 'application/json;charset=UTF-8'}
    headers2 = {'Content-Type': 'application/x-www-form-urlencoded'}
    headers3 = {'Content-Type': 'multipart/form-data'}
    headers4 = {}
    if v==True:
        headers1.update({'Cookie': cookies_value})
        return headers1
    elif v==3:
        headers3 = {'Cookie': cookies_value}
        return headers3
    elif v==4:
        headers4 = {'Cookie': cookies_value}
        return headers4
    else:
        headers2.update({'Cookie': cookies_value})
        return headers2


class GetAll:
    def __init__(self):
        self.tenant_value = readconfig_yaml(basekey='base_config', key='tenant_value')
        #self.headers = readconfig_ini()

    def add_Cate(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        """
        1. 添加分类
        """
        try:
            url = Url + r'/manager/gwforward/manager-webapi/content/companyFileCategory/saveCompanyfileCategory'
            imgurl = Public.readyaml(file=r'Door\AddProduct', key='p_url')
            imgId = Public.readyaml(file=r'Door\AddProduct', key='p_id')
            data = "id=0&type=1&parentId=&imgUrl=" + str(imgurl) + "&imgId=" + str(
                imgId) + "&newOpen=1&mobileNewOpen=1&showFlag=1&mobileShowFlag=1&linkUrl=&mobileLinkUrl=&iconUrl=&appId=24&name=%E4%BC%81%E4%B8%9A%E4%B8%8B%E8%BD%BD%E5%88%86%E7%B1%BB01&summaryCheck=&linkPath=&linkPathMobile=&des=123456789&mobileDes=&message=&keywords=&summary=&seoState=true&hidTitle=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22categoryName%22%7D%2C%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E4%B8%80%E7%BA%A7%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22oneCategoryName%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%5D&hidKeywords=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%85%B3%E9%94%AE%E8%AF%8D%22%2C%22id%22%3A%22categoryKeyword%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%5D&hidDescription=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22categoryName%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%2C%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E6%8F%8F%E8%BF%B0%22%2C%22id%22%3A%22categoryDescription%22%7D%5D&hidTitleSign=_&hidKeywordsSign=%2C&hidDescriptionSign=-&hidAddDescription=&seoTitleSign=_&seoKeywordsSign=%2C&seoDescriptionSign=-&seoTitle=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22categoryName%22%7D%2C%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E4%B8%80%E7%BA%A7%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22oneCategoryName%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%5D&seoKeywords=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%85%B3%E9%94%AE%E8%AF%8D%22%2C%22id%22%3A%22categoryKeyword%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%5D&seoDescription=%5B%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22categoryName%22%7D%2C%7B%22name%22%3A%22%E7%BD%91%E7%AB%99%E5%90%8D%E7%A7%B0%22%2C%22id%22%3A%22siteName%22%7D%2C%7B%22name%22%3A%22%E6%96%87%E4%BB%B6%E5%88%86%E7%B1%BB%E6%8F%8F%E8%BF%B0%22%2C%22id%22%3A%22categoryDescription%22%7D%5D&seoAddDescription=&authData=%5B%7B%22authType%22%3A1%2C%22authStr%22%3A%22GW_%3A24%3Acategory%3Aview%3A%22%2C%22roleIds%22%3A%22%22%7D%5D&authStr=GW_%3A24%3Acategory%3Aview%3A&authType=1&roleIds=&"
            r = requests.post(url=url, headers=readconfig_ini(v=2), data=data, verify=False)
            result = r.json()
            id = result['data']['id']

            return id
        except:
            singular = str(traceback.format_exc())
            outcome('red', singular)
            return singular

    def put_file(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        """
        1. 上传企业文件《企业测试文件》
        """
        try:
            url_getfile = Url + r'/manager/gwforward/dssresources/fileRepository/getFileByFileKey'
            url_getkey = Url + r'/manager/gwforward/dssresources/fileRepository/getKs3Signature?tenantId=%s' % (self.tenant_value)
            url_putkey = 'https://ks3-cn-beijing.ksyun.com/xgw-vod'
            url = Url + r'/manager/gwforward/dssresources/fileRepository/saveKs3FileInfo'  # 获取文件key
            file_path = Any_Path('File', 'testfile001.txt')
            f = open(file_path, "rb")
            file = {'file': f}
            # ---- --------上传金山文件的名------------------------
            data_putname = "fileNames=testfile001.txt"
            r1 = requests.post(url=url_getkey, headers=readconfig_ini(v=2),
                               data=data_putname, verify=False)

            # ---- --------获取金山文件的key------------------------
            data_getkey = {"acl": "public-read", "key": "${filename}", "fileName": "testfile001.txt"}
            r1 = requests.post(url=url_getkey, headers=readconfig_ini(),
                              json=data_getkey, verify=False)
            result1 = r1.json()
            key = result1['data']['key']
            signature = result1['data']['signature']['signature']
            policy = result1['data']['signature']['policy']
            # --------------上传金山文件---------------------------
            data_putkey = {'name': 'testfile001.txt',
                           'key': key,
                           'acl': 'public-read',
                           'signature': signature,
                           'KSSAccessKeyId': 'TMRzmmQZpYOxoUjagQ5E',
                           'policy': policy,
                           'Bucket': 'xgw-vod',
                           'file': ('testfile001.txt', f.read())}

            encode_data = encode_multipart_formdata(data_putkey)

            requests.post(url=url_putkey, headers={'Content-Type':encode_data[1]}, data=encode_data[0], verify=False)
            # ----------------上传自己的文件-----------------------------------
            data = {'fileName': 'testfile001.txt', 'title': "testfile001.txt", 'type': 1, 'size': 17}
            for i in [1, 2]:
                r = requests.post(url=url, headers=readconfig_ini(v=4), data=data, verify=False, files=file)
                result = r.json()
                id = result['data']['id']
                path = result['data']['path']
            f.close()
            return id, path
        except:
            singular = str(traceback.format_exc())
            outcome('red', singular)
            return singular

    def get_sortlist(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        """
        1. 获取排序列表都有那些规则id
        """
        try:
            url = Url + r'/manager/gwforward/manager-webapi/content/companyFile/toCustomSort'
            data = {}
            r = requests.post(url=url, headers=readconfig_ini(v=2), data=data, verify=False)
            result = r.json()
            id = result['data']['orderMode']
            return id
        except:
            singular = str(traceback.format_exc())
            outcome('red', singular)
            return singular


