import time
from selenium import webdriver
import os

driver = webdriver.Chrome(os.environ['CHROME_DRIVER'])  # Optional argument, if not specified will search path.

"""Google test"""
# driver.get('http://www.google.com/xhtml');
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!


"""Automate test"""
driver.get('http://inventwithpython.com') #opens the browser
time.sleep(5) # Let the user actually see something!
linkElem = driver.find_element_by_link_text('Read Online for Free') #selects the link
print(type(linkElem))
linkElem.click() # follows the "Read It Online" link
time.sleep(5) # Let the user actually see something!

driver.quit()
