import streamlit as st
import seaborn as sns
import pandas as pd

st.set_page_config(page_title="🐧 Penguin Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = sns.load_dataset('penguins').dropna()
    return df

df = load_data()

st.title("🐧 Penguin Species Dashboard")
st.markdown("""
This dashboard presents detailed analyses of the *palmerpenguins* dataset, focusing on differences between male and female penguins across species.   
""")

# High-level metrics
st.subheader("📊 Dataset Summary")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Records", len(df))
col2.metric("Species Count", df['species'].nunique())
col3.metric("Islands", df['island'].nunique())
col4.metric("Sex Categories", df['sex'].nunique())

st.markdown("---")
st.subheader("👉 Use the **sidebar navigation** to access the Female, Male, or Comparative Analysis pages.")
