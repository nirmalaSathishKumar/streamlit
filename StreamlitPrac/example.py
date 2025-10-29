import streamlit as st 
import time
st.title("Great way to get time zone")
st.write("My First App")
st.header("Enter time Zone")
t = st.time_input("Current Time:")

time.localtime()
time.timezone()
st.text("Enter Name:")
st.text_input("Enter Name here")
a = st.number_input("Enter number")
st.button("Click")
st.selectbox("what is your selection",["Add","Subtract"])
st.checkbox("Select please",["Add","Subract"])
st.radio("Selection you want",["Add","Subtract"])