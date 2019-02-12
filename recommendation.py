# -*- coding = utf-8 -*-


import collections
from operator import itemgetter

import math

from collections import defaultdict

import collections

import math



def calculateUserSimilarity(trainset):
    trainsetTable = defaultdict(set)
    for user, movies in trainset.items():  #Building movie-users table from our trainset movies
        for movie in movies:
            trainsetTable[movie].add(user)
    print('Building movie users inverse table success.')
    numberOfMovie = len(trainsetTable) #Number of movie on trainset

    userSimilarityMatrix = defaultdict(int)

    #Count co-rated items between users
    for movie, users in trainsetTable.items():
        for user1 in users:
            userSimilarityMatrix.setdefault(user1, defaultdict(int)) #user1 is our target user
            for user2 in users:
                if user1 == user2:
                    continue
                if 0: #TODO WE CAN ADD MORE THING IN HERE
                    continue
                else:  #if user1 and user2 both two rated movie same add +1

                    userSimilarityMatrix[user1][user2] += 1
    for user1, related_users in userSimilarityMatrix.items():
        numberOfItemUser1 = len(trainset[user1])
        for user2, count in related_users.items():
            numberOfItemUser2 = len(trainset[user2])
            userSimilarityMatrix[user1][user2] = count / math.sqrt(numberOfItemUser1 * numberOfItemUser2)

    print('users similarity calculated.')

    return userSimilarityMatrix, numberOfMovie



class Recommendation:
    def __init__(self, neighborNumber=10, numberOfRecommendation=40):
        self.neighborNumber = neighborNumber
        self.numberOfRecommendation = numberOfRecommendation
    def fit(self, trainset):
        self.userSimilarityMatrix, self.numberOfMovie=calculateUserSimilarity(trainset=trainset)
        self.trainset = trainset
        print('Train a new model success.')
    def recommend(self, user):
        K = self.neighborNumber
        N = self.numberOfRecommendation
        predictionScore = collections.defaultdict(int)
        watchedMovies = self.trainset[user]

        sortedList = sorted(self.userSimilarityMatrix[user].items(),
                                                      key=itemgetter(1), reverse=True)[0:K]
        for similarUser, similarityFactor in sortedList:
            for movie, rating in self.trainset[similarUser].items():
                if movie in watchedMovies:
                    continue
                predictionScore[movie] += similarityFactor * rating

        bestScores = [movie for movie, _ in sorted(predictionScore.items(), key=itemgetter(1), reverse=True)[0:N]]
        return bestScores

    def test(self, testset):
        self.testset = testset
        N = self.numberOfRecommendation
        hit = 0
        recommendationCount = 0
        testCount = 0
        recCount=0
        for i, user in enumerate(self.trainset):
            testMovies = self.testset.get(user, {})
            recMovies = self.recommend(user)  # type:list
            for movie in recMovies:
                if movie in testMovies:
                    hit += 1
            recCount += N
            testCount += len(testMovies)
        precision = hit / (1.0 * recCount)
        recall = hit / (1.0 * testCount)
        #TODO RMSE, MAE WILL BE ADDED
        print('Precision: ', precision)
        print('Recall: ',recall)
