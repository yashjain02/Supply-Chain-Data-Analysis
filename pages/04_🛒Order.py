import streamlit as st
import pandas as pd
import plotly.express as px

df1 = pd.read_csv('dataset/DataCoSupplyChainDataset.csv',encoding='ISO-8859-1')

# Order by Category
st.title('Order by Category')
df3 = df1.groupby(['Category Name'])['Order Id'].count().reset_index(name='Number of Orders').sort_values(by='Number of Orders',ascending= True)
chart_3 = px.bar(df3, x='Number of Orders',y = 'Category Name',color ='Number of Orders')
st.write(chart_3)
#Geo Features

st.title('Order by Region')
df4 = df1.groupby(['Order Region'])['Order Id'].count().reset_index(name='Number of Orders').sort_values(by= 'Number of Orders', ascending= True)
chart_4 = px.bar(df4,x = 'Order Region',y='Number of Orders',color ='Number of Orders')
st.write(chart_4)



st.area_chart(df1['Days for shipping (real)'].head(100))
