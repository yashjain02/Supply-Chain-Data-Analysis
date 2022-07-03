import streamlit as st
import pandas as pd
import plotly.express as px

df1 = pd.read_csv('dataset/DataCoSupplyChainDataset.csv',encoding='ISO-8859-1')

options=st.selectbox('Select option below',['Order Id','Order Profit Per Order'],key=1)
if options == 'Order Id':
    df1['Customer_ID_STR']=df1['Customer Id'].astype(str)
    data_customers=df1.groupby(['Customer_ID_STR'])['Order Id'].count().reset_index(name=options).sort_values(by= options, ascending= False)
    fig1 = px.bar(data_customers.head(20),x='Customer_ID_STR', y= options, color=options)
    st.plotly_chart(fig1)
else:
    df1['Customer_ID_STR']=df1['Customer Id'].astype(str)
    data_customers_profit=df1.groupby(['Customer_ID_STR'])['Order Profit Per Order'].sum().reset_index(name='Profit of Orders').sort_values(by= 'Profit of Orders', ascending= False)
    fig2=px.bar(data_customers_profit.head(20),x='Profit of Orders', y='Customer_ID_STR' , color='Profit of Orders'      )
    st.plotly_chart(fig2)

cus = df1[(df1['Order Status'] == 'SUSPECTED_FRAUD')]
fig8=cus['Customer Fname'].value_counts().nlargest(10)
fraudcus=px.bar(fig8, title="Top 10 Highest Fraud Customers")
st.plotly_chart(fraudcus)
