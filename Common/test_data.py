import pytest
import yaml
# class TestData:
#     @pytest.mark.parametrize(["a","b"],yaml.safe_load(open("./data.yaml")))
#     def test_data(self,a,b):
#         print(a+b)

class TestDemo:
    # @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yaml")))
    # def test_demo(self,env):
    #     if "test" in env:
    #         print("这是测试环境")
    #         print("测试环境ip是：",env["test"])
    #     elif "dev" in env:
    #         print("这是开发环境")
    #         print("开发环境ip是:",env["dev"])

    @pytest.mark.parametrize("data",yaml.safe_load(open("./data.yaml")))
    def test_demo2(self,data):
        if "yqsz" in data:
            print("易强是个大傻X")
            print("隆重介绍：",data["yqsz"])
        elif "js" in data:
            print("洪江是个大帅哥")
            print("隆重介绍：",data["js"])
