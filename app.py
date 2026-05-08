import streamlit as st
import pandas as pd
import seaborn as sns

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
taxis = pd.read_csv(url)


c1 = st.container()
c1.title("Bienvenue sur le site de Fabrice",text_alignment='center')
c = st.container(border=True, horizontal_alignment='center')
choix = c.selectbox("Indiquez votre arrondissement de récupération", taxis['pickup_borough'].unique())
    

if choix == "Bronx":
    c.write(f"Tu as choisi : {choix}")
    c.image("images/bronx.jpg")
elif choix == "Queens":
    c.write(f"Tu as choisi : {choix}")
    c.image("images/queens.jpg")
elif choix == "Manhattan":
    c.write(f"Tu as choisi : {choix}")
    c.image("images/manhattan.jpg")
elif choix == "Brooklyn":
    c.write(f"Tu as choisi : {choix}")
    c.image("images/brooklyn.jpg")
else:
    c.write(f"Fais ton choix")
    c.image("images/nan.jpg")

st.page_link("https://github.com/One-Up-Dev/streamlit.git", label="Code Source", icon=":material/code_blocks:")
