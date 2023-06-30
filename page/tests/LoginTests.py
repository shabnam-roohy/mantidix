from page.Login import Login
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
from page.MainPage import MainPage

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(5)

query = "Python"

browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
browser.implicitly_wait(5)

Login = Login(browser=browser)
MainPage = MainPage(browser=browser)

Login.enter_username("Admin")
Login.enter_password("admin123")
Login.click_on_login_button()
sleep(5)
MainPage.check_main_page()
