import streamlit as st
import pandas as pd
import plotly.express as px

df1 = pd.read_csv('dataset/DataCoSupplyChainDataset.csv',encoding='ISO-8859-1')

#Delivey status per region
st.title('Delivery Status by Region')
df2 = df1.loc[(df1['Delivery Status'] == "Shipping canceled") | (df1['Delivery Status'] == "Late delivery"), ["Delivery Status","Order Region", "Order Id"]]  # Row and column selection
df2 = df2.groupby(['Delivery Status','Order Region'])['Order Id'].count().reset_index(name='Number of Orders').sort_values(
    by='Number of Orders', ascending=False)
chart_2 = px.bar(df2.head(50), x='Delivery Status', y='Number of Orders', color='Order Region')
st.write(chart_2)
st.write('This graph displays the delivery status group by region. Almost all late delivery has happened in Central America and Western Europa.')

st.title('Delivery Status')
df6 = df1.groupby(['Delivery Status'])['Order Id'].count().reset_index(name='Number of Orders').sort_values(by='Number of Orders', ascending=False)
chart_1 = px.pie(df6,values='Number of Orders', names='Delivery Status')
st.write(chart_1)
st.write('This pie chart shows that there is a problem with the delivery. The percentage of late delivery is very large. It accounts for 54.8%.')


st.title('Days for shipping (real) Vs Days for shipment (scheduled)')
df4 = df1[['Days for shipping (real)', 'Days for shipment (scheduled)','Type']]
ch=px.area(df4,x='Type',y='Days for shipping (real)',color='Days for shipment (scheduled)')
st.write(ch)
st.write('This area graph shows whenever customer did Transfer Type received the delivery late and whoever did through payment received early ')
st.title('Delivery status VS Sales per customer')
fig11=px.violin(df1,x='Delivery Status',y='Sales per customer',color='Type')
st.plotly_chart(fig11, x='Delivery Status',y='Sales per customer', figsize=(10,10))
st.write('Customer who paid through online banking their shipping got cancelled and maximum of customer who paid through debit card has received delivery late')
