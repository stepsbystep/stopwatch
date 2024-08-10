import streamlit as st


def create():
    st.write("Create Account Page")

def manage():
    st.write("Manage Account Page")

def learn():
    st.write("Learn about managing your account")

def trial():
    st.write("Try managing your account")


pages = {
    "Your account": [
        st.Page(create, title="Create your account"),
        st.Page(manage, title="Manage your account"),
    ],
    "Resources": [
        st.Page(learn, title="Learn about us"),
        st.Page(trial, title="Try it out"),
    ],
}

pg = st.navigation(pages)
pg.run()