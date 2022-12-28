from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

import time
import random

driver = webdriver.Edge()

#open tab
# ... take the code from the options below
driver.get("http://etabc.tw/etest/default.asp?dt=1&db=3012")

# Setting up the tests...
driver.find_element(By.NAME, "endno").send_keys("\ue003\ue003\ue003\ue0033012")
driver.find_element(By.NAME, "classname").send_keys("122")
driver.find_element(By.NAME, "name").send_keys("测试用")
driver.find_element(By.NAME, "seatno").send_keys("36")
Select(driver.find_element("name",'chooseno')).select_by_visible_text('100')
Select(driver.find_element("name",'examtime')).select_by_value('15')

driver.find_element(By.XPATH, value="//input[@value='開始測驗']").click()

# Make the tests...



#dictionary attack
convert = [i.strip().split(' = ') for i in open('dictionary.txt', 'r', encoding='UTF-8')]
for i in range(100):
    value = driver.find_element(By.XPATH, value = "/html/body/form/div/table/tbody/tr[" + str(i+3) + "]/td[2]").text
    answer = driver.find_element(By.NAME, "no" + str(i))
    for chinese, english in convert:
        if(chinese == value):
            answer.send_keys(english)
            break
time.sleep(random.randint(128,600))
driver.find_element(By.XPATH, value="//input[@value=' 完畢交卷 ']").click()


# close the tab
try:
    time.sleep(5)
finally:
    driver.quit()