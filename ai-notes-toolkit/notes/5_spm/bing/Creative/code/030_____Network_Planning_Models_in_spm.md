### Network Planning Models in spm

- Network planning models are used to plan and manage software projects by using graphical representations of activities and events.
- They help to visualize the sequence, duration, order, and dependencies of tasks required to complete the project.
- They also help to estimate the project completion time, identify the critical path, and optimize the use of resources.
- There are two main types of network planning models: activity-on-node (AON) and activity-on-arrow (AOA).
- In AON, the activities are represented by nodes (boxes) and the dependencies are represented by arrows (lines) between the nodes.
- In AOA, the activities are represented by arrows (lines) and the events are represented by nodes (circles).
- AON is more commonly used than AOA because it is easier to draw and modify, and it can handle complex dependencies and dummy activities.
- An example of an AON network diagram is shown below:

```
  A
 / \
B   C
 \ /
  D
 / \
E   F
 \ /
  G
```

- In this diagram, there are seven activities (A, B, C, D, E, F, G) and six nodes (1, 2, 3, 4, 5, 6).
- The arrows indicate the precedence relationships between the activities. For example, activity A must be completed before activities B and C can start.
- The nodes indicate the start and finish points of the activities. For example, node 1 is the start point of activity A, and node 2 is the finish point of activity A and the start point of activities B and C.
- The duration of each activity can be written above or below the arrow or node. For example, activity A has a duration of 5 days.
- The network diagram can be used to calculate the earliest start time (EST), earliest finish time (EFT), latest start time (LST), latest finish time (LFT), and slack time (SL) of each activity.
- The EST and EFT of an activity are the earliest possible times that the activity can start and finish, respectively, given the dependencies and durations of the preceding activities.
- The LST and LFT of an activity are the latest possible times that the activity can start and finish, respectively, without delaying the project completion time.
- The SL of an activity is the amount of time that the activity can be delayed without affecting the project completion time. It is calculated by subtracting the EFT from the LFT, or the EST from the LST.
- The critical path is the longest path of activities in the network diagram that determines the project completion time. It is the path with zero slack time for all the activities.
- The critical path can be identified by tracing the activities with the same EST and LST, or the same EFT and LFT.
- In the example above, the critical path is A-B-D-E-G, with a project completion time of 20 days.
- The network planning model can be used to optimize the project schedule by reducing the duration or cost of the activities on the critical path, or by adding or removing dependencies between the activities.