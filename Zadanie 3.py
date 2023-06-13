#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = pd.read_csv('https://bit.ly/2nNFoRe', na_values='?')

#Zadanie 1
max_price = data['price'].max()
most_expensive_car = data[data['price'] == max_price]

#Zadanie 2
count_per_company = data['company'].value_counts()

#Zadanie 3
average_price = data['price'].mean()

#Zadanie 4
median_price = data['price'].median()

# Zadanie 5
expensive_cars = data[data['price'] > median_price]

# Zadanie 6
data['length_cm'] = data['length'] * 2.54

# Zadanie 7: 
cylinder_mapping = {'four': 4, 'six': 6, 'five': 5, 'eight': 8, 'two': 2, 'twelve': 12, 'three': 3}
data['num-of-cylinders'] = data['num-of-cylinders'].map(cylinder_mapping)

# Wyświetlenie wyników
print("Najdroższy samochód:")
print(most_expensive_car)
print("\nLiczba wierszy dla każdej marki:")
print(count_per_company)
print("\nŚrednia cena:", average_price)
print("Mediana ceny:", median_price)
print("\nSamochody, których cena jest większa od mediany:")
print(expensive_cars)
print("\nPrzekonwertowana długość w centymetrach:")
print(data['length_cm'])
print("\nPrzekonwertowana liczba cylindrów:")
print(data['num-of-cylinders'])


# In[ ]:




