# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 15:26:46 2018

@author: gy17m2a
"""

import agent

agents = []

agents.append(agent.Agent(1))
agents.append(agent.Agent(2))
agents.append(agent.Agent(3))
agents.append(agent.Agent(4))
agents.append(agent.Agent(5))
print(agents)

newagents = agents[:]
print(newagents)
newagents[0].hi()

agents[0].hi()
agents[0].setValue(2)
agents[0].hi()

newagents[0].hi()

'''
a = 
b = agent.Agent(1)
print(a.hi())
print(b.hi())

print(a == b)

a.value = b.value
print(a.hi())
print(a == b)
'''
