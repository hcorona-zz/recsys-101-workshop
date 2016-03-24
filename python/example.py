import os
import urllib
import zipfile
import pandas as pd

# resources
# https://www.codementor.io/spark/tutorial/building-a-recommender-with-apache-spark-python-example-app-part1
# http://grouplens.org/datasets/movielens/
# https://raw.githubusercontent.com/zacharski/pg2dm-python/master/ch2/recommender.py

small_dataset_url = 'http://files.grouplens.org/datasets/movielens/ml-latest-small.zip'
datasets_path = os.path.join('data')
small_dataset_path = os.path.join(datasets_path, 'ml-latest-small.zip')
#small_f = urllib.request.urlretrieve(small_dataset_url, small_dataset_path)


with zipfile.ZipFile(small_dataset_path, "r") as z: z.extractall(datasets_path)

# load ratings
small_ratings_file = os.path.join(datasets_path, 'ml-latest-small', 'ratings.csv')
small_ratings_raw_data = pd.read_csv(small_ratings_file)
small_ratings_raw_data.head()
ratings = small_ratings_raw_data

# load movie metadata
small_movies_file = os.path.join(datasets_path, 'ml-latest-small', 'movies.csv')
small_movies_raw_data = pd.read_csv(small_movies_file)
movies = small_movies_raw_data

ratings = ratings.merge(movies, on='movieId').drop(['genres','timestamp','movieId'],1)

import recommenders as re

recs = re.recommend(59, ratings, 20, 10)