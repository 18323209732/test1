import requests
import pytest
from jsonpath import jsonpath
from requests_xml import XMLSession
from hamcrest import *
from requests.auth import HTTPBasicAuth

class TestDemo:
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level":1,
            "name":'yqsz',

        }
        r = requests.get('https://httpbin.testing-studio.com/get',params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": 'yqsz',

        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_header(self):
        r = requests.get('https://httpbin.testing-studio.com/get',headers={"h":"header demo"})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['headers']['H'] =="header demo"

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": 'yqsz',

        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()["json"]['level'] == 1

    def test_hogwarts_json(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '霍格沃兹测试学院公众号'
        assert jsonpath(r.json(),'$..name')[0] == '霍格沃兹测试学院公众号'

    def test_hamcrest(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert jsonpath(r.json(), '$..name')[0] == '霍格沃兹测试学院公众号'
        assert_that(r.json()['category_list']['categories'][0]['name'],equal_to('霍格沃兹测试学院公众号'))

    def test_cookies(self):
        header = {
            'User-Agent': 'hogwarts'
                  }
        cookie_data = {
            "hogwarts":'school',
            "teacher":"AD"
        }
        r = requests.get('https://httpbin.testing-studio.com/cookies',headers = header,cookies = cookie_data)
        print(r.request.headers)

    def test_auth(self):
        r = requests.get("https://httpbin.testing-studio.com/basic-auth/banana/123",auth = HTTPBasicAuth("banana","123"))
        print(r.text)