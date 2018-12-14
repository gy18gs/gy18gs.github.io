#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:01:59 2018

@author: Georgia
"""

"""
This is an agent based model running from a GUI in which there is a run menu.
On Windows desktop:
    When the code is run, a window will appear on your computer screen.
    To run the model, restart the kernel, find this window and select 'Run' from the menu bar
On Mac OSX:
    When the code is run, a python window titled 'Model' will appear
    To run the model, restart the kernel, select the 'Model' popup from the desktop
    Open the popup, and select 'Model' > 'Run model' from the independent menu bar
    
The model displays blue and red agents, moving in space and 'eating' the environment
"""


###############################################################
"""
Step 1:
    Importing functions.  
"""

import random
#import operator
import matplotlib

matplotlib.use('macosx')
# non-Mac operating systems use the below matplotlib.use functions
#matplotlib.use('TkInter')
#matplotlib.use('TkAgg')

import matplotlib.pyplot
import agentframework
import csv
#import sys
import matplotlib.animation
import tkinter
import requests
import bs4


###############################################################
"""
Step 2:
    Pulling data from the web.
    This scrapes a web page to get the starting locations for the agents.
"""

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs)


###############################################################
"""
Step 3:
    Creating the environment.
    The imported csv is raster data, with each value being equivalent to a pixel in an image, arranged in a grid.
        This raster grid is the environment in which the agents interact.
    
    The environment = [] is the empty container in which to put this raster environment
        The empty list 'rowlist = []' allows the data to be shifted into a 2D list
        This makes each row a new list in our environment, with each row filled with values
"""

environment = []

f = open("in.csv", newline = '')
reader = csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)
for row in reader:      #list of rows
    rowlist = []
    for value in row:       #list of value
        #print(value)        #floats
        rowlist.append(value)
    environment.append(rowlist) #list of values for the row added to total environment
    #in the loop for row in reader, not in loop for value in row
f.close()


###############################################################
"""
Step 4:
    Creating agents.
    
    Setting up a colour array:
        Red -- red is assigned to every value of an even number
        Blue -- blue is assigned to every value of an odd number.
        
"""

num_of_agents = 10
agents = []

neighbourhood = 20
num_of_iterations = 100

# set up colour array
colour = []

# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, i, x, y))
    #agents.append(agentframework.Agent(environment,agents,i))
    # Set up colour array
    if i%2 == 0:
        colour.append('red')
    else :
        colour.append('blue')
        
carry_on = True

###############################################################

"""
Step 5:
    Animate the agents and plotting them in the environment.
    
    Move the agents:
        Agents move, 'eat' the environment, and share their store with other agents in the neighbourhood.
        Agents are shuffled randomly after each iteration of the model.
            

"""

def update(frame_number):
# updates the display in the animation
    
    fig.clear() # clear the figure
    global carry_on
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
 
    # Move the agents
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood) # share store with other agents in the neighbourhood
        # remove comment to view agents
        #print(agents[i]._x,agents[i]._y)
        
    if random.random() < 0.1:
        carry_on = False
        #print("stopping condition")
        
    for i in range(num_of_agents):
        # Plot the agents
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y, color=colour[i])
    # Shuffle the agents randomly after each iteration of the model.
    random.shuffle(agents)
    

def gen_function(b = [0]):
    a = 0
    global carry_on # not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# returns control and waits next call.
        a = a + 1
        
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    #canvas.show()
    canvas.draw()

###############################################################
"""
Step 6:
    Initialise GUI window
        The GUI is set up using tkinter,
        this creates a window and a menu with a single menu item:
            Model > Run model
"""
# set up the figure and loop variables
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

root = tkinter.Tk() 
root.wm_title("Model")

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
# Note, in MacOSX this has an independent Menu bar from which to run the model

model_menu.entryconfig("Run model", state="disabled") 
# Until the user has chosen files, then:
model_menu.entryconfig("Run model", state="normal")

tkinter.mainloop()

###############################################################
"""
End of model.
"""
##############################################################    

        
        