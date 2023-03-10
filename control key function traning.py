from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://qavbox.github.io/demo/signup/")
driver.implicitly_wait(25)
action = ActionChains(driver)
driver.find_element(By.ID,"username").send_keys("thnajsx")
mail=driver.find_element(By.ID,"email")
action.key_down(Keys.CONTROL).key_down("A").key_down("c").key_up(Keys.CONTROL).perform()
action.click(mail).key_down(Keys.CONTROL).key_down("V").key_up(Keys.CONTROL).perform()
time.sleep(10)

driver.quit()