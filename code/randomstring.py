import random


# Documentation
# https://docs.python.org/3.7/library/random.html#random.choice


def randomstring(path):
    '''
    Picks a random string
    '''
    rando = random.choice(path)
    output = '%s' % (rando)
    return output


# print(randomstring('../data/file0.txt'))
