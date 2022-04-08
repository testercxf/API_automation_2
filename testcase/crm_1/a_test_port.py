import  pytest
import requests
from common.yaml_util import YamlUtil

class Testsendrequest():

    @pytest.mark.parametrize('caseinfo',YamlUtil().read_crmcases_yaml("crm_user_file.yaml"))
    def test_crm_imgae(self,caseinfo):
        '''上传文件'''
        #读取extract.yam的token
        Admin_Token = YamlUtil().read_yaml("Admin-Token")
        print(caseinfo['name'])
        method = caseinfo['request']['method']
        url = YamlUtil().read_config_yaml("config.yaml","ip")+caseinfo['request']['url']
        data = caseinfo['request']['data']
        files = caseinfo['request']['files']
        header = {
            'Admin-Token':Admin_Token
        }
        rep = requests.request(method,url,data=data,files=files,headers=header)
        print(rep.json())
        #断言：code的值是否等于0
        assert rep.json()['code'] == 0


    @pytest.mark.parametrize("caseinfo",YamlUtil().read_crmcases_yaml("crm_tasklist.yaml"))
    def test_crm_tasklist(self,caseinfo):
        '''首页全部任务列表'''
        Admin_Token = YamlUtil().read_yaml("Admin-Token")
        print(caseinfo['name'])
        method = caseinfo['request']['method']
        url = YamlUtil().read_config_yaml("config.yaml","ip")+caseinfo['request']['url']
        data = caseinfo['request']['data']
        header = {
            'Admin-Token':Admin_Token
        }
        rep = requests.request(method,url=url,data=data,headers=header)
        print(rep.json())
        #断言：全部任务列表框的关键字是否为“任务”
        if rep.json()['data']['list'] !="":
            print("任务列表有数据")
        else:
            print("暂无任务")


    @pytest.mark.parametrize("caseinfo",YamlUtil().read_crmcases_yaml("crm_righttask.yaml"))
    def test_crm_righttask(self,caseinfo):
        '''右边任务列表'''
        Admin_Token = YamlUtil().read_yaml("Admin-Token")
        print(caseinfo['name'])
        method = caseinfo['request']['method']
        url = YamlUtil().read_config_yaml("config.yaml","ip")+caseinfo['request']['url']
        header = {
            "Admin-Token":Admin_Token
        }
        rep = requests.request(method,url,headers=header)
        print(rep.json())
        if rep.json()['data'] !="":
            print("任务列表有数据")
        else:
            print("任务列表为空")



