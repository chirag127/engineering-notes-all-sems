### Network Planning Models in spm

- Network planning models are used to plan and manage software projects by using graphical representations of activities and events.
- They help to visualize the sequence, duration, order, and dependencies of tasks necessary to complete the project.
- They also help to estimate the project completion time, identify the critical path, and allocate resources efficiently.
- There are two main types of network planning models: activity-on-node (AON) and activity-on-arrow (AOA).
- In AON, the activities are represented as nodes (boxes) and the lines between nodes represent the dependencies. The nodes may also show the activity name, duration, start time, and finish time.
- In AOA, the activities are represented as arrows joining circles (nodes), which show the start and completion time of the activities. The arrows may also show the activity name and duration.
- Both AON and AOA use the same notation to indicate the dependencies among activities: finish-to-start (FS), start-to-start (SS), finish-to-finish (FF), and start-to-finish (SF).
- A network planning model can be constructed by following these steps:
  - Identify the activities and their durations.
  - Identify the dependencies among activities and their types.
  - Draw the network diagram using either AON or AOA notation.
  - Calculate the earliest start time (ES), earliest finish time (EF), latest start time (LS), and latest finish time (LF) for each activity using the forward and backward pass methods.
  - Calculate the total float (TF) and free float (FF) for each activity using the formula: TF = LF - EF or LS - ES, and FF = ES of successor - EF of predecessor.
  - Identify the critical path, which is the longest path in the network diagram with zero float.
  - Identify the critical activities, which are the activities on the critical path.
  - Identify the slack activities, which are the activities with positive float.
  - Update the network diagram as the project progresses and changes occur.