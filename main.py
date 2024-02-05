import streamlit as st
from PIL import Image
import io

def set_background(image_path):
    page_bg_img ='''
    <style>
    body {
    background-image: url("'''+ image_path +'''");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AIzaSyBHbwExz2si0nSkHSRUDK8w8Han9N4hk6I")
def ai(txt):
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("from now your name is hakern and your a ethical hacker , your real name is mohan s and reply to this in short: "+txt)
    return response.text


st.title("SIMPLE AI MP")

command=st.chat_input("WATHA ENNA DA VENNUM?")

if "message" not in st.session_state:
    st.session_state.message=[]

for chat in st.session_state.message:
     with st.chat_message(chat["role"]):
        st.write(chat["message"])   

if command:
    with st.chat_message("user"):
        st.write(command)
        st.session_state.message.append({"role":"user","message":command})

    if "hello" in command:
        with st.chat_message("bot"):
            st.write("sollra badu enna vennum?")
            st.session_state.message.append({"role":"bot","message":"sollra badu enna vennum"})
    elif "who" in command:
        with st.chat_message("bot"):
            st.write("IM MP assistant")
            st.session_state.message.append({"role":"bot","message":"IM MP assistant"})
    else:
        with st.chat_message("bot"):
            data=ai(command)
            st.write(data)
            st.session_state.message.append({"role":"bot","message":data})



print(st.session_state.message)           




     
