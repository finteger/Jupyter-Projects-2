from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import csv

#initialize the Chrome web driver
driver = webdriver.Chrome()

page_url = 'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401'

#Fetching the web page
driver.get(page_url)

# Wait for the table to load 
driver.implicitly_wait(10)

# Get the page source after JavaScript execution
page_source = driver.page_source

# Parse the HTML content
soup = BeautifulSoup(page_source, 'html.parser')

# Find the table element
table = soup.find(id='simpleTable')

if table:
    #Extact column headers
    headers = []




