
from bottle import template
import webbrowser
import sys

class_title = """# coding=utf-8
import unittest
import traceback
import requests
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import urllib3


class {}(MyTest):

    condition = True
    type_condition = False
    # {}"""

case_body = """
    
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def {}(self):
        # {}
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.{}(url, headers=self.headers, {}=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular
        """

case_data = '''%s:
  product: #产品管理
    - url: /manager-webapi/product/productInformation/list  # 邮件地址
      modular: 产品列表  # 接口注释
      className: manage_product  # 接口类名
      funName:
        - test_product_getlist: {  # 接口方法名
          url: /dssform/formData/saveFormData,
          level: 中,   #级别
          author: 陈建波,  #作者
          bar: {"appId":2,"cateId":null,"showCaseId":null,"attributeId":0,"pcStatus":null,"moStatus":null,"startDate":"","endDate":"","keyword":"","pageSize":15,"pageNumber":1,"orderColumn":"","order_productName":"","order_productCode":"","order_cateName":"","order_retailPrice":"","order_publishTime":"","order_pcStatus":"","order_moStatus":"","order_shortUrl":""},
          test_data: {},
          case_name: 产品列表,
          expected: [200,'success'],  # 预期结果
          mode: post,  # 请求类型
          re_bar: json, # 请求参数
          }'''

pypublic = '''
# coding=utf-8
import requests
from random import randint,choice
import random,os,re
import json
import requests
import time
from random import randint
from datetime import date,timedelta
from Common.ReadYaml import ReadPublic, ConfigYaml
projectName = ConfigYaml("projectName").base_config
Url = ConfigYaml(projectName).base_url
'''

publicyaml = '''add_customer:
  - url: /add/customerParam
    bar: {}
'''



html_head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1"/>
    <title>接口自动化测试报告</title>
    <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
    <script src="http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="https://www.echartsjs.com/examples/vendors/echarts/echarts.min.js"></script>
    <script type="text/javascript" src="https://www.echartsjs.com/examples/vendors/echarts-stat/ecStat.min.js"></script>
    <script type="text/javascript" src="https://www.echartsjs.com/examples/vendors/echarts/map/js/china.js"></script>
    <script type="text/javascript" src="https://www.echartsjs.com/examples/vendors/echarts/map/js/world.js"></script>
    <script type="text/javascript" src="https://www.echartsjs.com/examples/vendors/echarts/extension/dataTool.js"></script>
    <link href="../static/mycss.css" rel="stylesheet">
    <script src="../static/alljs.js"></script>
</head>
<body>
"""

html_body = '''
<div>
    <h1>Scrm接口自动化测试报告</h1>
    <hr>
    <div class="staticdis">
        <div>
            <table class="table table-bordered">
                <tbody>
                <tr>
                    <td>项目版本</td>
                    <td>{}</td>
                    <td>测试环境</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>用例执行数</td>
                    <td>{}</td>
                    <td>执行总用时</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>开始时间</td>
                    <td>{}</td>
                    <td>结束时间</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>用时最长</td>
                    <td>{}</td>
                    <td>用时最短</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>平均时长</td>
                    <td>{}</td>
                    <td>成功率</td>
                    <td>{}</td>
                </tr>
                </tbody>
            </table>
        </div>
        <div id="picture">
            <script>
                statistical({}, {}, {}, {}, {});
            </script>
        </div>
    </div>
'''
html_button = '''
<div class="button">
        <div><a href="#all" data-toggle="tab">全部({})</a></div>
        <div><a href="#success" data-toggle="tab">成功({})</a></div>
        <div><a href="#fail" data-toggle="tab">失败({})</a></div>
        <div><a href="#error" data-toggle="tab">错误({})</a></div>
        <div><a href="#timeout" data-toggle="tab">超时({})</a></div>
        <div><a href="#skip" data-toggle="tab">跳过({})</a></div>
    </div>
'''

html_all = '''
<div class="tab-content content" id="content">
    <div class="tab-pane active" id="all">
        <table class="table table-hover other">
            <thead>
                <tr>
                    <td>用例名称</td>
                    <td>用例描述</td>
                    <td>优先级</td>
                    <td>接口地址</td>
                    <td>测试结果</td>
                    <td>负责人</td>
                    <td>用时时间</td>
                    <td>详细信息</td>
                </tr>
            </thead>
'''
html_all_case = '''
<tr>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td><a href="javascript:showClassDetail('{}_{}','hidd_{}_{}')" id="{}_{}">详细</a></td>
</tr>
    <tr class='hiddenRow' id="hidd_{}_{}">
        <td colspan='8'>
            <div>
               <pre class="text-left">
               {}
               </pre>
            </div>
        </td>
    </tr>
'''

html_all_end = '''
    </table>
</div>
'''

html_sum__end = '''
        </div>
    </body>
</html>
'''


html_other = '''
<div class="tab-pane" id="{}">
    <table class="table table-hover other">
        <thead>
            <tr>
                <td>用例名称</td>
                <td>用例描述</td>
                <td>优先级</td>
                <td>接口地址</td>
                <td>测试结果</td>
                <td>负责人</td>
                <td>用时时间</td>
                <td>详细信息</td>
            </tr>
        </thead>
        
'''
