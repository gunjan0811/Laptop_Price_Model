# 💻 Laptop Price Predictor

A web application built with Streamlit that predicts the price of a laptop based on its specifications such as brand, RAM, storage, display, CPU, GPU, etc.

# Demo

👉 Live App on Streamlit Cloud- https://laptoppricemodel-8i5pkoirbnx4jugutgz639.streamlit.app/

# Project Structure

├── app.py                # Streamlit web app
├── pipe.pkl              # Trained machine learning pipeline
├── df.pkl                # Dataframe with unique feature values (for dropdowns)
├── laptop_prices.csv     # Dataset used for training
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation


# Features

1-Interactive web app using Streamlit.

2-Takes laptop specifications as input:

3-Brand (Company)

4-Type (Ultrabook, Gaming, etc.)

5-RAM size

6-Operating System

7-Screen resolution & size

8-Touchscreen, IPS, Retina display options

9-CPU & GPU brand

10-Primary & Secondary storage (size & type)

11-Predicts laptop price in Euros (€).

12-Simple and beginner-friendly deployment on Streamlit Cloud.

# Installation

git clone https://github.com/your-username/laptop-price-predictor.git
cd laptop-price-predictor
pip install -r requirements.txt

# Usage

## Run the Streamlit app locally:

streamlit run app.py

# Deployment

This project is deployed on Streamlit Cloud.

Steps to deploy:

Push code + model files to GitHub.

Go to Streamlit Cloud.

Select your repo and deploy.

Get a shareable public link.

# License

This project is licensed under the MIT License.
