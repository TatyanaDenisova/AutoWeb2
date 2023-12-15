from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_RESULT_LOGIN = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_BTN_CREATE = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_POST_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label""")
    LOCATOR_POST_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label""")
    LOCATOR_POST_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_POST_DATE = (By.XPATH, """//*[@id="create-item"]/div/div/div[5]/div/div/label/input""")
    LOCATOR_POST_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_POST_RESULT = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTACT_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACT_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text
    
    def get_text_blog(self):
        text_field = self.find_element(TestSearchLocators.LOCATOR_RESULT_LOGIN, time=3)
        text = text_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def click_button_create(self):
        logging.info("Click create post button")
        self.find_element(TestSearchLocators.LOCATOR_BTN_CREATE).click()

    def enter_title_post(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_POST_TITLE[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE)
        login_field.send_keys(word)


    def enter_content_post(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_POST_CONTENT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_POST_CONTENT)
        login_field.clear()
        login_field.send_keys(word)


    def click_post_button(self):
        logging.info("Click 'to save post' button")
        self.find_element(TestSearchLocators.LOCATOR_POST_BTN).click()

    def get_post(self):
        post_field = self.find_element(TestSearchLocators.LOCATOR_POST_RESULT, time=3)
        text = post_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_POST_RESULT[1]}")
        return text

    def click_contact(self):
        logging.info("Click contact")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT).click()

    def enter_your_name(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_NAME[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_NAME)
        login_field.clear()
        login_field.send_keys(word)

    def enter_your_email(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_EMAIL[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_EMAIL)
        login_field.clear()
        login_field.send_keys(word)

    def enter_your_content(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_CONTENT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_CONTENT)
        login_field.clear()
        login_field.send_keys(word)

    def click_contact_us_btn(self):
        logging.info("Click contact us button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()