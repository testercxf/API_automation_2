import pytest
import  os

if  __name__ == "__main__":
    pytest.main()
    #指定生成报告的路径
    os.system("allure generate  ./temp   -o  ./reports  --clean")
