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
        logging.info('downloading dataset ')
        zf = urllib.request.urlretrieve(dataset_url, dataset_path)
        with zipfile.ZipFile(dataset_path, "r") as z: z.extractall(datasets_folder)
    else:
        logging.info('dataset was already downloaded')

    # return the extracted folder that contains all the rating files
    logging.info('sucess getting dataset folder')
    return os.path.splitext(dataset_path)[0]


def load_personal_ratings(datasets_folder, ratings_file, username):
    """
    :param datasets_folder:
    :param ratings_file:
    :param username:
    :return:
    """
    # load personal ratings and format into the right format
    my_ratings_file = os.path.join(datasets_folder, ratings_file)
    my_ratings = pd.read_csv(my_ratings_file)
    my_ratings['userId'] = username
    my_ratings['timestamp'] = int(round(time.time() * 1000))
    my_ratings = my_ratings[['userId', 'movieId', 'rating', 'timestamp']]
    return my_ratings
