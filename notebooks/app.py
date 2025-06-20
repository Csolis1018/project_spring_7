import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Vehicules in the US')
hist_button = st.button('Oprime este boton si quieres crear un histograma')

if hist_button:
    st.write('No se diga mas!')
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button(
    'o mejor oprime este otro boton para una grafica de dispersion')

if disp_button:
    st.write('Sabia que presionarias mejor este boton!')
    fig = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)
