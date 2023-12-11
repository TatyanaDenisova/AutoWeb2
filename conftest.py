import pytest
from module import Site
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    


@pytest.fixture()
def log_xpath():
    return """//*[@id="login"]/div[1]/label/input"""

@pytest.fixture()
def pass_xpath():
    return """//*[@id="login"]/div[2]/label/input"""

@pytest.fixture()
def btn_xpath():
    return """//*[@id="login"]/div[3]/button"""

@pytest.fixture()
def result_xpath():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def result_login():
    return """//*[@id="app"]/main/div/div[1]/h1"""

@pytest.fixture()
def btn_create():
    return """//*[@id="create-btn"]"""

@pytest.fixture()
def title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label"""

@pytest.fixture()
def description():
    return """//*[@id="create-item"]/div/div/div[2]/div/label"""

@pytest.fixture()
def content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture()
def date():
    return """//*[@id="create-item"]/div/div/div[5]/div/div/label/input"""


@pytest.fixture()
def post_btn():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""

@pytest.fixture()
def post_result():
    return """//*[@id="app"]/main/div/div[1]/div/div[3]"""

@pytest.fixture()
def site():
    my_site = Site(testdata["address"])
    yield my_site
    my_site.close()