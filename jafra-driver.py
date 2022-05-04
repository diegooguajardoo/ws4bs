from selenium import webdriver
from selenium.webdriver.common.keys import Keys #tto be able to input Enter Key
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("http://www.jafranet.com.mx")

#print(driver.title)

def field(id,input):
	try:
		fd = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID,id))
		)
	except:
		driver.quit()

	time.sleep(3)
	fd.send_keys(input)


field("cta_h","1033094")
username = driver.find_element_by_id("cta_h")
username.send_keys(Keys.TAB)

field("pwd_h", "****")
password = driver.find_element_by_id("pwd_h")
password.send_keys(Keys.ENTER)

print("done vehiculo")

#field("Marcas", "marcas", "HYUNDAI")
#https://www.youtube.com/watch?v=b5jt2bhSeXs&ab_channel=TechWithTim


#driver.quit() quits all https://www.youtube.com/watch?v=Xjv1sY630Uc&ab_channel=TechWithTim
#driver.close() closes tab