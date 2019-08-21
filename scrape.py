import requests
from bs4 import BeautifulSoup

r = requests.get("https://kamigame.jp/FF7/ボス/34.html")

soup = BeautifulSoup(r.content, "html.parser")

for i in soup.select("h1, h2, h3"):
    print(i.getText())

