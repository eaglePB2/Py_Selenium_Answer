from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

import time
import random



# Input
ClassName = input("班級: ")
Name = input("姓名: ")
SeatNo = input("座號: ")
ChooseNo = input("挑選: < 10 | 20 | 25 | 40 | 50 | 80 | 100 | 125 | 150 | 200 | 250>")
ExamTime = input("測驗時間: < 1 | 3 | 5 | 10 | 15 | 20 | 25 | 30 | 35 | 40>")

driver = webdriver.Edge()

# open tab
# ... take the code from the options below
driver.get("http://etabc.tw/etest/default.asp?dt=3&db=G3012")

# Setting up the tests...
driver.find_element(By.NAME, "endno").send_keys("\ue003\ue003\ue003\ue0033012")
driver.find_element(By.NAME, "classname").send_keys(ClassName)
driver.find_element(By.NAME, "name").send_keys(Name)
driver.find_element(By.NAME, "seatno").send_keys(SeatNo)
Select(driver.find_element("name",'chooseno')).select_by_visible_text(ChooseNo)
Select(driver.find_element("name",'examtime')).select_by_value(ExamTime)

driver.find_element(By.XPATH, value="//input[@value='開始測驗']").click()

# Attempting the tests...

# Dictionary attack
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
