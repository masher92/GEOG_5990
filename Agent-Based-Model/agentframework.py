import random

class Agent():
        
    def __init__(self, environment, agents):
        self.environment = environment
        self.agents = agents
        self.store = 0 # We'll come to this in a second.
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
    
    def hi(self):
        print("hello world")    

    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x= (self.x - 1) % 100
    
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        
    def distance_between (self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
        
    def share_with_neighbours(self, neighbourhood): 
        for agent in self.agents :
            # Do not calculate the distance between an agent and itsself
            if agent is not self:
                dist = self.distance_between(agent)
                if dist <= neighbourhood:
                    average = (self.store + agent.store)/2
                    self.store = average
                    agent.store = average
                   # print("sharing " + str(dist) + " " + str(average))
                
                
        

            
