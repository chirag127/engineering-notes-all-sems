# Network Planning Models in SPM

- Network planning models are used to plan and manage software projects by visualizing the sequence of tasks, their duration, and their dependencies.
- Network planning models can help to estimate the project completion time, identify the critical path, allocate resources, monitor progress, and handle uncertainties.
- There are two main types of network planning models: activity-on-node (AON) and activity-on-arrow (AOA).
- In AON, each node represents an activity and each arrow represents a dependency. The nodes can have attributes such as duration, start time, finish time, and slack.
- In AOA, each arrow represents an activity and each node represents an event. The arrows can have attributes such as duration, earliest start time, latest start time, earliest finish time, latest finish time, and float.
- AON and AOA can be converted to each other by using dummy activities or dummy events.
- There are two common methods for analyzing network planning models: CPM (Critical Path Method) and PERT (Program Evaluation and Review Technique).
- CPM assumes that the activity durations are deterministic and calculates the critical path, which is the longest path in the network and determines the minimum project completion time.
- PERT assumes that the activity durations are probabilistic and follows a beta distribution. It calculates the expected duration, variance, and standard deviation of each activity and the project. It also calculates the probability of completing the project within a given time.