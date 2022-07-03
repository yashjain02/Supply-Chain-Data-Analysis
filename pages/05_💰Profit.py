import streamlit as st
import pandas as pd
import plotly.express as px

df1 = pd.read_csv('dataset/DataCoSupplyChainDataset.csv',encoding='ISO-8859-1')

options1 = st.selectbox('Select option below',['Category Name','Order Region'],key=2)

loss = df1[(df1['Benefit per order']>0)]
fug5=loss[options1].value_counts().nlargest(10)
fig5=px.bar(fug5, title="Products with most Profit")
st.plotly_chart(fig5)

