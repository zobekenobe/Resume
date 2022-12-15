import streamlit as st
import pandas as pd

def show_project4():

        st.title('Image Classification')     
        st.write('This app uses the imagenet dataset; which contains 1000 classes to classify random objects. The user uploads a .jpeg image, selects a classifier (vgg16, vgg19, resnet50, mobilenetv2, inceptionv3) from the drop down menu. The image is classified and the app draws a bounding box around the image with its classification probability.')
        st.write('Libraries used')
        lib = pd.DataFrame({
            'Mathematical and data processing Libraries' : ['tensorflow-keras', 'pandas', 'opencv', 'numpy'],
            'Visualization Libraries' : ['seaborn', 'matplotlib', 'plotly', ''],
            'deployment / dashboarding ' : ['Streamlit','','','']
            }, index = None)
        st.table(lib)
        st.info('Check out the app [here](https://zobekenobe-imageclassifier-app-rl972f.streamlit.app/)')
        st.image('image_classifier.jpg')
        st.caption('Screenshot of the front page')