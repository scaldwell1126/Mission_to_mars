#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests


# In[4]:


#Initialize Browser
def initialize_browser():
    executable_path = {"executable_path": "/Users/scott/downloads/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# In[ ]:




mars_info = {}

def scrape_mars_news():
    try:
        browser = initialize_browser()
        
        url = "http://mars.nasa.gov/news"
        browser.visit(url)
        
        #HTML object
        html = browser.html
        
        #Parse HTML with BS
        soup = BeautifulSoup(html, 'html.parser')
        
        #Retrieve news article 
        article = soup.find("div", class_="list_text")
        news_p = article.find("div", class_="article_teaser_body").text
        news_title = article.find("div", class_="content_title").text
        news_date = article.find("div", class_="list_date").text
        
        #Dictionary entry from Mars news 
        mars_info['news_date'] = news_date
        mars_info['news_title'] = news_title
        mars_info['summary'] = news_p
        
         return mars_info
        
    finally:
        
        browser.quit()
        
    


# In[ ]:


#Featured Image 

def scrape_mars_image():
    try:
        browser = initialize_browser()
        
        url_img = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(url_img)
        
        #HTML Object
        html = browser.html
        
        #Parse with BS
        soup = BeautifulSoup(html_image, 'html.parser')
        
        image = soup.find("img", class_="thumb")["src"]
        img_url = "http://jpl.nasa.gov"+image
        featured_image_url = img_url
       
        
        mars_info{'featured_image_url'} = featured_image_url
        
        return mars_info
    finally:
        browser.quit()
        
        
        


# In[ ]:


def scrape_mars_weather():
    
    try:
        browswer = initialize_browser()
        
        url_weather = "https://twitter.com/marswxreport?lang=en"
        browser.visit(url_weather)
        
        html = browser.html
        
        soup = BeautifulSoup(html_weather, 'html.parser')
        
        tweets = soup.find_all('div', class_='js-tweet-text-container')
        
        for tweet in tweets:
    weather_tweet = tweet.find('p').text
            if 'Sol' and 'pressure' in weather_tweet:
            print(weather_tweet)
                break
            else:
                pass
        
        mars_info{'weather_tweet'} = weather_tweet
        
        return mars_info
    finally:
        browser.quit()


# In[ ]:


def scrape_mars_facts():
    
    try:
        
        url_facts = "https://space-facts.com/mars/"
        html = browser.html
        soup = BeautifulSoup(html_facts, 'html.parser')
        
        mars_facts = pd.read_html(url_facts)
        
        mars_df = mars_facts[0]
        
        mars_df.columns
        
        del mars_df['Earth']
        mars_df.columns = ['Mars', 'Value']
        mars_df.set_index('Mars', inplace=True)
        
        mars_df.to_html()
        data= mars_df.to_dict(orient='records')
        
        mars_info{'mars_facts'} = data
        
        return mars_info
    finally:
        browser.quit()


# In[ ]:


def scrap_mars_hemispheres():
    
    try:
        browser = initialize_browser()
        url_hemispheres = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(url_hemispheres)
        
        html_hemispheres = browser.html
        soup = BeautifulSoup(html_hemispheres, 'html.parser')
        
        items = soup.find_all('div', class_='item')
        
        hemispheres_images_url = []
        hemispheres_main_url = "https://astrogeology.usgs.gov"
        
    for i in items:
        title = i.find('h3').text
        partial_img_url = i.find('a', class_='itemLink product-item')['href']
        browser.visit(hemispheres_main_url + partial_img_url)
        partial_img_html = browser.html
        #Parse HTML with BS for every instance of hemisphere info 
        soup = BeautifulSoup(partial_img_html, 'html.parser')
        #Retrieve full image source
        img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
        #Append retrived info into a list of dictionaries 
        hemispheres_images_url.append({"title" : title, "img_url" : img_url})
        
        mars_info{'hemispheres_image_url'} = hemispheres_image_url
        
         return mars_info
    finally:
        browser.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




