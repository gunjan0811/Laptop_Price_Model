import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load saved model + dataframe
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("💻 Laptop Price Predictor")

# Input widgets
company = st.selectbox('Company', df['Company'].unique())
type_name = st.selectbox('Type', df['TypeName'].unique())
ram = st.selectbox('RAM (GB)', sorted(df['Ram'].unique()))
os = st.selectbox('Operating System', df['OS'].unique())

screen = st.selectbox('Screen',df['Screen'].unique())
touchscreen = st.selectbox('Touchscreen', ['Yes', 'No'])
ips = st.selectbox('IPS Panel', ['Yes', 'No'])
retina = st.selectbox('Retina Display', ['Yes', 'No'])

cpu_company = st.selectbox('CPU Company', df['CPU_company'].unique())
gpu_company = st.selectbox('GPU Company', df['GPU_company'].unique())

primary_storage = st.selectbox('Primary Storage (GB)', sorted(df['PrimaryStorage'].unique()))
secondary_storage = st.selectbox('Secondary Storage (GB)', sorted(df['SecondaryStorage'].unique()))
primary_storage_type = st.selectbox('Primary Storage Type', df['PrimaryStorageType'].unique())
secondary_storage_type = st.selectbox('Secondary Storage Type', df['SecondaryStorageType'].unique())

if st.button('💰 Predict Price'):
   


    # Ensure numeric features are integers
    ram = int(ram)
    primary_storage = int(primary_storage)
    secondary_storage = int(secondary_storage)

    # Arrange inputs in same order as training data
    input_dict = {
        'Company': [company],
        'TypeName': [type_name],
        'Ram': [ram],
        'OS': [os],
        'Screen': [screen],
        'Touchscreen': [touchscreen],
        'IPSpanel': [ips],
        'RetinaDisplay': [retina],
        'CPU_company': [cpu_company],
        'PrimaryStorage': [primary_storage],
        'SecondaryStorage': [secondary_storage],
        'PrimaryStorageType': [primary_storage_type],
        'SecondaryStorageType': [secondary_storage_type],
        'GPU_company': [gpu_company]
    }

    query = pd.DataFrame(input_dict)

    # Predict
    prediction = pipe.predict(query)[0]

    st.success(f"Estimated Laptop Price: €{int(np.exp(prediction))}")
