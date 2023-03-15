# Network Planning Models in SPM

- Network planning models are used to plan and manage software projects by using graphical representations of activities and events.
- They help to visualize the sequence, duration, order, and dependencies of tasks necessary to complete the project.
- They also help to estimate the project cost, time, and resources, and to identify the critical path and the risks involved.
- There are two main types of network planning models: activity-on-node (AON) and activity-on-arrow (AOA).
- In AON, the activities are represented by nodes (boxes) and the dependencies are represented by arrows (lines) between the nodes.
- In AOA, the activities are represented by arrows and the nodes represent the start and end points of the activities.
- Both AON and AOA use the same notation to indicate the activity name, duration, and slack time.
- The activity name is written above the node or arrow, the duration is written below the node or arrow, and the slack time is written in brackets next to the node or arrow.
- The slack time is the amount of time that an activity can be delayed without affecting the project completion time.
- The critical path is the longest path of activities in the network, which determines the minimum project completion time.
- The activities on the critical path have zero slack time and are called critical activities.
- Any delay in a critical activity will delay the whole project.
- The critical path can be identified by using the forward pass and backward pass methods, which calculate the earliest start time (EST), earliest finish time (EFT), latest start time (LST), and latest finish time (LFT) of each activity.
- The EST and EFT are calculated by adding the activity duration to the maximum of the EFTs of the preceding activities.
- The LST and LFT are calculated by subtracting the activity duration from the minimum of the LSTs of the succeeding activities.
- The slack time is then calculated by subtracting the EST from the LST or the EFT from the LFT.
- The critical path is the path of activities that have zero slack time.
- An example of a network planning model using AON notation is shown below:

![AON example](https://www.gristprojectmanagement.us/software-2/images/fig-6-1.jpg)

- The critical path is A-B-D-E-F-G, with a total duration of 28 days.
- The slack time of each activity is shown in brackets next to the node.
- For example, activity C has a slack time of 4 days, which means it can be delayed by up to 4 days without affecting the project completion time.