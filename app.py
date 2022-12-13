import streamlit as st
st.set_page_config('wide')
project_list = [
    'About me',
    'Software Developer Salary Prediction',
    'Random Badminton Player Selector',
    'Palmers Penguin Predictor',
    'Image Classification using Transfer Learning'
]

option = st.sidebar.selectbox(options = project_list,label = 'Select an interesting project')


from PIL import Image
image = Image.open('me.jpeg')
st.title('My growing Portfolio of small machine learning projects')

col1, col2 = st.columns([10,2])
with col2:
    st.image(image, width = 200)
    st.caption('Zoheb Khan')

with col1:
    st.markdown("Hi there, welcome to my portfolio")
    st.markdown("Im a computational research scientist working as Post-Doctoral Research Fellow at the University College Dublin")
    st.markdown("I use computational fluid dynamics and artificial intelligence to simulate and study flow fields in membrane separators")
    st.markdown("I love spending time outdoors and when not in the lab, I cycle, run and play badminton")
    st.markdown("To get in touch or know more about professional work, connect with me on [LinkedIn](https://www.linkedin.com/in/zobekenobe/)")
