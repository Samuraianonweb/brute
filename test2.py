import requests
import urllib

link = "https://raw.githubusercontent.com/Samuraianonweb/password/main/1_500.txt"

page = urllib.request.urlopen(link)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

with open(html, 'r') as f:
    mas = f.read().splitlines()
for x in mas:
    print(x)
