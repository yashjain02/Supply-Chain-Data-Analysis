import streamlit as st
import pandas as pd
import plotly.express as px

df1 = pd.read_csv('dataset/DataCoSupplyChainDataset.csv',encoding='ISO-8859-1')
st.title('Number of order and order profit VS Customer')
options=st.selectbox('Select option below',['Order Id','Order Profit Per Order'],key=1)
if options == 'Order Id':
    df1['Customer_ID_STR']=df1['Customer Id'].astype(str)
    data_customers=df1.groupby(['Customer_ID_STR'])['Order Id'].count().reset_index(name='Number Of Orders').sort_values(by= 'Number Of Orders', ascending= False)
    fig1 = px.bar(data_customers.head(20),x='Customer_ID_STR', y= 'Number Of Orders', color='Number Of Orders')
    st.plotly_chart(fig1)
    st.write('Customer Id number 5654 has ordered the highest items amoung all customers')
else:
    df1['Customer_ID_STR']=df1['Customer Id'].astype(str)
    data_customers_profit=df1.groupby(['Customer_ID_STR'])['Order Profit Per Order'].sum().reset_index(name='Profit of Orders').sort_values(by= 'Profit of Orders', ascending= False)
    fig2=px.bar(data_customers_profit.head(20),x='Profit of Orders', y='Customer_ID_STR' , color='Profit of Orders'      )
    st.plotly_chart(fig2)
    st.write('Customer id 2641 has given highest profit per order')

st.title('Names of top fraud customers')
cus = df1[(df1['Order Status'] == 'SUSPECTED_FRAUD')]
fig8 = cus['Customer Fname'].value_counts().nlargest(10)
fraudcus = px.bar(fig8, title="Top 10 Highest Fraud Customers")
st.plotly_chart(fraudcus)
st.write('Customers having first name as Mary are tend to be fraud')

st.title('Number of Orders of different Customer Segments')
data_Customer_Segment=df1.groupby(['Customer Segment'])['Order Id'].count().reset_index(name='Number of Orders').sort_values(by= 'Number of Orders', ascending= False)
fig3 = px.pie(data_Customer_Segment, values='Number of Orders', names= 'Customer Segment' , title= 'Number of Orders of different Customer Segments',
       width=600 , height=600 , color_discrete_sequence = px.colors.sequential.RdBu, )
st.plotly_chart(fig3)
st.write('Majority of customers are consumers and least have setup home office')
