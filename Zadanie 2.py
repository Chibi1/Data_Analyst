#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


data = pd.read_csv('https://bit.ly/2K8JOur', sep='\t')

equipment = data['Wyposażenie'].str.get_dummies(sep='|')

data = pd.concat([data, equipment], axis=1)

print(data)


# In[ ]:




