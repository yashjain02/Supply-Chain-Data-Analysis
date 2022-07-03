import streamlit as st
import pandas as pd
import plotly.express as px

df1 = pd.read_csv('dataset/DataCoSupplyChainDataset.csv',encoding='ISO-8859-1')

df_date = df1[['order date (DateOrders)', 'Sales']]
df_date['order_date'] = pd.to_datetime(df_date['order date (DateOrders)'])
df_date["Quarter"] = df_date['order_date'].dt.quarter
df_date["Month"] = df_date['order_date'].dt.month
df_date["Year"] = df_date['order_date'].dt.year
df_date['Month'] = df_date['Month'].astype(str)
df_date['Year'] = df_date['Year'].astype(str)
df_date['Quarter'] = df_date['Quarter'].astype(str)

#Sale per Year
st.title('Sale per Year')
df6 = df_date.groupby(['Year'])['Sales'].sum().reset_index(name='Sales of Orders').sort_values(by= 'Sales of Orders', ascending= False)
chart_6 = px.line(df6, x="Year", y="Sales of Orders")
st.write(chart_6)

#Monthly sale deviation with respect to the average
st.title('Monthly sale deviation with respect to the average')
df7 = df_date.groupby(['Month'])['Sales'].sum().reset_index(name='Sales of Orders').sort_values(by= 'Month', ascending= True)
avg = df7['Sales of Orders'].mean()
percent_sale = ((df7[['Sales of Orders']]-avg)/avg)*100
df7['Percent_sale'] = percent_sale
st.write('Average sale:',avg)
chart_7 = px.bar(df7, x='Month', y='Percent_sale',color='Percent_sale')
st.write(chart_7)


fig11=px.violin(df1['Type'],df1['Delivery Status'],df1['Sales per customer'],color='Type')
st.plotly_chart(fig11, figsize=(10,10))
