# Libraries
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
from streamlit_card import card
from datetime import date
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title='About Us',
                   page_icon=':people_hugging:', layout='wide', initial_sidebar_state='collapsed')
st.markdown("<h1 style='text-align: center; color: black;font-size:50px'>NASSCOM CAPGEMINI HACKATHON</h1><hr>",
            unsafe_allow_html=True)

st.header("START UP PLAN")
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("OUR APPLICATION'S MAJOR FEATURES")
st.write("""
    1. Dynamic Forecasting of AQI and Temperature Data using live data.
    2. Using a scheduler based approach of training the models based on the live data.
    3. Live Dashboard for each Tier 2 city in Telangana with various filters.
    4. Real Time Capturing of Data using Web Scraping Strategy.
    5. Displaying our EDA and various statistical analysis and visuals showing the effectiveness and scalabilty of our predictions
""")
st.subheader("OUR NEXT APPROACHES TOWARDS SETTING UP OUR START UP")
st.write("""
    1. Our major objective of building up our startup application is towards building a an application towards our environment
    2. So on our first approach we have a plan to capture user emails and details of people visiting our page and sending them daily alerts on the AQI and heatwave levels
    3. We have also planned to send our forecasted values as an idea about the future days so that people can take precautionary messages accordingly.
    4. We have also planned to create a complete dashboard by generating a lot of KPI measures and make people aware about the statistics of their places.
    5. Maintain a good quality of the data and provide paid reliable data source endpoints to fetch the reliable data maintained. 
""")
st.markdown("<hr>", unsafe_allow_html=True)
st.header("ARCHITECTURE DIAGRAM")
arch = Image.open('./images/architecture.png')
arch.resize((300, 400))
st.image(arch, caption="Architecture Diagram")
st.header("ABOUT US - TEAM PSG DS 2K19")
st.markdown("<hr>", unsafe_allow_html=True)
user1_col1, padding, user1_col2 = st.columns((6, 1, 15), gap="small")
with user1_col1:
    ashish = Image.open('./images/Ashish.jpg')
    ashish = ashish.resize((400, 500))
    st.image(ashish, caption="Team Member 1 - Ashish")
with user1_col2:
    st.header("Ashish K")
    st.write("""Hello This is Ashish K, from PSG College of Technology currently pursuing my 4th year MSc Data Science course at PSG College of Technology.\n
    AREAS OF INTEREST : MACHINE LEARNING\n
    WORK EXPERIENCE   : Summer Intern At Goldman Sachs\n
    GITHUB PROFILE    : https://github.com/Ashishkumaraswamy\n
    LINKEDIN URL      : https://www.linkedin.com/in/ashish-kumaraswamy/\n
    ROLE IN HACKATHON : Developed the scheduler scripts running in AWS\n
                        so as to get dynamic predictions taking into account\n
                        of the current values. Developed the hourly, daily and\n
                        monthly schedulers for this work and storing the results\n 
                        in AWS S3 bucket.   
    """)
st.markdown("<hr>", unsafe_allow_html=True)
user2_col1, padding, user2_col2 = st.columns((15, 1, 6), gap="small")
with user2_col2:
    jega = Image.open('./images/mathan.jpg')
    jega = jega.resize((400, 500))
    st.image(jega, caption="Team Member 2 - Mathana Mathav")
with user2_col1:
    st.header("Mathana Mathav")
    st.write("""Hello This is Mathana Mathav, from PSG College of Technology currently pursuing my 4th year MSc Data Science course at PSG College of Technology.\n
    AREAS OF INTEREST : FULL STACK DATA SCIENTISTS\n
    WORK EXPERIENCE   : SDE Summer Intern At Zerodown\n
    GITHUB PROFILE    : https://github.com/mathanamathav\n
    LINKEDIN URL      : https://www.linkedin.com/in/mathana-mathav-a-s-615b65205/\n
    ROLE IN HACKATHON : Worked on data pipelines , making data source ready for \n
                        machine learning engineer building streamlit application \n
                        , backend flask-REST API application and \n 
                        deployed the backend application to Azure. 
    """)
st.markdown("<hr>", unsafe_allow_html=True)
user3_col1, padding, user3_col2 = st.columns((6, 1, 15), gap="small")
with user3_col1:
    jega = Image.open('./images/jega.png')
    jega = jega.resize((400, 500))
    st.image(jega, caption="Team Member 3 - Jegadeesh M S")
with user3_col2:
    st.header("Jegadeesh M S")
    st.write("""Hello This is Jegadeesh M S, from PSG College of Technology currently pursuing my 4th year MSc Data Science course at PSG College of Technology.\n
    AREAS OF INTEREST : MACHINE LEARNING\n
    WORK EXPERIENCE   : Data Analyst Summer Intern At Buckman\n
    GITHUB PROFILE    : https://github.com/jegadeesh2001\n
    LINKEDIN URL      : https://www.linkedin.com/in/jegadeesh-manickam-9b112597/\n
    ROLE IN HACKATHON : Worked on Timeseries forecasting of AQI and\n
                        Heatwave occurence for different cities along with the\n
                        corresponding model evaluation. The results were then\n
                        deployed to our streamlit application. 
    """)
