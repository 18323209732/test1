
# coding=utf-8
import configparser
import urllib3
from Common.ReadWriteIni import ReadWrite
from Common.ReadYaml import ConfigYaml
import traceback
import os,requests
import requests.packages.urllib3
from Common.FontColor import outcome
import yaml
from ruamel.yaml import RoundTripDumper


def readyaml(file=None, key=None):
    """
    1. 获取文件当前路劲+文件名称
    2. 打开yaml文件
    3. 转译文件内容获取对应key的值
    """
    path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\%s\Public.yaml" % file
    try:
        with open(path, 'r', encoding='utf-8') as f:
            value = yaml.load(f.read(), Loader=yaml.Loader)[key]
        return value
    except:
        pass


def readyaml_case(key=None):
    """
    1. 获取case.yaml的橱窗列表
    2. 转译文件内容获取对应test03_keywords_listShowcase的URL值
    """
    path = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\Case.yaml"
    try:
        with open(path, 'r', encoding='utf-8') as f:
            # value = yaml.load(f.read(), Loader=yaml.Loader)[key]
            value = yaml.load(f.read())['Door']['listShowcase'][0]['funName'][0]['test03_keywords_listShowcase']['url']

        return value
    except:
        pass


def writeyaml(w_key=None, w_value=None, n=None):
    """
    1. 打开当前文件下的yaml文件，n传入写入方法（a 为追加方式写入，w 为清空后重写）
    2. 传入要写入的key：value
    3. 转译文件，传入参数，去重｛｝，方便yaml直接读取数据
    """
    with open("Public.yaml", n, encoding="utf-8") as yaml_file:
        data = {w_key: w_value}
        yaml.dump(data, yaml_file, Dumper=RoundTripDumper, allow_unicode=True)


def readconfig_yaml(basekey='base_url', key='Door'):
    path = os.path.abspath(os.path.join(os.getcwd(), "../.."))+r'\Config\Config.yaml'
    with open(path, 'r', encoding='utf-8') as f:
        value = yaml.load(f.read(), Loader=yaml.Loader)[basekey][key]
    return value


def readconfig_ini(v=True):
    path = os.path.abspath(os.path.join(os.getcwd(), "../.."))+r'\Door\Config.ini'
    config = configparser.ConfigParser()
    config.read(path)
    cookies_value = config.get("session", "cookies")
    headers1 = {'Content-Type': 'application/json;charset=UTF-8'}
    headers2 = {'Content-Type': 'application/x-www-form-urlencoded'}
    headers3 = {'Content-Type': 'multipart/form-data'}
    if v==True:
        headers1.update({'Cookie': cookies_value})
        return headers1
    elif v==3:
        headers3 = {'Cookie': cookies_value}
        return headers3
    else:
        headers2.update({'Cookie': cookies_value})
        return headers2


class GetAll:
    def __init__(self):
        self.tenant_value = readconfig_yaml(basekey='base_config', key='tenant_value')
        self.headers = readconfig_ini()

    def get_product_attribute(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        """
        1. 获取属性列表默认属性id
        """
        try:
            data = {}
            url = readconfig_yaml() + r'/manager/gwforward/manager-webapi/product/productAttribute/list?tenantId=%s&appId=2&sortField=' % (self.tenant_value)
            r = requests.get(url, headers=readconfig_ini(v=1), data=data, stream=True, verify=False)
            result = r.json()
            id = result['data']['list'][0]['id']
            # print(result['data']['list'])
            return id
        except:
            singular = str(traceback.format_exc())
            outcome('red', singular)
            return singular

    def get_attribute(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        """
        1. 添加规格、规格值
        2. 获取默认属性的规格
        3. 获取默认属性的规格值
        """
        try:
            # 给默认第一个属性添加规格和规格值
            url = readconfig_yaml() + r"/manager/gwforward/manager-webapi/product/productAttribute/saveAttribute?viewType=1&tenantId=%s&authPermission=attribute_add" % (self.tenant_value)
            data = {"id":1,"appId":2,"templateName":"默认属性类型","memo":"系统默认模版,全局只有一个","operType":"edit","paramDataArr":[],"buttonDataArr":[],"tabPageDataArr":[],"itemDataArr":[{"isrequire":"0","issearch":"0","unit":"","isdisplay":"0","fieldType":"0","subFieldType":"text","option":"","optionReferIdx":[],"promt":"请输入产品名称","defaultname":"产品名称","defaultcode":"name","aid":1,"isFix":"0","name":"产品名称","isRefer":0,"code":"name"},{"isrequire":"1","issearch":"1","unit":"","isdisplay":"0","fieldType":"0","subFieldType":"text","option":"","optionReferIdx":[],"promt":"请输入编号","defaultname":"编号","defaultcode":"code","aid":2,"isFix":"0","name":"编号","isRefer":0,"code":"code"},{"isrequire":"0","issearch":"1","unit":"","isdisplay":"0","fieldType":"0","subFieldType":"text","option":"","optionReferIdx":[],"promt":"请输入最低起订量","defaultname":"最低起订量","defaultcode":"moq","aid":17,"isFix":"0","name":"最低起订量","isRefer":0,"code":"moq"},{"isrequire":"0","issearch":"1","unit":"","isdisplay":"0","fieldType":"0","subFieldType":"text","option":"","optionReferIdx":[],"promt":"请输入交货期","defaultname":"交货期","defaultcode":"deliveryTime","aid":18,"isFix":"0","name":"交货期","isRefer":0,"code":"deliveryTime"},{"isrequire":"0","issearch":"1","unit":"kg","isdisplay":"0","fieldType":"0","subFieldType":"number","option":"","optionReferIdx":[],"promt":"请输入计费重量","defaultname":"计费重量","defaultcode":"chargedWeight","aid":19,"isFix":"0","name":"计费重量","isRefer":0,"code":"chargedWeight"},{"isrequire":"1","issearch":"1","unit":"","isdisplay":"0","fieldType":"0","subFieldType":"text","option":"","optionReferIdx":[],"promt":"请输入计量单位","defaultname":"计量单位","defaultcode":"unit","aid":3,"isFix":"0","name":"计量单位","isRefer":0,"code":"unit"},{"isrequire":"1","issearch":"1","unit":"","isdisplay":"0","fieldType":"0","subFieldType":"number","option":"","optionReferIdx":[],"promt":"请输入重量","defaultname":"重量","defaultcode":"weight","aid":4,"isFix":"0","name":"重量","isRefer":0,"code":"weight"},{"isrequire":"1","issearch":"1","unit":"元","isdisplay":"0","fieldType":"0","subFieldType":"number","option":"","optionReferIdx":[],"promt":"请输入市场价","defaultname":"市场价","defaultcode":"price","aid":5,"isFix":"0","name":"市场价","isRefer":0,"code":"price"},{"isrequire":"1","issearch":"1","unit":"元","isdisplay":"0","fieldType":"0","subFieldType":"number","option":"","optionReferIdx":[],"promt":"请输入零售价","defaultname":"零售价","defaultcode":"retailPrice","aid":6,"isFix":"0","name":"零售价","isRefer":0,"code":"retailPrice"},{"isrequire":"1","issearch":"1","unit":"","isdisplay":"0","fieldType":"0","subFieldType":"number","option":"","optionReferIdx":[],"promt":"请输入库存","defaultname":"库存","defaultcode":"stock","aid":7,"isFix":"0","name":"库存","isRefer":0,"code":"stock"},{"isrequire":"1","issearch":"1","unit":"","isdisplay":"0","fieldType":"1","subFieldType":"AREtext","option":"","optionReferIdx":[],"promt":"null","defaultname":"产品描述","defaultcode":"content","aid":8,"isFix":"0","name":"产品描述","isRefer":0,"code":"content"}],"specDataArr":[{"id":1,"specName":"尺寸","isRefer":0,"specType":0,"specValues":[{"id":1,"specValueName":"10寸","imgUrl":"","isRefer":0}]}],"filePageDataArr":[],"needDelId":{"attrIds":[],"paramIds":[],"buttonIds":[],"tabPageIds":[],"specIds":[]},"newLineNums":{}}
            r = requests.post(url, headers=self.headers, json=data, stream=True, verify=False)
            result = r.json()
            # print(result)
            # 添加产品页面，获取默认属性的规格和规格值
            attribute_id = GetAll().get_product_attribute()
            data = {}
            url = readconfig_yaml() + r'/manager/gwforward/manager-webapi/product/productAttribute/getAttributeDetail?tenantId=%s&appId=2&id=%s&operType=edit' % (self.tenant_value, attribute_id)
            r = requests.get(url, headers=self.headers, data=data, stream=True, verify=False)
            result = r.json()

            s_id = result['data']['specDataArr'][0]['id']  # 规格id
            specName= result['data']['specDataArr'][0]['specName']  # 规格名字
            value_id = result['data']['specDataArr'][0]['specValues'][0]['id']  # 规格值id
            specValueName = result['data']['specDataArr'][0]['specValues'][0]['specValueName']  # 规格值名字
            # print(value_id)
            return attribute_id, s_id, specName, value_id, specValueName
        except:
            singular = str(traceback.format_exc())
            outcome('red', singular)
            return singular

    def put_img(self, img_type='image/jpeg'):
            """
            :param img_path:图片的路径
            :param img_name:图片的名称
            :param img_type:图片的类型,这里写的是image/jpeg，也可以是png/jpg
            """
            requests.packages.urllib3.disable_warnings()
            headers = readconfig_ini(v=3)
            url = readconfig_yaml() + r'/manager/gwforward/dssresources/imageRepository/imageFileUpload'
            img_path = r"E:\Automate\Portal_interface\Img\产品用图.jpg"
            with open(img_path, "rb")as f:
                body = {'file': f}  # 图片的名称、图片的绝对路径、图片的类型（就是后缀）
                r = requests.post(url=url, headers=headers, data={'appId': ""}, files=body, verify=False)
                result = r.json()
                p_id = result['data']['id']
                p_url = result['data']['imgUrl']
                p_name = result['data']['name']
                # print(p_name)
                writeyaml(w_key='p_id', w_value=p_id, n='a')
                writeyaml(w_key='p_url', w_value=p_url, n='a')
                writeyaml(w_key='p_name', w_value=p_name, n='a')

    def showlist(self):
        """
        1.添加橱窗
        2.获取橱窗id
        """
        requests.packages.urllib3.disable_warnings()
        headers = readconfig_ini(v=2)
        url = readconfig_yaml() + r'/manager/gwforward/manager-webapi/product/productShowcase/save?tenantId=%s'% (self.tenant_value)
        data = {'showcaseId': '','showcaseName': '橱窗0号', 'appId': 2,'content': ''}
        r = requests.post(url, headers=headers, data=data, stream=True, verify=False)
        result = r.json()['data']['id']

        return result

    def get_mark(self):
        """
        1.添加标记
        2.获取标记id
        """
        requests.packages.urllib3.disable_warnings()
        headers = readconfig_ini(v=3)
        url = readconfig_yaml() + r'/manager/gwforward/manager-webapi/product/productMark/save?tenantId=%s&authPermission=tag_add'% (self.tenant_value)
        data = {'appId': 2, 'markName': '我的标记', 'imageId': readyaml(file='AddProduct', key='p_id'), 'imageurl': readyaml(file='AddProduct', key='p_url')}
        r = requests.post(url, headers=headers, data=data, stream=True, verify=False)


        url2 = readconfig_yaml() + r'/manager/gwforward/manager-webapi/product/productMark/list?tenantId=%s&appId=2'% (self.tenant_value)
        r2 = requests.get(url2, headers=self.headers,  stream=True, verify=False)
        result = r2.json()['data'][-1]['id']
        # print(result)
        return result


if __name__ == '__main__':
    GetAll().get_mark()
