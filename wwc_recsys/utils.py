import os
import zipfile
import logging
import urllib
import time
import pandas as pd


def load_dataset(dataset_url, datasets_folder):
    """
    queries any of the movielens dataset and stores it into the desired folder
    :param dataset_url: the url from where to fetch the dataset (from movielens.org)
    :param dataset_path: the path on where to store the dataset
    :return: the path to the dataset folder
    """
    zipfile_name = os.path.basename(dataset_url)
    dataset_path = os.path.join(datasets_folder, zipfile_name)

    # if the .zip file doesn't exist
    if not os.path.isfile(dataset_path):
        print('downloading dataset')
        logging.info('downloading dataset %s', dataset_url)
        zf = urllib.request.urlretrieve(dataset_url, dataset_path)
        with zipfile.ZipFile(dataset_path, "r") as z: z.extractall(datasets_folder)
    else:
        logging.info('dataset was already downloaded')

    # return the extracted folder that contains all the rating files
    logging.info('sucess getting dataset folder')
    return os.path.splitext(dataset_path)[0]


def load_personal_ratings(datasets_folder, ratings_file, customer_number):
    """
    :param datasets_folder:
    :param ratings_file:
    :param username:
    :return:
    """
    # load personal ratings and format into the right format
    my_ratings_file = os.path.join(datasets_folder, ratings_file)
    my_ratings = pd.read_csv(my_ratings_file)
    my_ratings['userId'] = customer_number
    my_ratings['timestamp'] = int(round(time.time() * 1000))
    my_ratings = my_ratings[['userId', 'movieId', 'rating', 'timestamp']]
    return my_ratings


def merge_datasets(datasets_folder, dataset_url, my_ratings_file):
    """
    :param datasets_folder: where to store the dataset
    :param dataset_url: the url to download the dataset from
    :param my_ratings_file: where is the personal recommendations file stored
    :return: a dataframe with the ratings (merges original ratings with personal ratings)
    """

    # load ratings
    dataset_path = load_dataset(dataset_url, datasets_folder)
    ratings_file = os.path.join(dataset_path, 'ratings.csv')
    ratings = pd.read_csv(ratings_file)
    ratings.head()

    # append my ratings to ratings dataframe
    customer_number = ratings.userId.max() + 1
    my_ratings = load_personal_ratings(datasets_folder, my_ratings_file, customer_number=customer_number)
    ratings = ratings.append(my_ratings)

    # load movie metadata
    movies_file = os.path.join(dataset_path, 'movies.csv')
    movies = pd.read_csv(movies_file)
    movies.head()

    # lets use movie titles instead of id's to make things more human readable
    ratings = ratings.merge(movies, on='movieId').drop(['genres','timestamp','movieId'],1)
    ratings = ratings[['userId', 'title', 'rating']]
    ratings.columns = ['customer', 'movie', 'rating']

    return [ratings, customer_number]
