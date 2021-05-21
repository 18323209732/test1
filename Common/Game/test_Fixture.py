import pytest
#
# @pytest.fixture()
# def login():
#     print("需要登陆")
#
# class TestDemo:
#     def setup(self):
#         print("第一步，打开浏览器")
#     def teardown(self):
#         print("第五步，关闭浏览器")
#     def test_a(self):
#         print("test_a")
#         pass
#     def test_b(self):
#         print("test_b")
#         pass
#     def test_c(self):
#         print("test_c")
#         pass


def provider():
    for i in range(5):
        yield i

p = provider()
print(next(p))
print(next(p))
print(next(p))
print(next(p))