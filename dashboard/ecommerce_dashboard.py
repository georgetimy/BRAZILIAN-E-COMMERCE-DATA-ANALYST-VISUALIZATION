# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 13:38:45 2023

@author: jorsj
"""
#Import the required libraries
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Reading a DataFrame from a CSV file
customer_df = pd.read_csv('dashboard/customer_df.csv')
top_product = pd.read_csv('dashboard/top_product.csv')

# Rename columns to avoid conflicts
customer_df = customer_df.rename(columns={"customer_unique_id": "customer_id_total"})
top_product = top_product.rename(columns={"order_id": "order_id_total"})

# Streamlit page configuration
st.set_page_config(page_title="BRAZILIAN E-COMMERCE DATA ANALYST VISUALIZATION")

# Displays the title
st.title("BRAZILIAN E-COMMERCE DATA ANALYST VISUALIZATION")

# Displays subtitles for cities with the most subscribers
st.subheader('The following are the cities in Brazil with the largest number of customers')

# Counting the number of unique customers per city and picking the top 5 cities
top_city = customer_df.groupby(by="customer_city").customer_id_total.nunique().sort_values(ascending=False).head(5)
top_city
# Specifies the city to be colored with a specific color (for example, Sao Paulo)
city_result = 'sao paulo'

# Set up colors for each bar
colors = ['red' if city == city_result else 'blue' for city in top_city.index]

# Create a bar chart with matplotlib
fig, ax = plt.subplots()
ax.bar(top_city.index, top_city, color=colors)

# Add labels to the x-axis
plt.xticks(rotation=45, ha='right')  # Rotate city names so they don't overlap

# Displays bar charts using Streamlit
st.pyplot(fig)

# Menampilkan instruksi
instructions_1 = f"""
From the bar chart that we have seen above,
the city with the largest number of customers is the {city_result} city.
"""
st.write(instructions_1)

# Displays subtitles for products with the most sales in Sao Paulo
st.subheader('The following are categories of product names with the highest sales figures in Sao Paulo')

# Counts the number of unique orders per product category and takes the top 5 categories
top_product_english = top_product.groupby(by="product_category_name_english").order_id_total.nunique().sort_values(ascending=False).head(5)
top_product_english

# Determine the product categories that will be colored with a special color
product_result = 'bed_bath_table'  # Replace it with the desired product category
colors_product = ['orange' if category == product_result else 'green' for category in top_product_english.index]

# Create a bar chart with matplotlib
fig_product, ax_product = plt.subplots()
ax_product.bar(top_product_english.index, top_product_english, color=colors_product)

# Add labels to the x-axis
plt.xticks(rotation=45, ha='right')  # Rotate product category names so they don't overlap

# Displays bar charts using Streamlit
st.pyplot(fig_product)

# Displays instructions
instructions_2 = f"""
From the bar chart that we have seen above,
The product category with the largest number of sales in the city of Sao Paulo is
{product_result}.
"""
st.write(instructions_2) 
