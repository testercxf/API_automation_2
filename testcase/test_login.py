import allure
import pytest
import requests
from common.yaml_util import YamlUtil

class  TestLogin:


    @allure.severity(allure.severity_level.BLOCKER)     #标记用例等级
    # 实现用例参数化
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_crmcases_yaml("crm_login.yaml"))
    def test_crm_login(self, caseinfo):
        '''悟空crm登录'''
        print(caseinfo['name'])
        method = caseinfo['request']['method']
        url = YamlUtil().read_config_yaml("config.yaml", "ip") + caseinfo['request']['url']
        data = caseinfo['request']['data']
        rep = requests.request(method, url=url, data=data)
        # 断言：如果返回的响应里没有Admin-Token就不写入token值到extract.yml
        if "Admin-Token" in rep.json():
            YamlUtil().write_yaml({"Admin-Token": rep.json()['Admin-Token']})
        else:
            print("token写入失败！")