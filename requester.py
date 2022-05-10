from requests_html import HTML, HTMLSession

#with open("inde.html") as html_file:
#	source = html_file.read()
#	html = HTML(html=source)

session = HTMLSession()
r = session.get(
    "https://www.jcchouinard.com/web-scraping-with-python-and-requests-html/")

titles = r.html.find("h2")
for title in titles:
	print(title.text)