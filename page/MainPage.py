class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.dashboard_lable_ahref = "/web/index.php/dashboard/index"

    def check_main_page(self):
        self.browser.find_element('css selector', 'a[href="/web/index.php/dashboard/index"]')
