import streamlit as st
import pandas as pd

st.title("🎉 Upcoming Cricket Events")

data = pd.read_csv("data/events.csv")
st.dataframe(data)

st.map()  # Optional: to show map if locations are geocoded
