from bs4 import BeautifulSoup #webparser
import requests #HTTP request, to get HTML
import selenium import webdriver #Needed for dynamic scraping

# driver = webdriver.Chrome()

# requesting website
res = requests.get("https://www.springfieldspringfield.co.uk/movie_scripts.php")

# using soup to parse information from website as a XML
soup = BeautifulSoup(res.text, "lxml") #Type is a soup

# This is a list that contains all the information in the soup,
# which contains the movies titles and years
outer_box = soup.find('div', {'class': "main-content-left"})
# print(outer_box.prettify()) # type is a element.tag

"""
Selenium
"""
# This is a list of the movie titles and years
movie_titles_list = outer_box.find_all('a', {'class': "script-list-item"})
# print(movie_titles_list)
# print(type(movie_titles_list))

for movie in movie_titles_list:
    full_name = movie.text #The actually movie title and year

    # using "(" as a delimiter, then taking out ")" in the year
    name, year = full_name.split("(")[0], full_name.split("(")[1][:-1]
    # print(name)
