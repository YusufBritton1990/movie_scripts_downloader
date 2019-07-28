from bs4 import BeautifulSoup
import requests

# requesting website
res = requests.get("https://www.springfieldspringfield.co.uk/movie_scripts.php")

# using soup to parse information from website as a XML
soup = BeautifulSoup(res.text, "html.parser") #Type is a soup

# This is a list that contains all the information in the soup,
# which contains the movies titles and years
outer_box = soup.find('div', {'class': "main-content-left"})
# print(outer_box.prettify()) # type is a element.tag

"""
NOTE: In order to scrape the list, the JS of the page has to load first, otherwise, movie_titles_list will return a nonetype

This is where Selenium comes into play
"""
# This is a list of the movie titles and years
movie_titles_list = outer_box.find_all('a', {'class': "script-list-item"})
print(movie_titles_list) #without Selenium, returns nonetype

# for movie in movie_titles_list:
    # name = movie.text
    # name = soup.find('div', {'class': "main-content-left"})
    # print(name)
