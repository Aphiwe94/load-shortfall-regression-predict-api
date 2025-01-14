"""

    Simple Script to test the API once deployed

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located at the root of this repo for guidance on how to use this
    script correctly.
    ----------------------------------------------------------------------

    Description: This file contains code used to formulate a POST request
    which can be used to develop/debug the Model API once it has been
    deployed.

"""

# Import dependencies
import requests
import pandas as pd
import numpy as np
from xgboost import XGBRegressor
import xgboost

# Load data from file to send as an API POST request.
# We prepare a DataFrame with the public test set + riders data
# from the Kaggle challenge.
test = pd.read_csv(r"..\df_test.csv")

print(test)
# Convert our DataFrame to a JSON string.
# This step is necessary in order to transmit our data via HTTP/S
feature_vector_json = test.iloc[1].to_json()
print(feature_vector_json)
# print(feature_vector_json.columns)
# Specify the URL at which the API will be hosted.
# NOTE: When testing your instance of the API on a remote machine
# replace the URL below with its public IP:

# url = 'http://http://192.168.0.110:5000/api_v0.1'
url = 'http://54.155.105.0:5000/api_v0.1'
#url = 'http://127.0.0.1:5000/api_v0.1'


# Perform the POST request.
print(f"Sending POST request to web server API at: {url}")
print("")
print(f"Querying API with the following data: \n {test.iloc[1].to_list()}")
print("")
# Here `api_response` represents the response we get from our API
api_response = requests.post(url, json=feature_vector_json)

# Display the prediction result
print("Received POST response:")
print("*"*50)
print(f"API prediction result: {api_response.json()}")
print(f"The response took: {api_response.elapsed.total_seconds()} seconds")
print("*"*50)
