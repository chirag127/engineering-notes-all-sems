A network planning model is a graphical representation of the activities and events involved in a software project. It shows the sequence, duration, and dependencies of the tasks required to complete the project. It is used to plan, monitor, and control the project progress and resources.

There are different types of network planning models, such as activity-on-node, activity-on-arrow, Gantt chart, PERT, and CPM. One of the most common network planning models is the activity-on-node model, which uses nodes (boxes) to represent the activities and arrows to represent the dependencies. The following diagram illustrates the basic architecture of an activity-on-node network planning model:

```
+----------------+     +----------------+     +----------------+
| Activity A     |     | Activity B     |     | Activity C     |
| Duration: 5    |---->| Duration: 3    |---->| Duration: 4    |
| Start: 0       |     | Start: 5       |     | Start: 8       |
| Finish: 5      |     | Finish: 8      |     | Finish: 12     |
+----------------+     +----------------+     +----------------+
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
       |                     +---------------------+
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
       +---------------------+                     |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       +-------------------------------------------+
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
       |                                           |
+----------------+     +----------------+     +----------------+
| Activity D     |     | Activity E     |     | Activity F     |
| Duration: 6    |---->| Duration: 2    |---->| Duration: 7    |
| Start: 5       |     | Start: 11      |     | Start: 13      |
| Finish: 11     |     | Finish: 13     |     | Finish: 20     |
+----------------+     +----------------+     +----------------+
```

The diagram shows six activities (A, B, C, D, E, F) and their durations, start times, and finish times. The arrows indicate the dependencies between the activities, such as A must finish before B can start, and B and C must finish before E can start. The diagram can be used to identify the critical path, which is the longest path of activities that determines the minimum time to complete the project. In this case, the critical path is A-B-C-F, with a total duration of 20. The diagram can also be used to calculate the slack time, which is the amount of time an activity can be delayed without affecting the project completion time. For example, activity D has a slack time of 9, which means it can be delayed by up to 9 time units without affecting the project duration.