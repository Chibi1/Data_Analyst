#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import requests


response = requests.get('http://api.nbp.pl/api/exchangerates/tables/A?format=json')
data = response.json()

rates = data[0]['rates']

codes = []
names = []
mid = []
ask = []

for rate in rates:
    codes.append(rate['code'])
    names.append(rate['currency'])
    mid.append(rate['mid'])
    
df = pd.DataFrame({'Currency': names, 'Mid': mid,}, index=codes)

print(df)


# In[ ]:





# In[ ]:




