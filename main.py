# 1. 区分文件类型，不同解析方式
# 2. 必要参数必填
# 3. 放入全局变量
from util import variable as var
from config import config as config



if __name__ == "__main__":
    '''初始化配置类'''
    var._init()
    c = config.PutConfig('./application/a.yml')
    c.put_config()
    print(var.get_value("config"))

    
    

