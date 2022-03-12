#NEED TO COME BACK TO THIS SINCE I THINK THE ALGORITHM IS BROKEN

#Linear Regression, also just known as the line of best fit
#Will just create my own sample data, but this is very easy to think of use-cases, such as finding the correlation between 2 properties

class p:
    x: float
    y: float
    def __init__(self, x, y):
        self.x = x
        self.y = y

points = [p(8, 3), p(2, 10), p(11, 3), p(6, 6), p(5, 8), p(4, 12), p(9, 4), p(1, 14), p(12, 2)] #sample data

#calculate line of best fit:

#Create 2D array to represent grid table
#Table Columns are: X | Y | XY | X^(2)
table = []
totals = [] #the last row, the totals

def printTable():
    print(["X", "Y", "XY", "X^(2)"])
    for row in table:
        print(row)
    print(f"Totals: {totals}")

totalX = 0
totalY = 0
totalXY = 0
totalX2 = 0
for point in points:
    XY = point.x * point.y
    X2 = point.x ** 2
    table.append([point.x, point.y, XY, X2])
    totalX += point.x
    totalY += point.y
    totalXY += XY
    totalX2 += X2

totals = [totalX, totalY, totalXY, totalX2]

#y = mx + c
#Equation for gradient -> m = ((n * totalXY) - (totalX * totalY)) / ((n * totalX2) - (totalX)^(2))
#n = number of points
n = len(points)
m = ((n * totalXY) - (totalX * totalY)) / ((n * totalX2) - (totalX ** 2))

#Equation for y-Intercept -> c = (totalY - (m * totalX)) / n
c = (totalY - (m * totalX)) / n


#Plot graph and line
import matplotlib.pyplot as plt
import numpy as np

xPoints = []
yPoints = []
for point in points:
    xPoints.append(point.x)
    yPoints.append(point.y)

plt.scatter(xPoints, yPoints, color="purple")

#get largest X in dataset
largestX = 0
for point in points:
    if point.x > largestX:
        largestX = point.x
x = np.linspace(0, largestX) # constructs a numpy array of [0.0, 1.0, ... 10.0]
plt.plot(x, m*x+c, color="purple") 

plt.show()
