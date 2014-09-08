# Eugene Fedotov
# Brute Force program for the Traveling Sales Person problem

import re, itertools, math, cProfile

cityList = []       # will store permutations of [1 .. n]
coordList = []      # will store the coordinates of all the cities
n = 0       # will be the number of cities
pDistance = 0
def BruteForce(g):
    with open(g) as file:
        for i, line in enumerate(file):
            if i == 3:
                n = re.findall(r'\d+', line)     
                n = int(n[0])    # n is the number of cities in g
                for j in range(1, n+1):
                    cityList.append(j)      # create permuations of [1 .. n]
            if i >= 6 and i <= (5 + n):
                coordList.append(re.findall(r'\d+', line))

                
    file.close()
    permGen = itertools.permutations(cityList)     # permGen is a generator of the permutations of [1 .. n]
    
    
    for p in permGen:   #              # p is the first permutation of permGen
        break           #

    bestTourSoFar = list(p) # bestTourSoFar is the tour corresponding to p
    bestDistanceSoFar = 0
    for i in range(0, n - 1):
        x2 = int(coordList[bestTourSoFar[i]][1])
        y2 = int(coordList[bestTourSoFar[i]][2])
        x1 = int(coordList[bestTourSoFar[i] - 1][1])
        y1 = int(coordList[bestTourSoFar[i] - 1][2])
        bestDistanceSoFar += math.hypot(x2 - x1, y2 - y1)       # bestDistanceSoFar is the cost of bestTourSoFar
        pDistance = bestDistanceSoFar
    # Print total cost for first permutation.
    # print(bestDistanceSoFar)

# while (permGen has more permutations)
    for q in permGen:   # p is the next permutation of permGen
        t = list(q) # t is the tour corresponding to p
        distance = 0
        for i in range(0, n):
            x2 = int(coordList[i + 1][1])
            y2 = int(coordList[i + 1][2])
            x1 = int(coordList[i][1])
            y1 = int(coordList[i][2])
            distance += math.hypot(x2 - x1, y2 - y1)       # distance is the cost of bestTourSoFar
            if distance > bestDistanceSoFar:
               bestTourSoFar = t
               bestDistanceSoFar = distance      
            if x2 == 7 and y2 == 9:
                break    
        bestDistanceSoFar = bestDistanceSoFar + pDistance
    print("Best tour:  ")
    print("\n")
    print(bestTourSoFar)
    print("\n")
    print("Best cost:  ")
    print("\n")
    print(bestDistanceSoFar)
    print("\n")
    #return bestTourSoFar

g = "mini1.tsp"     # graph g
cProfile.run('BruteForce(g)')