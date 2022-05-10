from requests_html import HTML

with open("inde.html") as html_file:
	source = html_file.read()
	html = HTML(html=source)

match = html.find("title", first = True)

print(match.text)