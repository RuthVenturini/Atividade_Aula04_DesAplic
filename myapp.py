# -*- coding: utf-8 -*-
"""myapp.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19RHdeMEP0m-URlP9u9dUt0FitL6zrbx3

Disciplina: Desenvolvimento de Aplicações Geoespaciais

Aluna: Ruth Venturini Mariani
"""

!pip install streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
#     import streamlit as st
#     st.title("A minha primeira aplicação Streamlit")
#     st.write("Olá, mundo!")
#

!npm install localtunnel

!streamlit run app.py &>/content/logs.txt &

!npx localtunnel --port 8501 & curl ipv4.icanhazip.com

st.set_page_config(page_title="Aula 04 - Desenvolvimento de aplicações geoespaciais")
st.write("Exercício de aula")
!streamlit run /usr/local/lib/python3.11/dist-packages/colab_kernel_launcher.py

"""1 - Ao se digitar dois endereços, calcular a distância geodésica entre eles e plotar no mapa."""

from geopy.geocoders import Nominatim
import folium

geolocator = Nominatim(user_agent='ruthventurini.academico@gmail.com')
endereco1 = input ("Entre com o primeiro endereço: ")
endereco2 = input ("Entre com o segundo endereço: ")
localizacao1 = geolocator.geocode(endereco1)
localizacao2 = geolocator.geocode(endereco2)

coordinates = [
    [localizacao1.latitude, localizacao1.longitude],
    [localizacao2.latitude, localizacao2.longitude]
]

from geographiclib.geodesic import Geodesic
import math
geod = Geodesic.WGS84
g = geod.Inverse(localizacao1.latitude, localizacao1.longitude, localizacao2.latitude, localizacao2.longitude)

print("A distância é {:.3f} m.".format(g['s12']))

mapa = folium.Map(location=[(localizacao1.latitude + localizacao2.latitude) / 2, (localizacao1.longitude + localizacao2.longitude) / 2], zoom_start=8)

folium.Marker([localizacao1.latitude, localizacao1.longitude], popup=endereco1, icon=folium.Icon(color='green', icon='star')).add_to(mapa)
folium.Marker([localizacao2.latitude, localizacao2.longitude], popup=endereco2, icon=folium.Icon(color='blue', icon='star')).add_to(mapa)
folium.PolyLine(
    locations=coordinates,
    color='red',
    weight=5,
    tooltip="Distância Geodésica",
).add_to(mapa)

mapa
