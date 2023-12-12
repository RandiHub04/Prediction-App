### Load libraries
import streamlit as st
from PIL import Image

#display the C title
st.title("Mudra Design")

##set team image
image = Image.open('Team logo/images.jpeg')


#set the desire size
new_size = (400, 400)

#Rezise the image
resized_image= image.resize(new_size)

##set the image 
st.image (resized_image)


##info about the team
st.write("Mudra Design adalah Starup yang berfokus pada pelayanan Desain grafis,editing video")




#Button to send an email
if st.button("Contact We via Email"):
    st.markdown('<a href= "randiatulaufa@gmail.com">Send Email</a>', unsafe_allow_html=True)


#Button to visit LinkedIn profile
if st.button("Visit My LinkedIn Profile"):
    st.markdown('<a href= "">https://www.linkedin.com/in/randi-atul-aufa-20455a229</a>', unsafe_allow_html=True)

#Button to github
if st.button("Check out my github repositories"):
    st.markdown('<a href= "">https://github.com/RandiHub04?tab=repositories</a>', unsafe_allow_html=True)

