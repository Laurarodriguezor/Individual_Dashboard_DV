import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    return sns.load_dataset('penguins').dropna()

df = load_data()
male_df = df[df['sex'] == 'Male']

st.title("👨‍🔬 Male Penguin Analysis")

# Metrics
st.subheader("📊 Key Metrics (Male)")
col1, col2, col3 = st.columns(3)
col1.metric("Avg. Body Mass (g)", f"{male_df['body_mass_g'].mean():.1f}")
col2.metric("Avg. Flipper Length (mm)", f"{male_df['flipper_length_mm'].mean():.1f}")
col3.metric("Avg. Bill Length (mm)", f"{male_df['bill_length_mm'].mean():.1f}")

# Body Mass Distribution by Species
st.subheader("📈 Body Mass Distribution by Species")
fig1 = px.violin(male_df, x='species', y='body_mass_g', color='species', box=True, points="all")
st.plotly_chart(fig1, use_container_width=True)

# Correlation Plot
st.subheader("📐 Correlation: Bill Length vs Flipper Length")
fig2 = px.scatter(male_df, x='bill_length_mm', y='flipper_length_mm', color='species',
                  size='body_mass_g', hover_data=['island'])
st.plotly_chart(fig2, use_container_width=True)

# Heatmap of Measurements (focus + context)
st.subheader("🔥 Measurement Heatmap")
heat_df = male_df[['species', 'body_mass_g', 'flipper_length_mm', 'bill_length_mm', 'bill_depth_mm']].groupby('species').mean()
st.dataframe(heat_df.style.background_gradient(cmap='PuBu'))
