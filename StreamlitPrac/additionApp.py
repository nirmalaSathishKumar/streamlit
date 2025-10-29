import streamlit as st 
import time
st.title("Addition APP")
st.header("Add Two numbers")
n1 = st.number_input("Enter a number n1 : ",1,100)
n2 = st.number_input("Enter a number n2 : ",1,100)

if st.button("Add"):
    c = n1 + n2
    st.success(f"Addition of {n1} and {n2} is {c}")
