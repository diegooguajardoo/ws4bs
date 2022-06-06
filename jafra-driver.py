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
driver.set_window_size(800, 768)
driver.set_window_position(0, 0)



def field(id,input):
	try:
		fd = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID, id))
		)
	except:
		driver.quit()

	time.sleep(1)
	fd.send_keys(input)

def login():
	field("cta_h","1033094")
	username = driver.find_element(By.ID,"cta_h")
	username.send_keys(Keys.TAB)

	inpss = input("Type the pssword: ")
	field("pwd_h", input = inpss)
	password = driver.find_element(By.ID,"pwd_h")
	password.send_keys(Keys.ENTER)

	print("Authentication Passed")
	return True


if login() == True:
	driver.implicitly_wait(3)
	try:
		barra = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.ID, "ulMenus"))
		)
		lista = barra.find_element((By.CLASS_NAME, "nav-dinam"))
		print(lista.text)
	except:
		print("No ul was found")
		driver.quit()
	
	#try:
	#	fd = WebDriverWait(driver, 20).until(
	#            EC.presence_of_element_located(
	#            	(By.ID, "reporte"))
	#	)
	#	print(fd)
	#except:
	#	print(f"Failed to find: {fd}")
	#	driver.quit()


#driver.quit() quits all https://www.youtube.com/watch?v=Xjv1sY630Uc&ab_channel=TechWithTim
#driver.close() closes tab