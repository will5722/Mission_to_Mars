#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup as bs
import time
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[11]:


news_url = 'https://redplanetscience.com/'
browser.visit(news_url)


# In[12]:


mars_html = browser.html
soup = bs(mars_html, 'html.parser')


# In[13]:


news_title = soup.find('div', class_='content_title').text
news_text = soup.find('div', class_='article_teaser_body').text
print(f"Latest news title: {news_title}")
print(f"Article paragraph: {news_text}")


# In[14]:


img_url = "https://spaceimages-mars.com/"
browser.visit(img_url)


# In[15]:


img_html = browser.html
soup = bs(img_html, 'html.parser')


# In[21]:


img_url = soup.find("img", class_="headerimage fade-in").get("src")


featured_image_url = f"https://spaceimages-mars.com/{img_url}"
print(featured_image_url)


# In[34]:


facts_url = "https://galaxyfacts-mars.com/"
browser.visit(facts_url)
facts_df = pd.read_html(facts_url)
#facts_df
table = facts_df[0]
table = table.rename(columns={0: "Mars - Earth Comparison", 1: "Mars", 2: "Earth"})
table = table.drop(index=0)
table


# In[35]:


table_html = table.to_html("facts_table")
table_html


# In[44]:


hemi_url = "https://marshemispheres.com/"
browser.visit(hemi_url)
hemi_html = browser.html
soup = bs(hemi_html, 'html.parser')


# In[45]:


hemi_img_urls = []
results = soup.find_all("div", class_="item")

for result in results:
    title = result.h3.text
    href = result.find("a")["href"]
    hemisphere_img_url = f"https://marshemispheres.com/{href}"
    browser.visit(hemisphere_img_url)
    hemisphere_html = browser.html
    soup = soup = bs(hemisphere_html, 'html.parser')
    hemisphere_img_url = soup.find("img", class_="wide-image").get("src")
    hemi_img_urls.append({"title": title, "img_url": f"https://marshemispheres.com/{hemisphere_img_url}"})
    
print(hemi_img_urls)


# In[ ]:




