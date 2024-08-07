import time

from features.pageObject.BasePage import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)

    def setName(self, name):
        self.type("name_XPATH", name)

    def setPhone(self, phone):
        self.type("phone_XPATH", phone)

    def setEmail(self, email):
        self.type("email_XPATH", email)

    def setCountry(self, country):
        self.select("country_XPATH", country)

    def setCity(self, city):
        self.type("city_XPATH", city)

    def setUsername(self, username):
        self.type("username_XPATH", username)

    def setPassword(self, password):
        self.type("password_XPATH", password)

    def submitForm(self):
        self.click("submit_XPATH")

    def clicklogin(self):
        self.click("loginForm_TAGNAME")
    # def enterusername(self, user):
    #     self.type("enteruser_XPATH", user)
    def movetologin(self):
        self.moveTo("loginpage_XPATH")

    def enterusername(self, user):
        self.type("enteruser_XPATH", user)

    def enterpassword(self, passw):
        self.type("enterpass_XPATH", passw)

    def submitLogin(self):
        self.click("clicksubmit_XPATH")
        time.sleep(2)