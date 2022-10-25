# **Self Driving Vehicle**
This project was a part of Summer Intern Program at [IV Labs](https://www.ivlabs.in/), the AI and Robotics Community of VNIT.

This project focuses on making a model of Self Driving Vehicle using Tabular Reinforcement Learning Techniques.
# **Description**
Make a Reinforcement Learning (RL) Model which can drive a car without any external assistance (i.e. Learning from its own experience).







# **Graphs**

![](https://i.imgur.com/pvKLUIF.jpg)

# **Implementation**
&nbsp;&nbsp;&nbsp;&nbsp;
## State Space
1)16 angles out of which we picked up only 5 to reduce our state space .Took only front and side angles ignoring backward ones.

2)Discretized distances by 0.2 to reduce state space using if  statements.\
  if(d>=0 and d<0.2):\
        return 1\
    elif(d>=0.2 and d<0.4):\
        return 2\
    elif(d>=0.4 and d<=1):\
        return 0

* ### Observation Space
We used LiDar observation to measure relative distances of ego vehicle from other vehicles. In this method we don't need separate x,y coordinates and velocities are also not required thus,reducing the state space .Also,this method gives accurate and consistent results.
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
Q learning \
It is an off policy learning method of action values Q(s,a) in which we allow both behaviour and target policies to improve greedily.

## Environment
env =gym.make('highway-v0')
## Reward 
'collision_reward': -1\
'lane_change_reward': 0\
'right_lane_reward': 0.1\
'high_speed_reward': 0.4\
'reward_speed_range': [20, 30]\
Out of these 5 rewards which are defined we used only first 3 rewards in our code.


# **Dependencies**
***
* pip
* gym
* matplotlib
# **Installation**
***
* Clone this repository
* Navigate to the cloned repository
* Run command $ pip install -e ./
