#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup as bs
import time
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager




executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)



def scrape():

    news_url = 'https://redplanetscience.com/'
    browser.visit(news_url)

    mars_html = browser.html
    soup = bs(mars_html, 'html.parser')

    news_title = soup.find('div', class_='content_title').text
    news_text = soup.find('div', class_='article_teaser_body').text






    img_url = "https://spaceimages-mars.com/"
    browser.visit(img_url)

    img_html = browser.html
    soup = bs(img_html, 'html.parser')

    img_url = soup.find("img", class_="headerimage fade-in").get("src")

    featured_image_url = f"https://spaceimages-mars.com/{img_url}"



    


    facts_url = "https://galaxyfacts-mars.com/"
    browser.visit(facts_url)
    facts_df = pd.read_html(facts_url)
    #facts_df
    table = facts_df[0]
    table = table.rename(columns={0: "Mars - Earth Comparison", 1: "Mars", 2: "Earth"})
    table = table.drop(index=0)

    table_html = table.to_html("facts_table")
    table_html





    hemi_url = "https://marshemispheres.com/"
    browser.visit(hemi_url)
    hemi_html = browser.html
    soup = bs(hemi_html, 'html.parser')

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



    mars_data_dict = {
        "mars_news": {"news_title": news_title, "news_text": news_text},
        "mars_featured_img": featured_image_url,
        "mars_facts": table_html,
        "mars_hemispheres": hemi_img_urls
    }

    browser.quit()
    
    return mars_data_dict

    if __name__ == "__main__":
        print(scrape())
        








