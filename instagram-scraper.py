from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # tto be able to input Enter Key
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/stories/diego.guajardo/2838888826872376508/")

def get_element(clss):
	try:
		fd = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.CLASS_NAME, clss))
		)
	except:
		driver.quit()


get_element(clss = "qF0y9          Igw0E     IwRSH      eGOV_       acqo5  vwCYk                                                                                lDRO1")
