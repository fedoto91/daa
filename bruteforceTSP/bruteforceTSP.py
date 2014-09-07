import re, itertools, math

cityList = []       # will store permutations of [1 .. n]
coordList = []      # will store the coordinates of all the cities
n = 0       # will be the number of cities

def BruteForce(g):
    xTotal = 0
    yTotal = 0
    with open(g) as file:
        for i, line in enumerate(file):
            if i == 3:
                n = re.findall(r'\d+', line)     
                n = int(n[0])    # n is the number of cities in g
                for j in range(1, n+1):
                    cityList.append(j)      # create permuations of [1 .. n]
            if i >= 6 and i < (6 + n):
                coordList.append(re.findall(r'\d+', line))

                
    file.close()
    permGen = itertools.permutations(cityList)     # permGen is a generator of the permutations of [1 .. n]
    
    
    for p in permGen:   #
        print(p)        # p is the first permutation of permGen
        break           #

    bestTourSoFar = p # bestTourSoFar is the tour corresponding to p
    bestTourSoFarList = list(bestTourSoFar)
    for i in range(0, n):     # loop as many times as there are cities
        xTotal -= int(coordList[bestTourSoFarList[0] - 1][1])
        yTotal -= int(coordList[bestTourSoFarList[0] - 1][2])
    xTotal = abs(xTotal)
    yTotal = abs(yTotal)
    bestCostSoFar = math.hypot(xTotal, yTotal) # bestCostSoFar is the cost of bestTourSoFar
    print(bestCostSoFar)

g = "mini1.tsp"     # graph g
BruteForce(g)