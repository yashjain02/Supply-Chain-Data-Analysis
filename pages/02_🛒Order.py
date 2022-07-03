import streamlit as st
import pandas as pd
import plotly.express as px

df1 = pd.read_csv('dataset/DataCoSupplyChainDataset.csv',encoding='ISO-8859-1')

# Order by Category
st.title('Order by Category')
df3 = df1.groupby(['Category Name'])['Order Id'].count().reset_index(name='Number of Orders').sort_values(by='Number of Orders',ascending= True)
chart_3 = px.bar(df3, x='Number of Orders',y = 'Category Name',color ='Number of Orders')
st.write(chart_3)
st.write('This bar graph shows that  Men Shoes, Hiking and Camping, Sports Shopping, Electronics, and Golf Balls are the top 5 most purchased products.')
#Geo Features

st.title('Order by Region')
df4 = df1.groupby(['Order Region'])['Order Id'].count().reset_index(name='Number of Orders').sort_values(by= 'Number of Orders', ascending= True)
chart_4 = px.bar(df4,x = 'Order Region',y='Number of Orders',color ='Number of Orders')
st.write(chart_4)
st.write('Most of the orders come from Western Europe, Central America, South America, Oceania, Northern Europe, Southeast Asia, Southern Europe.')

