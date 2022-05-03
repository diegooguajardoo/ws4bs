from selenium import webdriver
from selenium.webdriver.common.keys import Keys #tto be able to input Enter Key
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.avisosdeocasion.com/autos-usados-y-nuevos.aspx?PlazaBusqueda=2&utm_campaign=include_avisos_en_portada_elnorte&utm_source=categorias&utm_medium=vehiculos")

#print(driver.title)

def field():
	try:
		vehiculo = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.NAME, "txtBusquedaPalabraMaster"))
		)
	except:
		driver.quit()

	time.sleep(5)
	vehiculo.send_keys("Hyundai Accent")
	vehiculo.send_keys(Keys.RETURN)

field()
print("done vehiculo")

#field("Marcas", "marcas", "HYUNDAI")


#driver.quit() quits all https://www.youtube.com/watch?v=Xjv1sY630Uc&ab_channel=TechWithTim
#driver.close() closes tab