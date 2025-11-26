import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth

st.set_page_config(page_title="Secure Name Search", layout="centered")

usernames = ["user1", "user2", "user3", "user4"]
names = ["User One", "User Two", "User Three", "User Four"]
import streamlit_authenticator as stauth

passwords = ["test123"] * 4  # or any list of passwords

hasher = stauth.Hasher()  # No arguments

import streamlit_authenticator as stauth

passwords = ["test123"]*4

import streamlit_authenticator as stauth

passwords = ["test123"] * 4

import streamlit_authenticator as stauth

passwords = ["test123"] * 4

import streamlit_authenticator as stauth

passwords = ["test123"]*4

import streamlit_authenticator as stauth

passwords = ["test123"]*4

credentials = {
    "usernames": {
        "user1": {"name": "User One", "password": "test123"},
        "user2": {"name": "User Two", "password": "test123"},
        "user3": {"name": "User Three", "password": "test123"},
        "user4": {"name": "User Four", "password": "test123"}
    }
}

authenticator = stauth.Authenticate(
    names,
    usernames,
   passwords = ["test123"]*4
hashed_passwords = stauth.Hasher(passwords).generate()
authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    "some_cookie_name",
    "some_signature_key",
    cookie_expiry_days=30
)
    "some_cookie_name",
    "some_signature_key",
    cookie_expiry_days=30
)

authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    "demo_cookie",
    "demo_key",
    cookie_expiry_days=1
)

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
