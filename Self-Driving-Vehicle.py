import highway_env
import numpy as np
import random
import gym
import highway_env
from matplotlib import pyplot as plt


#constants
alpha = 0.5
gamma = 0.9
epsilon = 1
f=open('Qvalue','w')
env = gym.make('highway-v0')
env.configure({
    "observation": {
        "type": "LidarObservation",
        "vehicles_count": 15,
    },
    "absolute": False
})

obs = env.reset()

def discretizeDistance(d):
    if(d>=0 and d<0.33):
        return 0
    elif(d>=0.33 and d<0.67):
        return 1
    elif(d>=0.67 and d<=1):
        return 2

def hashing(a,b,c,d,e):
     return(a +(3*b)+(9*c)+(27*d)+(81*e))
     
def epsilon_greedy(hash ,epsilon):
    action = 0
    
    #explore:
    if np.random.uniform(0,1) < epsilon:
        action = random.choice([0,1,2,3,4])
        
    #greedy policy:
    else:
        t= max(q[hash])
        action = q[hash].index(t)
    return action
s =[]
q={}
ep = []
ep_rew =[]

e=1
for episode in range(3000):
    env.reset()
    currentState = [discretizeDistance(obs[0][0]), discretizeDistance(obs[2][0]), discretizeDistance(obs[4][0]), discretizeDistance(obs[12][0]), discretizeDistance(obs[14][0])]
    

    p= hashing(discretizeDistance(obs[0][0]), discretizeDistance(obs[2][0]), discretizeDistance(obs[4][0]), discretizeDistance(obs[12][0]), discretizeDistance(obs[14][0]))    
    
    ep_reward = 0
    epsilon = epsilon- 0.0005
    #if currentState not in s:
        #s.append(currentState)
    if q.get(p) is None: 
        q[p]=[0.0,0.0,0.0,0.0,0.0]
        
    
   

    t=0
    truncated = False
    f.write('Epsiode'+str(e))
    f.write('\n')
    while(not truncated):
        a1 = epsilon_greedy(p, epsilon)
        #env.render()
        obs ,reward, truncated,info= env.step(a1)
        
        nextState = [discretizeDistance(obs[0][0]), discretizeDistance(obs[2][0]), discretizeDistance(obs[4][0]), discretizeDistance(obs[12][0]), discretizeDistance(obs[14][0])]
        r= hashing(discretizeDistance(obs[0][0]), discretizeDistance(obs[2][0]), discretizeDistance(obs[4][0]), discretizeDistance(obs[12][0]), discretizeDistance(obs[14][0]))    
    
    
        #if nextState not in s:
          #s.append(nextState) 
        if q.get(r) is  None :  
          q[r]=[0.0,0.0,0.0,0.0,0.0]


    
        
        a2 = epsilon_greedy(r, 0)


        q[p][a1]=  q[p][a1]+ alpha*(reward + gamma*(max(q[r]))-q[p][a1])
        t=q[p][a1]
        
        for i in range (a1):
            f.write(str(q[p][i]))
            f.write('\n')
        #print(q)
        p=r
        currentState = nextState
        #a1 =a2
        #action1 =  epsilon_greedy(r, epsilon)
        ep_reward +=reward
        #plt.imshow(env.render(mode="rgb_array")) 
    print(episode)
    print(ep_reward) 
    ep_rew.append(ep_reward)
    ep.append(episode)
#plt.figure()
    e=e+1
    if len(ep)%100==0:
        plt.plot(ep, ep_rew)
        plt.show()
        #f.write(ep)
        #f.write(plt.plot(ep,ep_rew))
f.close()