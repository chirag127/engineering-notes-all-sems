Forward pass and backward pass are techniques used in project management to calculate the duration and slack of each activity in a network diagram. They are also known as the two-pass technique.

The forward pass is the process of moving forward from the start node to the end node of the network diagram, and calculating the early start (ES) and early finish (EF) values for each activity. The ES is the earliest time an activity can start, and the EF is the earliest time an activity can finish. The EF is calculated by adding the activity duration to the ES.

The backward pass is the process of moving backward from the end node to the start node of the network diagram, and calculating the late start (LS) and late finish (LF) values for each activity. The LF is the latest time an activity can finish without delaying the project, and the LS is the latest time an activity can start without delaying the project. The LS is calculated by subtracting the activity duration from the LF.

The slack or float of an activity is the amount of time an activity can be delayed without affecting the project duration. It is calculated by subtracting the ES from the LS, or the EF from the LF. The critical path is the sequence of activities that has zero slack and determines the project duration.

The following diagram illustrates the basic steps of the forward pass and backward pass techniques in a network diagram with four activities (A, B, C, and D) and their durations (5, 4, 3, and 6 days respectively).

```
+-----+    +-----+    +-----+    +-----+
|     |    |     |    |     |    |     |
|  A  |    |  B  |    |  C  |    |  D  |
|     |    |     |    |     |    |     |
+-----+    +-----+    +-----+    +-----+
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          +----------+          |
  |                               |
  |                               |
  +-------------------------------+
```

Step 1: Perform the forward pass by moving from left to right and calculating the ES and EF values for each activity.

```
+-----+    +-----+    +-----+    +-----+
|     |    |     |    |     |    |     |
|  A  |    |  B  |    |  C  |    |  D  |
|     |    |     |    |     |    |     |
+-----+    +-----+    +-----+    +-----+
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          +----------+          |
  |                               |
  |                               |
  +-------------------------------+
ES=0   ES=5   ES=5   ES=8   ES=14
EF=5   EF=9   EF=8   EF=11  EF=20
```

Step 2: Perform the backward pass by moving from right to left and calculating the LF and LS values for each activity.

```
+-----+    +-----+    +-----+    +-----+
|     |    |     |    |     |    |     |
|  A  |    |  B  |    |  C  |    |  D  |
|     |    |     |    |     |    |     |
+-----+    +-----+    +-----+    +-----+
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |