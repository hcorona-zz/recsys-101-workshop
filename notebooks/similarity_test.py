import pandas as pd
import wwc_recsys.utils as utils
import wwc_recsys.similarity as similarity

# Get the dataset folder. If the dataset is not download, it downloads it and unzips it
datasets_folder = '/users/hcorona/github/WWC-recsys/data/'
dataset_url = 'http://files.grouplens.org/datasets/movielens/ml-latest-small.zip'
my_ratings_file = 'ratings_humberto.csv'


[ratings, my_customer_number] = utils.merge_datasets(datasets_folder, dataset_url, my_ratings_file)
ratings_matrix = ratings.pivot_table(index='customer', columns='movie', values='rating', fill_value=0)
ratings_matrix = ratings_matrix.transpose()
movie_list = pd.DataFrame(ratings_matrix.index)


# movie_list[movie_list['movie'].str.contains("Mystic River")]
movie_list = ['Juno (2007)', 'Harry Potter and the Chamber of Secrets (2002)', 'Django Unchained (2012)']
for movie_test in movie_list:
    print(similarity.compute_nearest_neighbours(movie_test, ratings_matrix, 'intersection')[0:10])
    print(similarity.compute_nearest_neighbours(movie_test, ratings_matrix, 'pearson')[0:10])
    print('\n')

