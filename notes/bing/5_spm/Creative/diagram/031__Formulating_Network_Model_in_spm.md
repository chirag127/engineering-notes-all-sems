A network model is a graphical representation of the activities and their interrelationships in a project. In software project management (SPM), a network model can help to plan, schedule, monitor and control the project activities. There are different ways to formulate a network model, such as activity-on-node (AON), activity-on-arrow (AOA), or precedence diagramming method (PDM).

One of the most common methods is the activity-on-node (AON) approach, where each node (box) represents an activity and each edge (line) represents a dependency between activities. The edges can have different types of dependencies, such as finish-to-start (FS), start-to-start (SS), finish-to-finish (FF), or start-to-finish (SF). The edges can also have different attributes, such as duration, cost, or resource requirements.

The following diagram illustrates the basic architecture of an AON network model in SPM:

```
+-----------------+     +-----------------+     +-----------------+
| Activity A      |     | Activity B      |     | Activity C      |
| Duration: 5 days|     | Duration: 3 days|     | Duration: 4 days|
| Cost: $1000     |     | Cost: $500      |     | Cost: $800      |
| Resource: X     |     | Resource: Y     |     | Resource: Z     |
+-----------------+     +-----------------+     +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         +---------------------+---------------------+
         | FS                  | FS                  |
         | Lag: 2 days         | Lag: 1 day          |
         |                     |                     |
         v                     v                     v
+-----------------+     +-----------------+     +-----------------+
| Activity D      |     | Activity E      |     | Activity F      |
| Duration: 6 days|     | Duration: 4 days|     | Duration: 7 days|
| Cost: $1200     |     | Cost: $600      |     | Cost: $900      |
| Resource: X     |     | Resource: Y     |     | Resource: Z     |
+-----------------+     +-----------------+     +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         +---------------------+---------------------+
         | FF                  | FF                  |
         | Lag: 0 days         | Lag: 0 days         |
         |                     |                     |
         v                     v                     v
+-----------------+
| Activity G      |
| Duration: 8 days|
| Cost: $1500     |
| Resource: X     |
+-----------------+
```

In this diagram, each activity has a duration, a cost, and a resource requirement. The dependencies between activities are shown by the edges, with the type and the lag of each dependency. For example, activity A must finish before activity D can start, with a lag of 2 days. This means that activity D cannot start until 2 days after activity A finishes. Similarly, activity D and activity E must finish before activity G can start, with no lag. This means that activity G can start as soon as both activity D and activity E finish.

A network model can help to identify the critical path, the slack time, the earliest and latest start and finish times, and the total project duration and cost. It can also help to optimize the resource allocation, the risk management, and the quality assurance of the project. A network model is a useful tool for SPM, but it also has some limitations, such as the uncertainty of the activity durations, the complexity of the network, and the need for constant updating and monitoring.