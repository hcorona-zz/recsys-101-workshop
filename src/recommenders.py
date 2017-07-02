import pandas as pd
import logging
import src.similarity as similarity


def sort_recommendations(recommendations, N):
    """
    :param recommendations: a list with all the recommendations
    :param N: number of recommendations to return
    :return: a dataframe with the recommendations
    """
    recommendations.sort()
    recommendations.reverse()
    recommendations = recommendations[0:N]
    return pd.DataFrame(recommendations, columns=['rating', 'movie'])


def recommend_iknn(ratings, target_customer, K= 10, N= 10, similarity_metric='pearson'):
    """
    Give list of recommendations to a particular user
    :param target_customer: user for which we want to compute recommendations
    :param ratings: a dataframe with ratings
    :param K: how many neigbhours to use in UK-NN algorithm
    :param N: how many recommendations to output in top-N recommendations
    :param similarity_metric: which similarity metric to use
    :return: a dataframe with a list of recommendations and the predicted rating
    """

    # create the rating matrix: for small datasets should fit in memory
    # @todo (question) how long will it take to get recommendations for all users (exercise)
    ratings_matrix = ratings.pivot_table(index='customer', columns='movie', values='rating', fill_value=0)
    ratings_matrix = ratings_matrix.transpose()

    # user movies
    user_movies = ratings_matrix[target_customer][ratings_matrix[target_customer] > 0]

    recommendations = {}
    simSums = {}

    # for each movie the user rated, get all the possible neighbours
    for user_movie in user_movies.index:
        nearest = similarity.compute_nearest_neighbours(user_movie, ratings_matrix.drop(target_customer,1), similarity_metric)[1:K+1]

        # calculate the predicted rating for each recommendations
        for movie in nearest.item.unique():
            weight = nearest.similarity[nearest.item == movie]
            prediction = user_movies[user_movie]*weight
            # if there is a new movie, set the similarity and sums to 0
            recommendations.setdefault(movie, 0)
            simSums.setdefault(movie, 0)
            recommendations[movie] += prediction.values[0]
            simSums[movie] += weight.values[0]

    # Divide each total score by total weighting to get an average
    recs_normalized = [(recommendations/simSums[movie], movie) for movie, recommendations in recommendations.items()]

    # normalise so that the sum of weights for each movie adds to 1
    return sort_recommendations(recs_normalized, N)


def recommend_uknn(ratings, target_customer , K=10, N=10, similarity_metric='pearson'):
    """
    Give list of recommendations to a particular user
    :param target_customer: user for which we want to compute recommendations
    :param ratings: a dataframe with ratings
    :param K: how many neigbhours to use in UK-NN algorithm
    :param N: how many recommendations to output in top-N recommendations
    :param similarity_metric: which similarity metric to use
    :return: a dataframe with a list of recommendations and the predicted rating
    """
    # create the rating matrix: for small datasets should fit in memory
    # @todo (question) how long will it take to get recommendations for all users (excercise)
    ratings_matrix = ratings.pivot_table(index='customer', columns='movie', values='rating', fill_value=0)

    # get the nearest neighbours and compute the total distance
    # normalize scores to add to 1
    # only compute from [1:K] to avoid self correlation (index 0)
    neighbours = similarity.compute_nearest_neighbours(target_customer, ratings_matrix, similarity_metric)[1:K+1]
    logging.info('computed nearest neighbours using %s', similarity_metric)

    # @todo: (question)
    # - here we recommend movies the target user may have already rated. How can we solve that? (exercicse)
    # Iterate through the k nearest neighbors, accumulating their ratings
    recommendations = {}
    simSums = {}

    for neighbour in neighbours.item.unique():

        weight = neighbours.similarity[neighbours.item == neighbour]
        neighbour_ratings = ratings.ix[ratings.customer == neighbour]

        # calculate the predicted rating for each recommendations
        for movie in neighbour_ratings.movie.unique():
            prediction = neighbour_ratings.rating[neighbour_ratings.movie == movie]*weight.values[0]
            # if there is a new movie, set the similarity and sums to 0
            recommendations.setdefault(movie, 0)
            simSums.setdefault(movie, 0)

            recommendations[movie] += prediction.values[0]
            simSums[movie] += weight.values[0]

    # normalise so that the sum of weights for each movie adds to 1
    recs_normalized = [(recommendations/simSums[movie], movie) for movie, recommendations in recommendations.items()]
    return sort_recommendations(recs_normalized, N)


# @todo: (improvement add this model as a example
# read this great blog and try to implement the example
# it produces really good recommendations
# http://sifter.org/~s
def recommend_mf():
    return 0