
import yaml		#导入yaml模块

#封装一个类方法
class RWyaml(object):

    def __init__(self, file_name):
        self.y = yaml
        self.file = file_name   #yaml文件绝对路径

    #字典形式读取所有内容
    def read_yaml_all(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            # return self.y.load(f, Loader=self.y.FullLoader)
            return self.y.load(f)


    #写入（完善了下，可修改key值,但不使用空表）
    def write_yaml(self, nb, key, value):
        data = {nb: {key: value}}
        old_data = self.read_yaml_all()

        if nb in old_data:
            old_data[nb][key] = value
            with open(self.file, 'w', encoding='utf-8') as f:
                self.y.dump(old_data, f)
                # print('写入成功：%s' % old_data)
        else:
            with open(self.file, 'a', encoding='utf-8') as f:
                self.y.dump(data, f)
                # print('写入成功：%s' % data)

    #读取节点下面key的值
    def read_yaml_value(self, nb, key):
        with open(self.file, 'r', encoding='utf-8') as f:
            # data = self.y.load(f, Loader=self.y.FullLoader)
            data = self.y.load(f)
            try:
                if nb in data.keys():
                    return data[nb][key]
                else:
                    print('节点nb:%s不存在！' % nb)
            except KeyError as e:
                print('key：%s不存在！' % key)


if __name__=='__main__':
	#执行
    import os
    path = os.path.dirname(os.path.abspath('.')) + '/Door/content/Public.yaml'

    yaml = RWyaml(path)
    # yaml.write_yaml('nb2', 'name', 'Tom')
    print(yaml.read_yaml_value('nb1', 'name'))
    print(yaml.read_yaml_all())