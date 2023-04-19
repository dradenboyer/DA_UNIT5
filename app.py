import streamlit as st
import pandas as pd
import numpy as np



st.title(':green[Supermarket Data]')
df = pd.read_csv('supermarket.csv')

st.subheader(':red[Top 10 performing stores]')
cols = ['store_id', 'store_area', 'items_available', 'daily_customer_count', 'store_sales']
st.bar_chart(df['store_sales'].nlargest(n=10))

st.subheader(':red[Lowest 10 performing stores]')
st.bar_chart(df['store_sales'].nsmallest(n=10))

st.subheader(':orange[Top 5 performing areas]')
st.bar_chart(df['store_area'].nlargest(n=5))

st.subheader(':orange[Lowest 5 performing areas]')
st.bar_chart(df['store_area'].nsmallest(n=5))

st.line_chart(df['daily_customer_count'])
