
# coding=utf-8
from ruamel.yaml import RoundTripDumper
from Common.Route import Any_Path
import yaml


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
            yaml.dump(data, yaml_file,  allow_unicode=True)
        else:
            yaml.dump(data, yaml_file, Dumper=RoundTripDumper, allow_unicode=True)