import pandas as pd
import logging
import numpy


def common_sim(rating1, rating2):
    """
    :param rating1:
    :param rating2:
    :return: number of common items
    """
    rating1 = rating1[rating1 != 0]
    rating2 = rating2[rating2 != 0]
    return len(rating1.index.intersection(rating2.index))

# @todo implement pearson similarity
def pearson_sim(rating1, rating2):
    return numpy.corrcoef(list(rating1), list(rating2))[0, 1]


# @todo implement jaccard similarity
def jaccard_sim(rating1, rating2):
    return 0


# @todo implement most popular similarity
def most_popular(rating1, rating2):
    return 0


def calculate_distance(rating1, rating2, distance_metric):
    """
    :param rating1:
    :param rating2:
    :param distance_metric:
    :return:
    """
    if distance_metric == 'intersection': return common_sim(rating1, rating2)
    if distance_metric == 'pearson': return pearson_sim(rating1, rating2)


def compute_nearest_neighbours(username, ratings_matrix, distance_metric):
    """
    creates a sorted list of users based on their distance to username
    :param username:
    :param ratings_maxtrix:
    :param distance_metric: tells which function to use to calculate metric
    :return:
    """
    distances = []
    rating1 = ratings_matrix.ix[username]
    for user in ratings_matrix.index:
        distance = calculate_distance(rating1, ratings_matrix.ix[user], distance_metric)
        distances.append((user, distance))
    distances = pd.DataFrame(distances, columns=['userId', 'similarity']).sort_values(by='similarity', ascending=False)
    return distances


def recommend(username, ratings, K, N, similarity_metric):
    """
    Give list of recommendations to a particular user
    :param username: user for which we want to compute recommendations
    :param ratings: a dataframe with ratings
    :param K: how many neigbhours to use in UK-NN algorithm
    :param N: how many recommendations to output in top-N recommendations
    :param similarity: which similarity metric to use
    :return: a dataframe with a list of recommendations and the predicted rating
    : adding this to see if it's updated
    """
    print('hello im in')
    # create the rating matrix: for small datasets should fit in memory
    ratings_p = ratings.pivot_table(index='userId', columns='title', values='rating', fill_value=0)

    # get the nearest neighbours and compute the total distance
    # normalize scorses to add to 1
    # [1:K] to avoid self correlation
    nearest = compute_nearest_neighbours(username, ratings_p, similarity_metric)[1:K+1]
    nearest['similarity'] = nearest.similarity / nearest.similarity.sum()
    logging.info('computed nearest neighgours using %s',similarity_metric)

    # @todo: here we recommend movies the target user may have already rated
    # @todo: change the code so we only recommend movies unknown for the tartget user
    # userRatings = ratings.ix[ratings.userId == username]
    # ratedMovies = ratings.title[ratings.userId == username]

    # Iterate through the k nearest neighbors, accumulating their ratings
    recommendations = {}
    for k in range(K):
        # distance and name between two users
        weight = nearest.iloc[k].similarity
        name = nearest.iloc[k].userId
        # get the ratings for this neigbhour
        neighborRatings = ratings.ix[ratings.userId == name]

        # calculate the predicted rating for each recommendations
        for movie in neighborRatings.title.unique():
            prediction = neighborRatings.rating[neighborRatings.title == movie]*weight
            # if it's the first neighbours who is recommending this movie
            if movie not in recommendations: recommendations[movie] = prediction.values[0]
            # if this movie has been recommended  by other neighbours
            else: recommendations[movie] = recommendations[movie] + prediction.values[0]
    # now make list from dictionary
    recommendations = pd.DataFrame(recommendations, columns=['title', 'rating']).sort_values(by='rating', ascending=False)
    print(' ------ ')
    print(recommendations)
    # only return the top N recommendations
    return recommendations
