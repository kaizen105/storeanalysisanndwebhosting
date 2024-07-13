import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

def modifc():
    data=pd.read_csv('Sample - Superstore_Updated_pr.csv')
    data.dropna(inplace=True)      
    data.fillna(method='ffill', inplace=True)     
    data.drop_duplicates(inplace=True)           
    data['Product ID'] = data['Product ID'].astype('category')       
    data['space']=data['Region'].map({'North':1,'South':2,'West':3,'East':4})  
    data['prefix']=data['Customer ID'].apply(lambda x:x[0:2])
    data['Order Date'] = pd.to_datetime(data['Order Date'], format='%d-%m-%Y')        #Changing the data type to date
    data['Ship Date'] = pd.to_datetime(data['Order Date'], format='%d-%m-%Y')         #Changing the data type to date
    data['Shipping Duration'] = (data['Ship Date'] - data['Order Date']).dt.days
    np.random.seed(0)  # Setting seed for reproducibility
    random_duration = np.random.randint(1, 10, size=len(data))  # Generate random integers between 1 and 10
    # Add random duration to 'Order Date' to create 'Ship Date'
    data['Ship Date'] = data['Order Date'] + pd.to_timedelta(random_duration, unit='D')
    # Calculate shipping duration
    data['Shipping Duration'] = random_duration #Creating a random sample duration
    def seas(x):
        y=x.month
        if y in [12,1]:
            return 'Winter'
        elif y in [2,3]:
            return 'Spring'
        elif y in [4,5,6]:
            return 'Summer'
        elif y in [7,8]:
            return 'Monsoon'
        else:
            return 'Autumn'      
    data['Seasons']=data['Ship Date'].apply(seas)
    return data  

data=modifc()
