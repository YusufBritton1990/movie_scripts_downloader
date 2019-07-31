from bs4 import BeautifulSoup #webparser
import requests #HTTP request, to get HTML
from selenium import webdriver #Needed for dynamic scraping
import os #Needed to connect to ChromeDriver

"""Requesting website"""
# Using requests
res = requests.get("https://www.springfieldspringfield.co.uk/movie_scripts.php?order=0&page=1")

"""Using BeautifulSoup to parse HTML as a soup object"""
# Using Request res information from website as a XML
soup = BeautifulSoup(res.text, "lxml") #Using requests, Type is a soup

"""Using BeautifulSoup to make movie alphabet and page count interables"""
alphabetHTML = soup.find('div', {'class': "search-and-alpha"})
# print(alphabetHTML.prettify())

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

"""Requesting movie scripts from each page"""

for letter in orderList:
    # Using requests
    url = f"https://www.springfieldspringfield.co.uk/movie_scripts.php?order={letter}&page=1"
    res = requests.get(url)
    # print(url)

    soup = BeautifulSoup(res.text, "lxml") #Using requests, Type is a soup

    """Parsing out movies"""
    # This is a list that contains all the information in the soup,
    # which contains the movies titles and years
    outer_box = soup.find('div', {'class': "main-content-left"})

    # This is a list of the movie titles and years
    movie_titles_list = outer_box.find_all('a', {'class': "script-list-item"})

    for movie in movie_titles_list:
        full_name = movie.text #The actually movie title and year

        # using "(" as a delimiter, then taking out ")" in the year
        name, year = full_name.split("(")[0], full_name.split("(")[1][:-1]
        print(name)
