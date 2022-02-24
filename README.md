# Kaggle_competition

  ![airnbn-logo](./img/airbnb_logo.png)


Este proyecto es de una competición de [Kaggle](https://www.kaggle.com/c/airbnb-madrid-ironhack/leaderboard) para encontrar el mejor modelo predictivo de precios para un conjunto de alquieres de Airbnb en Amsterdam

***
## Método
1. Descarga de datos e importación como pandas data frame.
2. Exploración incial de datos.
3. Limpieza del dataframe eliminando columnas que no aportan información para predecir el precio, limpiando otras y haciendo un 'get_dummies' de pandas con otras.
4. Busqueda del modelo que permita predecir el precio de mejor manera, para ello se han usado primero diferentes modelos y luego la librería h2o.
5. Exportación de las predicciones del modelo ganador.

## Documentos
### Jupyter notebooks
* [1.Clean.ipynb]()
* [2.Predictions.ipynb]()

### Data
* [train.csv](): Datos para entrenar el modelo descargados de Kaggle.
* [train_clean.csv](): Datos de entrenamiento limpios.
* [test.csv](): Datos para obtener predicciones descargados de Kaggle.
* [test_clean.csv](): Datos de predicciones limpios.
* [sample.csv](): Datos para subir las predicciones a Kaggle.

### Functions
* [cleaning_functions.py]()
* [predicting_functions.py]()


## Librerias
* [numpy](https://numpy.org/doc/1.22/)
* [pandas](https://pandas.pydata.org/pandas-docs/stable/) 
* [sys](https://docs.python.org/3/library/sys.html)
* [sklearn](https://www.kite.com/python/docs/sklearn)
* [h2o](https://docs.h2o.ai/h2o/latest-stable/h2o-py/docs/intro.html)


## Descripción de los datos

| Field 	| Type 	| Description 	|
|---	|---	|---	|
| id 	| integer 	| Airbnb's unique identifier for the listing 	|
| listing_url 	| text 	|  	|
| scrape_id 	| bigint 	| Inside Airbnb "Scrape" this was part of 	|
| last_scraped 	| datetime 	| UTC. The date and time this listing was "scraped". 	|
| name 	| text 	| Name of the listing 	|
| description 	| text 	| Detailed description of the listing 	|
| neighborhood_overview 	| text 	| Host's description of the neighbourhood 	|
| picture_url 	| text 	| URL to the Airbnb hosted regular sized image for the listing 	|
| host_id 	| integer 	| Airbnb's unique identifier for the host/user 	|
| host_url 	| text 	| The Airbnb page for the host 	|
| host_name 	| text 	| Name of the host. Usually just the first name(s). 	|
| host_since 	| date 	| The date the host/user was created. For hosts that are Airbnb guests this could be the date they registered as a guest. 	|
| host_location 	| text 	| The host's self reported location 	|
| host_about 	| text 	| Description about the host 	|
| host_response_time 	|  	|  	|
| host_response_rate 	|  	|  	|
| host_acceptance_rate 	|  	| That rate at which a host accepts booking requests. 	|
| host_is_superhost 	| boolean [t=true; f=false] 	|  	|
| host_thumbnail_url 	| text 	|  	|
| host_picture_url 	| text 	|  	|
| host_neighbourhood 	| text 	|  	|
| host_listings_count 	| text 	| The number of listings the host has (per Airbnb calculations) 	|
| host_total_listings_count 	| text 	| The number of listings the host has (per Airbnb calculations) 	|
| host_verifications 	|  	|  	|
| host_has_profile_pic 	| boolean [t=true; f=false] 	|  	|
| host_identity_verified 	| boolean [t=true; f=false] 	|  	|
| neighbourhood 	| text 	|  	|
| neighbourhood_cleansed 	| text 	| The neighbourhood as geocoded using the latitude and longitude against neighborhoods as defined by open or public digital shapefiles. 	|
| neighbourhood_group_cleansed 	| text 	| The neighbourhood group as geocoded using the latitude and longitude against neighborhoods as defined by open or public digital shapefiles. 	|
| latitude 	| numeric 	| Uses the World Geodetic System (WGS84) projection for latitude and longitude. 	|
| longitude 	| numeric 	| Uses the World Geodetic System (WGS84) projection for latitude and longitude. 	|
| property_type 	| text 	| Self selected property type. Hotels and Bed and Breakfasts are described as such by their hosts in this field 	|
| room_type 	| text 	| [Entire home/apt\|Private room\|Shared room\|Hotel]  All homes are grouped into the following three room types:  Entire place Private room Shared room Entire place Entire places are best if you're seeking a home away from home. With an entire place, you'll have the whole space to yourself. This usually includes a bedroom, a bathroom, a kitchen, and a separate, dedicated entrance. Hosts should note in the description if they'll be on the property or not (ex: "Host occupies first floor of the home"), and provide further details on the listing.  Private rooms Private rooms are great for when you prefer a little privacy, and still value a local connection. When you book a private room, you'll have your own private room for sleeping and may share some spaces with others. You might need to walk through indoor spaces that another host or guest may occupy to get to your room.  Shared rooms Shared rooms are for when you don't mind sharing a space with others. When you book a shared room, you'll be sleeping in a space that is shared with others and share the entire space with other people. Shared rooms are popular among flexible travelers looking for new friends and budget-friendly stays. 	|
| accommodates 	| integer 	| The maximum capacity of the listing 	|
| bathrooms 	| numeric 	| The number of bathrooms in the listing 	|
| bathrooms_text 	| string 	| The number of bathrooms in the listing.  On the Airbnb web-site, the bathrooms field has evolved from a number to a textual description. For older scrapes, bathrooms is used. 	|
| bedrooms 	| integer 	| The number of bedrooms 	|
| beds 	| integer 	| The number of bed(s) 	|
| amenities 	| json 	|  	|
| price 	| currency 	| daily price in local currency 	|
| minimum_nights 	| integer 	| minimum number of night stay for the listing (calendar rules may be different) 	|
| maximum_nights 	| integer 	| maximum number of night stay for the listing (calendar rules may be different) 	|
| minimum_minimum_nights 	| integer 	| the smallest minimum_night value from the calender (looking 365 nights in the future) 	|
| maximum_minimum_nights 	| integer 	| the largest minimum_night value from the calender (looking 365 nights in the future) 	|
| minimum_maximum_nights 	| integer 	| the smallest maximum_night value from the calender (looking 365 nights in the future) 	|
| maximum_maximum_nights 	| integer 	| the largest maximum_night value from the calender (looking 365 nights in the future) 	|
| minimum_nights_avg_ntm 	| numeric 	| the average minimum_night value from the calender (looking 365 nights in the future) 	|
| maximum_nights_avg_ntm 	| numeric 	| the average maximum_night value from the calender (looking 365 nights in the future) 	|
| calendar_updated 	| date 	|  	|
| has_availability 	| boolean 	| [t=true; f=false] 	|
| availability_30 	| integer 	| avaliability_x. The availability of the listing x days in the future as determined by the calendar. Note a listing may not be available because it has been booked by a guest or blocked by the host. 	|
| availability_60 	| integer 	| avaliability_x. The availability of the listing x days in the future as determined by the calendar. Note a listing may not be available because it has been booked by a guest or blocked by the host. 	|
| availability_90 	| integer 	| avaliability_x. The availability of the listing x days in the future as determined by the calendar. Note a listing may not be available because it has been booked by a guest or blocked by the host. 	|
| availability_365 	| integer 	| avaliability_x. The availability of the listing x days in the future as determined by the calendar. Note a listing may not be available because it has been booked by a guest or blocked by the host. 	|
| calendar_last_scraped 	| date 	|  	|
| number_of_reviews 	| integer 	| The number of reviews the listing has 	|
| number_of_reviews_ltm 	| integer 	| The number of reviews the listing has (in the last 12 months) 	|
| number_of_reviews_l30d 	| integer 	| The number of reviews the listing has (in the last 30 days) 	|
| first_review 	| date 	| The date of the first/oldest review 	|
| last_review 	| date 	| The date of the last/newest review 	|
| review_scores_rating 	|  	|  	|
| review_scores_accuracy 	|  	|  	|
| review_scores_cleanliness 	|  	|  	|
| review_scores_checkin 	|  	|  	|
| review_scores_communication 	|  	|  	|
| review_scores_location 	|  	|  	|
| review_scores_value 	|  	|  	|
| license 	| text 	| The licence/permit/registration number 	|
| instant_bookable 	| boolean 	| [t=true; f=false]. Whether the guest can automatically book the listing without the host requiring to accept their booking request. An indicator of a commercial listing. 	|
| calculated_host_listings_count 	| integer 	| The number of listings the host has in the current scrape, in the city/region geography. 	|
| calculated_host_listings_count_entire_homes 	| integer 	| The number of Entire home/apt listings the host has in the current scrape, in the city/region geography 	|
| calculated_host_listings_count_private_rooms 	| integer 	| The number of Private room listings the host has in the current scrape, in the city/region geography 	|
| calculated_host_listings_count_shared_rooms 	| integer 	| The number of Shared room listings the host has in the current scrape, in the city/region geography 	|
| reviews_per_month 	| numeric 	| The number of reviews the listing has over the lifetime of the listing 	|