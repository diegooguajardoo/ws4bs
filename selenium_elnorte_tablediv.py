from selenium import webdriver
from selenium.webdriver.common.keys import Keys #tto be able to input Enter Key
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

PATH = "/usr/local/bin/chromedriver"
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get(
	"https://www.vivanuncios.com.mx/s-venta-autos-camionetas/monterrey/v1c81l10980p1")

master = []
def Rawdata(clss,clk):
	try:
		vehiculo = WebDriverWait(driver, 16).until(
			EC.presence_of_element_located((By.CLASS_NAME, clss))
		)
		
		if clk == True:
			driver.find_element(by=By.CLASS_NAME,value=clss).click()
		table = vehiculo.find_elements(By.CLASS_NAME, "_1KYON")
		for i in table:
			print(i.text)

		#car = car.split(sep="\n")
		#return car
	except:
		print("Error")
		driver.quit()

master_list = []

car1 = Rawdata(clss="tileV2 REAdTileV2 regular listView", clk=False)
print("Found")
#master_list.append(car1)
#Rawdata(clss="navtool_right",clk=True)
#("NEXT\n")
#for i in range(0,3):
print(master_list)

#Rawdata(clss="ar13gris",clk=False)

#with open("autos.csv", "w") as csvfile:
#	csvwriter = csv.writer(csvfile)
#	csvwriter.writerow(master)

#https://www.youtube.com/watch?v=b5jt2bhSeXs&ab_channel=TechWithTim

#driver.quit() quits all https://www.youtube.com/watch?v=Xjv1sY630Uc&ab_channel=TechWithTim
#driver.close() closes tab