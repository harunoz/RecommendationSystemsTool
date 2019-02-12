from recommendation import Recommendation


import collections

import itertools
import random
from collections import namedtuple

BuiltinDataset = namedtuple('BuiltinDataset', ['path', 'sep', 'readerParams'])

BUILTIN_DATASETS = {
    'ml-100k':
        BuiltinDataset(
            path='data/ml-100k/u.data',
            sep='\t',
            readerParams=dict(line_format='User Item Rating',

                               sep='\t')
        ),
    'ml-1m'  :
        BuiltinDataset(
            path='data/ml-1m/ratings.dat',
            sep='::',
            readerParams=dict(line_format='User Item Rating',
                               sep='::')
        ),

}



class DataSet:
    def __init__(self):
        pass

    @classmethod
    def load_dataset(cls, name='ml-100k'):
        dataset = BUILTIN_DATASETS[name]
        with open(dataset.path) as f:
            ratings = [cls.parseLine(line, dataset.sep) for line in itertools.islice(f, 0, None)]
        print("Datasets sucessfully loaded.")
        return ratings

    @classmethod
    def parseLine(cls, line: str, sep: str):

        user, movie, rate = line.strip('\r\n').split(sep)[:3]
        return user, movie, rate

    @classmethod
    def trainTestSplit(cls, ratings, test_size=0.2):
        train, test = collections.defaultdict(dict), collections.defaultdict(dict)
        trainset_len = 0
        testset_len = 0
        for user, movie, rate in ratings:
            if random.random() <= test_size:
                test[user][movie] = int(rate)
                testset_len += 1
            else:
                train[user][movie] = int(rate)
                trainset_len += 1

        return train, test


def runModel():
    datasetName='ml-100k'
    ratings = DataSet.load_dataset(name=datasetName)
    trainset = DataSet.trainTestSplit(ratings, test_size=0.2)[0]
    testset= DataSet.trainTestSplit(ratings, test_size=0.2)[1]
    model = Recommendation()
    model.fit(trainset)
    model.test(testset)

runModel()