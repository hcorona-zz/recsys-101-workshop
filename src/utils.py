import os
import zipfile
import logging
import urllib
import time
import pandas as pd


def load_dataset(datasets_folder, dataset_url= "http://files.grouplens.org/datasets/movielens/ml-latest-small.zip"):
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
        logging.info('downloading dataset %s', dataset_url)
        zf = urllib.request.urlretrieve(dataset_url, dataset_path)
        with zipfile.ZipFile(dataset_path, "r") as z: z.extractall(datasets_folder)
    else:
        logging.info('dataset was already downloaded')

    # return the extracted folder that contains all the rating files
    logging.info('dataset stored in: %s', os.path.splitext(dataset_path)[0])
    return os.path.splitext(dataset_path)[0]


def load_personal_ratings(datasets_folder, ratings_file, customer_number):
    """
    :param datasets_folder: the folder where the original dataset was stored
    :param ratings_file: the file created with personal ratings
    :param username: the username to be assigned 
    :return: a structure with the personal ratings, incluiding a userId 
    """
    # load personal ratings and format into the right format
    my_ratings_file = os.path.join(datasets_folder, ratings_file)
    my_ratings = pd.read_csv(my_ratings_file)
    my_ratings['userId'] = customer_number
    my_ratings['timestamp'] = int(round(time.time() * 1000))
    my_ratings = my_ratings[['userId', 'movieId', 'rating', 'timestamp']]
    logging.info("loaded %d personal ratings", len(my_ratings.index))
    return my_ratings


def merge_datasets(dataset_folder, my_ratings_file):
    """
    :param dataset_folder: folder was previously the dataset is downloaded to
    :param my_ratings_file: where is the personal recommendations file stored
    :return: a dataframe with the ratings (merges original ratings with personal ratings)
    """

    # load original dataset ratings file
    ratings_file = os.path.join(dataset_folder, 'ratings.csv')
    ratings = pd.read_csv(ratings_file)

    # append personal ratings to ratings dataframe from original dataset
    customer_number = ratings.userId.max() + 1
    my_ratings = load_personal_ratings(dataset_folder, my_ratings_file, customer_number=customer_number)
    ratings = ratings.append(my_ratings)

    # load movie metadata
    movies_file = os.path.join(dataset_folder, 'movies.csv')
    movies = pd.read_csv(movies_file)
    logging.info("loaded %d movies", len(movies.index))

    # lets use movie titles instead of id's to make things more human readable
    ratings = ratings.merge(movies, on='movieId').drop(['genres','timestamp','movieId'],1)
    ratings = ratings[['userId', 'title', 'rating']]
    ratings.columns = ['customer', 'movie', 'rating']
    logging.info("loaded %d ratings in total", len(ratings.index))

    return [ratings, customer_number]
