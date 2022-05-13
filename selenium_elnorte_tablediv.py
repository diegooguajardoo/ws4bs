from selenium import webdriver
from selenium.webdriver.common.keys import Keys #tto be able to input Enter Key
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.avisosdeocasion.com/Detalle-Vehiculo.aspx?PlazaBusqueda=2&ClaveAviso=31360661&Plaza=2&Vehiculo=AUTOS&Modelo-Vehiculo=MINI%20CLUBMAN%202018&Precio-Vehiculo=478000&Imagenes=16&id_vehiculo=1")

#print(driver.title)


master = []
def Rawdata(clss,clk):
	try:
		vehiculo = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.CLASS_NAME, clss))
		)
		
		if clk == True:
			driver.find_element(by=By.CLASS_NAME,value=clss).click()
		table = vehiculo.find_elements(By.TAG_NAME, "tbody")
		for i in table:
			print(i.text)
			master =  i.text.split(sep="\n")
	except:
		driver.quit()

	#time.sleep(5)
	#vehiculo.send_keys("Hyundai Accent")
	#vehiculo.send_keys(Keys.RETURN)


Rawdata(clss="ar13gris",clk=False)

Rawdata(clss="navtool_right",clk=True)
print("NEXT\n")

with open("autos.csv", "w") as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(master)

#Rawdata("Marcas", "marcas", "HYUNDAI")
#https://www.youtube.com/watch?v=b5jt2bhSeXs&ab_channel=TechWithTim


#driver.quit() quits all https://www.youtube.com/watch?v=Xjv1sY630Uc&ab_channel=TechWithTim
#driver.close() closes tab