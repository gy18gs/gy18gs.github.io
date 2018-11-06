#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 11:23:24 2018

@author: Georgia
"""

import random
import operator
import matplotlib.pyplot
import time

start = time.perf_counter()

# The code to run, here.

end = time.perf_counter()

print("time = " + str(end - start))


def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
    
num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
for j in range(num_of_iterations):
        for i in range(num_of_agents):

            if random.random() < 0.5:
                agents[i][0] = (agents[i][0] + 1) % 100
            else:
                agents[i][0] = (agents[i][0] - 1) % 100

            if random.random() < 0.5:
                agents[i][1] = (agents[i][1] + 1) % 100
            else:
                agents[i][1] = (agents[i][1] - 1) % 100


answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
#print(answer)


matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

distance = distance_between(agents[0], agents[1])
#print(distance)

#finding maximum distances between agents
#new list is distances = []
distances = []

for i in range(num_of_agents):
    for j in range(num_of_agents):
        distance = distance_between(agents[i],agents[j])
        print (i,j,distance)
        distances.append(distance)
        
print (max(distances))

#finding minimum distances between agents
#need new list of distances, otherwise will call from the previous distance list
#i+1 avoids repeating with the first agent i.e. distances between 1 and 1 is 0
distances = []

for i in range(num_of_agents):
    for j in range(i+1, num_of_agents):
        distance = distance_between(agents[i],agents[j])
        print (i,j,distance)
        distances.append(distance)

print (min(distances))






