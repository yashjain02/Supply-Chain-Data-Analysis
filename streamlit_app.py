import streamlit as st
import pandas as pd
st.title('Supply Chain Data Analysis')

st.markdown('Dataset')
df1 = pd.read_csv('dataset/DataCoSupplyChainDataset.csv',encoding='ISO-8859-1')
st.dataframe(df1)
