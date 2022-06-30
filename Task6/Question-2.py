#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("https://raw.githubusercontent.com/cognizance-amrita/AI-Tasks/main/Task-1/Q2-Dataset.csv")


# In[3]:


df.head()


# In[5]:


missing_value_formats = ["n.a.","?","NA","n/a", "na", "--"]
df = pd.read_csv("https://raw.githubusercontent.com/cognizance-amrita/AI-Tasks/main/Task-1/Q2-Dataset.csv", na_values = missing_value_formats)
print(df['Alley'].head(10))


# In[7]:


print(df['LotFrontage'].isnull())


# In[8]:


print(df.isnull().sum())


# In[9]:


df['LotFrontage'].fillna(1, inplace=True)


# In[10]:


print(df['LotFrontage'])


# In[11]:


print(df['Alley'].isnull())


# In[12]:


df['Alley'].fillna('no alley name mentioned', inplace=True)
print(df['Alley'])


# In[20]:


print(df['BsmtQual'].isnull())


# In[32]:


df[df['BsmtQual'].isnull()]


# In[35]:


df['BsmtQual'].fillna('no value given here', inplace=True)


# In[36]:


df[df['BsmtQual'].isnull()]


# In[37]:


print(df['BsmtCond'].isnull())


# In[38]:


df[df['BsmtCond'].isnull()]


# In[39]:


df['BsmtCond'].fillna('None', inplace=True)


# In[40]:


df[df['BsmtCond'].isnull()]


# In[41]:


print(df['BsmtExposure'].isnull())


# In[42]:


df[df['BsmtExposure'].isnull()]


# In[43]:


df['BsmtExposure'].fillna('No given exposure', inplace=True)


# In[44]:


df[df['BsmtExposure'].isnull()]


# In[45]:


print(df['BsmtFinType1'].isnull())


# In[46]:


df[df['BsmtFinType1'].isnull()]


# In[47]:


df['BsmtFinType1'].fillna('Values yet to be updated', inplace=True)


# In[48]:


df[df['BsmtFinType1'].isnull()]


# In[49]:


print(df['BsmtFinType2'].isnull())


# In[50]:


df[df['BsmtFinType2'].isnull()]


# In[51]:


df['BsmtFinType2'].fillna('values not found', inplace=True)


# In[52]:


df[df['BsmtFinType2'].isnull()]


# In[53]:


print(df.isnull().sum())



