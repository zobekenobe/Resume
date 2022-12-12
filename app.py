import streamlit as st

project_list = [
    '',
    'Software Developer Salary Prediction',
    'Random Badminton Player Selector',
    'Palmers Penguin Predictor',
    'Image Classification using Transfer Learning'
]

option = st.sidebar.selectbox(options = project_list,label = 'Select an interesting project')


from PIL import Image
image = Image.open('me.jpeg')


st.image(image, width = 300 )
st.header('Zoheb Khan')
st.markdown("Hi, Im a computational research scientist working as Post-Doctoral research Fellow at the University College Dublin in the School of Chemical and Bioprocess Engineering")
st.markdown("I use computational fluid dynamics and artificial intelligence to simulate and study flow fields in membrane separators")
st.markdown("I love spending time outdoors and when not in the lab, I cycle, run and play badminton")
st.markdown("To get in touch or know more about professional work, connect with me on LinkedIn @ https://www.linkedin.com/in/zobekenobe/")