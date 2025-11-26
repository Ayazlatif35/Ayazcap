import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth

st.set_page_config(page_title="Secure Name Search", layout="centered")



name, auth_status, username = authenticator.login("Login", "main")

if auth_status is False:
    st.error("Incorrect username or password")
elif auth_status is None:
    st.warning("Please enter your username and password")

if auth_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.write(f"Logged in as: {name}")

    st.title("🔍 Secure Name Search App")

    df = pd.read_excel("sample_data.xlsx")

    search_name = st.text_input("Enter name to search:")

    if st.button("Search"):
        results = df[df["A"].astype(str).str.contains(search_name, case=False, na=False)]
        if results.empty:
            st.error("No matching records found.")
        else:
            st.success("Record found:")
            st.write(results[["A", "B", "C"]])
