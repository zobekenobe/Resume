import streamlit as st
import pandas as pd

def show_project1():

        st.title('Salary Prediction Estimator')     
        st.write('The StackOverflow dataset for the year 2020 was used for building this web app. You can find the newer datasets out here https://insights.stackoverflow.com/survey/2020. The user can enter the years of experience through a slider bar and the Country, Ehtnicity and Education Qualification to predict the salary.')
        st.write('Data preparation constituted of feature selection, data scaling, imputing and encoding etc. A supervised machine learning framework was built and the RandomForest regressor was chosen to the predict the final salary.')
        st.write('Libraries used')
        lib = pd.DataFrame({
            'Mathematical and data processing Libraries' : ['scikit-learn', 'pandas', 'statsmodels', 'numpy'],
            'Visualization Libraries' : ['seaborn', 'matplotlib', 'plotly', ''],
            'deployment / dashboarding ' : ['Streamlit','','','']
            })
        st.table(lib)
        st.info('Check out the app [here](https://zobekenobe-stackoverflow-salarypredictionmodel-app-ynmrdl.streamlitapp.com/) ')
        st.image('Salary.jpg')
        st.caption('Screenshot of the front page')
