import streamlit as st


st.set_page_config(page_title="My First Website", page_icon="🌐", layout="centered")
st.title("Welcome to my first Python Website!")

st.markdown(
    """
    <style>
           .stApp{
                background-color: rgb(122, 218, 199);
                color: rgb(66, 33, 32);
                font-family: 'Arial', sans-serif;
           }
              .stButton>button{
                 background-color: rgb(66, 33, 32);
                 color: white;
                 font-size: 16px;
                 padding: 10px 20px;
                 border-radius: 5px;
                 border: none;
                 cursor: pointer;
              }

    </style>

    """,
    unsafe_allow_html=True
)


st.sidebar.title("Navigation")
st.sidebar.write("Select a page to navigate:")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

if page == "Home":
    st.header("Home page!")
    st.write("This is a simple home page built with python and streamlit.")
    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Hello {name}! Thanks for visiting")

elif page == "About":
    st.header("About page!")
    st.write("This website is built entirely using python and streamlit uner 15 minutes!.")


elif page == "Contact":
    st.header("Contact Us")
    email = st.text_input("Enter your email")
    message = st.text_input("Enter your message.")
    if st.button("Submit"):
        st.success("Thank you we have received your message!")
