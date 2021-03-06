---
title: Test
---


# Hello World...

### ... and welcome to my website!

---

## *Who am I?*
#### I'm Georgia Scott, a GIS Master's student at the University of Leeds, and a Lancaster University Geography graduate.
#### I'm undertaking an introductory programming module, 'GEOG5990 Programming for Spatial Analysts: Core Skills'

---

## *What is this website for?*
#### This website is an online portfolio for my introductory programming module, GEOG5990.

#### The files provided for the GEOG5990 Assessment 1 are:
* #### **license.txt**
* #### **agentframework.py**
* #### **agents.py**
* #### **in.csv** (this is the environment for the model)
* #### and index2.md (hand-coded markdown)

##### These can be accessed through the 'View on GitHub' link at the top of this webpage.

---

## *So, what is the model?*
### The model is an agent-based model, which contains 3 basic elements:
### >**Model** code:
#### Which sets up the model, interacts with the user, and runs the model iterations and checks the stopping conditions.
### >**Environment** code:
#### Which represents the 'world' in which agents interact. This contains data as well as constraint the space and topology the agents can exist within -- *the **environment** is from an imported CSV of raster data, with each value being equivalent to a pixel in an image, arranged in a grid - this is where the agents interact.*
### >**Agent** code: 
#### Which builds agents, defines their behaviour, and any records of their state. Agents often have behaviours based around what is happening in the neighbourhood in which they are contained. Each agent will contain a list of all the other agents, so that agents can communicate with each other.
#### The **agent framework** holds a basic agent class to support the agents model, the agents are stored in a **2D raster environment**, and this environment is shared with all other agents in the model -- *the **agent framework** tells the agents how to interact with each other within the **neighbourhood**.*
#### The **neighbourhood** has a radius of 20:
##### -- if an agent is in the neighbourhood radius, the stores can be **shared** - you add the sum of the agent store and the self store, this is made to an average and split evenly between the two
##### -- if the distance between self and agent exceeds 20, **no sharing takes place** as the agent is not in the neighbourhood.


---
## *Running the model*
### *How do I run the model?*
#### This agent based model runs from a GUI in which there is a run menu. To run the model:
#### 1. Make sure that under \Tools\ > \Preferences\ > IPython console > the 'Graphics backend' is set to **Tkinter**
#### 2. Clear/restart the kernel
#### 3. Select the 'Model' popup from your desktop
[<img src="https://github.com/gy18gs/gy18gs.github.io/blob/master/Desktop.png">](https://github.com/gy18gs/gy18gs.github.io/blob/master/Desktop.png)
#### 4. Select 'Model' > 'Run model' from the menu bar.
[<img src="https://github.com/gy18gs/gy18gs.github.io/blob/master/Model_popup.png">](https://github.com/gy18gs/gy18gs.github.io/blob/master/Model_popup.png)
#### This will then run the model, after a few moments, it will look like this below:
[<img src="https://github.com/gy18gs/gy18gs.github.io/blob/master/Model.png">](https://github.com/gy18gs/gy18gs.github.io/blob/master/Model.png)
## *
### *What can I expect when I run the model?*
#### The model displays **blue and red agents**, moving in space and 'eating' the 2D raster environment. *The agents are set up to be coloured red when they represent an even number, and blue when they represent an odd number.*
#### The starting location of the agents is determined from a web source, so the starting locations are always the same. However, the agents are shuffled randomly after each iteration of the model. *This ensures that the sharing of the agent stores doesn't favour one agent over another.*
#### As the model is run, the IPython console displays: the **distance between the agents** and the **store value.**

---
### *Any issues when creating the model?*
##### In future versions of this model, I would hope to be able to write code that prevent the 'Figure 1' popup from appearing alongside the 'Model' popup. At the moment, the 'Figure 1' does nothing and is harmless, however, ideally only the Model popup would appear when the code is run!
##### Also, ideally the agents would be set as either red or blue, and remain as the same colour throughout the duration the model is run.

---
## *Thank you for visiting my website.*



