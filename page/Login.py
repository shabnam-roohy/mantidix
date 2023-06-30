class Login:
    def __init__(self, browser):
        self.browser = browser
        self.username_textbox_name = "username"
        self.password_textbox_name = "password"
        self.login_button_type = "submit"
        self.wait = 5

    def enter_username(self, username):
        self.browser.find_element('name', self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.browser.find_element('name', self.password_textbox_name).send_keys(password)

    def click_on_login_button(self):
        self.browser.find_element('class name', 'orangehrm-login-button').click()

    def wait_application(self, wait):
        self.browser.implicitly_wait(wait)
