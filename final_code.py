import highway_env
import numpy as np
import random
import gym
import highway_env
from matplotlib import pyplot as plt


#constants
alpha = 0.1
gamma = 0.9
epsilon = 1.0

env = gym.make('highway-v0')
env.configure({
    "observation": {
        "type": "LidarObservation",
        "vehicles_count": 15,
        "maximum_range" : 20,
        "cells" : 8,
    },
    "absolute": False,
    "action" : {
        "type" : "DiscreteMetaAction",
        "lateral" : True,
        "target_speed" :30
    }
})


def discretizeDistance(d):
    if(d>=0 and d<0.2):
        return 1
    elif(d>=0.2 and d<0.4):
        return 2
    elif(d>=0.4 and d<=1):
        return 0

def hashing(a,b,c,d,e): 
     return(a +(3*b)+(9*c)+(27*d)+(81*e))
     
def epsilon_greedy(hash ,epsilon):
    action = 0
    
    #explore:
    if np.random.uniform(0,1) < epsilon:
        action = random.choice([0,1,2])
        
    #greedy policy:
    else:
        t= max(q[hash])
        action = q[hash].index(t)
    return action
s =[]
q={}
ep = []
ep_rew =[]
avg_reward =0
avg_rew =[]

for episode in range(3000):
    obs=env.reset()
    currentState = [discretizeDistance(obs[0][0]), discretizeDistance(obs[1][0]), discretizeDistance(obs[2][0]), discretizeDistance(obs[6][0]), discretizeDistance(obs[7][0])]
    

    p= hashing(discretizeDistance(obs[0][0]), discretizeDistance(obs[1][0]), discretizeDistance(obs[2][0]), discretizeDistance(obs[6][0]), discretizeDistance(obs[7][0]))    
    
    ep_reward = 0
    epsilon = epsilon- (1/2000)
    #if currentState not in s:
        #s.append(currentState)
    if q.get(p) is None: 
        q[p]=[0.0,0.0,0.0]
        
    
   

    
    truncated = False
    while(not truncated):
        a1 = epsilon_greedy(p, epsilon)
        env.render()
        #if episode>2500:
         #  env.render()
        obs ,reward, truncated,info= env.step(a1)
        
        nextState = [discretizeDistance(obs[0][0]), discretizeDistance(obs[1][0]), discretizeDistance(obs[2][0]), discretizeDistance(obs[6][0]), discretizeDistance(obs[7][0])]
        r= hashing(discretizeDistance(obs[0][0]), discretizeDistance(obs[1][0]), discretizeDistance(obs[2][0]), discretizeDistance(obs[6][0]), discretizeDistance(obs[7][0]))    
    
    
        #if nextState not in s:
          #s.append(nextState) 
        if q.get(r) is  None :  
          q[r]=[0.0,0.0,0.0]


    
        
        a2 = epsilon_greedy(r, 0)


        q[p][a1]=  q[p][a1]+ alpha*(reward + gamma*(max(q[r]))-q[p][a1])

        #print(q)
        p=r
        currentState = nextState
        #a1 =a2
        #action1 =  epsilon_greedy(r, epsilon)
        ep_reward +=reward
        #plt.imshow(env.render(mode="rgb_array")) 
    avg_reward += ep_reward
    avg = avg_reward/(episode+1)
    avg_rew.append(avg)
   
    print(episode+1)
    print(ep_reward)
    print("running_avg=",avg)   
    #if(len(ep)%250==0):
     # plt.figure()
      #plt.plot(ep, ep_rew)
      #plt.show()   
    ep_rew.append(ep_reward)
    ep.append(episode+1)
plt.figure()
plt.plot(ep, ep_rew)
plt.plot(ep,avg_rew)
plt.show()
