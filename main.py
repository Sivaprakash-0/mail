
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from telnetlib import EC

print("Welcome to automated club recruitment finder through gmail! Note:If code doesn't work, run it again it will work. Have fun!\n")
from selenium.webdriver.support import expected_conditions as EC



import time

from selenium.webdriver.support.wait import WebDriverWait

service= Service(executable_path="chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.get("https://mail.google.com/mail/u/0/?pli=1#inbox")
WebDriverWait(driver, 10).until(
   EC.presence_of_element_located((By.ID, "identifierId"))
)


input_element = driver.find_element(By.ID,"identifierId")

mail =input("Enter email id")
input_element.send_keys(mail+Keys.ENTER)


WebDriverWait(driver, 5).until(
   EC.presence_of_element_located((By.NAME, "Passwd"))
)
passo=input("Enter password")
password = driver.find_element(By.NAME,"Passwd")
password.send_keys(passo+Keys.ENTER)

time.sleep(5)
WebDriverWait(driver, 20).until(
   EC.presence_of_element_located((By.NAME, "q"))
)

club = driver.find_element(By.NAME,"q")
club.send_keys("club recruitment"+Keys.ENTER)


time.sleep(20)






driver.quit()
