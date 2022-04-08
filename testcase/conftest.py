import  pytest
from common.yaml_util import  YamlUtil

# 所有同目录测试文件运行前都会执行conftest.py文件
#用例前置
@pytest.fixture(scope="session",autouse=True)
def clear_extract():
    YamlUtil().claer_yaml()

