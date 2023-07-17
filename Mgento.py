from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
actions = ActionChains(browser)
browser.maximize_window()
browser.get("https://magento.softwaretestingboard.com/")
sleep(1)

el1  = browser.find_element('id', 'search')
el1.click()
el1.send_keys("hoodie")

el2 = browser.find_element('xpath', "//button[@type='submit']")
el2.click()
sleep(2)

el3= browser.find_element('css selector', ".product-items>li:first-child")
el3.click()
sleep(3)

el4 = browser.find_element('id', 'option-label-size-143-item-169')
el4.click()
sleep(3)

el5= browser.find_element('id', 'option-label-color-93-item-57')
el5.click()
sleep(3)
try:

    el6= browser.find_element('xpath', "//*[@id= 'product-addtocart-button']")
    el6.click()
    sleep(6)
    el7= browser.find_element('css selector', "message-success>div")
    assert el7.is_displayed()
    assert el7.text == "You added Selene Yoga Hoodie to your "

    print("el7 assertion passed")
except NoSuchElementException:
    print("el7 assertion failed")

el7= browser.find_element('xpath', "//div[@class= 'product data items']/ child :: *[@id='tab-label-description']")
el7.click()
sleep(3)