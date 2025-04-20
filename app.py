import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Données d'exemple pour entraîner le modèle
X = np.array([
    [2, 400, 22, 80, 6.5],
    [0, 500, 20, 90, 6.2],
    [1, 300, 25, 70, 6.8]
])
y = np.array([4.2, 4.0, 3.2])

model = LinearRegression()
model.fit(X, y)

st.title("🌾 Assistant IA - Prédiction du rendement du blé")

sol = st.selectbox("Type de sol", ["Limoneux", "Argileux", "Sableux"])
pluie = st.slider("Pluie (mm)", 200, 600, 400)
temp = st.slider("Température (°C)", 10, 40, 22)
engrais = st.slider("Engrais (kg/ha)", 0, 150, 80)
ph = st.slider("pH du sol", 5.0, 8.0, 6.5)

sol_mapping = {"Argileux": 0, "Sableux": 1, "Limoneux": 2}
sol_code = sol_mapping[sol]

if st.button("Prédire le rendement"):
    donnees = np.array([[sol_code, pluie, temp, engrais, ph]])
    pred = model.predict(donnees)
    st.success(f"🌾 Rendement estimé : {pred[0]:.2f} tonnes/ha")