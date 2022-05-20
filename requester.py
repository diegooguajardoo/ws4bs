from distutils import errors
from sqlite3 import Row
from requests_html import HTML
import csv

#with open ("JAFRAnet.html", errors="ignore") as html_file1:
#	source = html_file1.read()
#	html = HTML(html=source)
#	html.render()
#

def scrape():
	with open("JAFRAnet.html", errors="ignore") as html_file:
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
	print(f"Directas {directas} e indirectas {indirectas} total {total}")
	
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

animadoras = scrape()

with open('jafra.csv', 'w',) as csvfile:
	csvwriter = csv.writer(csvfile)
#	csvwriter.writerows(table_heads)
#	csvwriter.writerows(header)
	csvwriter.writerows(animadoras)
