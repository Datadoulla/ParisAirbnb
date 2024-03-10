import pickle
import statsmodels.api as sm
import pandas as pd
import numpy as np



def model_predict(data, model_pkl='models/model_simple_2023.pkl'):

    with open(model_pkl, 'rb') as file:
        loaded_model = pickle.load(file)

    srt_conf = loaded_model.get_prediction(data).conf_int(alpha=0.05)
    srt_pre = loaded_model.predict(data)

 
    srt = {
    'predict': round(np.exp(srt_pre).iloc[0]*0.9372,2),
    'born_inf': round(np.exp(srt_conf)[0][0]*0.9372,2),
    'born_sup': round(np.exp(srt_conf)[0][1]*0.9372,2)
    }


    return srt


#if __name__ == '__main__':
 #   model_predict()