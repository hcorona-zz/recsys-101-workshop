import os
import pandas as pd
import WWC_recsys.utils as utils
import WWC_recsys.recommenders as recommenders
# @todo add license


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
ratings = ratings[['userId','title','rating']]
ratings.columns = ['customer','movie','rating']

# get recommendations for a single user using UKNN method
recommendations = recommenders.recommend_uknn(target_customer=username, ratings=ratings, K=5, N=10, similarity_metric='pearson')
print(recommendations)
recommendations = recommenders.recommend_iknn(target_customer=username, ratings=ratings, K=20, N=10, similarity_metric='pearson')
print(recommendations)
