#!/usr/bin/env python
# coding: utf-8

# In[18]:


#pip install --user kaggle


# In[19]:


#from kaggle.api.kaggle_api_extended import KaggleApi
#api = KaggleApi()
#api.authenticate()


# In[ ]:





# In[20]:


#!kaggle datasets download -d camnugent/california-housing-prices


# In[21]:


import pandas as pd
import numpy as np
from zipfile import ZipFile
import os
import streamlit as st


# In[33]:


#zf = ZipFile('california-housing-prices.zip')
#zf.extractall()
#zf.close()

with ZipFile("/Users/sabrinathoen/case_goed/california-housing-prices.zip", 'r') as zObject:
     zObject.extractall(
        path="/Users/sabrinathoen/case_goed")
df = pd.read_csv('housing.csv')
              


# In[34]:


#df = pd.read_csv('housing.csv')


# In[35]:


df.head()


# In[36]:


df.info()


# In[37]:


df.shape


# In[38]:


df.columns


# In[39]:


st.title("Case 2: California Housing Prices")


# In[40]:


InputOcean = st.sidebar.selectbox("Select Ocean Proximity", ("<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"))


# In[41]:


OceanSelect = df[df["ocean_proximity"] == InputOcean]


# In[42]:


st.dataframe(OceanSelect)


# In[43]:


tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")


# In[ ]:




