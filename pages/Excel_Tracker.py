import streamlit as st
import pandas as pd

df=pd.read_excel('Test_data_excel.xlsx')

st.dataframe(df)