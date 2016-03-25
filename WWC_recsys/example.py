import os
import pandas as pd
import WWC_recsys.utils as utils
import WWC_recsys.uknn as uknn
import logging
# @todo add license

# resources:
# https://github.com/cataska/programming-collective-intelligence-code
# https://www.codementor.io/spark/tutorial/building-a-recommender-with-apache-spark-python-example-app-part1
# http://grouplens.org/datasets/movielens/
# https://raw.githubusercontent.com/zacharski/pg2dm-python/master/ch2/recommender.py
# http://www.recsyswiki.com/wiki/MovieLens
# https://en.wikipedia.org/wiki/Collaborative_filtering


#  Code file for the book Programmer's Guide to Data Mining
#  http://guidetodatamining.com
#  Ron Zacharski
# https://raw.githubusercontent.com/zacharski/pg2dm-python/master/ch2/recommender.py


# Get the dataset folder
# If the dataset is not download, it downloads it and unzips it
datasets_folder = '/users/hcorona/github/WWC-recsys/data/'
dataset_url = 'http://files.grouplens.org/datasets/movielens/ml-latest-small.zip'
dataset_path = utils.load_dataset(dataset_url, datasets_folder)

# load ratings
ratings_file = os.path.join(dataset_path, 'ratings.csv')
ratings = pd.read_csv(ratings_file)
ratings.head()

# append my ratings to ratings dataframe
username = ratings.userId.max() + 1
my_ratings = utils.load_personal_ratings(datasets_folder, 'ratings_humberto.csv', username=username)
ratings = ratings.append(my_ratings)

# load movie metadata
movies_file = os.path.join(dataset_path, 'movies.csv')
movies = pd.read_csv(movies_file)
movies.head()

# lets use movie titles instead of id's to make things more human readable
ratings = ratings.merge(movies, on='movieId').drop(['genres','timestamp','movieId'],1)
print(ratings.ix[ratings.userId == username])

# get recommendations for a single user using UKNN method
# @todo make recommendations of length N (we don't want all recommendations)
recommendations = uknn.recommend(username=username, ratings=ratings, K=40, N=10, similarity_metric='intersection')
print(recommendations[:10])

recommendations_pearson = uknn.recommend(username=username, ratings=ratings, K=40, N=10, similarity_metric='pearson')
print(recommendations_pearson[:10])

# @todo run recommendations on all users and evaluate based on PRC-N

# @todo run spark ALS on the same data and get recommendations
# @todo add ALS model
# recommendations_als = matrix_factorization.recommend