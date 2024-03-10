import pickle
import statsmodels.api as sm
import pandas as pd
import numpy as np



def model_predict(data, model_pkl='models/model_simple_2023.pkl'):

# Define the file paths for the model and the dataset


    # Load the model from the pickle file
    with open(model_pkl, 'rb') as file:
        loaded_model = pickle.load(file)

    # Read the dataset from the CSV file
    # Ensure the correct path to the CSV file and encoding method are specified
    # dt = pd.read_csv(dt_file, sep=";", encoding='latin-1')

    # Perform prediction and calculate confidence intervals
    srt_conf = loaded_model.get_prediction(data).conf_int(alpha=0.05)
    srt_pre = loaded_model.predict(data)

    # Prepare the results dictionary
    # Ensure necessary libraries like numpy (np) are imported
    srt = {
    'predict': round(np.exp(srt_pre).iloc[0]*0.9372,2),
    'born_inf': round(np.exp(srt_conf)[0][0]*0.9372,2),
    'born_sup': round(np.exp(srt_conf)[0][1]*0.9372,2)
    }

    # Print the results
    #print(srt)
    return srt


#if __name__ == '__main__':
 #   model_predict()