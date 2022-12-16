import numpy as np
from itertools import permutations



x = int(input("Number of cities: "))

b = np.random.randint(50,size=(x,x))
b_symm = (b + b.T)

a = []

for i in b_symm:
	a.append(i)

for i in range(len(a)):
	items = a[i]
	for j in range(len(items)):
		if i == j:
			a[i][j] = 0
		else: continue

def travellingSalesmanProblem(data):
	graph = data
	s = 0

	numberOfCities = len(graph)

	cities = []
	possiblePath = []
	pathLength = []

	for i in range(numberOfCities):
		if i != s:
			cities.append(i)

	nextCitiesPath=permutations(cities)
	for i in nextCitiesPath:
		# store current Path weight(cost)
		currentPathLength = 0
		# compute current path weight
		k = s
		for j in i:
			currentPathLength += graph[k][j]
			k = j
		currentPathLength += graph[k][s]

		for cities in i:
			cities += 1

		possiblePath.append(i)
		pathLength.append(currentPathLength)
			
	bestPathLengthIndex = pathLength.index(min(pathLength))
	bestPath = possiblePath[bestPathLengthIndex]
	print(graph)

	for i in bestPath:
		print("Go to city number" + str(i+1))

	print("Then comeback to city number 1")
	print("Total distance: " + str(min(pathLength)))

if __name__ == "__main__":
	travellingSalesmanProblem(b_symm)