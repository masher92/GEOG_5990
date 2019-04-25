###### Model script for running ABM

# Import packages
import random

## Agent 1
# Set up variables as random points within a 100x100 grid.
y0 = random.randint(0,99)
x0 = random.randint(0,99)
# Check whether variables assigned correctly
print(y0, x0)

# Random-walk one step. 
# Y variable
if random.random() < 0.5:
    y0 += 1 # this means y0 = y0 +1
else :
    y0 -= 1# this means y0 = y0 -1    
    
# X variable
if random.random() < 0.5:
    x0 += 1 # this means y0 = y0 +1
else :
    x0 -= 1# this means y0 = y0 -1   
    
print(y0, x0)    

# Random-walk another step. 
# Y variable
if random.random() < 0.5:
    y0 += 1 # this means y0 = y0 +1
else :
    y0 -= 1# this means y0 = y0 -1    
    
# X variable
if random.random() < 0.5:
    x0 += 1 # this means y0 = y0 +1
else :
    x0 -= 1# this means y0 = y0 -1  
    
## Agent 2
# Set up variables as random points within a 100x100 grid.
y1 = random.randint(0,99)
x1 = random.randint(0,99)
# Check whether variables assigned correctly
print(y1, x1)

# Random-walk one step. 
# Y variable
if random.random() < 0.5:
    y1 += 1 # this means y0 = y0 +1
else :
    y1 -= 1# this means y0 = y0 -1    
    
# X variable
if random.random() < 0.5:
    x1 += 1 # this means y0 = y0 +1
else :
    x1 -= 1# this means y0 = y0 -1   
    
print(y1, x1)    

# Random-walk another step. 
# Y variable
if random.random() < 0.5:
    y1 += 1 # this means y0 = y0 +1
else :
    y1 -= 1# this means y0 = y0 -1    
    
# X variable
if random.random() < 0.5:
    x1 += 1 # this means y0 = y0 +1
else :
    x1 -= 1# this means y0 = y0 -1      
    
### Calculate the distance between the 2 agents
distance = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5 

