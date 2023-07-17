from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
actions = ActionChains(browser)
browser.maximize_window()
browser.get("https://www.play2.automationcamp.ir/")
sleep(1)

browser.execute_script("window.scrollBy(0,400)")
sleep(2)

# click by id
el1  = browser.find_element('id', 'fname')
el1.click()
el1.send_keys("shabnam")

el2  = browser.find_element('id', 'lname')
el2.click()
el2.send_keys("roohi")

el3  = browser.find_element('id', 'male')
el3.click()
sleep(3)


# click by xpath & and method
el5 = browser.find_element('xpath', "//*[@id= 'moption' and @name= 'option1']")
el5.click()
sleep(4)

# click by xpath and index method
el6 = browser.find_element('xpath', "(//*[text() = 'Option 1'])[1]")
el6.click()
sleep(3)

# click by xpath and parent,child method
el7 = browser.find_element('xpath', "//*[@id= 'owc']//*[@value= 'option 2']")
el7.click()
sleep(3)

el0= browser.find_element('xpath', "// tr [ td[text()= 'Actor']]")
actions.context_click(el0).perform()
sleep(3)