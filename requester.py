from distutils import errors
from sqlite3 import Row
from requests_html import HTML
import csv

with open ("JAFRAnet.html", errors="ignore") as html_file:
	source = html_file.read()
	html = HTML(html=source)
	html.render()
	#names = html.find("element.head", first=True)
#print(html.text)

count =0
data_from_file = html.text

report = html.find(".table-blk#reporte", first=True)
table_body = report.find("tbody", first= True)
#print(table.text[0:100]) #prints table body section

tabletxt = table_body.text
tp = tabletxt.splitlines()

def list_split(listA, n):
	for x in range(0, len(listA), n):
		loc = listA.index("D")
		every_chunk = listA[x: n+x]   #chunks are additive and need to be divided into chunks when "D" condition is met.

		if len(every_chunk) < n:
			every_chunk = every_chunk + \
			[None for y in range(n-len(every_chunk))]
		yield every_chunk

tp=(list(list_split(tp,19)))

#header = ["Nombre", "Veliz", "Saldo"]
#data = ["Nora", "1033094", "$0"] needed headers for new table

#print(tp)

with open('jafra.csv', 'w',) as csvfile:
	csvwriter = csv.writer(csvfile)
	
	csvwriter.writerows(tp[:len(tp)])
	if tp == "I":
		print("FOUND")



#for i in data:
#	count +=1
#	if i == "I":
#		print(data[count:count+10])
#		print(html.text[count])


#takes data from html local file, grabs text from it, 
