import numpy as np
import pandas as pd
import streamlit as st
# from pandas_profiling import ProfileReport
from pandas_profiling import ProfileReport
# import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from sklearn.datasets import load_diabetes, load_boston
import requests
import json


def eda():

    st.markdown('''
    ***AutoDS***
    This is the **exploratory data analysis** section of the AutoDS App
    ''')

    with st.sidebar.header('Upload the input CSV'):
        
        uploaded_file = st.sidebar.file_uploader(
            "Upload the input CSV file", type=["csv"])
        st.sidebar.markdown("""
    [Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
    """)


    if uploaded_file is not None:

        @st.cache
        def load_csv():

            csv = pd.read_csv(uploaded_file)

            return csv

        df = load_csv()
        pr = ProfileReport(df, explorative=True)
        st.header('**Uploaded DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Exploratory Data Analysis Report**')
        st_profile_report(pr)

    else:
        st.info('Awaiting for CSV file to be uploaded.')
        if st.button('Press to use data from StepZen GraphQL API Endpoint Dataset'):
            # Example data
            @st.cache
            def load_data():

                url = "https://publicffa4e870ac4ce0e8.stepzen.net/api/root/__graphql"

                payload="{\"query\":\"query rootQuery($access_control_request_headers: String!, $api_key: String!, $collection: String, $dataSource: String, $database: String){\\n    rootQuery(access_control_request_headers: $access_control_request_headers, api_key: $api_key, collection: $collection, dataSource: $dataSource, database: $database){\\n        documents{\\n            _id\\n            age\\n            education\\n            fnlwgt\\n            income\\n            occupation\\n            race\\n            relationship\\n            sex\\n            workclass\\n        }\\n    }\\n}\",\"variables\":{\"dataSource\": \"Cluster0\",\"database\": \"stepzen_hackathon\",\"collection\": \"stepzen_hackathon\",\"access_control_request_headers\": \"*\",\"api_key\": \"wUOByXq1EgMcUJIyrffarLgsO26Y5XNCOVTM6VeKiu8Rx8slc9S6k7soCdC1Lu1b\"}}"
                headers = {
                'Content-Type': 'application/json'
                }

                response = requests.request("POST", url, headers=headers, data=payload)

                out = response.json()
                df = pd.json_normalize(out["data"]["rootQuery"]["documents"])
                df = df.drop(columns=['_id'])
                df = df.replace('?', np.NaN)
                return df

            df = load_data()
            pr = ProfileReport(df, explorative=True)
            st.header('**Example DataFrame**')
            st.write(df)
            st.write('---')
            st.header('**Exploratory Data Analysis Report**')
            st_profile_report(pr)
