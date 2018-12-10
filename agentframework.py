#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:08:42 2018

@author: Georgia
"""

import random
class Agent():
    def __init__ (self,environment,agents,id):
        #random.seed(random_seed)
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)            
        self.environment = environment
        self.agents = agents
        self.store = 0
        self.id = id
#assign ID to each agent
#always have agent 1 as red
#        def __init__ (environment):
#            self.environment = environment
#            self.store = 0
        
    def __str__(self):
        return " x " + str(self._x) + " y " + str(self._y)
    
    def move (self):
        if random.random() < 0.5:
            self._y = self._y + 1
        else:
            self._y = self._y - 1
        if random.random() < 0.5:
            self._x = self._x + 1
        else:
            self._x = self._x - 1
            
    def eat(self): # can you make it eat what is left?
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
    '''
    self and neighbourhoods are arguments
    self is looking at all the agents, brought by the list
    brought from the outside world
    for each agent, you calculate the distance between agent and self
    if distance is less than 20, so in the neighbourhood, you can share
    if you're in the radius, you add the sum of their store and self store
    this is then made to an average and split evenly between the two
    if the distance between self and agent exceeds 20, no sharing takes place
    '''
    def share_with_neighbours(self,neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))
    
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
    
            
            

            