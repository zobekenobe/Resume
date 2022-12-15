import streamlit as st
import pandas as pd

def show_project2():

        st.title('Random Badminton Player Selector')     
        st.write('Currently there are two systems to schedule badminton games, the first either using the age old system of using pegs or then using a paid system')
        c1, c2 = st.columns(2)
        with c1:
            st.image('pegs.jpg', width = 300)
            st.caption('Scheduling badminton games using the peg system')
        with c2:
            st.image('commercial_badminton.jpg', width = 375)
            st.caption('Using paid commercial software')

        st.write('The task of randomly alloting players to the courts has been automated with a simple python script, that is efficient and also doesnt incur any expenses.')
        st.write('The user simply creates a list of participants on a Google Sheet, enters the number of courts available and also the time alloted to each play. The app generates a list of players randomly selected, ensuring everyone gets to play rotating players after the set time')

        st.write('Libraries used')
        lib = pd.DataFrame({
            'Mathematical and data processing Libraries' : ['pandas', 'numpy'],
            'deployment / dashboarding ' : ['Streamlit','Google Sheets']
            })
        st.table(lib)
        st.info('Check out the app [here](https://zobekenobe-random-player-badminton-app-pruvft.streamlit.app/) ')
        st.image('badminton.jpg')
        st.caption('Screenshot of the front page')