
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import datetime
now = datetime.now()
s1 = str(now.strftime("%H:%M:%S"))


driver = webdriver.Firefox()
vars = {}
driver.get("https://www.primevideo.com/")

driver.set_window_size(1050, 721)
driver.find_element(By.ID, "pv-nav-sign-in").click()
driver.find_element(By.ID, "ap_email").send_keys('xyz@gmail.com')
driver.find_element(By.ID, "ap_password").send_keys("password")
driver.find_element(By.ID, "signInSubmit").click()
driver.find_element(By.ID, "nav-profiles-dropdown-label").click()
driver.find_element(By.ID, "pv-nav-your-watchlist").click()
driver.find_element(By.CSS_SELECTOR, ".UaW15H:nth-child(1) img").click()
driver.find_element(By.CSS_SELECTOR, ".dQsn0O .\\_2gd2MR").click()

while True:
	now = datetime.now()
	s2 = str(now.strftime("%H:%M:%S"))
	tdelta = datetime.strptime(s2, '%H:%M:%S') - datetime.strptime(s1, '%H:%M:%S')
	try:
		driver.current_url
	except:
		print('Print total time spend:',tdelta)
		exit()
	
