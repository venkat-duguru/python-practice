import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://app.vwo.com/#/login")
driver.find_element(By.ID, "login-username").send_keys("dvenkateshbabu143@gmail.com")
#driver.find_element(By.ID, "login-password").send_keys("Venkat@78")
driver.find_element(By.XPATH, "//input[@button='button']").click()
#driver.find_element(By.XPATH, "//input[@type='submit']").click()
#time.sleep(6)