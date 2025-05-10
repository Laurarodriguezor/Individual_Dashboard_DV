import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    return sns.load_dataset('penguins').dropna()

df = load_data()
male_df = df[df['sex'] == 'Male']
female_df = df[df['sex'] == 'Female']

st.title("⚖️ Comparative Analysis: Male vs. Female Penguins")

# Summary Gaps
st.subheader("📊 Overall Measurement Gaps")
gap_df = pd.DataFrame({
    'Measurement': ['Body Mass (g)', 'Flipper Length (mm)', 'Bill Length (mm)'],
    'Male Avg': [male_df['body_mass_g'].mean(), male_df['flipper_length_mm'].mean(), male_df['bill_length_mm'].mean()],
    'Female Avg': [female_df['body_mass_g'].mean(), female_df['flipper_length_mm'].mean(), female_df['bill_length_mm'].mean()],
})
gap_df['Gap (Male - Female)'] = gap_df['Male Avg'] - gap_df['Female Avg']
st.dataframe(gap_df.style.background_gradient(cmap='Blues', subset=['Gap (Male - Female)']))

# Side-by-side bar chart
st.subheader("📊 Measurement Comparison by Sex (Separated by Variable)")

# Define custom colors
color_map = {'Male': '#2ca02c',  # dark green
             'Female': '#ff9896'}  # light pink

for i, row in gap_df.iterrows():
    measurement = row['Measurement']
    male_avg = row['Male Avg']
    female_avg = row['Female Avg']
    
    single_df = pd.DataFrame({
        'Sex': ['Male', 'Female'],
        'Average': [male_avg, female_avg]
    })
    
    fig = px.bar(
        single_df, x='Sex', y='Average', color='Sex',
        color_discrete_map=color_map,
        barmode='group',
        text='Average',
        title=f"{measurement} Comparison"
    )
    
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)


# species-level gap
st.subheader("⚡ Species-Level Body Mass Gaps")

# Calculate gap
male_avg = male_df.groupby('species')['body_mass_g'].mean()
female_avg = female_df.groupby('species')['body_mass_g'].mean()
gap_series = male_avg - female_avg

species_gap = gap_series.reset_index()
species_gap.columns = ['species', 'Gap']

# Define consistent species colors (same across pages)
species_color_map = {
    'Adelie': '#1f77b4',      # dark blue
    'Chinstrap': '#aec7e8',   # light blue
    'Gentoo': '#d62728'       # red
}

fig2 = px.bar(
    species_gap, x='species', y='Gap', color='species',
    color_discrete_map=species_color_map,
    labels={'Gap': 'Body Mass Gap (g)'},
    title="Male-Female Body Mass Gap per Species"
)
fig2.update_layout(showlegend=False)
st.plotly_chart(fig2, use_container_width=True)



