import requests
from bs4 import BeautifulSoup

r = requests.get("https://kamigame.jp/FF7/ボス/34.html")

soup = BeautifulSoup(r.content, "html.parser")

file = open("FF7 ボス攻略.txt", 'w')

for i in soup.select("h1, h2, h3, p"):
    print(i.getText())
    file.write(i.getText() + '\n')

file.close()
