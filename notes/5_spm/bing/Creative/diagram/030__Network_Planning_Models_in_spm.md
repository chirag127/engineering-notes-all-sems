A network planning model in software project management is a model that uses graphical representations of activities and events to visualize the sequence of tasks necessary to complete the project. It is used to identify the duration, order of activities, and dependencies among tasks.

There are different ways to represent a network planning model, such as activity-on-arrow, activity-on-node, or precedence networks. In this response, I will use the activity-on-node approach, which represents the activities as nodes (boxes) and the lines between nodes represent the dependencies.

The following diagram illustrates the basic architecture of a network planning model in software project management:

```
+-----------------+    +-----------------+    +-----------------+
| Start           |    | Activity A      |    | Activity B      |
| (Node 1)        |----| (Node 2)        |----| (Node 3)        |
+-----------------+    +-----------------+    +-----------------+
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
+-----------------+    +-----------------+    +-----------------+
| Activity C      |    | Activity D      |    | Activity E      |
| (Node 4)        |----| (Node 5)        |----| (Node 6)        |
+-----------------+    +-----------------+    +-----------------+
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
                          |    |    |    |
+-----------------+    +-----------------+    +-----------------+
| Activity F      |    | Activity G      |    | End             |
| (Node 7)        |----| (Node 8)        |----| (Node 9)        |
+-----------------+    +-----------------+    +-----------------+
```

In this diagram, each node represents an activity that has a duration and a resource requirement. The lines between nodes represent the dependencies or precedence relationships between activities. For example, activity A must be completed before activity B can start, and activity B must be completed before activity C, D, and E can start. The start node (node 1) represents the point at which the project can start, and the end node (node 9) represents the point at which the project is completed.

The network planning model can be used to calculate the critical path, which is the longest path of activities from start to end, and the slack or float, which is the amount of time that an activity can be delayed without affecting the project completion date. The network planning model can also be used to perform risk analysis, resource allocation, and cost estimation.