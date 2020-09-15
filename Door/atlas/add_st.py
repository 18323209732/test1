# coding=utf-8
import unittest
import traceback
from random import choice

import requests

from Common.CusMethod import random_str
from Common.FontColor import outcome
from Common.MyUnit import MyTest
from Common.ReadYaml import ConfigYaml
from Common.DataHandle import ReRun
import urllib3
from ddt import ddt, data,file_data
from Common.ReExecution import Get_Cls_Fun
from Common.Route import Any_Path
from Door.atlas.Public import Public_Data as curre
my_data = curre()
atlas_ids = my_data.get_atlas()
class_ids = my_data.get_class()
picture_ids = my_data.get_pictures()
news_class = my_data.get_news_class()
news_ids = my_data.get_news_id()

pb_data = type("pb_data", (object,), {})
setattr(pb_data, "news_ids",news_ids)
setattr(pb_data, "picture_ids", picture_ids)
setattr(pb_data, "class_ids", class_ids)
setattr(pb_data, "atlas_ids", atlas_ids)
setattr(pb_data, "news_ids", news_ids)


@ddt
class add_atlas(MyTest):

    condition = True
    type_condition = True
    # 企业图册

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_add_atlas(self):
        # 添加企业图册
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")

            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_pictures()
                value = choice(pb_data.picture_ids)
            else:
                value = choice(pb_data.picture_ids)

            img_url = value.get('imgUrl')
            id = value.get('id')
            name = value.get('name')
            self.data['commonAtlasName'] = random_str("自动化企业图册...")
            self.data['commonAtlasDescription'] = random_str("<p>自动化企业图册详细内容数据...</p>\n")
            self.data['commonAtlasSummary'] = random_str("自动化企业图册描述数据...")
            self.data['keywords'] = random_str("关键词...")
            self.data['atlasCategoryArr'] = [f"{class_id}"]
            self.data["atlasImgs"][0]['id'] = f"{id}"
            self.data["atlasImgs"][0]['imgId'] = f"{id}"
            self.data["atlasImgs"][0]['thumbId'] = f"{id}"
            self.data["atlasImgs"][0]['name'] = name
            self.data["atlasImgs"][0]['relativeImgUrl'] = img_url
            self.data["atlasImgs"][0]['imgUrl'] = img_url
            self.data["atlasImgs"][0]['thumbUrl'] = img_url
            self.data["atlasImgs"][0]['relativeThumbUrl'] = img_url

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
    def test_addmuchpicture_atlas(self):
        # 添加企业图册_多张图片
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")

            if len(pb_data.picture_ids) > 2:
                value = pb_data.picture_ids[0]
                value_ = pb_data.picture_ids[1]
            else:
                my_data.file_upload()
                my_data.file_upload()
                pb_data.picture_ids = my_data.get_pictures()
                value = pb_data.picture_ids[0]
                value_ = pb_data.picture_ids[1]
            id_1 = value.get('id')
            id_2 = value_.get('id')

            img_url = value.get('imgUrl')
            img_url_1 = value_.get('imgUrl')
            name_1 = value.get('name')
            name_2 = value_.get('name')
            self.data['commonAtlasName'] = random_str("自动化企业图册...")
            self.data['commonAtlasDescription'] = random_str("<p>自动化企业图册详细内容数据...</p>\n")
            self.data['commonAtlasSummary'] = random_str("自动化企业图册描述数据...")
            self.data['keywords'] = random_str("关键词...")

            self.data['atlasCategoryArr'] = [f"{class_id}"]
            self.data["atlasImgs"][0]['id'] = f"{id_1}"
            self.data["atlasImgs"][0]['imgId'] = f"{id_1}"
            self.data["atlasImgs"][0]['thumbId'] = f"{id_1}"
            self.data["atlasImgs"][0]['name'] = name_1
            self.data["atlasImgs"][0]['relativeImgUrl'] = img_url
            self.data["atlasImgs"][0]['imgUrl'] = img_url
            self.data["atlasImgs"][0]['thumbUrl'] = img_url
            self.data["atlasImgs"][0]['relativeThumbUrl'] = img_url
            self.data["atlasImgs"][1]['atlasCategoryArr'] = [class_id]
            self.data["atlasImgs"][1]['id'] = f"{id_2}"
            self.data["atlasImgs"][1]['imgId'] = f"{id_2}"
            self.data["atlasImgs"][1]['thumbId'] = f"{id_2}"
            self.data["atlasImgs"][1]['name'] = name_2
            self.data["atlasImgs"][1]['relativeImgUrl'] = img_url_1
            self.data["atlasImgs"][1]['imgUrl'] = img_url_1
            self.data["atlasImgs"][1]['thumbUrl'] = img_url_1
            self.data["atlasImgs"][1]['relativeThumbUrl'] = img_url_1
                
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
    def test_imageupload_atlas(self):
        # 本地文件上传
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            file_path = Any_Path("File", "edit.jpg")
            del self.headers[self.type]
            f = open(file_path, "rb")
            file = {"file": f}
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.post(url, headers=self.headers, data=self.data, files=file, stream=True, verify=False)
            f.close()
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_image_atlas(self):
        # 更改缩略图
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_pictures()
                img_url = choice(pb_data.picture_ids).get("imgUrl")
            else:
                img_url = choice(pb_data.picture_ids).get("imgUrl")

            img_name = img_url.split("/")[-1]

            url = ConfigYaml(self.projectName).base_url + f"/repository/image/{img_name}"
            r = requests.get(url, headers=self.headers, json=self.data, stream=True, verify=False)
            self.result = r.content
            if self.result:
                self.result = {"status": 200,"msg":"success"}

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_link_atlas(self):
        # 添加链接
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_sort_atlas(self):
        # 拖拽排序
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if len(pb_data.atlas_ids) > 2:
                value = pb_data.atlas_ids[0]
                value_ = pb_data.atlas_ids[1]
            else:
                my_data.add_atlas()
                my_data.add_atlas()
                pb_data.atlas_ids = my_data.get_atlas()
                value = pb_data.atlas_ids[0]
                value_ = pb_data.atlas_ids[1]
            id_one = value.get("id")
            id_two = value_.get("id")
            url = ConfigYaml(self.projectName).base_url + self.url + f"&sectionIds={id_one}&targetId={id_two}&minOrder=9&maxOrder=10&direction=-1"
            r = requests.get(url, headers=self.headers, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_delete_atlas(self):
        # 删除
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if not pb_data.atlas_ids:
                pb_data.atlas_ids = my_data.get_atlas()
                id = pb_data.atlas_ids.pop(0).get("id")
            else:
                id = pb_data.atlas_ids.pop(0).get("id")
            url = ConfigYaml(self.projectName).base_url + self.url + f"&id={id}"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_deleteMulti_atlas(self):
        # 删除
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if len(pb_data.atlas_ids) > 2:
                id_1 = pb_data.atlas_ids.pop(0).get("id")
                id_2 = pb_data.atlas_ids.pop(1).get("id")
            else:
                my_data.add_atlas()
                my_data.add_atlas()
                pb_data.atlas_ids = my_data.get_atlas()
                id_1 = pb_data.atlas_ids.pop(0).get("id")
                id_2 = pb_data.atlas_ids.pop(1).get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&atlasIds={id_1},{id_2}"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_addmuchclass_atlas(self):
        # 添加多分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_pictures()
                value = choice(pb_data.picture_ids)
            else:
                value = choice(pb_data.picture_ids)
            img_url = value.get('imgUrl')
            id = value.get('id')
            name = value.get('name')
            if len(pb_data.class_ids) > 2:
                class_id_1 = pb_data.class_ids[0].get("id")
                class_id_2 = pb_data.class_ids[1].get("id")
            else:
                my_data.add_class()
                my_data.add_class()
                pb_data.class_ids = my_data.get_class()
                class_id_1 = pb_data.class_ids[0].get("id")
                class_id_2 = pb_data.class_ids[1].get("id")

            self.data['commonAtlasName'] = random_str("自动化企业图册...")
            self.data['commonAtlasDescription'] = random_str("<p>自动化企业图册详细内容数据...</p>\n")
            self.data['commonAtlasSummary'] = random_str("自动化企业图册描述数据...")
            self.data['keywords'] = random_str("关键词...")
            self.data['atlasCategoryArr'] = [f"{class_id_1}", f"{class_id_2}"]
            self.data["atlasImgs"][0]['id'] = f"{id}"
            self.data["atlasImgs"][0]['imgId'] = f"{id}"
            self.data["atlasImgs"][0]['thumbId'] = f"{id}"
            self.data["atlasImgs"][0]['name'] = name
            self.data["atlasImgs"][0]['relativeImgUrl'] = img_url
            self.data["atlasImgs"][0]['imgUrl'] = img_url
            self.data["atlasImgs"][0]['thumbUrl'] = img_url
            self.data["atlasImgs"][0]['relativeThumbUrl'] = img_url
                
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
    def test_addclass_atlas(self):
        # 快捷添加分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_pictures()
                value = choice(pb_data.picture_ids)
            else:
                value = choice(pb_data.picture_ids)
            img_url = value.get('imgUrl')
            img_id = value.get('id')

            self.data['atlasCategory']['name'] = random_str("自动化企业图册分类...")
            self.data['atlasCategory']['imgUrl'] = img_url
            self.data['atlasCategory']['imgId'] = img_id
            self.data['atlasCategory']['keywords'] = random_str("关键词...")
            self.data['atlasCategory']["imgThumbUrl"] = img_url
            self.data['atlasCategory']["des"] = random_str("自动化企业图册分类描述内容...")
            self.data['atlasCategory']["summary"] = random_str("自动化企业图册分类描述内容...")

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
    def test_content_atlas(self):
        # 相关内容数据获取
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

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
    def test_addcontent_atlas(self):
        # 添加
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_pictures()
                value = choice(pb_data.picture_ids)
            else:
                value = choice(pb_data.picture_ids)
            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")
            if not pb_data.news_ids:
                pb_data.news_ids = my_data.get_news_id()
                news_id = choice(pb_data.news_ids).get("id")
            else:
                news_id = choice(pb_data.news_ids).get("id")

            img_url = value.get('imgUrl')
            id = value.get('id')
            name = value.get('name')
            self.data['commonAtlasName'] = random_str("自动化企业图册...")
            self.data['commonAtlasDescription'] = random_str("<p>自动化企业图册详细内容数据...</p>\n")
            self.data['commonAtlasSummary'] = random_str("自动化企业图册描述数据...")
            self.data['keywords'] = random_str("关键词...")
            self.data['atlasCategoryArr'] = [f"{class_id}"]
            self.data["atlasImgs"][0]['id'] = f"{id}"
            self.data["atlasImgs"][0]['imgId'] = f"{id}"
            self.data["atlasImgs"][0]['thumbId'] = f"{id}"
            self.data["atlasImgs"][0]['name'] = name
            self.data["atlasImgs"][0]['relativeImgUrl'] = img_url
            self.data["atlasImgs"][0]['imgUrl'] = img_url
            self.data["atlasImgs"][0]['thumbUrl'] = img_url
            self.data["atlasImgs"][0]['relativeThumbUrl'] = img_url
            self.data['relevantContentList'][1]['contentList'] = [news_id]
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
    def test_savecontinu_atlas(self):
        # 保存并继续
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_pictures()
                value = choice(pb_data.picture_ids)
            else:
                value = choice(pb_data.picture_ids)
            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")
            if not pb_data.news_ids:
                pb_data.news_ids = my_data.get_news_id()
                news_id = choice(pb_data.news_ids).get("id")
            else:
                news_id = choice(pb_data.news_ids).get("id")

            img_url = value.get('imgUrl')
            id = value.get('id')
            name = value.get('name')
            self.data['commonAtlasName'] = random_str("自动化企业图册...")
            self.data['commonAtlasDescription'] = random_str("<p>自动化企业图册详细内容数据...</p>\n")
            self.data['commonAtlasSummary'] = random_str("自动化企业图册描述数据...")
            self.data['keywords'] = random_str("关键词...")
            self.data['atlasCategoryArr'] = [f"{class_id}"]
            self.data["atlasImgs"][0]['id'] = f"{id}"
            self.data["atlasImgs"][0]['imgId'] = f"{id}"
            self.data["atlasImgs"][0]['thumbId'] = f"{id}"
            self.data["atlasImgs"][0]['name'] = name
            self.data["atlasImgs"][0]['relativeImgUrl'] = img_url
            self.data["atlasImgs"][0]['imgUrl'] = img_url
            self.data["atlasImgs"][0]['thumbUrl'] = img_url
            self.data["atlasImgs"][0]['relativeThumbUrl'] = img_url
            self.data['relevantContentList'][1]['contentList'] = [news_id]

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
    def test_talke_atlas(self):
        # 说明
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            url = self.url.split("?")[0]

            r = requests.get(url, stream=True, verify=False)
            self.result = r.content
            if "keywords" in str(self.result):
                self.result = {"status": 200}

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular


    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_addlink_atlas(self):
        # 添加链接
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")

            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_pictures()
                value = choice(pb_data.picture_ids)
            else:
                value = choice(pb_data.picture_ids)

            img_url = value.get('imgUrl')
            id = value.get('id')
            self.data['atlasCategoryArr'] = [f"{class_id}"]
            self.data['commonAtlasName'] = random_str("自动化企业图册链接...")
            self.data['imgId'] = id
            self.data['linkAtlasName'] = random_str("自动化企业图册链接...")
            self.data['commonAtlasDescription'] = random_str("<p>自动化企业图册详细链接内容数据...</p>\n")
            self.data['linkAtlasSummary'] = random_str("自动化企业图册描述链接数据...")
            self.data['keywordsLink'] = random_str("链接关键词...")
            self.data['imgUrl'] = img_url


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
    def test_muchaddlink_atlas(self):
        # 多选分类链接
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")

            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_pictures()
                value = choice(pb_data.picture_ids)
            else:
                value = choice(pb_data.picture_ids)

            if len(pb_data.class_ids) > 2:
                class_id_1 = pb_data.class_ids[0].get("id")
                class_id_2 = pb_data.class_ids[1].get("id")
            else:
                my_data.add_class()
                my_data.add_class()
                pb_data.class_ids = my_data.get_class()
                class_id_1 = pb_data.class_ids[0].get("id")
                class_id_2 = pb_data.class_ids[1].get("id")

            img_url = value.get('imgUrl')
            id = value.get('id')
            self.data['atlasCategoryArr'] = [f"{class_id}"]
            self.data['imgId'] = id
            self.data['commonAtlasName'] = random_str("自动化企业图册链接...")
            self.data['linkAtlasName'] = random_str("自动化企业图册链接...")
            self.data['commonAtlasDescription'] = random_str("<p>自动化企业图册详细链接内容数据...</p>\n")
            self.data['linkAtlasSummary'] = random_str("自动化企业图册描述链接数据...")
            self.data['keywordsLink'] = random_str("链接关键词...")
            self.data['imgUrl'] = img_url
            self.data['atlasCategoryArr'] = [f"{class_id_1}",f"{class_id_2}"]
                
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
    def test_list_atlas(self):
        # 添加链接
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_sortcom_atlas(self):
        # 企业图册库列表
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if len(pb_data.atlas_ids) > 2:
                id_one = pb_data.atlas_ids[0].get("id")
                id_two = pb_data.atlas_ids[1].get("id")
            else:
                my_data.add_atlas()
                my_data.add_atlas()
                pb_data.atlas_ids = my_data.get_atlas()
                id_one = pb_data.atlas_ids[0].get("id")
                id_two = pb_data.atlas_ids[1].get("id")

            del self.headers[self.type]

            url = ConfigYaml(self.projectName).base_url + self.url + f"&sectionIds={id_one}&targetId={id_two}&minOrder={id_one}&maxOrder={id_two}&direction=-1"
            r = requests.get(url, headers=self.headers, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_headsort_atlas(self):
        # 表头排序
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
    def test_atlas_page_atlas(self):
        # 搜索
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not pb_data.atlas_ids:
                pb_data.atlas_ids = my_data.get_atlas()
                name = choice(pb_data.atlas_ids).get("name")
            else:
                name = choice(pb_data.atlas_ids).get("name")

            self.data["keywords"] = name

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
    def test_shaixuan_atlas(self):
        # 筛选
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
    def test_update_atlas(self):
        # 编辑
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not pb_data.atlas_ids:
                pb_data.atlas_ids = my_data.get_atlas()
                id = choice(pb_data.atlas_ids).get("id")
            else:
                id = choice(pb_data.atlas_ids).get("id")
            self.data['commonAtlasName'] = random_str("编辑后的企业图册链接...")
            self.data['id'] = id

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
    def test_transfer_atlas(self):
        # 转移
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.atlas_ids:
                pb_data.atlas_ids = my_data.get_atlas()
                id = choice(pb_data.atlas_ids).get("id")
            else:
                id = choice(pb_data.atlas_ids).get("id")
            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")

            url = ConfigYaml(self.projectName).base_url + self.url +f"&atlasIds={id}&categoryIds={class_id}"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_piliangtransfer_atlas(self):
        # 批量转移
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if len(pb_data.atlas_ids) > 2:
                id = pb_data.atlas_ids[0].get("id")
                id_2 = pb_data.atlas_ids[1].get("id")
            else:
                my_data.add_atlas()
                my_data.add_atlas()
                pb_data.atlas_ids = my_data.get_atlas()
                id = pb_data.atlas_ids[0].get("id")
                id_2 = pb_data.atlas_ids[1].get("id")
            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&atlasIds={id},{id_2}&categoryIds={class_id}"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_updateShowPc_atlas(self):
        # 批量转移
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.atlas_ids:
                pb_data.atlas_ids = my_data.get_atlas()
                id = choice(pb_data.atlas_ids).get("id")
            else:
                id = choice(pb_data.atlas_ids).get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&atlasIds={id}&state=1"

            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()


            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_updatehidePc_atlas(self):
        # 批量转移
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.atlas_ids:
                pb_data.atlas_ids = my_data.get_atlas()
                id = choice(pb_data.atlas_ids).get("id")
            else:
                id = choice(pb_data.atlas_ids).get("id")
            url = ConfigYaml(self.projectName).base_url + self.url + f"&atlasIds={id}&state=0"

            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_updatepihidePc_atlas(self):
        # 批量隐藏
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if len(pb_data.atlas_ids) > 2:
                id = pb_data.atlas_ids[0].get("id")
                id_2 = pb_data.atlas_ids[1].get("id")
            else:
                my_data.add_atlas()
                my_data.add_atlas()
                pb_data.atlas_ids = my_data.get_atlas()
                id = pb_data.atlas_ids[0].get("id")
                id_2 = pb_data.atlas_ids[1].get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&atlasIds={id},{id_2}&state=0"

            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_updatepishowPc_atlas(self):
        # 批量显示
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.atlas_ids) > 2:
                id = pb_data.atlas_ids[0].get("id")
                id_2 = pb_data.atlas_ids[1].get("id")
            else:
                my_data.add_atlas()
                my_data.add_atlas()
                pb_data.atlas_ids = my_data.get_atlas()
                id = pb_data.atlas_ids[0].get("id")
                id_2 = pb_data.atlas_ids[1].get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&atlasIds={id},{id_2}&state=1"

            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_deletedata_atlas(self):
        # 删除
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.atlas_ids:
                pb_data.atlas_ids = my_data.get_atlas()
                id = choice(pb_data.atlas_ids).get("id")
            else:
                id = choice(pb_data.atlas_ids).get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&id={id}"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_pildelete_atlas(self):
        # 批量删除
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if len(pb_data.atlas_ids) > 2:
                id = pb_data.atlas_ids.pop(0).get("id")
                id_1 = pb_data.atlas_ids.pop(1).get("id")
            else:
                my_data.add_atlas()
                my_data.add_atlas()
                pb_data.atlas_ids = my_data.get_atlas()
                id = pb_data.atlas_ids.pop(0).get("id")
                id_1 = pb_data.atlas_ids.pop(1).get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&atlasIds={id},{id_1}"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_page_atlas(self):
        # 翻页
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
    def test_adatlasca_atlas(self):
        # 添加普通分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_pictures()
                value = choice(pb_data.picture_ids)
            else:
                value = choice(pb_data.picture_ids)

            img_url = value.get('imgUrl')
            img_id = value.get('id')

            self.data['atlasCategory']['name'] = random_str("自动化普通企业图册分类...")
            self.data['atlasCategory']['imgUrl'] = img_url
            self.data['atlasCategory']['imgId'] = img_id
            self.data['atlasCategory']['keywords'] = random_str("普通关键词...")
            self.data['atlasCategory']["imgThumbUrl"] = img_url
            self.data['atlasCategory']["des"] = random_str("自动化普通企业图册分类描述内容...")
            self.data['atlasCategory']["summary"] = random_str("自动化普通企业图册分类描述内容...")

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
    def test_adlink_atlas(self):
        # 添加链接分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_pictures()
                value = choice(pb_data.picture_ids)
            else:
                value = choice(pb_data.picture_ids)

            img_url = value.get('imgUrl')
            img_id = value.get('id')

            self.data['atlasCategory']['name'] = random_str("自动化链接企业图册分类...")
            self.data['atlasCategory']['imgUrl'] = img_url
            self.data['atlasCategory']['imgThumbUrl'] = img_url
            self.data['atlasCategory']['imgId'] = img_id
            self.data['atlasCategory']['keywords'] = random_str("链接关键词...")
            self.data['atlasCategory']["imageUrl"] = img_url
            self.data['atlasCategory']["des"] = random_str("自动化链接企业图册分类描述内容...")
            self.data['atlasCategory']["summary"] = random_str("自动化链接企业图册分类描述内容...")
                
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
    def test_selectlink_atlas(self):
        # 添加链接分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
                
            url = ConfigYaml(self.projectName).base_url + self.url
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_adlinkji_atlas(self):
        # 保存继续
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_pictures()
                value = choice(pb_data.picture_ids)
            else:
                value = choice(pb_data.picture_ids)

            img_url = value.get('imgUrl')
            img_id = value.get('id')

            self.data['atlasCategory']['name'] = random_str("自动化链接企业图册分类...")
            self.data['atlasCategory']['imgUrl'] = img_url
            self.data['atlasCategory']['imgThumbUrl'] = img_url
            self.data['atlasCategory']['imgId'] = img_id
            self.data['atlasCategory']['keywords'] = random_str("链接关键词...")
            self.data['atlasCategory']["imageUrl"] = img_url
            self.data['atlasCategory']["des"] = random_str("自动化链接企业图册分类描述内容...")
            self.data['atlasCategory']["summary"] = random_str("自动化链接企业图册分类描述内容...")
                
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
    def test_edite_atlas(self):
        # 编辑分类
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:

            if not pb_data.picture_ids:
                pb_data.picture_ids = my_data.get_pictures()
                value = choice(pb_data.picture_ids)
            else:
                value = choice(pb_data.picture_ids)
            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class()
                id = choice(pb_data.class_ids).get("id")
            else:
                id = choice(pb_data.class_ids).get("id")

            img_url = value.get('imgUrl')
            img_id = value.get('id')

            self.data["atlasCategory"]['id'] = id
            self.data["atlasCategory"]['name'] = random_str("编辑后的企业图册分类...")
            self.data["atlasCategory"]['imgUrl'] = img_url
            self.data["atlasCategory"]['imgId'] = img_id
            self.data["atlasCategory"]['keywords'] = random_str("编辑后的关键词...")
            self.data["atlasCategory"]["imgThumbUrl"] = img_url
            self.data["atlasCategory"]["des"] = random_str("编辑后的企业图册分类描述内容...")
            self.data["atlasCategory"]["summary"] = random_str("编辑后的企业图册分类描述内容...")

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
    def test_mobileshow_atlas(self):
        # 移动端显示
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.atlas_ids:
                pb_data.atlas_ids = my_data.get_atlas()
                id = choice(pb_data.atlas_ids).get("id")
            else:
                id = choice(pb_data.atlas_ids).get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&atlasIds={id}&state=1"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_mobilehide_atlas(self):
        # 移动端隐藏
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.atlas_ids:
                pb_data.atlas_ids = my_data.get_atlas()
                id = choice(pb_data.atlas_ids).get("id")
            else:
                id = choice(pb_data.atlas_ids).get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&atlasIds={id}&state=0"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_mobilepihide_atlas(self):
        # 移动端批量隐藏
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.atlas_ids) > 2:
                id = pb_data.atlas_ids[0].get("id")
                id_ = pb_data.atlas_ids[1].get("id")
            else:
                my_data.add_atlas()
                my_data.add_atlas()
                pb_data.atlas_ids = my_data.get_atlas()
                id = pb_data.atlas_ids[0].get("id")
                id_ = pb_data.atlas_ids[1].get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&atlasIds={id},{id_}&state=0"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_mobilepishow_atlas(self):
        # 移动端批量显示
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.atlas_ids) > 2:
                id = pb_data.atlas_ids[0].get("id")
                id_ = pb_data.atlas_ids[1].get("id")
            else:
                my_data.add_atlas()
                my_data.add_atlas()
                pb_data.atlas_ids = my_data.get_atlas()
                id = pb_data.atlas_ids[0].get("id")
                id_ = pb_data.atlas_ids[1].get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&atlasIds={id},{id_}&state=1"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_resort_atlas(self):
        # 拖拽排序
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type
            if len(pb_data.class_ids) > 2:
                class_id_1 = pb_data.class_ids[0].get("id")
                class_id_2 = pb_data.class_ids[1].get("id")
            else:
                my_data.add_class()
                my_data.add_class()
                pb_data.class_ids = my_data.get_class()
                class_id_1 = pb_data.class_ids[0].get("id")
                class_id_2 = pb_data.class_ids[1].get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&id={class_id_1}&targetId={class_id_2}&type=above"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_move_atlas(self):
        # 转移
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if len(pb_data.class_ids) > 2:
                class_id_1 = pb_data.class_ids[0].get("id")
                class_id_2 = pb_data.class_ids[1].get("id")
            else:
                my_data.add_class()
                my_data.add_class()
                pb_data.class_ids = my_data.get_class()
                class_id_1 = pb_data.class_ids[0].get("id")
                class_id_2 = pb_data.class_ids[1].get("id")
                
            url = ConfigYaml(self.projectName).base_url + self.url + f"&id={class_id_1}&targetId={class_id_2}"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_updateshowstate_atlas(self):
        # 显示电脑端
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&id={class_id}&flag=1"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_updatehidestate_atlas(self):
        # 隐藏电脑端
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class()
                class_id = choice(pb_data.class_ids).get("id")
            else:
                class_id = choice(pb_data.class_ids).get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&id={class_id}&flag=0"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_emobileshowstate_atlas(self):
        # 显示电脑端
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class()
                id = choice(pb_data.class_ids).get("id")
            else:
                id = choice(pb_data.class_ids).get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&id={id}&flag=1"
            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
        

    # @unittest.skipIf(condition, "暂时跳过")
    @ReRun(MyTest.setUp)
    def test_emobilehidestate_atlas(self):
        # 隐藏电脑端
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if self.type_condition:
                self.headers[self.type] = self.form_type

            if not pb_data.class_ids:
                pb_data.class_ids = my_data.get_class()
                id = choice(pb_data.class_ids).get("id")
            else:
                id = choice(pb_data.class_ids).get("id")

            url = ConfigYaml(self.projectName).base_url + self.url + f"&id={id}&flag=0"

            r = requests.get(url, headers=self.headers, data=self.data, stream=True, verify=False)
            self.result = r.json()

            self.time = r.elapsed.total_seconds()
        except:
            self.singular = str(traceback.format_exc())
            outcome('red', self.singular)
            return self.singular
