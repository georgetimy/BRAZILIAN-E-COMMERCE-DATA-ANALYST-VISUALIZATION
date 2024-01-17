# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 13:38:45 2023

@author: jorsj
"""
#Mengimport Library yang dibutuhkan
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Membaca DataFrame dari file CSV
customer_df = pd.read_csv('./customer_df.csv')
top_product = pd.read_csv('./top_product.csv')

# Mengganti nama kolom untuk menghindari konflik
customer_df = customer_df.rename(columns={"customer_unique_id": "customer_id_total"})
top_product = top_product.rename(columns={"order_id": "order_id_total"})

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="BRAZILIAN E-COMMERCE DATA ANALYST VISUALIZATION")

# Menampilkan judul
st.title("BRAZILIAN E-COMMERCE DATA ANALYST VISUALIZATION")

# Menampilkan subjudul untuk kota dengan jumlah pelanggan terbanyak
st.subheader('Berikut adalah kota-kota di Brazil dengan jumlah pelanggan terbanyak')

# Menghitung jumlah pelanggan unik per kota dan mengambil 5 kota teratas
top_city = customer_df.groupby(by="customer_city").customer_id_total.nunique().sort_values(ascending=False).head(5)
top_city
# Menentukan kota yang akan diwarnai dengan warna khusus (misalnya, Sao Paulo)
city_result = 'sao paulo'

# Menyiapkan warna untuk setiap bar
colors = ['red' if city == city_result else 'blue' for city in top_city.index]

# Membuat bar chart dengan matplotlib
fig, ax = plt.subplots()
ax.bar(top_city.index, top_city, color=colors)

# Menambahkan label pada sumbu x
plt.xticks(rotation=45, ha='right')  # Rotasi nama kota agar tidak tumpang tindih

# Menampilkan bar chart menggunakan Streamlit
st.pyplot(fig)

# Menampilkan instruksi
instructions_1 = f"""
Dari diagram batang yang telah kita lihat di atas,
kota dengan jumlah pelanggan terbesar adalah kota {city_result}.
"""
st.write(instructions_1)

# Menampilkan subjudul untuk produk dengan jumlah penjualan terbanyak di Sao Paulo
st.subheader('Berikut adalah kategori nama-nama produk dengan angka penjualan tertinggi di Sao Paulo')

# Menghitung jumlah pesanan unik per kategori produk dan mengambil 5 kategori teratas
top_product_english = top_product.groupby(by="product_category_name_english").order_id_total.nunique().sort_values(ascending=False).head(5)
top_product_english

# Menentukan kategori produk yang akan diwarnai dengan warna khusus
product_result = 'bed_bath_table'  # Gantilah dengan kategori produk yang diinginkan
colors_product = ['orange' if category == product_result else 'green' for category in top_product_english.index]

# Membuat bar chart dengan matplotlib
fig_product, ax_product = plt.subplots()
ax_product.bar(top_product_english.index, top_product_english, color=colors_product)

# Menambahkan label pada sumbu x
plt.xticks(rotation=45, ha='right')  # Rotasi nama kategori produk agar tidak tumpang tindih

# Menampilkan bar chart menggunakan Streamlit
st.pyplot(fig_product)

# Menampilkan instruksi
instructions_2 = f"""
Dari diagram batang yang telah kita lihat di atas,
kategori produk dengan jumlah penjualan terbesar di kota Sao Paulo adalah
{product_result}.
"""
st.write(instructions_2) 
