This project was a part of Summer Intern Program at [IV Labs](https://www.ivlabs.in/), the AI and Robotics Community of VNIT.

This project focuses on making a model of Self Driving Vehicle using Tabular Reinforcement Learning Techniques.
# **Description**
Make a Reinforcement Learning (RL) Model which can drive a car without any external assistance (i.e. Learning from its own experience).

![highway](https://user-images.githubusercontent.com/102024497/197385400-43e11f8e-a46b-4058-a8f9-c68c31dedc6b.gif)

# **Implementation**
&nbsp;&nbsp;&nbsp;&nbsp;
## State Space
1)16 angles out of which we picked up only 5 to reduce our state space .Took only front and side angles ignoring backward ones.\
2)Discretized distances to reduce state space.
## Action Space
#### Discrete Meta Actions
The available meta-actions consist in changing the target lane.

The full corresponding action space is defined in ACTIONS_ALL

ACTIONS_ALL = {\
        0: 'LANE_LEFT',\
        1: 'IDLE',\
        2: 'LANE_RIGHT',\
    }
## Observation Space
We used lidar observation to measure relative distances of ego vehicle  from other vehicles.
## Method Used
Q learning \
One of the strengths of Q-Learning is that it is able to compare the expected utility of the available actions without requiring a model of the environment. Reinforcement Learning is an approach where the agent needs no teacher to learn how to solve a problem.
# **Environment**
env =gym.make('highway-v0')
