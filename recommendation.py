import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

def get_list_movies():
	return dfMovies[['tconst', 'title', 'startYear']]

def read_local_csv(fileName):
    with pd.read_csv(f"./data/filtered.{fileName}.csv.gz",
                 index_col = 0, 
                 chunksize=1000) as reader: 
        return pd.concat(chunk for chunk in reader)

def get_recommendation(moveId):
	#return model_from_sun.predict(df_weather[['SUNHOUR']])
	#return df_title_basics[['tconst', 'originalTitle']].sample(n=5)
	return dfMovies[['tconst', 'originalTitle']].sample(n=5)

def get_recommendation_by_NearestNeighbors(moveId):
	X_test = dfNearestNeighbors[dfNearestNeighbors.tconst == moveId].drop(['title', 'tconst', 'originalTitle', 'runtimeMinutes'], axis = 1)
	X_test_scaled = scalerNearestNeighbors.transform(X_test)
	neighbors = distanceKNN.kneighbors(X_test_scaled)
	return dfNearestNeighbors.loc[neighbors[1][0], ['tconst' , 'title']].tail(5)


# exemple weather
# link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
# df_weather = pd.read_csv(link)
# X = df_weather[['SUNHOUR']] 
# y = df_weather['MAX_TEMPERATURE_C'] 
# model_from_sun = LinearRegression().fit(X, y)

# IMDB
#df_title_basics = read_local_csv("title.basics")
#df_title_basics.reset_index(inplace=True)

# dataframe liste de recherche de films
#dfMovies = pd.read_csv("./data/film_FR_1.csv", sep=";")
dfMovies = pd.read_csv("./data/ML_Os_Lg.csv", sep=",")

# model 1
#dfNearestNeighbors = pd.read_csv('./data/ML_filmFR.csv' , sep = ',', parse_dates = True ,on_bad_lines='skip' , na_values =r'\N', low_memory=False)
dfNearestNeighbors = pd.read_csv('./data/ML_Os_Lg.csv' , sep = ',', parse_dates = True ,on_bad_lines='skip' , na_values =r'\N', low_memory=False)
dfNearestNeighbors = dfNearestNeighbors.drop_duplicates(subset=['tconst'], ignore_index = True)
dfNearestNeighbors = dfNearestNeighbors.drop(columns = ['Unnamed: 0'])
X = dfNearestNeighbors.drop(['title' , 'tconst','originalTitle', 'runtimeMinutes'], axis = 1)
scalerNearestNeighbors = StandardScaler()
X_train_scaled = scalerNearestNeighbors.fit_transform(X)
distanceKNN = NearestNeighbors(n_neighbors = 6).fit(X_train_scaled)