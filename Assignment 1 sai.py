#!/usr/bin/env python
# coding: utf-8
# Project Idea: Scrape the data out of the website and save the data either in the CSV or Excel file. Also usethe Pandas library to use the  scrapped data into a DataFrame
# # Installing libraries

# In[1]:


pip install bs4 


# In[2]:


pip install requests


# # importing libraries

# In[3]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# # create empty arrays

# In[4]:



quotes = []
authors = []
tags = []


# # loop over page 1 to 5

# In[5]:



for pages in range(1,5): 
        
    url = f"http://quotes.toscrape.com/page/{pages}/"
    response = requests.get(url)
    response=response.content
    soup=BeautifulSoup(response,'html.parser')    
    for i in soup.findAll("div",{"class":"quote"}):
        quotes.append((i.find("span",{"class":"text"})).text)  
   
    for j in soup.findAll("div",{"class":"quote"}):
        authors.append((j.find("small",{"class":"author"})).text)    
        
    for k in soup.findAll("div",{"class":"tags"}):
        tags.append((k.find("meta"))['content'])


# # Create pandas dataframe

# In[6]:


df = pd.DataFrame({'Quote':quotes,'Author':authors,'Tag':tags})


# # print the dataframe

# In[7]:


print(df)


# # creating csv

# In[8]:


df.to_csv('Assignment1.csv')

