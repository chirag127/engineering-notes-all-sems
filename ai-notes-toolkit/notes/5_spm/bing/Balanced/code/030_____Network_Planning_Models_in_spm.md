### Network Planning Models in spm

- Network planning models are used to plan and manage software projects by using graphical representations of activities and events.
- They help to visualize the sequence, duration, order, and dependencies of tasks necessary to complete the project.
- They also help to identify the critical path, which is the longest sequence of tasks that determines the minimum time required to finish the project.
- There are two main types of network planning models: activity-on-node (AON) and activity-on-arrow (AOA).
- In AON, the activities are represented by nodes (boxes) and the dependencies are represented by arrows (lines) between nodes.
- In AOA, the activities are represented by arrows and the nodes represent the start and end points of the activities.
- Both AON and AOA use the same notation to indicate the duration and slack of each activity.
- Duration is the time required to complete an activity, and slack is the amount of time an activity can be delayed without affecting the project completion time.
- The duration and slack of each activity are calculated using the following formulas:

  - Earliest start time (ES) = maximum of the earliest finish times of all predecessor activities
  - Earliest finish time (EF) = ES + duration
  - Latest finish time (LF) = minimum of the latest start times of all successor activities
  - Latest start time (LS) = LF - duration
  - Slack = LF - EF = LS - ES

- The critical path is the sequence of activities with zero slack, meaning they cannot be delayed without delaying the project completion time.
- The critical path can be identified by tracing the activities with zero slack from the start node to the end node of the network.
- The critical path determines the project duration, which is equal to the earliest finish time of the end node.
- The network planning models can be used to perform various analyses, such as:

  - What-if analysis: to evaluate the impact of changes in the project scope, resources, or schedule on the project duration and cost.
  - Risk analysis: to identify and quantify the uncertainties and risks associated with the project activities and outcomes.
  - Resource allocation: to optimize the use of available resources (e.g. staff, equipment, materials) to complete the project within the time and budget constraints.
  - Performance measurement: to monitor and control the progress and performance of the project activities and deliverables.