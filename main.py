import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-century/"
requete = requests.get(URL)
page = requete.content
soup = BeautifulSoup(page, 'html.parser')

MY_ORDER = []

elements = soup.find_all(attrs={"data-test": lambda x: x and x.startswith("listicle-item-")})

# Afficher le contenu de chaque élément
for element in elements:
    h3 = element.find("h3")
    if h3:
        content = h3.text
        parts = content.split(') ')
        num = int(parts[0])
        title = parts[1]
        MY_ORDER.append((num, title))
        

with open('movies.csv', 'w') as file:
    file.write("Position, Title\n")
    MY_ORDER = sorted(MY_ORDER, key=lambda x: x[0])
    for num, title in MY_ORDER:
        file.write(f"{num}, {title}\n")
    file.close()
        
        
    