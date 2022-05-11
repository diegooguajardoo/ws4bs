from selenium import webdriver
from selenium.webdriver.common.keys import Keys #tto be able to input Enter Key
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


import time

PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("http://www.jafranet.com.mx")

#print(driver.title)

def field(id,input):
	try:
		fd = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID, id))
		)
	except:
		driver.quit()

	time.sleep(2)
	fd.send_keys(input)


field("cta_h","1033094")
username = driver.find_element(By.ID,"cta_h")
username.send_keys(Keys.TAB)

field("pwd_h", "2181")
password = driver.find_element(By.ID,"pwd_h")
password.send_keys(Keys.ENTER)

print("Authentication Passed")
Auth = True

#driver.get("https://www.jafranet.com.mx/JntCgi/JNTDCXANI.pgm")
#list = driver.find_element(By.CLASS_NAME, value="list-unstyled")

if Auth == True:
	saveas = ActionChains(driver).key_down(Keys.CONTROL)\
	    .key_down('s').key_up(Keys.CONTROL).key_up('s')
	saveas.perform()

try:
	fd = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
            	(By.ID, "reporte"))
	)
	print(fd)
except:
	print(f"Failed to find: {fd}")
	driver.quit()

#link = driver.find_element(By.LINK_TEXT, "Actualizado por animador")
#link.click()

#driver.quit() quits all https://www.youtube.com/watch?v=Xjv1sY630Uc&ab_channel=TechWithTim
#driver.close() closes tab