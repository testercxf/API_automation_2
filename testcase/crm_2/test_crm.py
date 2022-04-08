import requests
import pytest
from common.yaml_util import YamlUtil

class   Testsendcrm:

    @pytest.mark.parametrize("args",YamlUtil().read_crm_yaml("crm_work_a.yaml"))
    def test_work_a(self,args):
        """办公模块的公告列表"""
        Admin_Token = YamlUtil().read_yaml("Admin-Token")
        print(args['name'])
        method = args['request']['method']
        url = YamlUtil().read_config_yaml('config.yaml','ip')+args['request']['url']
        data = args['request']['data']
        headers = {
            "Admin-Token":Admin_Token
        }
        rep = requests.request(method,url,json=data,headers=headers)
        print(rep.json())
        #断言：返回的code码是否为0
        assert  rep.json()['code'] == 0


    @pytest.mark.parametrize("args",YamlUtil().read_crm_yaml("crm_work_task.yaml"))
    def test_work_task(self,args):
        """办公模块的任务列表"""
        Admin_Token = YamlUtil().read_yaml('Admin-Token')
        print(args['name'])
        method = args['request']['method']
        url = YamlUtil().read_config_yaml('config.yaml','ip')+args['request']['url']
        data = args['request']['data']
        headers = {
            "Admin-Token":Admin_Token
        }
        rep = requests.request(method,url,json=data,headers=headers)
        print(rep.json())
        # 断言：返回的报文里是否包含关键字并且返回的code码是否为0
        assert  "陈雪峰" in  rep.text and rep.json()['code'] == 0


    @pytest.mark.parametrize("args", YamlUtil().read_crm_yaml("crm_work_ea.yaml"))
    def test_work_eaa(self, args):
        """办公模块的审批列表"""
        Admin_Token = YamlUtil().read_yaml('Admin-Token')
        print(args['name'])
        method = args['request']['method']
        url = YamlUtil().read_config_yaml('config.yaml', 'ip') + args['request']['url']
        data = args['request']['data']
        headers = {
            "Admin-Token": Admin_Token
        }
        rep = requests.request(method,url,json=data,headers=headers)
        print(rep.json())
        # 断言：返回的code码是否为0
        assert  rep.json()['code'] == 0


    @pytest.mark.parametrize("args",YamlUtil().read_crm_yaml("crm_bi_staff.yaml"))
    def test_bi(self,args):
        """商业智能模块的查询员工客户信息"""
        Admin_Token = YamlUtil().read_yaml("Admin-Token")
        print(args['name'])
        method = args['request']['method']
        url = YamlUtil().read_config_yaml("config.yaml","ip")+args['request']['url']
        data = args['request']['data']
        headers = {
            "Admin-Token": Admin_Token
        }
        rep = requests.request(method,url,data=data,headers=headers)
        print(rep.json())
        # 断言：返回的code码是否为0
        assert rep.json()['code'] == 0


    @pytest.mark.parametrize("args",YamlUtil().read_crm_yaml("crm_bi_pm.yaml"))
    def test_bi_pm(self,args):
        """商业智能模块的2021年业绩目标完成情况"""
        Admin_Token = YamlUtil().read_yaml("Admin-Token")
        print(args['name'])
        method = args['request']['method']
        url = YamlUtil().read_config_yaml("config.yaml","ip")+args['request']['url']
        data = args['request']['data']
        headers = {
            "Admin-Token":Admin_Token
        }
        rep = requests.request(method,url,data=data,headers=headers)
        print(rep.json())
        #断言：月份是否为空
        # reps = rep.json()['data']
        # for i in range(len(reps)):
        #     j = reps[i]
        #     month = j['month']
        #     if month != '':
        #         pass
        #     else:
        #         raise Exception("月份有空值")


    @pytest.mark.parametrize("args",YamlUtil().read_crm_yaml("crm_bi_rk.yaml"))
    def test_bi_rk(self,args):
        """商业智能模块的本年回款金额排行"""
        Admin_Token = YamlUtil().read_yaml("Admin-Token")
        print(args['name'])
        method = args['request']['method']
        url = YamlUtil().read_config_yaml("config.yaml","ip")+args['request']['url']
        data = args['request']['data']
        headers = {
            "Admin-Token":Admin_Token
        }
        rep = requests.request(method,url,data=data,headers=headers)
        print(rep.json())
        # 断言：返回的code码是否为0
        assert rep.json()['code'] == 0


    @pytest.mark.parametrize("args", YamlUtil().read_crm_yaml("crm_project_new.yaml"))
    def test_project_new(self, args):
        """项目管理模块的创建项目"""
        Admin_Token = YamlUtil().read_yaml('Admin-Token')
        print(args['name'])
        method = args['request']['method']
        url = YamlUtil().read_config_yaml('config.yaml', 'ip') + args['request']['url']
        data = args['request']['data']
        headers = {
            "Admin-Token": Admin_Token
        }
        rep = requests.request(method,url,data=data, headers=headers)
        print(rep.json())
        # 断言：返回的code码是否为0并且断言关键字
        assert rep.json()['code'] == 0   and  rep.json()['data'][0]['roleName'] == "管理"


    @pytest.mark.parametrize("args", YamlUtil().read_crm_yaml("crm_project_message.yaml"))
    def test_project_message(self, args):
        """项目管理模块的项目信息"""
        Admin_Token = YamlUtil().read_yaml('Admin-Token')
        print(args['name'])
        method = args['request']['method']
        url = YamlUtil().read_config_yaml('config.yaml', 'ip') + args['request']['url']
        data = args['request']['data']
        headers = {
            "Admin-Token": Admin_Token
        }
        rep = requests.request(method, url, data=data, headers=headers)
        print(rep.json())
        # 断言：返回的code码是否为0
        assert  rep.json()['code'] == 0


    @pytest.mark.parametrize("args", YamlUtil().read_crm_yaml("crm_project_rb.yaml"))
    def test_bi_staff(self, args):
        """项目管理模块的回收站列表"""
        Admin_Token = YamlUtil().read_yaml('Admin-Token')
        print(args['name'])
        method = args['request']['method']
        url = YamlUtil().read_config_yaml('config.yaml', 'ip') + args['request']['url']
        data = args['request']['data']
        headers = {
            "Admin-Token": Admin_Token
        }
        rep = requests.request(method, url, json=data, headers=headers)
        print(rep.json())
        # 断言：返回的code码是否为0
        assert  rep.json()['code'] == 0