from requests_html import HTML
with ("inde.html") as html_file:
	source = html_file.read()
	html = HTML(html=source)
print(html.html)