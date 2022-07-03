import streamlit as st
import pandas as pd
import plotly.express as px

df1 = pd.read_csv('dataset/DataCoSupplyChainDataset.csv',encoding='ISO-8859-1')


st.title('Profit by Country')
df5 = df1.groupby([ 'Order Country', 'Order City'])['Order Profit Per Order'].sum().reset_index(name='Profit of Orders').sort_values(by= 'Profit of Orders', ascending= True)
chart_5 = px.choropleth(df5,locationmode='country names', locations='Order Country',
                    color='Profit of Orders',
                    hover_name='Order Country',
                    color_continuous_scale=px.colors.sequential.Plasma)
st.write(chart_5)
st.write('Profits mainly come from countries such as Indonesia, Australia, Argentina, Nicaragua, and Honduras.')
st.title('Countries with highest Fraud')
data2=df1[df1['Order Status'] == 'SUSPECTED_FRAUD']
data2=data2['Order Country'].value_counts().nlargest(10)
fig4=px.bar(data2,y='Order Country')
st.plotly_chart(fig4)
st.write('Customer from united states are tend to do fraud transaction')

