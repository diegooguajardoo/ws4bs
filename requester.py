from distutils import errors
from requests_html import HTML

with open ("JAFRAnet.html", errors="ignore") as html_file:
	source = html_file.read()
	html = HTML(html=source)
	#names = html.find("element.head", first=True)
#print(html.text)
count =0
data = html.text


for i in data:
	count +=1
	if i == "I":
		print(data[count:count+10])
#		print(html.text[count])


#takes data from html local file, grabs text from it, iterates lines, looks for "I", prints part of that line
