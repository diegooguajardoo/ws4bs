from requests_html import HTML
import csv

listatotal = []
def intro():
	noffiles = ""
	archivos = []
	while noffiles != 'quit':
		noffiles = input("\n\nCuántos archivos se van a analizar?: ")
		noffiles = int(noffiles)

		for i in range(1, noffiles+1):
			if i == 1:
				filenm = "JAFRANET.html"
				archivos.append(filenm)
			else:
				filenm = "JAFRANET (" + str(i -1) + ").html"
				archivos.append(filenm)

		print(f"Los archivos están nombrados {str(archivos)}?")
		qt = input("Correcto?: (si/no)").lower()
		if qt == "si":
			return archivos
		elif qt == "sí":
			return archivos

def scrape(fl):
	with open(file=fl, errors="ignore") as html_file:
		source = html_file.read()
		html = HTML(html=source)
		html.render()
	
	report = html.find(".table-blk#reporte", first=True)
	
	#headers
	table_head = report.find(".head")
	header =[]
	table_heads = []
	for i in range(0,2):
		title = table_head[i].text
		title = str(title)
		title=title.splitlines()
		table_heads.append(title)
	header.append(table_heads)
	
	#data
	table_body = report.find("tbody", first=True)
	table_data = table_body.find("td")
	
	#counter
	directas = 0
	indirectas = 0
	total = 0
	
	for i in range(0,len(table_data)):
		table_data1 = (table_data[i].text)
		if table_data1 == "I":
			indirectas = indirectas + 1
			total = total + 1
		elif table_data1 == "D":
			directas = directas + 1
			total = total + 1
	print(f"ESTADO DE CUENTA DE: {table_data[2].text}")
	print(f"Se registraron {total} animadoras: directas {directas} e indirectas {indirectas}\n")
	
	animadoras = []
	count = 0
	for e in range(1,(total+1)):
		animadora = []
		for i in range(0,25):
			cell = table_data[count+i].text
			animadora.append(cell)
		count = count + i
		animadoras.append(animadora)
	return animadoras

archivos = intro()

for i in archivos:
	try:
		fragmento = scrape(fl=i)
		listatotal = listatotal + fragmento
	except:
		print("ERROR: Hacen falta archivos o se encuentran nombrados diferente. Por favor revisar e intentar nuevamente")

with open('jafrarawdata.csv', 'w',) as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerows(listatotal)





