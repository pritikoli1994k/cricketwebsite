import streamlit as st
import pandas as pd

st.title("🏆 Match Results")

data = pd.read_csv("data/matches.csv")
st.dataframe(data)

winner = st.selectbox("Filter by Winner:", data['Winner'].unique())
filtered = data[data['Winner'] == winner]
st.write("### Matches Won by", winner)
st.dataframe(filtered)
