### Network Planning Models in spm

- Network planning models are used to plan and manage software projects by using graphical representations of activities and events.
- They help to visualize the sequence, duration, order, and dependencies of tasks necessary to complete the project.
- They also help to identify the critical path, which is the longest sequence of tasks that determines the minimum time required to finish the project.
- There are two main types of network planning models: activity-on-node (AON) and activity-on-arrow (AOA).
- In AON, the activities are represented by nodes (boxes) and the dependencies are represented by arrows (lines) between nodes.
- In AOA, the activities are represented by arrows and the nodes represent the start and end points of the activities.
- AON is more commonly used than AOA because it is easier to draw and modify, and it can handle complex dependencies better.
- An example of an AON network for a software project is shown below:

```
+------+    +------+    +------+
| A(5) |----| B(3) |----| C(4) |
+------+    +------+    +------+
   |            |            |
   |            |            |
   |            |            |
   |            |            |
   |            |            |
   |            |            |
   |            |            |
   |            |            |
   |            |            |
   |            |            |
   |            |            |
   |            |            |
   |            +------+    +------+
   |                   |----| D(2) |
   |                   +------+    +------+
   |                          |----| E(6) |
   |                          +------+    +------+
   |                                 |----| F(7) |
   |                                 +------+    +------+
   |                                        |----| G(8) |
   |                                        +------+    +------+
   |                                               |----| H(9) |
   |                                               +------+    +------+
   |                                                      |----| I(10)|
   +------------------------------------------------------+    +------+
```

- The numbers in parentheses indicate the duration of each activity in days.
- The critical path is A-B-C-D-E-F-G-H-I, which has a total duration of 54 days.
- A mnemonic to remember the steps of network planning is: **DAD** (Draw, Analyze, Develop).
  - Draw the network diagram using AON or AOA notation.
  - Analyze the network to find the critical path and the slack time for each activity.
  - Develop the project schedule based on the network analysis and the available resources.