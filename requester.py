from distutils import errors
from sqlite3 import Row
from requests_html import HTML
import csv

with open ("JAFRAnet.html", errors="ignore") as html_file:
	source = html_file.read()
	html = HTML(html=source)
	html.render()

report = html.find(".table-blk#reporte", first=True)
table_body = report.find("tbody", first= True)
table_data = table_body.find("td")
initial = table_data[0].text

animadoras = []
acc = 0
for e in range(1,2):
	animadora = []
	for i in range(0,23):
		cell = table_data[acc+e].text
		acc =+ 1
		animadora.append(cell)   ##revisar esta secuencia
animadoras.append(animadora)

def looker(pt):
	resultsofsearch = table_body.find("tr")
	rst = (resultsofsearch[pt].text)
	tbl = rst.splitlines()
	return tbl

def selector(n):
	master = []
	for i in range(n*3-3,n*3-1):
		master.append(looker(i))
	return master

master2 = []
rw = table_body.find("tr",first=True).text
for i in range(1,int((len(rw)/2))-5):
	master2.extend(selector(i))

table_body = str(table_body.text)
line = table_body.split(sep="\n")

def list_split(listA, n):
	for x in range(0, len(listA)):
		if x == "D":
			loc = listA.index("D")
		elif x == "I":
			loc = listA.index("I")
		every_chunk = listA[loc+1: loc+n]   #chunks are additive and need to be divided into chunks when "D" condition is met.
		new_table = new_table.append(every_chunk)
		
		if len(every_chunk) < n:
			every_chunk = every_chunk + \
			[None for y in range(n-len(every_chunk))]
		yield every_chunk
	print(new_table)


with open('jafra.csv', 'w',) as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerows(animadoras)
