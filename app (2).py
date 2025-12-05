
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

def load_data(file_path):
    """Loads data from a CSV file into a pandas DataFrame."""
    if not os.path.exists(file_path):
        st.error(f"Error: The file '{file_path}' was not found.")
        return None
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

st.set_page_config(layout="wide")

st.title("Video Game Sales Dashboard")

# Load data
file_path = 'video_games_sales.csv'
data = load_data(file_path)

if data is not None:
    st.success("Data loaded successfully!")
    st.subheader('Raw Data Overview')
    st.dataframe(data.head())

    st.subheader('Total Global Sales by Genre')
    # Group by genre and sum sales
    sales_by_genre = data.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)

    # Create the bar chart for genre
    fig_genre, ax_genre = plt.subplots(figsize=(12, 6))
    sales_by_genre.plot(kind='bar', ax=ax_genre)
    ax_genre.set_title('Total Global Sales by Genre')
    ax_genre.set_xlabel('Genre')
    ax_genre.set_ylabel('Total Global Sales (in millions)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig_genre)

    st.subheader('Total Global Sales by Platform')
    # Group by platform and sum sales
    sales_by_platform = data.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False)

    # Create the bar chart for platform
    fig_platform, ax_platform = plt.subplots(figsize=(12, 6))
    sales_by_platform.plot(kind='bar', ax=ax_platform)
    ax_platform.set_title('Total Global Sales by Platform')
    ax_platform.set_xlabel('Platform')
    ax_platform.set_ylabel('Total Global Sales (in millions)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig_platform)

else:
    st.warning("Please ensure the CSV file is in the correct path.")
