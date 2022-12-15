import streamlit as st
from PIL import Image
from project1 import show_project1
from project2 import show_project2
# from project3 import show_project3
# from project4 import show_project4

st.set_page_config('Zohebs Machine learning portfolio', layout = 'wide')
project_list = [
    'Welcome',
    'Software Developer Salary Prediction',
    'Random Badminton Player Selector',
    'Palmers Penguin Predictor',
    'Image Classification using Transfer Learning'
]

option = st.sidebar.selectbox(options = project_list,label = 'Select an interesting project')


if option == project_list[0]:
    image = Image.open('me.jpeg')
    st.title('My growing Portfolio of small machine learning projects')

    col1, col2 = st.columns([4,2])
    with col2:
        st.image(image, width = 200)
        st.caption('Zoheb Khan')

    with col1:
        st.markdown("Hi there, welcome to my portfolio")
        st.markdown("Im a computational research scientist working as Post-Doctoral Research Fellow at the University College Dublin")
        st.markdown("I use computational fluid dynamics and artificial intelligence to simulate and study flow fields in membrane separators")
        st.markdown("I love spending time outdoors and when not in the lab, I cycle, run and play badminton")
        st.markdown("To get in touch or know more about professional work, connect with me on [LinkedIn](https://www.linkedin.com/in/zobekenobe/)")

elif option == project_list[1]:
    show_project1()
elif option == project_list[2]:
    show_project2()