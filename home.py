import streamlit as st
import pandas as pd

# ------------------ Page Setup ------------------
st.set_page_config(page_title="Cricket Info Website", page_icon="🏏", layout="wide")

# ------------------ Sidebar Menu ------------------
st.sidebar.title("🏏 Cricket Info Portal")
menu = st.sidebar.radio(
    "Navigate to:",
    ["Home", "Players", "Matches", "Events", "Match Enrollment", "Contact", "About"]
)

# ------------------ Home Section ------------------
if menu == "Home":
    st.title("🏠 Welcome to the Cricket Info Portal")
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/4/42/Cricket_balls_in_a_row.jpg",
        use_container_width=True
    )
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

# ====================== MATCH ENROLLMENT FORM ======================
elif menu == "Match Enrollment":
    st.header("📝 Match Enrollment Form")
    st.write("Register your team for upcoming cricket tournaments!")

    with st.form("match_form"):
        team_name = st.text_input("Team Name")
        captain_name = st.text_input("Captain Name")
        players_count = st.number_input("Number of Players", min_value=1, max_value=15)
        contact_email = st.text_input("Contact Email")
        tournament = st.selectbox("Select Tournament", ["World Cup", "Asia Cup", "IPL", "T20 Series"])
        submit_btn = st.form_submit_button("Submit Enrollment")

        if submit_btn:
            if team_name and captain_name and contact_email:
                st.success(f"✅ {team_name} has been successfully enrolled for {tournament}!")
            else:
                st.error("⚠️ Please fill all required fields.")

# ====================== CONTACT PAGE ======================
elif menu == "Contact":
    st.header("📩 Contact Us")
    st.write("We’d love to hear from you! Fill out the form below:")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        send_btn = st.form_submit_button("Send")

        if send_btn:
            if name and email and message:
                st.success("✅ Thank you! Your message has been sent successfully.")
            else:
                st.error("⚠️ Please fill in all the fields.")

    st.markdown("---")
    st.markdown("📧 Email: support@cricketinfo.com")
    st.markdown("🌐 Website: [www.cricketinfo.com](http://www.cricketinfo.com)")

# ------------------ About Section ------------------
elif menu == "About":
    st.title("ℹ️ About This Website")
    st.write("""
    This is a simple cricket information portal built using **Python** and **Streamlit**.  
    It displays data from CSV files — including details of players, match results, and upcoming tournaments.
    
    **Developer:** Priti Koli 💻  
    **Technology Used:** Streamlit, Pandas  
    **Version:** 2.0
    """)
