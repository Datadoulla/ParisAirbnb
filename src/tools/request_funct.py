import pandas as pd
import numpy as np


def continuous_var(bathrooms, accommodates, bedrooms):

    return {
            'const':1,
            'accommodates':accommodates,
            'bedrooms':bedrooms,
            'bathrooms':bathrooms,
            'accommodates_squared':accommodates**2,
            'bedrooms_squared':bedrooms**2,
            'bathrooms_squared':bathrooms**2,
            }
    

def neighbour_dummies(neighbour):
    neighbourhood_list = ['Batignolles-Monceau', 'Buttes-Chaumont', 'Buttes-Montmartre', 'Entrepôt','Gobelins', 'Ménilmontant', 
                        'Observatoire', 'Opéra', 'Panthéon', 'Passy', 'Popincourt', 'Reuilly', 'Vaugirard']


    neighbourhood_dict = {}

    for i in neighbourhood_list:
        if i == neighbour:
            key = 'neighbourhood_cleansed_'+i
            value = 1
        else:
            key = 'neighbourhood_cleansed_'+i
            value = 0
        
        neighbourhood_dict[key] = value
        
    return neighbourhood_dict


def property_dummies(property):
    
    property_list = ['Entire rental unit', 'Private room in hostel', 'Private room in rental unit', 'Room in boutique hotel', 'Room in hotel']


    property_dict = {}

    for i in property_list:
        if i == property:
            key = 'property_type_'+i
            value = 1
        else:
            key = 'property_type_'+i
            value = 0
        
        property_dict[key] = value
        
    return property_dict


def room_dummies(room):
    return {'room_type_Entire home/apt': 0 if room == 'Non' else 1}


def request_data(bathrooms, accommodates, bedrooms, neighbour, property, room):
    data_dict = continuous_var(bathrooms, accommodates, bedrooms)
    data_dict.update(neighbour_dummies(neighbour))
    data_dict.update(property_dummies(property))
    data_dict.update(room_dummies(room))

    data_df = pd.DataFrame.from_dict(data_dict, orient='index').T
    return data_df



#if __name__ == '__main__':
 #   request_data(bathrooms, accommodates, bedrooms, neighbour, property, room)