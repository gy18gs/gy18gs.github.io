#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:08:42 2018

@author: Georgia
"""
############################################################### 
"""
This agent framework holds a basic agent class to support the agents model.
The agents in the model are held within a 2D raster environment.
The environment is shared with all other agents in the model, who interact within this environment.
"""

import random

class Agent():
    def __init__ (self,environment,agents,id,x,y):
        
        """
        Positional arguments:
            environment -- the raster environment to be shared with all agents
            agents -- refers to all agents in the environment
            x -- the x axis locational coordinate for this agent
            y -- the y axis locational coordinate for this agent

        X and Y values:
            Instead of setting x and y as commented out below, you are
            passing in x and y from the web file.
            
            The below (x/y = None) ensures that the model will still run
            even if the x and y values exceed those given in the web file.
        """
        
        if (x == None):
            self._x = random.randint(0,100)
        else:
           self._x = x
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = x   

        #self._x = random.randint(0,99)
        #self._y = random.randint(0,99)            
        self.environment = environment
        self.agents = agents
        self.store = 0
        #self._x = x
        #self._y = y
        self.id = id #this assigns an ID to each agent

############################################################### 
   
    """
    Returns:
        A description of the agent's location and store.

    """    
        
    def __str__(self):
        return " x " + str(self._x) + " y " + str(self._y)
    
    
    """
    This moves the agent randomly in 2D space.
    """
    
    
    def move (self):
        if random.random() < 0.5:
            self._y = self._y + 1
        else:
            self._y = self._y - 1
        if random.random() < 0.5:
            self._x = self._x + 1
        else:
            self._x = self._x - 1
         
            
    def eat(self): #can you make it eat what is left?
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
    
    
    """
    Self and neighbourhoods are arguments.
    Self is looking at all the agents
        -- agents are brought from the outside world (the web source)
    For each agent, you calculate the distance between agent and self.
    
    Positional argument:
        neighbourhood -- neighbourhood value of 20.
    
    If the distance between self and agent is 20:
        -- agent is in the neighbourhood radius, therefore the stores can be shared
        --- you add the sum of the agent store and self store
        ---- this is then made to an average and split evenly between the two
        
    If the distance between self and agent exceeds 20:
        -- no sharing takes place, as agent is not in the neighbourhood
    """
    
    
    def share_with_neighbours(self,neighbourhood):
        for agent in self.agents:
            if agent != self: #prevents agent from sharing with itself
                dist = self.distance_between(agent)
                if dist <= neighbourhood:
                    sum = self.store + agent.store
                    ave = sum /2
                    self.store = ave
                    agent.store = ave
                    # prints the distance between agents and the store
                    print(str(dist) + " " + str(ave))
    
    
    """
    Calculate and returns the distance between 'self' and 'agent'.
    
    Positional agruments:
        agent -- an instance of this agent class
    
    Returns:
        The distance between self and agent.
    
    """
    
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
    
    
    
    
    
    
            
            

            