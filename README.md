> # **Self Driving Vehicle**
This project focuses on making a model of Self Driving Vehicle using Tabular Reinforcement Learning Techniques.
# **Description**
Make a Reinforcement Learning (RL) Model for highway environment using Q learning.



![TLSKXgR](https://user-images.githubusercontent.com/102024497/222049309-0b7e8fe0-dd52-4634-a1c7-3d97e0722c36.gif)



# **Implementation**
&nbsp;&nbsp;&nbsp;&nbsp;
## Observation Space
We used LiDar observation to measure relative distances of ego vehicle from other vehicles. In this method we don't need separate x,y coordinates and velocities are also not required thus,reducing the state space .Also,this method gives accurate and consistent results.
## State Space
All possible states of our environment includes relative distances between ego vehicle and other vehicles and angles or directions where other vehicles are present.This makes our state space too large so to reduce it we :\
1)Took 16 angles out of which we picked up only 5 to reduce our state space .Took only front and side angles ignoring backward ones as while driving our priority is to avoid collision of our agent car from the ones infront of it.\
2)Discretized distances by 0.2 to reduce state space .This step is necessary as it is difficult to work on continuous state space (large state space).

 
## Action Space
#### Discrete Meta Actions

The full corresponding action space is defined in ACTIONS_ALL

ACTIONS_ALL = {\
        0: 'LANE_LEFT',\
        1: 'IDLE',\
        2: 'LANE_RIGHT',\
        3: 'FASTER',\
        4: 'SLOWER'\
    }\
Out of the 5 available actions we trained our agent using 3 actions(LANE LEFT,IDLE,LANE RIGHT).We are planning to further extend the project using all  5 actions(i.e we will also invlove the role of velocities).

## Method Used
#### Q learning 
Q-learning is a model-free, off-policy reinforcement learning that will find the best course of action, given the current state of the agent.Model-free means that the agent uses predictions of the environment’s expected response to move forward. In the Q-Learning algorithm, the goal is to learn iteratively the optimal Q-value function using the Bellman Optimality Equation.

## Environment
env =gym.make('highway-v0')
## Reward 
'collision_reward': -1\
'lane_change_reward': 0\
'right_lane_reward': 0.1\
'high_speed_reward': 0.4\
'reward_speed_range': [20, 30]\
Out of these 5 rewards which are defined we used only first 3 rewards in our code.
# **Graphs**
#### Testing Graph For 300 Episodes
![image](https://github.com/Shreya62002/Self-Driving-Vehicle/assets/102024497/30204b03-6bb4-47e5-9f1b-aaf4a275a613)


![image](https://github.com/Shreya62002/Self-Driving-Vehicle/assets/102024497/9c7a671b-aa0b-4fde-9b70-c35a85d24866)


# **Dependencies**

* pip
* gym
* matplotlib
* NumPy
# **Installation**
* Clone this repository
* Navigate to the cloned repository
* Run command $ pip install -e ./

