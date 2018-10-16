#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:58:55 2018

@author: Georgia
"""

import matplotlib.pyplot
import random
data = []
processed_data = []


num_of_agents = 10
agents = []

#created agents
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
   # print (agents[i][0],agents[i][1])
print(agents)


# Fill with random data.
for i in (range(0,99)):
    datarow = []
    for j in (range(0,99)):
        datarow.append(random.randint(0,255))
    data.append(datarow)

# Blur.
for i in (range(1,98)):
    datarow = []
    for j in (range(1,98)):
        sum = data[i][j]
        sum += data[i-1][j]
        sum += data[i+1][j]
        sum += data[i][j+1]
        sum += data[i][j-1]
        sum /= 5
        datarow.append(sum)
    processed_data.append(datarow)
    

number_of_iterations = 10
for i in (range(1,number_of_iterations)):
    # Move agent.
    if random.random() < 0.5:
        agents[i][0] += 1
    else:
        agents[i][0] -= 1
        
    '''
    # Check if off edge and adjust.
    if agents[i][0] < 0:
        agents[i][0] = 0
    if agents[i][1] < 0:
        agents[i][0] = 0
    if agents[i][0] > 99:
        agents[i][0] = 99
    if agents[i][1] > 99:
        agents[i][0] = 99
    '''
    if random.random() < 0.5:
        agents[i][0] = (agents[i][0] + 1) % 100
    else:
        agents[i][0] = (agents[i][0] - 1) % 100


#matplotlib.pyplot.ylim(40, 50)
#matplotlib.pyplot.xlim(40, 50)
matplotlib.pyplot.ylim(2, 96)
matplotlib.pyplot.xlim(2, 96)
#matplotlib.pyplot.imshow(data)
#matplotlib.pyplot.show()
matplotlib.pyplot.imshow(processed_data)
#matplotlib.pyplot.show()

#matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
#matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()
