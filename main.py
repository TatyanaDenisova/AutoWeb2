import yaml
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])

if __name__ == "__main__":
    css_selector = "span.mdc-floating-label"
    print(site.get_element_property("css", css_selector, "height"))
    xpath = """ //*[@id="login"]/div[3]/button/span"""
    print(site.get_element_property("xpath", xpath, "color"))

