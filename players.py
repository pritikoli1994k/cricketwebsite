import streamlit as st
import pandas as pd

st.title("🏏 Players Information")

data = pd.read_csv("data/players.csv")
st.dataframe(data)

player_name = st.selectbox("Select a Player:", data['Name'])
player_info = data[data['Name'] == player_name]
st.write("### Player Details:")
st.write(player_info)
