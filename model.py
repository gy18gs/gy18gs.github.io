#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:14:04 2018

@author: Georgia
"""

import matplotlib.pyplot
import operator
import random

num_of_agents = 10
num_of_iterations = 100
agents = []

# Randomly assign agents
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
print(agents)

print(agents[0])
print(agents[0][0])
print(agents[0][1])
agents[0][1] = 50
print(agents[0])
print(agents[0][1])

# Randomly move all agents
for i in range(num_of_agents):
    if random.random() < 0.5:
        agents[i][0] = agents[i][0] + 1
    else:
        agents[i][0] = agents[i][0] - 1
    if random.random() < 0.5:
        agents[i][1] = agents[i][1] + 1
    else:
        agents[i][1] = agents[i][0] - 1
print(agents)

#answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
#print(answer)

print(max(agents))
print(max(agents, key=operator.itemgetter(0))) 
print(max(agents, key=operator.itemgetter(1))) 

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color='red')
matplotlib.pyplot.show()

