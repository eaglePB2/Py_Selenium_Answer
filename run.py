from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

import time
import random

# 此系統只支援：教育部字表，題庫為2000（填充題）或3000（依字母），隨機.

# Input
TitleNo = input("目前只支援2000（填充題）或3000（依字母），請輸入 2000 還是 3012: ")
ClassName = input("請輸入班級: ")
Name = input("請輸入姓名: ")
SeatNo = input("請輸入座號: ")
EndNo = input("請輸入最大範圍: ")
ChooseNo = input("挑選: < 10 | 20 | 25 | 40 | 50 | 80 | 100 | 125 | 150 | 200 | 250>\t")
ExamTime = input("測驗時間: < 1 | 3 | 5 | 10 | 15 | 20 | 25 | 30 | 35 | 40>\t")

driver = webdriver.Edge()

# open tab
# ... take the code from the options below
driver.get("http://etabc.tw/etest/default.asp?dt=1&db=" + TitleNo)

# Setting up the tests...
driver.find_element(By.NAME, "endno").send_keys("\ue003\ue003\ue003\ue003"+EndNo)
driver.find_element(By.NAME, "classname").send_keys(ClassName)
driver.find_element(By.NAME, "name").send_keys(Name)
driver.find_element(By.NAME, "seatno").send_keys(SeatNo)
Select(driver.find_element("name",'chooseno')).select_by_visible_text(ChooseNo)
Select(driver.find_element("name",'examtime')).select_by_value(ExamTime)

driver.find_element(By.XPATH, value="//input[@value='開始測驗']").click()

# Attempting the tests by using Mp3 Voice Vocab Attack...

for i in range(int(ChooseNo)):
    value = driver.find_element(By.XPATH, value = "/html/body/form/div/table/tbody/tr[" + str(i+3) + "]/td[3]/a").get_attribute("onmouseover").split("/")[-1].split(".")[0].strip()
    driver.find_element(By.NAME, "no" + str(i)).send_keys(value)
time.sleep(random.randint(420,int(ExamTime)*60))
driver.find_element(By.XPATH, value="//input[@value=' 完畢交卷 ']").click()


# close the tab
try:
    time.sleep(5)
finally:
    driver.quit()
