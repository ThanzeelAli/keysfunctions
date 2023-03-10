from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.implicitly_wait(25)
action=ActionChains(driver)


rightcc = driver.find_element(By.XPATH,"//span[contains(text(),'right click me')]")
action.context_click(rightcc).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
alert = driver.switch_to.alert
alert.accept()


driver.quit()