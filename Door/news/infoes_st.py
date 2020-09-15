# coding=utf-8
import unittest
import traceback
import requests
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import urllib3
from random import choice
from Door.news.Public import Public_Data as pd
from Common.CusMethod import get_data_time, random_char, thead_sort, random_str, show_sort, get_hour_second

my_data = pd()
news_ids = my_data.get_news_ids()
picture_ids = my_data.get_picture_ids()
class_ids = my_data.get_class_ids()

pb_data = type("pb_data", (object,), {})
setattr(pb_data, "news_ids",news_ids)
setattr(pb_data, "picture_ids", picture_ids)
setattr(pb_data, "class_ids", class_ids)

class infoes_news(MyTest):

    condition = True
    # 新闻资讯
    type_condition = True

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_all_news(self):
        # 全部资讯页面
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_noclass_news(self):
        # 无内容分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular
        
    
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_search_news(self):
        # 搜索新闻资讯
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if not pb_data.news_ids:
                pb_data.news_ids = my_data.get_news_ids()
                news_name = choice(pb_data.news_ids).get("title")
            else:
                news_name = choice(pb_data.news_ids).get("title")

            self.data['keywords'] = news_name
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_screen_news(self):
        # 筛选新闻资讯
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_picture_ids()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")
            self.data['cateId'] = class_id
            self.data['pcStatus'] = choice([0, 1, -1])
            self.data['startDate'] = get_data_time(-7)
            self.data['startDate'] = get_data_time(0)
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_turnpage_news(self):
        # 翻页
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            self.data['ec_p'] = int(random_char())
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_theadsort_news(self):
        # 表头排序
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            self.data['ec_s_title'] = thead_sort()
            self.data['ec_s_categorys'] = thead_sort()
            self.data['ec_s_pubDate'] = thead_sort()
            self.data['ec_s_viewCount'] = thead_sort()
            self.data['ec_s_showFlag'] = thead_sort()

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_dragsort_news(self):
        # 拖拽排序
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if len(pb_data.news_ids) > 2:
                    id_one = pb_data.news_ids[0].get("id")
                    id_two = pb_data.news_ids[1].get("id")
            else:
                my_data.add_news()
                my_data.add_news()
                pb_data.news_ids = my_data.get_news_ids()
                id_one = pb_data.news_ids[0].get("id")
                id_two = pb_data.news_ids[1].get("id")

            self.data['targetId'] = id_one
            self.data['sectionIds'] = id_two

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_edit_news(self):
        # 编辑新闻资讯
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not pb_data.news_ids:
                pb_data.news_ids = my_data.get_news_ids()
                news_id = choice(pb_data.news_ids).get("id")
            else:
                news_id = choice(pb_data.news_ids).get("id")
            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_picture_ids()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")

            self.data['id'] = news_id
            self.data['title'] = random_str("自动化测试编辑后数据")
            self.data['infotype'] = class_id
            self.data['content'] = random_str("<p>自动化测试新闻资讯内容数据</p>\n")

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red',self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_browse_news(self):
        # 浏览新闻资讯
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.news_ids:
                pb_data.news_ids = my_data.get_news_ids()
                news_id = choice(pb_data.news_ids).get("id")
            else:
                news_id = choice(pb_data.news_ids).get("id")

            self.data['id'] = news_id
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_updatetransfer_news(self):
        # 转移新闻资讯
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.news_ids:
                pb_data.news_ids = my_data.get_news_ids()
                news_id = choice(pb_data.news_ids).get("id")
            else:
                news_id = choice(pb_data.news_ids).get("id")
            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")

            self.data['id'] = news_id
            self.data['cateId'] = class_id

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_updatepcview_news(self):
        # 显示电脑版
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.news_ids:
                pb_data.news_ids = my_data.get_news_ids()
                news_id = choice(pb_data.news_ids).get("id")
            else:
                news_id = choice(pb_data.news_ids).get("id")

            self.data['id'] = news_id
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_hide_news(self):
        # 隐藏电脑版
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.news_ids:
                pb_data.news_ids = my_data.get_news_ids()
                news_id = choice(pb_data.news_ids).get("id")
            else:
                news_id = choice(pb_data.news_ids).get("id")

            self.data['id'] = news_id
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_copy_news(self):
        # 复制
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            if not pb_data.news_ids:
                pb_data.news_ids = my_data.get_news_ids()
                news_id = choice(pb_data.news_ids).get("id")
            else:
                news_id = choice(pb_data.news_ids).get("id")

            self.data['id'] = news_id
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_top_news(self):
        # 置顶
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.news_ids:
                pb_data.news_ids = my_data.get_news_ids()
                news_id = choice(pb_data.news_ids).get("id")
            else:
                news_id = choice(pb_data.news_ids).get("id")

            self.data['id'] = news_id
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_recommend_news(self):
        # 推荐
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.news_ids:
                pb_data.news_ids = my_data.get_news_ids()
                news_id = choice(pb_data.news_ids).get("id")
            else:
                news_id = choice(pb_data.news_ids).get("id")

            self.data['id'] = news_id

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_savetags_news(self):
        # 标记
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            if not pb_data.news_ids:
                pb_data.news_ids = my_data.get_news_ids()
                news_id = choice(pb_data.news_ids).get("id")
            else:
                news_id = choice(pb_data.news_ids).get("id")

            self.data['tags'][0]['infoId'] = news_id
            self.data['tags'][1]['infoId'] = news_id
            self.data['id'] = news_id

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_delete_news(self):
        # 删除
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.news_ids:
                pb_data.news_ids = my_data.get_news_ids()
                news_id = pb_data.news_ids.pop(0).get("id")
            else:
                news_id = pb_data.news_ids.pop(0).get("id")

            self.data['id'] = news_id

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_transfer_news(self):
        # 批量转移
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if len(pb_data.news_ids) > 2:
                    news_id_one = pb_data.news_ids[0].get("id")
                    news_id_two = pb_data.news_ids[1].get("id")
            else:
                my_data.add_news()
                my_data.add_news()
                pb_data.news_ids = my_data.get_news_ids()
                news_id_one = pb_data.news_ids[0].get("id")
                news_id_two = pb_data.news_ids[1].get("id")

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")

            self.data['cateId'] = class_id
            self.data['id'] = [news_id_one, news_id_two]

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_pcview_news(self):
        # 批量显示电脑版
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.news_ids) > 2:
                news_id_one = pb_data.news_ids[0].get("id")
                news_id_two = pb_data.news_ids[1].get("id")
            else:
                my_data.add_news()
                my_data.add_news()
                pb_data.news_ids = my_data.get_news_ids()
                news_id_one = pb_data.news_ids[0].get("id")
                news_id_two = pb_data.news_ids[1].get("id")

            self.data['id'] = [news_id_one, news_id_two]

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_hidepcview_news(self):
        # 批量隐藏电脑版
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.news_ids) > 2:
                news_id_one = pb_data.news_ids[0].get("id")
                news_id_two = pb_data.news_ids[1].get("id")
            else:
                my_data.add_news()
                my_data.add_news()
                pb_data.news_ids = my_data.get_news_ids()
                news_id_one = pb_data.news_ids[0].get("id")
                news_id_two = pb_data.news_ids[1].get("id")

            self.data['id'] = [news_id_one, news_id_two]

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_batchdelete_news(self):
        # 批量删除
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.news_ids) > 2:
                news_id_one = pb_data.news_ids.pop(0).get("id")
                news_id_two = pb_data.news_ids.pop(1).get("id")
            else:
                my_data.add_news()
                my_data.add_news()
                pb_data.news_ids = my_data.get_news_ids()
                news_id_one = pb_data.news_ids.pop(0).get("id")
                news_id_two = pb_data.news_ids.pop(1).get("id")

            self.data['id'] = [news_id_one, news_id_two]

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_batchrecommend_news(self):
        # 批量删除
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.news_ids) > 2:
                news_id_one = pb_data.news_ids.pop(0).get("id")
                news_id_two = pb_data.news_ids.pop(1).get("id")
            else:
                my_data.add_news()
                my_data.add_news()
                pb_data.news_ids = my_data.get_news_ids()
                news_id_one = pb_data.news_ids.pop(0).get("id")
                news_id_two = pb_data.news_ids.pop(1).get("id")

            self.data['id'] = [news_id_one, news_id_two]

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_cancelrecommend_news(self):
        # 批量取消推荐
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.news_ids) > 2:
                news_id_one = pb_data.news_ids[0].get("id")
                news_id_two = pb_data.news_ids[1].get("id")
            else:
                my_data.add_news()
                my_data.add_news()
                pb_data.news_ids = my_data.get_news_ids()
                news_id_one = pb_data.news_ids[0].get("id")
                news_id_two = pb_data.news_ids[1].get("id")

            self.data['id'] = [news_id_one, news_id_two]

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_canceltop_news(self):
        # 批量置顶
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.news_ids) > 2:
                news_id_one = pb_data.news_ids[0].get("id")
                news_id_two = pb_data.news_ids[1].get("id")
            else:
                my_data.add_news()
                my_data.add_news()
                pb_data.news_ids = my_data.get_news_ids()
                news_id_one = pb_data.news_ids[0].get("id")
                news_id_two = pb_data.news_ids[1].get("id")

            self.data['id'] = [news_id_one, news_id_two]

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_batchcancel_news(self):
        # 批量取消置顶
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if len(pb_data.news_ids) > 2:
                news_id_one = pb_data.news_ids[0].get("id")
                news_id_two = pb_data.news_ids[1].get("id")
            else:
                my_data.add_news()
                my_data.add_news()
                pb_data.news_ids = my_data.get_news_ids()
                news_id_one = pb_data.news_ids[0].get("id")
                news_id_two = pb_data.news_ids[1].get("id")

            self.data['id'] = [news_id_one, news_id_two]

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_customsort_news(self):
        # 展示排序
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            self.data['orderMode'] = show_sort()
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_add_news(self):
        # 普通资讯新增
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()
                id = choice(pb_data.class_ids).get("id")
            else:
                id = choice(pb_data.class_ids).get("id")
            self.data['infotype'] = id
            self.data['cateGoryIds'] = id
            self.data['title'] = random_str("自动化新增普通新闻资讯...")
            self.data['content'] = random_str("<p>自动化新增新闻资讯内容....</p>\n")
            self.data['summary'] = random_str("自动化新增普通新闻资讯描述....")
            self.data['keyWords'] = random_str("关键词....")
            self.data['author'] = random_str("自动化测试...")
            self.data['source'] = random_str("自动化测试来源...")

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_addpicture_news(self):
        # 图片资讯新增
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_picture_ids()
                img_url = choice(pb_data.picture_ids).get('imgUrl')
            else:
                img_url = choice(pb_data.picture_ids).get('imgUrl')

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()
                id = choice(pb_data.class_ids).get("id")
            else:
                id = choice(pb_data.class_ids).get("id")
            self.data['infotype'] = id
            self.data['cateGoryIds'] = id
            self.data['title'] = random_str("自动化新增图片新闻资讯")
            self.data['content'] = random_str("<p>自动化新增新闻资讯内容....</p>\n")
            self.data['summary'] = random_str("自动化新增普通新闻资讯描述....")
            self.data['keyWords'] = random_str("关键词....")
            self.data['author'] = random_str("自动化测试...")
            self.data['source'] = random_str("自动化测试来源...")
            self.data['imgs'][0]['relativeImgUrl'] = img_url
            self.data['imgs'][0]['relativeThumbUrl'] = img_url
            self.data['imgs'][0]['imgUrl'] = img_url
            self.data['imgs'][0]['thumbUrl"'] = img_url
            self.data['infoImgUrl'] = img_url

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_addlink_news(self):
        # 链接资讯新增
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_picture_ids()
                img_url = choice(pb_data.picture_ids).get('imgUrl')
            else:
                img_url = choice(pb_data.picture_ids).get('imgUrl')

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()
                id = choice(pb_data.class_ids).get("id")
            else:
                id = choice(pb_data.class_ids).get("id")
            
            self.data['infotype'] = id
            self.data['cateGoryIds'] = id
            self.data['title'] = random_str("自动化新增图片新闻资讯")
            self.data['summary'] = random_str("自动化新增普通新闻资讯描述....")
            self.data['keyWords'] = random_str("关键词....")
            self.data['imgs'][0]['imgUrl'] = img_url
            self.data['infoImgUrl'] = img_url
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_getkeywords_news(self):
        # 自动获取关键词
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_addcategor_news(self):
        # 快捷添加分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            self.data['name'] = random_str("自动化新增分类....")
            self.data['des'] = random_str("<p>自动化测试分类内容数据....</p>\n")

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_timing_news(self):
        # 定时发布
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            self.data['title'] = random_str("自动化新增定时任务新闻资讯")
            self.data['content'] = random_str("<p>自动化新增定时任务新闻资讯内容....</p>\n")
            self.data['summary'] = random_str("自动化新增定时任务新闻资讯描述....")
            self.data['keyWords'] = random_str("关键词....")
            self.data['author'] = random_str("自动化测试...")
            self.data['source'] = random_str("自动化测试来源...")
            self.data['pubDate'] = get_hour_second(2)

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_brelevant_news(self):
        # 定时发布
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()
                id = choice(pb_data.class_ids).get("id")
            else:
                id = choice(pb_data.class_ids).get("id")

            self.data['infotype'] = id
            self.data['cateGoryIds'] = id
            self.data['title'] = random_str("自动化新增相关内容新闻资讯")
            self.data['content'] = random_str("<p>自动化新增相关内容新闻资讯内容....</p>\n")
            self.data['summary'] = random_str("自动化新增相关内容新闻资讯描述....")
            self.data['keyWords'] = random_str("关键词....")
            self.data['author'] = random_str("自动化测试...")
            self.data['source'] = random_str("自动化测试来源...")
            contentList = next(pd().get_application)
            self.data['relecontentList'][1]['contentList'] = [contentList]
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_extension_news(self):
        # 推广优化
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()
                id = choice(pb_data.class_ids).get("id")
            else:
                id = choice(pb_data.class_ids).get("id")
            self.data['infotype'] = id
            self.data['cateGoryIds'] = id
            self.data['title'] = random_str("自动化新增推广优化新闻资讯")
            self.data['content'] = random_str("<p>自动化新增推广优化新闻资讯内容....</p>\n")
            self.data['summary'] = random_str("自动化新增推广优化新闻资讯描述....")
            self.data['keyWords'] = random_str("关键词....")
            self.data['author'] = random_str("自动化测试...")
            self.data['source'] = random_str("自动化测试来源...")
            self.data['seoAddDescription'] = random_str("推广优化描述...")

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_senior_news(self):
        # 高级设置
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()
                id = choice(pb_data.class_ids).get("id")
            else:
                id = choice(pb_data.class_ids).get("id")
            self.data['infotype'] = id
            self.data['cateGoryIds'] = id
            self.data['title'] = random_str("自动化新增高级设置新闻资讯")
            self.data['content'] = random_str("<p>自动化新增高级设置新闻资讯内容....</p>\n")
            self.data['summary'] = random_str("自动化新增高级设置新闻资讯描述....")
            self.data['keyWords'] = random_str("关键词....")
            self.data['author'] = random_str("自动化测试...")
            self.data['source'] = random_str("自动化测试来源...")
            self.data['pubDate'] = get_hour_second(2)
            self.data['seoAddDescription'] = random_str("高级设置描述...")
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_cmuchpicture_news(self):
        # 多图片上传
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if len(pb_data.picture_ids) > 2:
                img_url_one = pb_data.picture_ids[0].get("imgUrl")
                img_url_two = pb_data.picture_ids[1].get("imgUrl")
            else:
                my_data.file_upload()
                my_data.file_upload()
                pb_data.picture_ids = my_data.get_picture_ids()
                img_url_one = pb_data.picture_ids[0].get("imgUrl")
                img_url_two = pb_data.picture_ids[1].get("imgUrl")

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class_ids()
                id = choice(pb_data.class_ids).get("id")
            else:
                id = choice(pb_data.class_ids).get("id")

            self.data['infotype'] = id
            self.data['cateGoryIds'] = id
            self.data['title'] = random_str("自动化新增多图片新闻资讯")
            self.data['content'] = random_str("<p>自动化新增多图片新闻资讯内容....</p>\n")
            self.data['summary'] = random_str("自动化新增多图片新闻资讯描述....")
            self.data['keyWords'] = random_str("关键词....")
            self.data['author'] = random_str("自动化测试...")
            self.data['source'] = random_str("自动化测试来源...")
            self.data['imgs'][0]['relativeImgUrl'] = img_url_one
            self.data['imgs'][0]['relativeThumbUrl'] = img_url_one
            self.data['imgs'][0]['imgUrl'] = img_url_one
            self.data['imgs'][0]['thumbUrl"'] = img_url_one
            self.data['imgs'][1]['relativeImgUrl'] = img_url_two
            self.data['imgs'][1]['relativeThumbUrl'] = img_url_two
            self.data['imgs'][1]['imgUrl'] = img_url_two
            self.data['imgs'][1]['thumbUrl"'] = img_url_two
            self.data['infoImgUrl'] = img_url_one

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        
    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_aselect_news(self):
        # 选择图片连接
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_picture_ids()
                img_url = choice(pb_data.picture_ids).get('imgUrl')
            else:
                img_url = choice(pb_data.picture_ids).get('imgUrl')

            self.data['title'] = random_str("自动化新增选择连接新闻资讯99...")
            self.data['content'] = random_str("<p>自动化新增选择连接新闻资讯内容....</p>\n")
            self.data['summary'] = random_str("自动化新增选择连接新闻资讯描述....")
            self.data['keyWords'] = random_str("关键词....")
            self.data['pubDate'] = get_hour_second(2)
            self.data['imgs'][0]['imgUrl'] = img_url
            self.data['infoImgUrl'] = img_url

            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        