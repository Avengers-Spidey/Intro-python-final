import matplotlib.pyplot as plt
import csv

x_all = []
y_all = []
x = []
y = []

data_x = open('/Users/sreyapt/Documents/GitHub/Intro-python-final/dataX.csv')
data_y = open('/Users/sreyapt/Documents/GitHub/Intro-python-final/dataY.csv')

x_reader = csv.reader(data_x)
count = 0;
for row in x_reader:
   if ('X values of sin' in row ):
       continue
   for field in row:
       x_all.append(float(field))
       if (count < 251):
           x.append(float(field))
           count +=1

y_reader = csv.reader(data_y)
count = 0;
for row in y_reader:
   if ('Y values of sin' in row ):
       continue
   for field in row:
       y_all.append(float(field))
       if (count <251):
           y.append(float(field))
           count += 1

area = 0.0
delta = x[1]-x[0]
for i in range(250):
   area += y[i]*delta

plt.plot(x_all, y_all)
plt.fill_between(x, y)
plt.text(0.25, 0, "area = " + str(area))
plt.show()

