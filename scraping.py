#!/usr/bin/env python
# coding: utf-8

# 10.3.3 Scrape Mars Data: The News

#Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

# 10.3.5 Import Pandas
import pandas as pd


# Set up executable path
executable_path = {'executable_path': ChromeDriverManager().install()}

# Set up the URL for scraping
browser = Browser('chrome', **executable_path, headless=False)


# Visit the Mars NASA news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Add an optional delay for loading the page
browser.is_element_present_by_css('div.list_test', wait_time=1)


# Set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# Begin scraping the site
slide_elem.find('div', class_='content_title')


# Use the parent element to find the first `a` tag and save it
## as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images


# 10.3.4 Visit the Space Images Mars site
url = 'https://spaceimages-mars.com'
browser.visit(url)


# Find and click the full image button - indexing direct browser to click
## second button [1]
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting HTML with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# 10.3.5 Scrape the "Mars Planet Profile" table from HTML with Pandas
df = pd.read_htmldf = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# Use Pandas .to_html function to convert the DataFrame back into HTML-ready
## code
df.to_html()

# End Browser session
browser.quit()

