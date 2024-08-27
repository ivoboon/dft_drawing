import csv
import math
import matplotlib.pyplot as plt
import numpy

totalPoints = int(10)
pointsList = [0]
xCoordinates_equal = []
yCoordinates_equal = []

xCoordinates = []
yCoordinates = []
pathLength = [0]
anX = []
bnX = []
anY = []
bnY = []

with open('star.csv', newline ='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        xCoordinates.append(float(row[0]))
        yCoordinates.append(float(row[1]))

for i in range(len(xCoordinates)-1):
    Length = math.sqrt(math.pow(xCoordinates[i+1]-xCoordinates[i],2)+math.pow(yCoordinates[i+1]-yCoordinates[i],2))
    pathLength.append(Length+pathLength[i])

for i in range(totalPoints):
    pointsList.append(pointsList[i]+pathLength[-1]/totalPoints)

xCoordinates_equal.append(xCoordinates[0])
yCoordinates_equal.append(yCoordinates[0])

for i in range(len(pointsList)-1):
    for j in range(len(pathLength)):
        if pathLength[j] >= pointsList[i+1]:
            aandeel = (pointsList[i+1]-pathLength[j-1])/(pathLength[j]-pathLength[j-1])
            xCoordinates_equal.append(xCoordinates[j-1]+(xCoordinates[j]-xCoordinates[j-1])*aandeel)
            yCoordinates_equal.append(yCoordinates[j-1]+(yCoordinates[j]-yCoordinates[j-1])*aandeel)
            break

if len(xCoordinates_equal) != len(pointsList):
    xCoordinates_equal.append(xCoordinates[-1])
    yCoordinates_equal.append(yCoordinates[-1])

xCoordinates = xCoordinates_equal
yCoordinates = yCoordinates_equal
pathLength = pointsList

a0X = float()
a0Y = float()

for i in range(len(xCoordinates)-1):
    a0X += ((xCoordinates[i+1]+xCoordinates[i])/2)*(pathLength[i+1]-pathLength[i])
    a0Y += ((yCoordinates[i+1]+yCoordinates[i])/2)*(pathLength[i+1]-pathLength[i])

for i in range(int((len(xCoordinates)-1)/2)):
    anXt = float()
    bnXt = float()
    anYt = float()
    bnYt = float()
    for j in range(len(xCoordinates)-1):
        anXt += ((xCoordinates[j+1]*math.cos(2*math.pi*(i+1)*pathLength[j+1]/pathLength[-1])+xCoordinates[j]*math.cos(2*math.pi*(i+1)*pathLength[j]/pathLength[-1]))/2)*(pathLength[j+1]-pathLength[j])
        bnXt += ((xCoordinates[j+1]*math.sin(2*math.pi*(i+1)*pathLength[j+1]/pathLength[-1])+xCoordinates[j]*math.sin(2*math.pi*(i+1)*pathLength[j]/pathLength[-1]))/2)*(pathLength[j+1]-pathLength[j])
        anYt += ((yCoordinates[j+1]*math.cos(2*math.pi*(i+1)*pathLength[j+1]/pathLength[-1])+yCoordinates[j]*math.cos(2*math.pi*(i+1)*pathLength[j]/pathLength[-1]))/2)*(pathLength[j+1]-pathLength[j])
        bnYt += ((yCoordinates[j+1]*math.sin(2*math.pi*(i+1)*pathLength[j+1]/pathLength[-1])+yCoordinates[j]*math.sin(2*math.pi*(i+1)*pathLength[j]/pathLength[-1]))/2)*(pathLength[j+1]-pathLength[j])
    anXt = 2*anXt/pathLength[-1]
    bnXt = 2*bnXt/pathLength[-1]
    anYt = 2*anYt/pathLength[-1]
    bnYt = 2*bnYt/pathLength[-1]
    anX.append(anXt)
    bnX.append(bnXt)
    anY.append(anYt)
    bnY.append(bnYt)
a0X = a0X/pathLength[-1]
a0Y = a0Y/pathLength[-1]

xFourier = []
yFourier = []
timeFourier = []
time = float(0)
dt = float(0.001)

while time < pathLength[-1]:
    timeFourier.append(time)
    xFourierTemp = a0X
    yFourierTemp = a0Y
    for i in range(len(anX)):
        xFourierTemp += anX[i]*math.cos(2*math.pi*(i+1)*time/pathLength[-1]) + bnX[i]*math.sin(2*math.pi*(i+1)*time/pathLength[-1])
        yFourierTemp += anY[i]*math.cos(2*math.pi*(i+1)*time/pathLength[-1]) + bnY[i]*math.sin(2*math.pi*(i+1)*time/pathLength[-1])
    xFourier.append(xFourierTemp)
    yFourier.append(yFourierTemp)
    time += dt

plt.subplot(3,1,1)
plt.plot(xCoordinates,yCoordinates)
plt.plot(xFourier,yFourier)
plt.axis('equal')
plt.subplot(3,1,2)
plt.plot(pathLength,xCoordinates)
plt.plot(timeFourier,xFourier)
plt.subplot(3,1,3)
plt.plot(pathLength,yCoordinates)
plt.plot(timeFourier,yFourier)
plt.show()