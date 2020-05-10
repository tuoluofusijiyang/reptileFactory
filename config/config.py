import os,yaml,abc,json
from util import variable as var


class Config(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read_file(self):
        pass


class JsonConfig(Config):
    def __init__(self,file_name):
        self.file_name = file_name
    '''读取JSON配置，放入全局变量'''
    def read_file(self):
        # 读取json文件内容,返回字典格式
        with open(self.file_name, 'r', encoding='utf8')as fp:
            json_data = json.load(fp)
            var.set_value('config',json_data)


class YamlConfig(Config):
    def __init__(self,file_name):
        self.file_name = file_name
    '''读取yaml配置，放入全局变量'''
    def read_file(self):
        # 读取yml文件内容,返回字典格式
        with open(self.file_name, 'r', encoding='utf8')as fp:
            json_data = yaml.load(fp, Loader=yaml.FullLoader)
            var.set_value('config', json_data)


class PutConfig():
    def __init__(self,file_name):
        self.file_name = file_name

    '''判断文件后缀名称，放入全局变量'''
    def put_config(self):
        if self.file_name.endswith('.json'):
            JsonConfig(self.file_name).read_file()
        elif self.file_name.endswith('.yml'):
            YamlConfig(self.file_name).read_file()
        else:
            raise BaseException('未适配的类型文件')