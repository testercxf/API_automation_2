import  os
import yaml

class  YamlUtil:

    #读取extract.yaml文件
    def read_yaml(self,key):
        #获得根目录然后打开yml文件，并读取。然后作为一个文件流
        with open(os.getcwd()+"/extract.yaml",mode="r",encoding="utf-8") as f:
            #传入文件流，Loader=yaml.FullLoader：加载所有。读取所有数据
             value = yaml.load(stream=f,Loader=yaml.FullLoader)
             return  value[key]

    #写入extract.yaml
    def  write_yaml(self,data):
        with open(os.getcwd()+"/extract.yaml",mode="a",encoding="utf-8") as f:
            #data=data：数据来源  allow_unicode=True：允许使用unicode编码
             yaml.dump(stream=f,data=data,allow_unicode=True)

    #清除extract.yaml
    def claer_yaml(self):
        with open(os.getcwd()+"/extract.yaml",mode="w",encoding="utf-8") as f:
            f.truncate()

    #读取测试用例crm_1的yaml文件
    def read_crmcases_yaml(self,yaml_name):
        with open(os.getcwd()+"/testcase/crm_1/"+yaml_name,mode="r",encoding="utf-8") as f:
             value = yaml.load(stream=f,Loader=yaml.FullLoader)
             return  value

    #读取测试用例crm_2的yaml文件
    def read_crm_yaml(self,yaml_name):
        with open(os.getcwd()+"/testcase/crm_2/"+yaml_name,mode="r",encoding="utf-8") as f:
             value = yaml.load(stream=f,Loader=yaml.FullLoader)
             return value


    #读取config.yaml文件
    def read_config_yaml(self,name_yaml,key):
        with open(os.getcwd()+"/.//"+name_yaml,mode="r",encoding="utf-8") as f:
             value = yaml.load(stream=f,Loader=yaml.FullLoader)
             return  value[key]

