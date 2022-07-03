import streamlit as st
import pandas as pd
import plotly.express as px

df1 = pd.read_csv('dataset/DataCoSupplyChainDataset.csv',encoding='ISO-8859-1')

#Delivey status per region
st.title('Delivery Status by Region')
df2 = df1.loc[(df1['Delivery Status'] == "Shipping canceled") | (df1['Delivery Status'] == "Late delivery"), ["Delivery Status","Order Region", "Order Id"]]  # Row and column selection
df2 = df2.groupby(['Delivery Status','Order Region'])['Order Id'].count().reset_index(name='Number of Orders').sort_values(
    by='Number of Orders', ascending=False)
chart_2 = px.bar(df2, x='Delivery Status', y='Number of Orders', color='Order Region')
st.write(chart_2)

data_Customer_Segment=df1.groupby(['Customer Segment'])['Order Id'].count().reset_index(name='Number of Orders').sort_values(by= 'Number of Orders', ascending= False)
fig3 = px.pie(data_Customer_Segment, values='Number of Orders', names= 'Customer Segment' , title= 'Number of Orders of different Customer Segments',
       width=600 , height=600 , color_discrete_sequence = px.colors.sequential.RdBu, )
st.plotly_chart(fig3)

st.title('Delivery Status')
df1 = df1.groupby(['Delivery Status'])['Order Id'].count().reset_index(name='Number of Orders').sort_values(by='Number of Orders', ascending=False)
chart_1 = px.pie(df1,values='Number of Orders', names='Delivery Status')
st.write(chart_1)