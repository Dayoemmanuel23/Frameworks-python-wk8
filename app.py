import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re

# Load cleaned sample dataset
@st.cache_data
def load_data():
    return pd.read_csv("cord19_cleaned.csv")

df = load_data()

st.title("📊 CORD-19 Sample Data Explorer")
st.write("Interactive exploration of COVID-19 research metadata (sample).")

# Sidebar filters
st.sidebar.header("Filters")
min_year, max_year = int(df['year'].min()), int(df['year'].max())
year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

journals = st.sidebar.multiselect("Select Journals", options=df['journal'].dropna().unique(), default=[])
if journals:
    filtered_df = filtered_df[filtered_df['journal'].isin(journals)]

st.write(f"Showing {len(filtered_df)} papers from {year_range[0]} to {year_range[1]}")

# Publications by year
st.subheader("📈 Publications by Year")
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(7,4))
sns.barplot(x=year_counts.index, y=year_counts.values, color='skyblue', ax=ax)
ax.set_xlabel("Year"); ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# Top Journals
st.subheader("🏛️ Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(y=top_journals.index, x=top_journals.values, palette='viridis', ax=ax)
st.pyplot(fig)

# Word Cloud
st.subheader("☁ Word Cloud of Paper Titles")
titles_text = " ".join(filtered_df['title'].dropna().astype(str))
titles_text = re.sub(r'[^A-Za-z ]', ' ', titles_text).lower()
wc = WordCloud(width=800, height=400, background_color='white', max_words=100).generate(titles_text)
fig, ax = plt.subplots(figsize=(10,5))
ax.imshow(wc, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

# Top Sources
st.subheader("📚 Distribution by Source")
source_counts = filtered_df['source_x'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(y=source_counts.index, x=source_counts.values, palette='coolwarm', ax=ax)
st.pyplot(fig)

# Data preview
st.subheader("📋 Sample Data")
st.dataframe(filtered_df[['title','authors','journal','year']].head(20))
