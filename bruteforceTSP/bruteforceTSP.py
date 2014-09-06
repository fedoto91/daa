import re, itertools

cityList = []   # will store permutations of [1 .. n]

def BruteForce(g):
    with open(g) as file:
        for i, line in enumerate(file):
            if i == 3:
                n = re.findall(r'\d+', line)     
                n = int(n[0])    # n is the number of cities in g
                for j in range(1, n+1):
                    cityList.append(j)      # create permuations of [1 .. n]
    file.close()
    permGen = itertools.permutations(cityList)     # permGen is a generator of the permutations of [1 .. n]

g = "mini1.tsp"     # graph g
BruteForce(g)    
