import streamlit as st
import pandas as pd

def show_project3():

        st.title('Palmers Penguin dataset prediction')     
        st.write('The Palmers Penguin dataset is used for building this web app to find the species of ')
        st.write('The user selects the Gender, Bill Length, Bill Depth, Flipper Length, Body Mass and the island and the app predicts the species of the penguin')
        st.write('Data preparation constituted of feature selection, data scaling, imputing and encoding etc. based on which a supervised machine learning classifier was built.')
        st.write('Libraries used')
        lib = pd.DataFrame({
            'Mathematical and data processing Libraries' : ['scikit-learn', 'pandas', 'statsmodels', 'numpy'],
            'Visualization Libraries' : ['seaborn', 'matplotlib', 'plotly', ''],
            'deployment / dashboarding ' : ['Streamlit','','','']
            })
        st.table(lib)
        st.info('Check out the app [here](https://zobekenobe-penguin-app-app-f10ya9.streamlit.app/) ')
        st.image('penguin.jpg')
        st.caption('Screenshot of the front page')