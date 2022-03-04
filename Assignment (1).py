#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT                                                                                   
#                                                                                                                  Kirti Rai

# Explanatory data analysis(EDA) on a car dataset

# In[1]:


#importing packages
import pandas as pd
import numpy as np
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #visualisation
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[2]:


df = pd.read_csv(r"C:\Users\LenovoS340iUIN\Downloads\rawdata\e5d3e859aa0c794be10b-b999fb4425b54c63cab088c0ce2c0d6ce961a563\\cars.csv")
df.head(5) #to display top 5 row


# In[3]:


df.tail(5) #to display bottom 5 rows


# In[4]:


df.dtypes


# In[5]:


#Total number of rows and columns
df.shape


# In[6]:


sns.boxplot(x=df['hp'])


# In[7]:


sns.boxplot(x=df['mpg'])


# In[8]:


sns.boxplot(x=df['gear'])


# In[9]:


sns.boxplot(x=df['carb'])


# In[10]:


sns.boxplot(x=df['wt'])


# In[11]:


# Plotting a Histogram
df.wt.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5)) 
plt.title("Number of cars by make")
plt.ylabel('Number of cars')
plt.xlabel('Make');


# In[12]:


df = df.dropna() # Dropping the missing values.
df.count()


# In[14]:


# Finding the relations between the variables.
plt.figure(figsize=(20,10))
c= df.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
c


# In[16]:


# Plotting a scatter plot
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['mpg'], df['wt'])
ax.set_xlabel('mpg')
ax.set_ylabel('wt')
plt.show()

