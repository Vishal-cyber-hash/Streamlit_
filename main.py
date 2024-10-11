import streamlit as st
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://Learnpy:Akku@learn.jv0fm.mongodb.net/youtube")
db = client['youtube']  # Database name
users_collection = db['users']  # Collection for user data

# Function to create a new account
def create_account(username, password):
    # Check if the user already exists
    if users_collection.find_one({"username": username}):
        return "Username already exists. Please choose a different username."
    else:
        # Insert the new user into the database
        users_collection.insert_one({"username": username, "password": password})
        return "Account created successfully!"


# Header with navigation options
st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to", ['Home', 'About', 'Contact', 'Login', 'Logout', 'Create New Account'])

# Home Page
if option == 'Home':
    st.title("Welcome to the Home Page")
    st.image(
        "https://cdn.pixabay.com/photo/2024/03/07/02/58/ai-generated-8617472_1280.jpg",
        caption='Photo Displayed Here',
        use_column_width=True
    )
    st.write("This is the home page. You can add more content or data visualizations here.")

# About Page
elif option == 'About':
    st.title("About Us")
    st.write("This is the about page. Provide information about your app or team here.")

# Contact Page
elif option == 'Contact':
    st.title("Contact Us")
    st.write("This is the contact page. You can include a form for users to reach out.")

# Login Page
elif option == 'Login':
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        # Check if the user exists in the database
        user = users_collection.find_one({"username": username, "password": password})
        if user:
            st.success(f"Welcome back, {username}!")
        else:
            st.error("Invalid username or password. Please try again.")

# Create New Account Page
elif option == 'Create New Account':
    st.title("Create New Account")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type='password')
    if st.button("Create Account"):
        message = create_account(new_username, new_password)
        if "successfully" in message:
            st.success(message)
        else:
            st.error(message)

# Logout Page
elif option == 'Logout':
    st.title("Logout")
    st.write("You have been logged out.")

# Footer
st.markdown("""
    <hr style="border: 1px solid gray;">
    <div class="footer">Created by Vishal</div>
""", unsafe_allow_html=True)
