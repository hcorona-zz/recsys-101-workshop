import pandas as pd
import numpy
from scipy.spatial.distance import cosine


def cosine_sim(rating1, rating2):
    """
    :param rating1:
    :param rating2:
    :return: cosine similarity between the two items / users
    """
    return (1 - cosine(rating1, rating2))


def common_sim(rating1, rating2):
    """
    :param rating1:
    :param rating2:
    :return: number of common items
    """
    rating1 = rating1[rating1 != 0]
    rating2 = rating2[rating2 != 0]
    return len(rating1.index.intersection(rating2.index))


def pearson_sim(rating1, rating2):
    """
    :param rating1:
    :param rating2:
    :return: pearson correlation between the two sets of ratings
    """
    return numpy.corrcoef(list(rating1), list(rating2))[0, 1]


def jaccard_sim(rating1, rating2):
    """
    :param rating1:
    :param rating2:
    :return: jaccard similarity between the two set of ratings
    https://en.wikipedia.org/wiki/Jaccard_index
    """

    set_1 = set(rating1[rating1 != 0].index)
    set_2 = set(rating1[rating2 != 0].index)

    intersection_cardinality = len(set.intersection(*[set_1, set_2]))
    union_cardinality = len(set.union(*[set_1, set_2]))
    return intersection_cardinality / float(union_cardinality)


# @todo: (question) implement most popular similarity
# @todo: (question) add an extra parameter that is needed
def most_popular(rating1, rating2):
    """
    :param rating1:
    :param rating2:
    :return: forget similarity, it returns the most popular items that both users share
    """


def calculate_distance(rating1, rating2, distance_metric):
    """
    :param rating1:
    :param rating2:
    :param distance_metric: which distance metric to use
    :return:
    """
    if distance_metric == 'intersection': return common_sim(rating1, rating2)
    if distance_metric == 'pearson' : return pearson_sim(rating1, rating2)
    if distance_metric == 'jaccard': return jaccard_sim(rating1, rating2)
    if distance_metric == 'cosine': return cosine_sim(rating1, rating2)
    else: raise Exception('the metric specified is not implemented!')


def compute_nearest_neighbours(item, ratings_matrix, distance_metric):
    """
    creates a sorted list of items (users or movies) based on their distance to the target
    :param item: the item to compare (can be a user or a movie)
    :param ratings_matrix:
    :param distance_metric: tells which function to use to calculate metric
    :return: distances for all the neighbours
    """
    distances = []
    rating1 = ratings_matrix.ix[item]
    for item in ratings_matrix.index:
        distance = calculate_distance(rating1, ratings_matrix.ix[item], distance_metric)
        distances.append((item, distance))
    distances = pd.DataFrame(distances, columns=['item', 'similarity']).sort_values(by='similarity', ascending=False)
    return distances
