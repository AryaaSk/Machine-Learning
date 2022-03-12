#Linear Regression, also just known as the line of best fit
class p:
    x: float
    y: float
    def __init__(self, x, y):
        self.x = x
        self.y = y

#I will be using data about students, checking the correlation between the study time and their GPA (American grading system)
#Using data from this: https://www.openintro.org/data/index.php?data=gpa_study_hours

#First get data
f = open("studentData.csv", "r")
studentData = f.readlines()
f.close()

del studentData[0] #this is the description line

points = [] #studyTime on X axis, gpa on Y axis
for line in studentData:
    lineData = line.split(",")
    studyTime = float(lineData[1])
    gpa = float(lineData[0])
    points.append(p(studyTime, gpa))

#points = [p(8, 3), p(2, 10), p(11, 3), p(6, 6), p(5, 8), p(4, 12), p(9, 4), p(1, 14), p(12, 2)] #sample data


#Calculate line of best fit:

#If you were doing this in real life, you would draw out a table with columns: | X | Y | XY | X^(2) |
#However you actually only need the totals/sums of these values, so we will just get those
totalX = 0
totalY = 0
totalXY = 0
totalX2 = 0
for point in points:
    XY = point.x * point.y
    X2 = point.x ** 2

    totalX += point.x
    totalY += point.y
    totalXY += XY
    totalX2 += X2

#y = mx + c
#Equation for gradient -> m = ((n * totalXY) - (totalX * totalY)) / ((n * totalX2) - (totalX)^(2))
#n = number of points
n = len(points)
m = ((n * totalXY) - (totalX * totalY)) / ((n * totalX2) - (totalX ** 2))

#Equation for y-Intercept -> c = (totalY - (m * totalX)) / n
c = (totalY - (m * totalX)) / n


#Uncomment below lines if you want to see a graph
"""
#Plot graph and line
import matplotlib.pyplot as plt
import numpy as np

xPoints = []
yPoints = []
for point in points:
    xPoints.append(point.x)
    yPoints.append(point.y)

plt.scatter(xPoints, yPoints, color="blue")

#get largest X in dataset
largestX = 0
for point in points:
    if point.x > largestX:
        largestX = point.x
x = np.linspace(0, largestX) # constructs a numpy array of [0.0, 1.0, ... 10.0]
plt.plot(x, m*x+c, color="purple") 

plt.show()
"""

#Testing data:
#Just removed a row from the data and using it to test: 3.4,20
testData = "3.7,10"
lineData = testData.split(",")
studyTime = float(lineData[1])
gpa = float(lineData[0])

#if we want to estimate the student's GPA based on the study time, then we substitute the X for studyTime in y = mx + c, since the X axis is studyTime, and the result will give us our estimate
estimatedGPA = (m * studyTime) + c
print(estimatedGPA) #gives us 3.5546738693005753

#or if we want to estimate the study time, we can do it the other way round
#so we need to rearrange the equation to give us x:
#y = mx + c
#mx = y - c
#x = (y - c) / m

estimatedStudyTime = (gpa - c) / m
print(estimatedStudyTime) #gives us 50.426806221436756

#One issue with this is that since the dataset is so varied, sometimes if the GPA is less than 3.5, it can give a negative study time, this is because the line of best fit starts at a GPA of 3.5.
#This is because the data is not very precise, and it is also why it is usually not a good idea to try and get the independant variable (study time) from the dependant variable (GPA)