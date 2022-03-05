#KNN Algorithm
#In this example I will use the Iris dataset: http://archive.ics.uci.edu/ml/datasets/Iris

#Need to import the data first
f = open("iris.data", "r")
data = f.readlines()
f.close()

#create the class element for each item
#there are 4 attributes: sepal length, sepal width, petal length and petal width
#for this first example I will use a 2D plane to make it simple, so I need to pick the 2 with the highest range
#Petal length and Petal width both have a high Class Correlation, so I will pick those
class iris:
    irisType: str
    pLength: float
    pWidth: float
    def __init__(self, pL, pW, irisType):
        self.pLength = float(pL)
        self.pWidth = float(pW)
        self.irisType = irisType[:-1] #to remove the \n at the end of the line

flowers = []

#now loop through the data and add it to the flowers list
for line in data:
    splitLine = line.split(",")
    pLength = splitLine[2]
    pWidth = splitLine[3]
    irisType = splitLine[4]
    
    flowers.append(iris(pLength, pWidth, irisType))

#now plot this data on a graph (different colours for each different type of iris)
#UNCOMMENT THIS CODE IF YOU WANT TO SEE A GRAPH
"""
import matplotlib.pyplot as plt

xPoints1 = [] #Iris-setosa
yPoints1 = []
xPoints2 = [] #Iris-versicolor
yPoints2 = []
xPoints3 = [] #Iris-virginica
yPoints3 = []

for f in flowers:
    if f.irisType == "Iris-setosa":
        xPoints1.append(f.pLength)
        yPoints1.append(f.pWidth)
    elif f.irisType == "Iris-versicolor":
        xPoints2.append(f.pLength)
        yPoints2.append(f.pWidth)
    else:
        xPoints3.append(f.pLength)
        yPoints3.append(f.pWidth)

plt.scatter(xPoints1, yPoints1, color="red")
plt.scatter(xPoints2, yPoints2, color="green")
plt.scatter(xPoints3, yPoints3, color="blue")
plt.show()
"""


#now that we have the data, lets make up some sample data and check where this will classify it
samplePetalLength = 2.3 #this should classify this as Iris-Setosa
samplePetalWidth = 0.8
"""
samplePetalLength = 4.5 #this should classify as Iris-Versicolor
samplePetalWidth = 1.5
"""
"""
samplePetalLength = 6 #this should classify as Iris-Virginica
samplePetalWidth = 2
"""

class distance: #making a new class  which just holds the distances from the samplePoint, and to which type of flower/iris
    length: float
    toType: str
    def __init__(self, d, t):
        self.length = d
        self.toType = t

import math

distances = []
for f in flowers:
    flowerX = f.pLength
    flowerY = f.pWidth
    sampleX = samplePetalLength
    sampleY = samplePetalWidth

    #calculate the distance inbetween using pythagoras's theorm a2 + b2 = c2
    #don't need to worry about negative numbers since the square will remove it
    a = sampleX - flowerX
    b = sampleY - flowerY
    c = math.sqrt((a**2) + (b**2)) #the distance in between the sample point and the current point (f)
    distances.append(distance(c, f.irisType))


#Now find the k lowest distances in the list
    #use python inbuilt function to sort the distances list based on distance's .length attribute
distances.sort(key=lambda x: x.length, reverse=False)

#set k to 10, so it gets the top 10 items in the list
k = 10
lowestDistances = distances[0: k]

#see which type has the highest amount
types = {}

for d in lowestDistances:
    try:
        types[d.toType] = types[d.toType] + 1
    except:
        types[d.toType] = 1 #the key didn't exist yet, so add the key and set it to 1 to add the value

mostCommonType = max(types, key=types.get) #get the most common type using the inbuilt max function
print(mostCommonType)









