import streamlit as st
import pandas as pd

# ------------------ Page Setup ------------------
st.set_page_config(page_title="Cricket Info Website", page_icon="🏏", layout="wide")

# ------------------ Sidebar Menu ------------------
st.sidebar.title("🏏 Cricket Info Portal")
menu = st.sidebar.radio(
    "Navigate to:",
    ["Home", "Players", "Matches", "Events", "About"]
)

# ------------------ Home Section ------------------
if menu == "Home":
    st.title("🏠 Welcome to the Cricket Info Portal")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/42/Cricket_balls_in_a_row.jpg", use_column_width=True)
    st.markdown("""
    ### 📌 About
    This website provides information about:
    - 🏏 **Players**: Stats and performance of top cricketers  
    - 🏆 **Matches**: Results and scores of matches  
    - 🎉 **Events**: Details of upcoming cricket tournaments  
    """)
    st.success("Use the sidebar to explore different sections!")

# ------------------ Players Section ------------------
elif menu == "Players":
    st.title("🏏 Player Information")

    try:
        data = pd.read_csv("data/players.csv")
        st.dataframe(data)

        player_name = st.selectbox("Select a Player:", data['Name'])
        player_info = data[data['Name'] == player_name]
        st.write("### Player Details:")
        st.write(player_info)
    except Exception as e:
        st.error(f"Error loading players data: {e}")

# ------------------ Matches Section ------------------
elif menu == "Matches":
    st.title("🏆 Match Results")

    try:
        data = pd.read_csv("data/matches.csv")
        st.dataframe(data)

        winner = st.selectbox("Filter by Winner:", data['Winner'].unique())
        filtered = data[data['Winner'] == winner]
        st.write(f"### Matches Won by {winner}")
        st.dataframe(filtered)
    except Exception as e:
        st.error(f"Error loading matches data: {e}")

# ------------------ Events Section ------------------
elif menu == "Events":
    st.title("🎉 Upcoming Cricket Events")

    try:
        data = pd.read_csv("data/events.csv")
        st.dataframe(data)
    except Exception as e:
        st.error(f"Error loading events data: {e}")

# ------------------ About Section ------------------
elif menu == "About":
    st.title("ℹ️ About This Website")
    st.write("""
    This is a simple cricket information portal built using **Python** and **Streamlit**.
    It displays data from CSV files — including details of players, match results, and upcoming tournaments.
    
    **Developer:** Priti Koli 💻  
    **Technology Used:** Streamlit, Pandas
    """)
