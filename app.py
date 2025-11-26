import streamlit as st  
import pandas as pd  
import streamlit_authenticator as stauth  

# --- USER AUTHENTICATION SETUP ---  
usernames = ["user1", "user2", "user3", "user4"]  
names = ["User One", "User Two", "User Three", "User Four"]  
passwords = ["test123"] * 4  

hashed_passwords = stauth.Hasher(passwords).generate()  

authenticator = stauth.Authenticate(  
    names,  
    usernames,  
    hashed_passwords,  
    "my_cookie_name",  
    "my_signature_key",  
    cookie_expiry_days=30  
)  

name, authentication_status, username = authenticator.login("Login", "main")  

if authentication_status:  
    st.write(f"Welcome *{name}*")  
    # Your app code here, e.g.:  
    st.write("This is your protected Streamlit app.")  
elif authentication_status == False:  
    st.error("Username/password is incorrect")  
else:  
    st.warning("Please enter your username and password")  
