#!/usr/bin/env python
# coding: utf-8

# In[1]:


#data manipulation
import numpy as np
import pandas as pd

#ploting
import matplotlib.pyplot as plt
import seaborn as sns

#statistical modeling
from scipy import stats
from scipy.stats import norm
import statsmodels.api as sm
from datetime import datetime
from watermark import watermark
print(watermark(packages="numpy, pandas,matplotlib, seaborn,scipy,statsmodels"))


# In[2]:


df = pd.read_csv('/Users/stevekim/Desktop/BrainStationSprintProject/EVChargingStationUsageCali.csv')


# In[3]:


print(df.head())


# In[4]:


df.columns


# Column names are too long keep it short and neat

# In[5]:


df.rename(columns={'Energy (kWh)' : 'Energy', 'GHG Savings (kg)': "GreenHouseGasSave",
                  'Transaction Date (Pacific Time)':'Transaction Date',
                   'Charging Time (hh:mm:ss)':'Charging Time',
                   'Total Duration (hh:mm:ss)': 'Total Duration',
                   'Gasoline Savings (gallons)': 'Gasoline Savings'
                  }, inplace=True)
print(df.columns)


# In[6]:


df.head()
#MAC stands for Media Access Control address, MAC addresses are used as a way to uniquely identify a device on a network at the data link layer of the OSI model


# In[ ]:





# In[7]:


df.info()


# In[8]:


df = df.drop(columns=['Country','State/Province','Currency'])


# Drop columns:
# Start Time Zone, End Time Zone. Report base on PDT no need to included in column
# Country, State/Province. Report is base on California State no need to include country and state
# Currency. No need to include currency 

# In[9]:


#Write an utility function to perform basic data quality checks

def basic_check(df):
    """
    should return Number of rows, Number of columns, Missing values,
    Duplicated columns, Duplicated rows
    """
    
    #take a look at the shape of dataset
    print(f'There are {df.shape[0]} rows and {df.shape[1]} columns in the dataset.')
    
    #take a look at the unique datatypes:
    print(f'Unique datatypes: {list(df.dtypes.unique())}')
    
    #check for missing values
    print(f'Missing values: {df.isnull().sum().any()}')
    
    #check for duplicates
    print(f'Duplicated columns: {df.T.duplicated().any()}')
    
    #row-level duplicates
    print(f'Duplicated rows: {df.duplicated().any()}')


# In[10]:


basic_check(df)


# In[11]:


df.describe().T
#Univartriate Analysis
#This dataset contains only numerical values
#Summary statistic


# In[12]:


df['Station Name'] = df['Station Name'].str.replace('PALO ALTO CA /','')
df['Station Name'].value_counts()


# In[13]:


df.columns


# In[14]:


df['Station Name'] = df['Station Name'].replace({'BRYANT # 1': 'BRYANT #1'})


# In[15]:


#Convert columns TotalDuration and charging time to seconds

df['Total Duration'] = pd.to_timedelta(df['Total Duration']).dt.total_seconds()
df['Charging Time'] = pd.to_timedelta(df['Charging Time']).dt.total_seconds()
df['TimeAfterCharged'] = (df['Total Duration'] - df['Charging Time']) / 60



# In[16]:


df.head()


# In[17]:


df['Postal Code'].value_counts()


# In[18]:


df['Address 1'].value_counts()


# In[19]:


df.groupby(['Address 1','Postal Code'])['Charging Time'].mean()/60
#Find the mean of charging time per address and postal code


# In[20]:


avgTimeBy_St = df.groupby(['Station Name', 'Address 1'])['Charging Time'].mean() / 60
avgTimeBy_St.sort_values(ascending=False)
#changing it to minute 
#average charging time by station


# In[21]:


#create histogram to show 
plt.figure(figsize = (12,12))
avgPerStation = df.groupby('Station Name')['Charging Time'].mean()/60 #convert back to minute fore readablity
avgPerStations = avgPerStation.sort_values(ascending=False)
avgPerStations.plot(kind='bar', color='green')
plt.title('Average Charging Time by Station')
plt.xlabel('Station Name')
plt.ylabel('Average Charging Time by Minute')
plt.show()


# Average time of Sherman 8 station is 342.808333 and address is 350 Sherman Ave.

# In[22]:


df.columns



# Dec 20 EDA process
# 

# In[34]:


df['Station Name'] = df['Station Name'].str.replace('BRYANT # 1', 'BRYANT #1')


# In[38]:


df['Total_Amount_For_Charging']  = df['Fee'] * df['Charging Time']


# In[39]:


df.groupby('Station Name')['Total_Amount_For_Charging'].sum()


# Total charging fee accumulate over 9 years

# In[45]:


#create histogram and see which station has highest 
plt.figure(figsize=(12,12))
totalAmount = df.groupby('Station Name')['Total_Amount_For_Charging'].sum()
total_Amount = totalAmount.sort_values(ascending=False)
total_Amount.plot(kind='bar', color = 'green')
plt.title('Total Sale Per Charging Station Over 9 Years')
plt.xlabel('Station Name')
plt.ylabel('Total Charging Fees')
plt.show()


# In[46]:


#plt.figure(figsize=(14,8))
#sns.regplot(x=df['Address 1'], y = df['GreenHouseGasSave'] )
#sns.despine()
#plt.title("Address 1 vs charging Time")


# In[23]:


#Display column names and cunt with Nulls
print(df[df == np.inf].count())


# In[27]:


df['County'].value_counts()


# In[28]:


df['County'].isna().sum()


# In[30]:


df.groupby(['Station Name','Address 1'])['Fee'].sum()


# In[47]:


#All the address location with free charging stations
df[df['Fee'] == 0]['Address 1'].unique()


# In[48]:


df[df['Fee']== 0]['Fee'].count()


# In[49]:


df[df['Fee'] > 0]['Station Name'].unique()


# In[50]:


df['Driver Postal Code'].value_counts()


# In[51]:


plt.figure(figsize=(14,8))
sns.regplot(x=df['Driver Postal Code'], y=df['Postal Code'])
sns.despine()
plt.title("Charging Station Postal Code vs Driver Postal Code")


# Many NaN values on County 
# Need to fill it up with actual county names

# In[52]:


df['County'].value_counts()


# In[58]:


df['County'].isna().sum()


# There are 84665 NaN values in County column

# In[64]:


# Create a map for county
#county_mapping = {
 # how to create and fill the map....
}

# Use the mapping to fill in NaN values in the 'County' column based on the 'Address' column
#df['County'] = df['Address 1'].map(county_mapping).fillna(df['County'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




