# # coding=utf-8
# import requests
# #
# # url = "https://account.300.cn/CAS/login/?service=http://new-api-console.300.cn/api-platform/home/centerMenu"
# # data = "username=CEM10097239&password=zok9phwv6n&platform=member&_eventId=submit&service=http://new-api-console.300.cn/api-platform/home/centerMenu"
# # header = {"Content-Type":"application/x-www-form-urlencoded"}
# # r = requests.post(url=url,data=data,headers=header)
# # print(r.headers)
# # qq = r.headers['Set-Cookie'].split(";")[0].split("=")[1]
# #
# # url1 = "http://new-api-console.300.cn/api-platform/home/centerMenu?ticket=ST-274693-sBfHy5LwNJiG5GAJjmJe-yunsso"
# # r1=requests.get(url=url1)
# # # print(r1.cookies)
# # jj = r1.headers['Set-Cookie'].split(";")[0].split("=")[1]
# # url2 = 'http://new-api-console.300.cn/api-platform/home/centerMenu;jsessionid={}'.format("3311B285BFA8ACDD0E845133BEB59C69")
# # print(url2)
# # r2=requests.get(url=url2,headers=header)
# # print(r2.headers)
# import json
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#
# data = {"category":{"id":"","ismobile":0,"status":0,"isSearch":0,"sequence":"","imageId":"","imageurl":"","parentId":"","addPId":"","addPname":"","editPId":"","eidtPname":"","categoryType":"0","windowtype":1,"mobileWindowType":1,"styleCategoryListId":"","styleProductDetailId":"","gototype":0,"defTabStyle":"","defDetailStyle":"","mobileStyleCategoryListId":"","mobileStyleProductDetailId":"","defTabStyleM":"","defDetailStyleM":"","appId":2,"categoryName":"33366644","linkurl":"","mobileLinkUrl":""},"choiceUrl":"","choiceUrlM":"","destype":0,"description":"","content":"","mobileContent":"","descriptionS":"","seoState":1,"hidTitle":[{"id":"categoryName","name":"产品基本分类名称"},{"id":"oneCategoryName","name":"产品基本分类一级分类名称"},{"id":"siteName","name":"网站名称"}],"hidKeywords":[{"id":"categoryKeyword","name":"产品基本分类关键词"},{"id":"siteName","name":"网站名称"}],"hidDescription":[{"id":"categoryName","name":"产品基本分类名称"},{"id":"siteName","name":"网站名称"},{"id":"categoryDescription","name":"产品基本分类描述"}],"hidTitleSign":"_","hidKeywordsSign":",","hidDescriptionSign":"-","seoTitleSign":"_","seoKeywordsSign":",","seoDescriptionSign":"-","seoTitle":[{"id":"categoryName","name":"产品基本分类名称"},{"id":"oneCategoryName","name":"产品基本分类一级分类名称"},{"id":"siteName","name":"网站名称"}],"seoKeywords":[{"id":"categoryKeyword","name":"产品基本分类关键词"},{"id":"siteName","name":"网站名称"}],"seoDescription":[{"id":"categoryName","name":"产品基本分类名称"},{"id":"siteName","name":"网站名称"},{"id":"categoryDescription","name":"产品基本分类描述"}],"authData":[{"authType":1,"authStr":"GW_:2:category:view:","roleIds":""}],"authStr":"GW_:2:category:view:","authType":1,"roleIds":""}
# header = {"Content-Type":"application/json;charset=UTF-8","Cookie":"GWSESSION=NTdlMmY4MWMtZjcxZC00MWY3LWJlMjctMTNhYTZhNzBiM2Zi"}
# url = 'https://2005285041-stsite-oper.pool601.yun300.cn/manager/gwforward/manager-webapi/product/appCategory/save?viewType=1&tenantId=196566&authPermission=classify_add'
# r = requests.post(url=url,json=data,headers=header,stream=True, verify=False)
# print(r.json())
import re

tt = {'status': 200, 'msg': 'success', 'success': True, 'data': [{'infos': 2, 'leaf': True, 'createDate': 1590595200000, 'status': 1, 'task': '6月', 'ismobile': '1', 'id': 2}]}
value = re.findall(f'\'msg\':(.*?),', str(tt))[0]
print(value.replace("'", ' ').replace('"', ' '))
if value=='success':
    print(11)
