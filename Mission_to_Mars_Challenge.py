#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Scrape Mars Data: The News

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

# iIport Pandas
import pandas as pd


# In[4]:


# Set up executable path
executable_path = {'executable_path': ChromeDriverManager().install()}

# Set up the URL for scraping
browser = Browser('chrome', **executable_path, headless=False)


# In[5]:


# Visit the Mars NASA news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Add an optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[6]:


# Set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[7]:


# Begin scraping the site
slide_elem.find('div', class_='content_title')


# ### Title

# In[8]:


# Use the parent element to find the first `a` tag and save it
## as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# ### Paragraph Text

# In[9]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[11]:


# Visit the Space Images Mars site
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[12]:


# Find and click the full image button - indexing direct browser to click
## second button [1]
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[13]:


# Parse the resulting HTML with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[14]:


img_soup.find('img', class_='fancybox-image')


# In[15]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[16]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Planet Profile

# In[17]:


# Scrape the "Mars Planet Profile" table from HTML with Pandas
df = pd.read_htmldf = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[18]:


# Use Pandas .to_html function to convert the DataFrame back into HTML-ready
## code
df.to_html()


# ## Module 10 Challenge - Mars Hemispheres Images

# In[19]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[20]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
links = browser.find_by_css('a.product-item img')


#2 Using a for loop, iterate through the tags
for i in range(4):
    # Create an empty dictionary inside the for loop
    hemispheres = {}
    
    # Click on each hemisphere link
    browser.find_by_css('a.product-item img')[i].click()
  
    # Navigate to the full resolution image page
    sample_elem = browser.links.find_by_text('Sample').first
    hemispheres['img_url'] = sample_elem['href']
    
    # Get Hemisphere title
    hemispheres['title'] = browser.find_by_css('h2.title').text   
    
    # Append hemisphere object to list
    hemisphere_image_urls.append(hemispheres)
    
    # Navigate backwards
    browser.back()


# In[21]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[22]:


# 5. End Browser session
browser.quit()

