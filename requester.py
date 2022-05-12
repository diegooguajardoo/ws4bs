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
print(f"Report is :{type(report)}")
table_body = report.find("tbody", first= True)
print(f"Table_body is: {type(table_body)}")
#print(table.text[0:100]) #prints table body section


def looker(pt):
	resultsofsearch = table_body.find("tr")
	rst = (resultsofsearch[pt].text)
	tbl = rst.split(sep="\n")
	print(tbl)

looker(6)

rw = table_body.find("tr",first=True).text

table_body = str(table_body.text)
line = table_body.split(sep="\n")
print(type(line))

rw = str(rw)
print(f"Rw is: {type(rw)}")

list_rows = rw.split(sep="\n")
print(f"ListRows is: {type(list_rows)}")

tabletxt = table_body
print(f"Tabletxt is: {type(tabletxt)}")
#print(tabletxt)

print(type(list_rows))
print(list_rows)

#tp = tabletxt.splitlines()
#print(len(tp))

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

#list(list_split(tp,23))

#header = ["Nombre", "Veliz", "Saldo"]
#data = ["Nora", "1033094", "$0"] needed headers for new table

#print(tp)

#with open('jafra.csv', 'w',) as csvfile:
#	csvwriter = csv.writer(csvfile)
#	for i in range(0,10):
#		looker(i)
#		#csvwriter.writerow(list_rows)



#x=0
#y= tp.index("D")
#
#for item in range(x:y):
#	csvwriter.writerows(item)


#for i in data:
#	count +=1
#	if i == "I":
#		print(data[count:count+10])
#		print(html.text[count])


#takes data from html local file, grabs text from it, 
