import streamlit as st
from PIL import Image

def home():

    st.title('Auto DS :bulb:')

    # image = Image.open('pages/eadf881914364166b46d00ab90b4415f.png')

    # st.image(image)

    st.markdown('''

    ## **Homepage** for the app to automate Data Science tasks :rocket:

    This app will support automated exploratory data analysis (EDA) and Auto ML for any dataset.

    Currently supported feature: **EDA**. Try it out!

    ## Usage :high_brightness:

    Your data needs to be in a certain format for the exploratory data analysis and autoML features to work correctly. The minimum requirement for the EDA is that your data file is a CSV.
    
    ***EDA*** :space_invader:

    For the exploratory data analysis, upload the CSV(s) to get the results!

 
    Built with :heart: by [Mashrin Srivastava](https://github.com/mashrin/) for the fellow data scientist and the data science community.
    ''')


   # ***AutoML*** :memo:

    # Datasets in CSV format with numerical values are perfect, just make sure to have the target value in the last column. Based on the model you choose
    # you will be able to change hyperparameters which will change the performance of the model. Testing different model hyperparameters can change the performance of the model greatly.

    # ***LazyCompare*** :chart_with_downwards_trend:

    # Similar to AutoML datasets will need to be in CSV format with numerical values with the target value in the last column. 20+ Machine learning models will be tested on the data given
    # and the user will be able to see the results.
