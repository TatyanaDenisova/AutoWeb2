import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)




def test_step1(site, log_xpath, pass_xpath, btn_xpath, result_xpath):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys("test")
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys("test")
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    err_lable = site.find_element("xpath", result_xpath)
    assert err_lable.text == "401"

def test_step2(site, log_xpath, pass_xpath, btn_xpath, result_login):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata["password"])
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    blog = site.find_element("xpath", result_login)
    assert blog.text == "Blog"


def test_step3(site, log_xpath, pass_xpath, btn_xpath, btn_create, title, description, content, date, post_btn, post_result):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata["password"])
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    create = site.find_element("xpath", btn_create)
    create.click()
    input3 = site.find_element("xpath", title)
    input3.send_keys(testdata["title"])
    input4 = site.find_element("xpath", description)
    input4.send_keys(testdata["description"])
    input5 = site.find_element("xpath", content)
    input5.send_keys(testdata["content"])
    input6 = site.find_element("xpath", date)
    input6.send_keys(testdata["date"])
    btn2 = site.find_element("xpath", post_btn)
    btn2.click()
    post = site.find_element("xpath", post_result)
    assert post.text == "text new text"

