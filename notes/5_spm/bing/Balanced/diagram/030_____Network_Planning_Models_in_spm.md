### Network Planning Models in spm

- Network planning models are used to visualize and analyze the sequence of tasks and events required to complete a software project.
- They help to identify the duration, order, and dependencies of activities, as well as the critical path and the slack time of the project.
- They can also be used to monitor and control the progress and performance of the project, and to handle uncertainties and risks.
- There are two main types of network planning models: activity-on-node (AON) and activity-on-arrow (AOA).
- In AON, the activities are represented by nodes (boxes) and the dependencies are represented by arrows (lines) between nodes.
- In AOA, the activities are represented by arrows and the nodes represent the start and end points of the activities.
- Both AON and AOA use the same notation to indicate the duration and the earliest and latest start and finish times of each activity.
- The duration of an activity is denoted by D, the earliest start time by ES, the earliest finish time by EF, the latest start time by LS, the latest finish time by LF, and the slack time by S.
- The slack time of an activity is the difference between its latest and earliest start or finish times. It indicates how much an activity can be delayed without affecting the project completion time.
- The critical path of a project is the longest path of activities from the start node to the end node. It determines the minimum time required to complete the project. Any delay in a critical activity will delay the project completion time.
- The critical activities are those that have zero slack time. They are marked by double lines in the network diagram.
- The following is an example of an AON network diagram for a software project:

![AON network diagram](https://www.gristprojectmanagement.us/software-2/images/fig-6-1.jpg)

- The following is an example of an AOA network diagram for the same project:

![AOA network diagram](https://www.gristprojectmanagement.us/software-2/images/fig-6-2.jpg)

- Both network diagrams show that the critical path of the project is A-B-C-D-E-F-G-H-I-J-K, with a total duration of 36 weeks.
- The slack time of each activity can be calculated by using the following formulas:

S = LS - ES = LF - EF

ES = max(EF of predecessors)

EF = ES + D

LS = min(LS of successors)

LF = LS - D

- For example, the slack time of activity L is:

S = LS - ES = LF - EF

S = 18 - 12 = 24 - 18

S = 6 weeks

- This means that activity L can be delayed by up to 6 weeks without affecting the project completion time.