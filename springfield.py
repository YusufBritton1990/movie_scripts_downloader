from bs4 import BeautifulSoup
import requests

# requesting website
res = requests.get("https://www.springfieldspringfield.co.uk/movie_scripts.php")

# using soup to parse information from HTML as XML
soup = BeautifulSoup(res.text, "lxml")

# This is a list that contains all the information in a block of code
# This contains the movies
outer_box = soup.find('div', {'class': "main-content-left"})
print(outer_box)
