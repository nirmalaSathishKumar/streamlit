import streamlit as st 

st.html('<h1 style="text-align: center;">EVEN or ODD</h1>')

col1, col2, col3 = st.columns(3,vertical_alignment='center')
with col1:
    icon=":material/emoji_people:"
    with st.popover(icon):
        st.write("Hi there !!! Welcome to MATH")

with col2:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUXmId6rC8EyQRjqeXU7h6y3IcHiDOzRor9A&s")

with col3:
            st.caption("Even numbers are divisible by 2 with no remainder, while odd numbers are not divisible by 2 and will always have a remainder of 1 \n :sparkler:")

col4, col5 = st.columns(2,vertical_alignment='center')

with col4:
    n1 = eval(st.text_area("Enter a number n: ",1,placeholder="Number"))
with col5:
    if st.button('Check Even Or Odd'):
        if n1 %2 == 0:
            st.success(f"{n1} is Even !!", icon="✅")
            st.badge("Success", icon=":material/check:", color="green")
            st.balloons()
            st.audio( data="fireworks.mp3", format="audio/mp3", loop=False,autoplay=True)
        else:
            st.success(f"{n1} is Odd !!",icon="✅")
            st.badge("Success", icon=":material/check:", color="green")
            st.balloons()
            st.audio( data="fireworks.mp3", format="audio/mp3", loop=False,autoplay=True)
