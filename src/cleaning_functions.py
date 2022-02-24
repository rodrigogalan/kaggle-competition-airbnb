import numpy as np
import pandas as pd
import re


def donwcast_df(x):
    '''Función para donwcastear todas las columnas de un dataframe y te devuelve el dataframe limpio'''
    for e in x.select_dtypes('object').columns:
        x[e]=x[e].astype('category')

    for e in x.select_dtypes('integer').columns:
        x[e]=pd.to_numeric(x[e], downcast='integer')

    for e in x.select_dtypes('float').columns:
        x[e]=pd.to_numeric(x[e], downcast='float')

    return x


def cleaning_host_response_time(x):
    '''Función para limpieza de la columna host_response_time'''
    if not x:
        return np.nan

    elif x =='a few days or more':
        return 1

    elif x =='within a day':
        return 2

    elif x == 'within a few hours':
        return 3

    elif x =='within an hour':
        return 4


def cleaning_host_response_rate(x):
    '''Función para limpieza de la columna host_response_rate'''
    if x!=x:
        return np.nan
       
    return int(x.rstrip("%"))


def cleaning_v_f(x):
    '''Función para limpieza de columnas con valores de verdadero (t) y falso (f)'''
    if x=="f": return 0
    else: return 1


def cleaning_bathrooms_text(x):
    '''Función para limpieza de columna bathrooms_text'''
    if x!=x: return np.nan
    elif x.split(" ")[0].replace('.','',1).isdigit():
        return float(x.split(" ")[0])
    else: return 0.5


def cleaning_amenities_n(x):
    '''Función para generar la columna de número de amenities'''
    if x!=x: return np.nan
    else: return len(x.lstrip("[").rstrip("]").replace('"',"").split(","))


def cleaning_property_type(x):
    if "shared" in x.lower():
        return 'shared'
    elif "hotel" in x.lower() or "hostel" in x.lower():
        return 'hotel'
    elif "room" in x.lower():
        return 'room'
    elif "entire" in x.lower() or "particular" in x.lower():
        return 'entire'
    else: return 'other'


def cleaning_amenities(x):
    '''Función para transformar la columna amenities en una lista'''
    return x.lstrip("[").rstrip("]").replace('"',"").split(", ")


def amenities_total(x):
    '''Función para hacer un get dummies de la columna amenities pero solo de aquellas amenities que tengan entre un 20% y un 80% de las propiedades para evitar añadir un
    número de columnas muy elevado y que tengan casi todos los valores iguales'''
    temp = pd.get_dummies(x['amenities'].explode()).groupby(level=0).sum() #Se genera un DF temporal con todas las columnas posibles del get dummies de amenties

    for e in list(temp.keys()): #Se añaden al DF original aquellas columnas que cumplen el requisito
        if temp[e].sum() <= x.shape[0]*0.8 and temp[e].sum() > x.shape[0]*0.2 and e != "Hangers":
            x=pd.concat([x, temp[e]], axis=1)
    
    x.drop(columns="amenities", inplace=True)

    return x


drop_columns=["id", "listing_url", "scrape_id", "last_scraped", "picture_url", "host_id", "host_url", "host_name", "host_about", "host_thumbnail_url", 
              "host_picture_url", "host_total_listings_count", "neighbourhood_group_cleansed", "bathrooms", "minimum_minimum_nights", "minimum_maximum_nights", 
              "minimum_nights_avg_ntm" ,"maximum_nights_avg_ntm", "calendar_updated", "availability_30",'availability_60', 'availability_90', 'availability_365',
              "calendar_last_scraped", "number_of_reviews_ltm", "number_of_reviews_l30d", "license", "name", "description", "neighborhood_overview", "host_since", 
              "host_location", "host_neighbourhood","host_listings_count", "host_acceptance_rate", "neighbourhood", 
              "maximum_minimum_nights", "maximum_maximum_nights", "has_availability", "first_review", "last_review", "instant_bookable", "reviews_per_month",
              'review_scores_accuracy', 'review_scores_rating', 'review_scores_checkin','review_scores_communication', 'review_scores_location','review_scores_value', 
              "calculated_host_listings_count", "calculated_host_listings_count_entire_homes", "calculated_host_listings_count_private_rooms", 
              "calculated_host_listings_count_shared_rooms", "bedrooms", "beds", "property_type"]

columns_dummies=["neighbourhood_cleansed", "room_type"]


def clean_total(x):
    '''Función para limpiar el dataframe completamente'''

    output=x.drop(columns=drop_columns) # Limpieza de columnas inútiles

    output.host_response_rate=x.host_response_rate.apply(cleaning_host_response_rate) # Lipieza de columna host_response_rate

    output.host_response_time=x.host_response_time.apply(cleaning_host_response_time) # Lipieza de columna host_response_time

    columnas_v_f=[]
    for e in list(x.drop(columns=drop_columns).keys()):
        if len(x[e].unique())==2:
            columnas_v_f.append(e)

    for e in columnas_v_f:
        output[e]=x[e].apply(cleaning_v_f) # Limpieza de columnas verdadero/falso
        
    output.bathrooms_text=x.bathrooms_text.apply(cleaning_bathrooms_text) # Limpieza de columna bathrooms_text

    output["host_verification_email"]=x.host_verifications.str.contains('email').astype(int) # "get_dummies" de columna host_verifications para la verificacion de email

    output["host_verification_phone"]=x.host_verifications.str.contains('phone').astype(int) # "get_dummies" de columna host_verifications para la verificacion de phone

    output.drop(columns='host_verifications', inplace=True) # Eliminación de la columna host_verifications

    output["amenities_n"]=x.amenities.apply(cleaning_amenities_n) # Creación de una columna con el número de amenities de la propiedad

    output.amenities = x.amenities.apply(cleaning_amenities) # Limpieza de la columna amenities a una lista de elementos

    output = amenities_total(output) # get_dummies de los elementos de la columna amenities que poseeen entre un 20% y un 80% de las propiedades

    for e in columns_dummies: # get_dummies de las columnas neighbourhood_cleansed y room_type
        dummies=pd.get_dummies(x[e])
        output=pd.concat([output, dummies], axis=1)
        output.drop(columns=e, inplace=True)

    output.bathrooms_text.fillna(value=1, inplace=True) # Relleno de nulos en la columna bathrooms_text
    output.review_scores_cleanliness.fillna(value=output.review_scores_cleanliness.mean(), inplace=True) # Relleno de nulos en la columna review_scores_cleanliness
    output.host_response_rate.fillna(value=0, inplace=True) # Relleno de nulos en la columna host_response_rate
    output.host_response_time.fillna(value=0, inplace=True) # Relleno de nulos en la columna host_response_time
    
    output = donwcast_df(output)

    return output
