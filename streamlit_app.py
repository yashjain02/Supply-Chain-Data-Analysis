import streamlit as st
import pandas as pd
st.title('Supply Chain Data Analysis')

with st.expander("Developed By", expanded=False):
    st.write("- Yash Kumar Jain ")
    st.write("- Thi truc linh Le")
st.write("A DataSet of Supply Chains used by the company DataCo Global was used for the analysis. Dataset of Supply "
         "Chain ,Areas of important registered activities : Provisioning , Production , Sales , Commercial "
         "Distribution.It also allows the correlation of Structured Data with Unstructured Data for knowledge "
         "generation.")

st.write('Type Data :')
st.write('Structured Data : DataCoSupplyChainDataset.csv')
st.write('Unstructured Data : tokenizedaccesslogs.csv (Clickstream)')

st.write("Types of Products : Clothing , Sports , and Electronic Supplies")
df1 = pd.read_csv('dataset/DataCoSupplyChainDataset.csv',encoding='ISO-8859-1')
st.dataframe(df1)
