import os
import random
import operator
import matplotlib.pyplot
import time
import csv
import sys

os.chdir("E:/Msc/Programming/Geog5590/Agent-Based-Model")
import agentframework

'''      
# Test connection to agent.framework
a = agentframework.Agent()
print(a.y, a.x)           
b = agentframework.Agent()
print(b.y, b.x)        
a.move()
print(a.y, a.x)
'''

           
# Read in the environment data (Raster)
f = open('E:/Msc/Programming/Geog5590/Agent-Based-Model/in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
environment = [] 
for row in reader:	# A list of rows
    rowlist = []
    for value in row:	# A list of value
        rowlist.append(value)
    environment.append(rowlist)        
f.close() # Don't close until you are done with the reader;
        # the data is read on request.        
                    
# Set up the number of agents, an array to store them and the number of iterations
# of agent coordinate movement that will be run.
        
# Set up so it can be run from the cmd as python model.py 10 100 20        
#num_of_agents = int(sys.argv[1])
#num_of_iterations = int(sys.argv[2])
#neighbourhood = int(sys.argv[3])

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

# Create an array to store the agents
agents = []

# Make the agents.
# Appended to each agent is the environment and a reference to the list of all other agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
    #agents.append(agentframework.Agent(agents))

# Move the agents
# Eat the environment
# Communicate with neighbours, find the closest neighbour and share resources with them.
for j in range(num_of_iterations):
    random.shuffle(agents)            
    for i in range(num_of_agents):
        agents[i].move()
        # Eat the environment
        agents[i].eat()
        # search for close neighbours, and share resources with them.
        agents[i].share_with_neighbours(neighbourhood)
        #print(i,j)

# Make plots
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

