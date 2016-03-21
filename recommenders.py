from math import sqrt
import pandas as pd
#  Code file for the book Programmer's Guide to Data Mining
#  http://guidetodatamining.com
#  Ron Zacharski
# https://raw.githubusercontent.com/zacharski/pg2dm-python/master/ch2/recommender.py





def common_sim(rating1, rating2):
    """
    :param rating1:
    :param rating2:
    :return: number of common items
    """
    rating1 = rating1[rating1 != 0]
    rating2 = rating1[rating2 != 0]
    return len(rating1.index.intersection(rating2.index))


def compute_nearest_neighbours(username, ratings_p):
    """
    creates a sorted list of users based on their distance to username
    :param username:
    :param ratings:
    :return:
    """
    distances = []
    rating1 = ratings_p.ix[username]
    for user in ratings_p.index:
        distance = common_sim(rating1 , ratings_p.ix[user])
        distances.append((distance, user))
    distances = pd.DataFrame(distances, columns=['userId','similarity']).sort_values(by='similarity',ascending=False)
    return distances


def recommend(username, ratings, K, n ):
    """Give list of recommendations"""
    recommendations = {}
    # first get list of users  ordered by nearness
    ratings_p = ratings.pivot_table(index='userId', columns='title', values='rating', fill_value=0)
    nearest = compute_nearest_neighbours(username,ratings_p)
    nearest = nearest[0:K]

    userRatings = ratings.ix[ratings.userId == username]
    totalDistance = nearest.similarity.sum()

    # now iterate through the k nearest neighbors
    # accumulating their ratings
    for i in range(K):
        # compute slice of pie
        weight = nearest.iloc[i].similarity / totalDistance
        # get the name of the person
        name = nearest.iloc[i].userId
        # get the ratings for this person
        neighborRatings = ratings.ix[ratings.userId == name]
        # get the name of the person
        # now find bands neighbor rated that user didn't
    for movie in neighborRatings.title.unique():
        if movie not in recommendations:
            prediction = neighborRatings.rating[neighborRatings.title == movie]* weight
            prediction = prediction.values[0]
            recommendations[movie] = prediction
        else:
            recommendations[movie] = (recommendations[movie] + prediction)
    # now make list from dictionary
    recommendations = list(recommendations.items())
    recommendations = pd.DataFrame(recommendations, columns=['title','rating']).sort_values(by='rating',ascending=False)

    return recommendations[:10]
