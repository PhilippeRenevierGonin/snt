import math
import random

if __name__ == '__main__':
    nbTentatives = 10000
    nbReussites = 0
    for i in range(1,nbTentatives+1):
        # https://docs.python.org/3.12/library/random.html#random.random
        x = random.uniform(0,2)
        y = random.uniform(0,2)
        distance = math.sqrt((x-1)*(x-1)+(y-1)*(y-1))
        if distance <= 1:
            nbReussites = nbReussites + 1
    pi = 4*nbReussites/nbTentatives
    print(f"approximation de pi = {pi}")