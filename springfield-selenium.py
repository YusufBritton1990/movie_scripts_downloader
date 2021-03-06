from bs4 import BeautifulSoup #webparser
import requests #HTTP request, to get HTML
from selenium import webdriver #Needed for dynamic scraping
import os #Needed to connect to ChromeDriver

"""Using Selenium to run chrome"""
driver = webdriver.Chrome(os.environ['CHROME_DRIVER'])
driver.get("https://www.springfieldspringfield.co.uk/movie_scripts.php")

"""Requesting website"""
# Using Selenium, which will return HTML
res = driver.execute_script("return document.documentElement.outerHTML")

"""Using BeautifulSoup to parse HTML as a soup object"""
# Using Selenium res to parse information
soup = BeautifulSoup(res, "lxml") #Using selenium, Type is a soup
driver.quit() #this will close window

# This is a list that contains all the information in the soup,
# which contains the movies titles and years
outer_box = soup.find('div', {'class': "main-content-left"})
# print(outer_box.prettify()) # type is a element.tag

# This is a list of the movie titles and years
movie_titles_list = outer_box.find_all('a', {'class': "script-list-item"})

for movie in movie_titles_list:
    full_name = movie.text #The actually movie title and year

    # using "(" as a delimiter, then taking out ")" in the year
    name, year = full_name.split("(")[0], full_name.split("(")[1][:-1]
    print(name)
