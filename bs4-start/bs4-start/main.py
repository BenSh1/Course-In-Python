from bs4 import BeautifulSoup


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents ,"html.parser")
print(soup.title)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)


heading = soup.find(name="h3", class_="heading")
print(heading.getText())

name = soup.select_one(selector="#name")
print(name)


headings = soup.select(".heading")
print(headings)




