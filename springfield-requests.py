from bs4 import BeautifulSoup #webparser
import requests #HTTP request, to get HTML
from selenium import webdriver #Needed for dynamic scraping
import os #Needed to connect to ChromeDriver, using enviroment variable
import time #track performance

start = time.time()

"""Requesting website"""
# Using requests to receive landing page
res = requests.get("https://www.springfieldspringfield.co.uk/movie_scripts.php?order=0&page=1")

"""Using BeautifulSoup to parse HTML as a soup object"""
# Using Request res information from website as a XML
soup = BeautifulSoup(res.text, "lxml") #Using requests, Type is a soup

"""Using BeautifulSoup to make movie alphabet iterable """
alphabetHTML = soup.find('div', {'class': "search-and-alpha"})

# Receive just the links
alphabetPages = alphabetHTML.find_all('a')

# # Normal List from a for loop
# orderList = []
# for link in alphabetPages:
#
#     orderElement = link.text #The actually movie title and year
#     # print(orderElement)
#     orderList.append(orderElement)

# List comprehension
orderList = [link.text for link in alphabetPages]
# print(orderList)

"""Requesting movie scripts from page count interable"""
PaginationHTML = soup.find('div', {'class': "pagination"})
# print(PaginationHTML.prettify())

Pagination = PaginationHTML.find_all('a')

# Retrieve the amount of pages of movies on each alphabet page
lastPage = int([link.text for link in Pagination][-1])
print(type(lastPage))

"""Scraping each movie title on each page in each alphabet order page"""
for letter in orderList:
    # Using requests, start on the initial page number of the alphabet order
    url = f"https://www.springfieldspringfield.co.uk/movie_scripts.php?order={letter}&page=1"
    res = requests.get(url)
    # print(url)

    soup = BeautifulSoup(res.text, "lxml") #Using requests, Type is a soup

    # This is a list that contains all the information in the soup,
    # which contains the movies titles and years
    outer_box = soup.find('div', {'class': "main-content-left"})

    # This is a list of the movie titles and years
    movie_titles_list = outer_box.find_all('a', {'class': "script-list-item"})

    """Getting the number page"""


    """Parsing out movies on each number page"""
    for movie in movie_titles_list:
        # for page in paginationList:
        full_name = movie.text #The actually movie title and year

        # spline full_name into the movie name and year.
        #for year, convert to an interger and not include parentheses
        name, year = full_name[:-6], int(full_name[-5:-1])
        print(name, year)

end = time.time()
print(end - start)
