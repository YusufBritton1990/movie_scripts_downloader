from bs4 import BeautifulSoup #webparser
import requests #HTTP request, to get HTML
from selenium import webdriver #Needed for dynamic scraping
import os #Needed to connect to ChromeDriver, using enviroment variable
import time #track performance
import pandas as pd
import numpy as np

# To track performance
start = time.time()

"""Requesting website"""
# Using requests to receive landing page
res = requests.get("https://www.springfieldspringfield.co.uk/movie_scripts.php?order=0&page=1")

"""Using BeautifulSoup to parse HTML as a soup object"""
# Using Request res information from website as a XML
soup = BeautifulSoup(res.text, "lxml") #Using requests, Type is a soup

"""Using BeautifulSoup to make movie alphabet iterable """
# Retrieve HTML of div element that contains alphabet links
alphabetHTML = soup.find('div', {'class': "search-and-alpha"})

# Receive just the links in the div
alphabetPages = alphabetHTML.find_all('a')

# # Normal List from a for loop, to understand how list comprehension works
# orderList = []
# for link in alphabetPages:
#
#     orderElement = link.text #The actually movie title and year
#     # print(orderElement)
#     orderList.append(orderElement)

# List comprehension, contains list of links as strings to append later
# as a URL parameter
orderList = [link.text for link in alphabetPages]

"""Scraping each movie title on each page in each alphabet order page"""

# Initial list to contain movie title and year it came out
movieList = []
yearList = []

for letter in orderList:
    # Using requests, start on the initial page number of the alphabet order
    # To not get booted from the site for scraping, adding timeout of 10 secs
    urlOrder = f"https://www.springfieldspringfield.co.uk/movie_scripts.php?order={letter}"
    res = requests.get(urlOrder, timeout=10)
    # print(url)

    soup = BeautifulSoup(res.text, "lxml") #Using requests, Type is a soup

    """Requesting movie scripts from page count interable"""
    PaginationHTML = soup.find('div', {'class': "pagination"})
    # print(PaginationHTML.prettify())

    Pagination = PaginationHTML.find_all('a')

    # Retrieve the amount of pages of movies on each alphabet page
    lastPage = int([link.text for link in Pagination][-1])
    # print(type(lastPage))

    for page in range(1,lastPage + 1):
        urlPage = urlOrder + f"&page={page}"
        res = requests.get(urlPage, timeout=5)

        soup = BeautifulSoup(res.text, "lxml") #Using requests, Type is a soup

        # This is a list that contains all the information in the soup,
        # which contains the movies titles and years
        outer_box = soup.find('div', {'class': "main-content-left"})

        # This is a list of the movie titles and years
        movie_titles_list = outer_box.find_all('a', {'class': "script-list-item"})

        """Parsing out movies on each number page"""
        for movie in movie_titles_list:
            # for page in paginationList:
            full_name = movie.text #The actually movie title and year

            # spline full_name into the movie name and year.
            #for year, convert to an interger and not include parentheses
            name, year = full_name[:-6], int(full_name[-5:-1])
            print(name, year)
            movieList.append(name)
            yearList.append(year)


# Creating dictionary format of data to add to a pandas DataFrame
d = {"Name": movieList, "Year":yearList}

# Adding dictionary d to DataFrame
df = pd.DataFrame(data=d)

# Converting DataFrame into a csv file
df.to_csv(r"C:\Users\Youth\Desktop\Projects\movie_scripters_downloader\movies.csv",index=False)

# performance tracking
end = time.time()
print(end - start)
