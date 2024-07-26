#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd  #data manipulation and anslysis
import matplotlib.pyplot as plt  #data visualization
import os


# In[2]:


import  plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.express as px


# In[3]:


import plotly.io as pio
pio.renderers.default ='notebook' #to initialize plotly


# In[4]:


df1 = pd.read_csv('covid.csv')


# In[5]:


df2 = pd.read_csv('covid_grouped.csv')


# In[6]:


df2.head()


# In[7]:


df2.tail()


# In[8]:


df1.head()


# # Data cleaning

# In[9]:


df2.isnull()


# In[10]:


df1.columns


# In[11]:


df1.dtypes


# In[12]:


df1.isnull().sum()


# In[13]:


df1.drop(['NewCases','NewRecovered','NewDeaths'],axis=1,inplace=True)


# In[14]:


# filling colums of null values in TotalTests with 0
df1['TotalTests']=df1['TotalTests'].fillna('0') 


# In[15]:


df1.dtypes


# In[16]:


# converting TotalTests (obj type) to numeric 
df1['TotalTests']=pd.to_numeric(df1['TotalTests'],errors = 'coerce')


# In[17]:


df1 = df1.fillna({
    'Country/Region': 'Unknown',
    'Continent': 'Unknown',
    'Population': 0.0,
    'TotalCases': 0,
    'TotalDeaths': 0.0,
    'TotalRecovered': 0.0,
    'ActiveCases': 0.0,
    'Serious,Critical': 0.0,
    'Tot Cases/1M pop': 0.0,
    'Deaths/1M pop': 0.0,
    'TotalTests': 0.0,
    'Tests/1M pop': 0.0,
    'WHO Region': 'Unknown',
    'iso_alpha': 'Unknown'
})


# In[18]:


df1.head()


# # creating tables

# In[19]:


from plotly.figure_factory import create_table


# In[20]:


table=create_table(df1.head(10),colorscale="blues")
py.iplot(table)


# # Quick Visualization with custom Bar Charts

# In[21]:


df1.columns


# In[22]:


px.bar(df1.head(10),x='Country/Region', y='TotalCases',color='TotalCases',
       height=600,hover_data=['Country/Region','Continent'])


# In[23]:


top10_df1_TC=df1.sort_values(by='TotalCases',ascending=False).head(30)


# In[24]:


px.bar(top10_df1_TC,x='Country/Region', y='TotalCases',color='Country/Region',
       height=600,hover_data=['Country/Region','Continent'])


# In[25]:


px.bar(df1,x='Country/Region', y='TotalDeaths',color='Country/Region',
       height=500,width=2000,hover_data=['Country/Region','Continent'])


# In[26]:


top_10_df1_TD = df1.sort_values(by='TotalDeaths', ascending=False).head(20)


# In[27]:


px.bar(top_10_df1_TD,x='Country/Region', y='TotalDeaths',color='Country/Region',
       height=500,width=1000,hover_data=['Country/Region','Continent'])


# In[28]:


px.bar(df1.head(10),x='Country/Region', y='TotalRecovered',color='Country/Region',
       height=500,width=700,hover_data=['Country/Region','Continent'])


# In[29]:


top10_df1_TR = df1.sort_values(by='TotalRecovered',ascending=False).head(20)


# In[30]:


px.bar(top10_df1_TR,x='Country/Region', y='TotalRecovered',color='Country/Region',
       height=500,width=1000,hover_data=['Country/Region','Continent'])


# In[31]:


px.bar(df1,x='TotalTests', y='Country/Region',color='TotalTests',orientation='h',
       height=1100,width=800,hover_data=['Country/Region','Continent'])


# In[32]:


px.bar(df1,x='TotalTests', y='Continent',color='TotalTests',orientation='h',
       height=600,width=700,hover_data=['Country/Region','Continent'])


# # Data Visualization using Bubble Chart

# In[33]:


df1.columns


# We will use log function while visualizing some of the upcoming charts. Why do we use log function??
# 
# 1) Handling Wide Range of Values:If your data includes both very small and very large values, a log scale can compress the range, making the chart more readable and easier to interpret. Linear scales can make it difficult to visualize and compare values that differ significantly. 
# 
# 2) Reducing Skewness:Log scales can reduce the skewness of data, making patterns more apparent and clustering of data points more manageable.
# 
# 3) Linearizing Exponential Relationships: If your data follows an exponential growth pattern, plotting on a log scale can linearize the relationship, making trends more evident and easier to analyze. This is common in fields like epidemiology (e.g., the spread of diseases) and finance (e.g., compound interest).
# 
# 4) Proportional Comparisons: Log scales highlight proportional changes rather than absolute changes. For example, a change from 1 to 10 is treated the same as a change from 10 to 100, emphasizing the factor change.
# 
# 5) Reducing the Impact of Outliers: Large outliers can dominate the visualization on a linear scale, making it hard to see the rest of the data. A log scale can mitigate this effect and provide a clearer view of the overall data distribution.
# 

# ### Total Cases vs Continents(50 Countries)

# In[34]:


px.scatter(df1,x='Continent',y='TotalCases',hover_data=['Country/Region','Continent'],
           color='TotalCases',size='TotalCases',size_max=80)


# In[35]:


px.scatter(df1,x='Continent',y='TotalCases',hover_data=['Country/Region','Continent'],
           color='TotalCases',size='TotalCases',size_max=80,log_y=True)


# ### Total tests vs Continent(50 countries)

# In[36]:


px.scatter(df1,x='Continent',y='TotalTests',hover_data=['Country/Region','Continent'],
           color='TotalTests',size='TotalTests',size_max=80)


# In[37]:


px.scatter(df1,x='Continent',y='TotalTests',hover_data=['Country/Region','Continent'],
           color='TotalTests',size='TotalTests',size_max=80,log_y=True)


# ### Total Deaths vs Continents(50)

# In[38]:


px.scatter(df1,x='Continent',y='TotalDeaths',hover_data=['Country/Region','Continent'],
           color='TotalDeaths',size='TotalDeaths',size_max=80,log_y=True)


# ### Total Cases vs Countries

# In[39]:


px.scatter(df1,x='Country/Region',y='TotalCases',hover_data=['Country/Region','Continent'],
           color='Country/Region',size='TotalCases',size_max=100,log_y=True)


# ### Total Deaths vs Countries(50)

# In[40]:


px.scatter(df1,x='Country/Region',y='TotalDeaths',hover_data=['Country/Region','Continent'],
           color='Country/Region',size='TotalDeaths',size_max=100)


# ### TotalTests/1M vs Countries

# In[41]:


px.scatter(df1,x='Country/Region',y='Tests/1M pop',hover_data=['Country/Region','Continent'],
           color='Tests/1M pop',size='Tests/1M pop',size_max=100)


# In[42]:


#Top values of columns
top_df1_TT = df1.sort_values(by='TotalTests', ascending=False).head(20)
top_df1_TD = df1.sort_values(by='TotalDeaths', ascending=False).head(20)
top_df1_TC = df1.sort_values(by='TotalCases', ascending=False).head(20)
top_df1_TM = df1.sort_values(by='Tests/1M pop', ascending=False).head(30)


# In[43]:


#Least values of columns
least_df1_TT = df1.sort_values(by='TotalTests', ascending=True).head(20)
least_df1_TD = df1.sort_values(by='TotalDeaths', ascending=True).head(20)
least_df1_TC = df1.sort_values(by='TotalCases', ascending=True).head(20)
least_df1_TM = df1.sort_values(by='Tests/1M pop', ascending=True).head(20)


# In[44]:


px.scatter(top_df1_TM,x='Country/Region',y='Tests/1M pop',hover_data=['Country/Region','Continent'],
           color='Tests/1M pop',size='Tests/1M pop',size_max=100)


# ### Total Cases vs Total Deaths

# In[45]:


px.scatter(df1,x='TotalCases',y='TotalDeaths',hover_data=['Country/Region','Continent'],
           color='TotalDeaths',size='TotalDeaths',size_max=100)


# Almost a linear relationship b/w TotalDeaths and ToatalCases.This is beacuse the higher the cases the more number of deaths. Russia is an exception beacuse they have less deaths compared to the cases thats been reported so Russia has been able to reduce the deaths by their precautionary methods

# In[46]:


px.scatter(df1,x='TotalCases',y='TotalDeaths',hover_data=['Country/Region','Continent'],
           color='TotalDeaths',size='TotalDeaths',size_max=80,log_x=True,log_y=True)


# ### Total tests vs Total Cases

# In[47]:


px.scatter(df1,x='TotalTests',y='TotalCases',hover_data=['Country/Region','Continent'],
           color='TotalTests',size='TotalTests',size_max=80,log_x=True,log_y=True)


# ## Advanced Data Visualization using line graph & Bar graph (Dataset 2) 

# This dataset(df2) contains DATE column which makes it more appropriate for more advanced visulization

# In[48]:


df2.columns


# In[49]:


df2.head()


# In[50]:


df2.tail()


# In[51]:


df2.dtypes


# In[52]:


df2.isnull().sum()


# In[53]:


df2.describe()


# ### Date vs Confirmed

# In[54]:


px.bar(df2,x='Date', y='Confirmed',color='Confirmed',hover_data=['Date','Confirmed','Country/Region'],height=400)


# In[55]:


px.bar(df2,x='Date', y='Confirmed',color='Confirmed',hover_data=['Date','Confirmed','Country/Region'],log_y=True,height=400)


# ### Date vs Deaths(all countries) [Line Graph]

# In[56]:


px.bar(df2,x='Date', y='Deaths',color='Deaths',hover_data=['Date','Confirmed','Country/Region'],log_y=False,height=400)


# ## Country Specific:Analysis of United States using Line graph and Bar Graph

# In[57]:


df_US = df2.loc[df2['Country/Region']=="US"]


# ### Date vs Confirmed

# In[58]:


px.bar(df_US,x='Date', y='Confirmed', color='Confirmed',height=400)


# In[59]:


px.line(df_US,x='Date', y='Confirmed',height=400)


# ### Date vs Recovered

# In[60]:


px.bar(df_US, x='Date', y='Recovered',color='Recovered',height=400)


# In[61]:


px.line(df_US, x='Date', y='Recovered',height=400)


# In[62]:


px.line(df_US, x='Date', y='Deaths',height=400)


# ### Date vs New cases

# In[63]:


px.line(df_US, x='Date', y='New cases',height=400)


# In[64]:


px.bar(df_US, x='Date', y='New cases',height=400)


# ## Country Specific:Analysis of India using Line graph and Bar Graph

# In[65]:


df_ind = df2.loc[df2['Country/Region']=="India"]


# ### Date vs Deaths

# In[66]:


px.line(df_ind, x='Date', y='Deaths',height=400)


# ### Date vs New cases 

# In[67]:


px.bar(df_ind, x='Date', y='New cases',height=400)


# In[68]:


px.line(df_ind, x='Date', y='New cases',height=400)


# There has been a steady rise in the number of new cases in India as compared to US.

# ### Date vs Confirmed

# In[69]:


px.bar(df_ind, x='Date', y='Confirmed',height=400)


# ### Date vs New deaths

# In[70]:


px.bar(df_ind, x='Date', y='New deaths',height=400)


# ### Date vs Recovered

# In[71]:


px.bar(df_ind, x='Date', y='Recovered',height=400)


# In[72]:


px.line(df_ind, x='Date', y='Recovered',height=400)


# In[73]:


px.line(df_ind, x='Date', y='New recovered',height=400)


# In[74]:


px.scatter(df_US,x='Confirmed',y='Deaths',height=400)


# In[75]:


px.scatter(df_ind,x='Confirmed',y='New cases',height=400)


# # Represent Geographic Data as Choropleth Maps

# A choropleth map displays divided geographical areas or regions that are colored,  shaded or patterned in relation to a data variable.
# 
# #Dataset2---df2             
# #parameters --- dataset,locations=ISOALPHA, color,hover_name,color_continuous_scale=[RdYiGn,Blues,Viridis.....],animation_frame = Date
# 
# Its an amazing representation of data in a map.Choropleth maps provide an easy way to visualize how an measurement varies across a geographical area or region

# ### Equi-rectangular Projection:Total cases

# In[77]:


px.choropleth(df2,locations='iso_alpha',color='Confirmed',hover_name='Country/Region',color_continuous_scale='Blues',animation_frame='Date')


# In[78]:


px.choropleth(df2,locations='iso_alpha',color='Deaths',hover_name='Country/Region',color_continuous_scale='Viridis',animation_frame='Date')


# ### Orthographic projection:Total Death

# In[79]:


px.choropleth(df2,locations='iso_alpha',color='Deaths',hover_name='Country/Region',
              color_continuous_scale='Viridis',
              projection='orthographic',animation_frame='Date')


# ### Equirectangular Projection: Total Recovered

# In[80]:


px.choropleth(df2,locations='iso_alpha',color='Recovered',hover_name='Country/Region',
              color_continuous_scale='rdylgn',
              projection='natural earth',animation_frame='Date')


# # Animations

# In[81]:


px.bar(df2,x='WHO Region',y='Confirmed',color='WHO Region',
      animation_frame='Date',hover_name='Country/Region')


# ### Bar animation: New cases

# In[82]:


px.bar(df2,x='WHO Region',y='New cases',color='WHO Region',
      animation_frame='Date',hover_name='Country/Region')


# # WordCloud(Reasons of Death)(New dataset-3)

# In[83]:


#Step1 Importing WordCloud and datasets
#Step2 Exploring data using pandas               #New dataset-3
#Step3 Creating WordCloud


# In[84]:


#Step3a : Convert the column with diseases count into list using tolist() function
#Step3b : Convert the list to one single string
#Step3c : Convert the string into WordCloud


# In[85]:


from wordcloud import WordCloud


# In[86]:


df3 = pd.read_csv('covid+death.csv')


# In[87]:


df3.head()


# In[88]:


df3.tail()


# In[89]:


df3.groupby(["Condition"]).count()


# In[90]:


df3.groupby(["Condition Group"]).count()


# In[91]:


## WORDCLOUD1 ----> "Condition" column


# In[92]:


sentences = df3['Condition'].tolist()


# In[93]:


#converting sentences to string
sentences_as_a_string = ' '.join(sentences)


# In[94]:


pip install --upgrade pip


# In[95]:


pip install --upgrade Pillow


# In[96]:


plt.figure(figsize=(14,14))
plt.imshow(WordCloud().generate(sentences_as_a_string))


# In[97]:


#WORDCLOUD 2 ---> "Condition Group" column


# In[98]:


column2_tolist=df3['Condition Group'].tolist()


# In[99]:


column_to_string=" ".join(column2_tolist)


# In[100]:


plt.figure(figsize=(15,15))
plt.imshow(WordCloud().generate(column_to_string))


# In[ ]:




