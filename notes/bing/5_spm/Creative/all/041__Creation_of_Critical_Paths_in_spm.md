### Creation of Critical Paths in spm

- Critical path is the longest sequence of activities from project start to finish that must be completed to ensure the project is finished by a certain time .
- Critical path method (CPM) is an algorithm for planning, managing and analyzing the timing of a project.
- The steps to create a critical path in spm are:
  - Step 1: Activity specification. Identify all the activities required to complete the project and list them in a table with their durations and dependencies.
  - Step 2: Activity sequence establishment. Draw a network diagram that shows the logical order of the activities and their dependencies using nodes and arrows. The nodes represent the activities and the arrows represent the precedence relationships.
  - Step 3: Network diagram. Label each node with the activity name, duration, earliest start time (ES), earliest finish time (EF), latest start time (LS), and latest finish time (LF). The ES and EF are calculated by adding the duration to the ES or EF of the preceding activity. The LS and LF are calculated by subtracting the duration from the LS or LF of the succeeding activity.
  - Step 4: Estimates for each activity. Estimate the optimistic time (O), most likely time (M), and pessimistic time (P) for each activity using historical data, expert judgment, or other methods. The expected time (E) for each activity can be calculated using the formula: E = (O + 4M + P) / 6. The variance (V) for each activity can be calculated using the formula: V = ((P - O) / 6)^2.
  - Step 5: Identification of the critical path. The critical path is the path with the longest duration in the network diagram. It can be identified by finding the activities with zero slack, which is the difference between the LF and EF or the LS and ES. The activities on the critical path have the highest risk of delaying the project completion and must be closely monitored and controlled.
  - Step 6: Critical path diagram to show project progresses. The critical path diagram is a graphical representation of the project schedule that shows the critical path and the progress of each activity. It can be updated periodically to reflect the actual start and finish times of the activities and to identify any deviations from the planned schedule.

- A mnemonic to remember the steps to create a critical path in spm is: **AS END** (Activity Specification, Activity Sequence Establishment, Network Diagram, Estimates, Critical Path Identification, Critical Path Diagram).
- A learning trick to understand the concept of critical path is to imagine a chain of dominoes. The dominoes represent the activities and the order in which they fall represents the precedence relationships. The critical path is the longest chain of dominoes that must fall to complete the project. If any domino on the critical path is delayed, the whole project will be delayed. The dominoes that are not on the critical path have some slack, which means they can fall earlier or later without affecting the project completion.

- An example of a network diagram and a critical path diagram for a software project is shown below:

```
Network Diagram:

  A(3)    B(4)    C(2)    D(5)    E(4)    F(6)    G(3)    H(2)    I(4)
 /-----> /-----> /-----> /-----> /-----> /-----> /-----> /-----> /
|       |       |       |       |       |       |       |       |
|       |       |       |       |       |       |       |       |
|       |       |       |       |       |       |       |       |
|       |       |       |       |       |       |       |       |
 \----> \----> \----> \----> \----> \----> \----> \----> \---->
  J(2)    K(3)    L(4)    M(3)    N(2)    O(5)    P(4)    Q(3)    R(2)

Critical Path Diagram:

  A(3)    B(4)    C(2)    D(5)    E(4)    F(6)    G(3)    H(2)    I(4)
 /-----> /-----> /-----> /-----> /-----> /-----> /-----> /----->