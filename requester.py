from requests_html import HTML, HTMLSession

#with open("inde.html") as html_file:
#	source = html_file.read()
#	html = HTML(html=source)

session = HTMLSession()
r = session.get("https://docs.python-requests.org/en/master/user/quickstart//")

section = r.html.find("document", first=True)

print(section.html)