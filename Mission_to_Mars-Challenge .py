#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd


# In[2]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path)


# In[3]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[4]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[5]:


slide_elem.find("div", class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### Featured Images

# In[8]:


# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# In[10]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[12]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[13]:


# Use the base URL to create an absolute URL
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


# In[15]:


df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# In[16]:


df.to_html()


# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path)


# # JPL Space Images Featured Image

# In[3]:


# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# In[4]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[5]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[6]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[7]:


# Use the base url to create an absolute url
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


# # Mars Facts

# In[8]:


df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
df.head()


# In[9]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[10]:


df.to_html()


# # D1: Scrape High-Resolution Mars??? Hemisphere Images and Titles

# ## Hemispheres

# In[11]:


# 1. Use browser to visit the URL 
url = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/index.html'

browser.visit(url)


# In[12]:


# Parse HTML with soup
html_hemispheres = browser.html
hemisphere_soup = soup(html_hemispheres, 'html.parser')
hemispheres = hemisphere_soup.find_all('div', class_='item')

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

hemispheres_url = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/'

# Loop through list of all hemisphere info
for x in hemispheres:
    
    # Store title
    title = x.find('h3').text
    
    ending_img_url = x.find('a', class_='itemLink product-item')['href']
    
    browser.visit(hemispheres_url + ending_img_url)
    
    img_html = browser.html
    img_soup = soup(img_html, 'html.parser')
    img_url = hemispheres_url + img_soup.find('img', class_='wide-image')['src']
    
    # Append to a dictionary
    hemisphere_image_urls.append({'img_url' : img_url, 'title' : title})


# In[13]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[14]:


# 5. Quit the browser
browser.quit()


# In[ ]:




