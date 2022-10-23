This project was a part of Summer Intern Program at [IV Labs](https://www.ivlabs.in/), the AI and Robotics Community of VNIT.

This project focuses on making a model of Self Driving Vehicle using Tabular Reinforcement Learning Techniques.
# **Implementation**
&nbsp;&nbsp;&nbsp;&nbsp;
## State Space
1)16 angles out of which we picked up only 5 to reduce our state space .Took only front and side angles ignoring backward ones.
2)Discretized distances to reduce state space.
## Action Space
#### Discrete Meta Actions
The DiscreteMetaAction type adds a layer of speed and steering controllers on top of the continuous low-level control, so that the ego-vehicle can automatically follow the road at a desired velocity. Then, the available meta-actions consist in changing the target lane and speed that are used as setpoints for the low-level controllers.

The full corresponding action space is defined in ACTIONS_ALL

ACTIONS_ALL = {\
        0: 'LANE_LEFT',\
        1: 'IDLE',\
        2: 'LANE_RIGHT',\
        3: 'FASTER',\
        4: 'SLOWER'\
    }\
## Observation Space
We used lidar observation to measure relative distances of ego vehicle  from other vehicles.
