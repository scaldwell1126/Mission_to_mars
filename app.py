#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, redirect 
import PyMongo
import scrape_mars
import os


# In[ ]:


# Create an instance of Flask app
app = Flask(__name__)


# In[ ]:


app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# In[ ]:


@app.route("/")
def home(): 
    
     # Find data
    mars_info = mongo.db.mars_info.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_info)


# In[ ]:


# Route that will trigger scrape function
@app.route("/scrape")
def scrape(): 

    # Run scrapped functions
    mars_info = mongo.db.mars_info
    mars_data = scrape_mars.scrape_mars_news()
    mars_data = scrape_mars.scrape_mars_image()
    mars_data = scrape_mars.scrape_mars_facts()
    mars_data = scrape_mars.scrape_mars_weather()
    mars_data = scrape_mars.scrape_mars_hemispheres()
    mars_info.update({}, mars_data, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




