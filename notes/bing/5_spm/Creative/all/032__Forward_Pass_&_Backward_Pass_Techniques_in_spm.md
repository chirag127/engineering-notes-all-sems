### Forward Pass & Backward Pass Techniques in spm

- Forward pass and backward pass are techniques used to calculate the earliest and latest start and finish times of the activities in a project network diagram.
- Forward pass is the process of moving from the first activity to the last activity in the network diagram and calculating the earliest start (ES) and earliest finish (EF) times of each activity.
- Backward pass is the process of moving from the last activity to the first activity in the network diagram and calculating the latest start (LS) and latest finish (LF) times of each activity.
- The difference between the latest and earliest times of an activity is called the total float (TF), which represents the amount of time an activity can be delayed without affecting the project completion time.
- The critical path is the sequence of activities that has the least amount of total float and determines the minimum duration of the project.
- The forward pass and backward pass techniques can be applied to any type of network diagram, such as activity-on-node (AON) or activity-on-arrow (AOA).
- The steps for performing the forward pass and backward pass techniques are as follows:

  - Forward pass:
    - Start with the first activity in the network diagram and assign it an ES of zero and an EF equal to its duration.
    - For each subsequent activity, calculate its ES as the maximum EF of its predecessors and its EF as the sum of its ES and duration.
    - Repeat this process until you reach the last activity in the network diagram and record its EF as the project completion time.

  - Backward pass:
    - Start with the last activity in the network diagram and assign it an LF equal to its EF and an LS equal to its LF minus its duration.
    - For each preceding activity, calculate its LF as the minimum LS of its successors and its LS as the difference between its LF and duration.
    - Repeat this process until you reach the first activity in the network diagram and record its LS as zero.

  - Total float and critical path:
    - For each activity, calculate its TF as the difference between its LF and EF or between its LS and ES.
    - Identify the activities that have a TF of zero and mark them as critical. These activities form the critical path of the project.
    - The project completion time is equal to the EF or LF of the last activity on the critical path.

- An example of applying the forward pass and backward pass techniques to an AON network diagram is shown below:

```
   A(5)   B(4)   C(3)
  /  \    /  \    /  \
 /    \  /    \  /    \
0      5       9      12
 \    /  \    /  \    /
  \  /    \  /    \  /
   D(2)   E(6)   F(4)
    \      |      /
     \     |     /
      \    |    /
       \   |   /
        \  |  /
         \ | /
          14
```

- The ES, EF, LS, LF, and TF values of each activity are shown in the table below:

| Activity | ES | EF | LS | LF | TF |
|----------|----|----|----|----|----|
| A        | 0  | 5  | 0  | 5  | 0  |
| B        | 5  | 9  | 5  | 9  | 0  |
| C        | 9  | 12 | 9  | 12 | 0  |
| D        | 0  | 2  | 3  | 5  | 3  |
| E        | 9  | 15 | 9  | 15 | 0  |
| F        | 12 | 16 | 12 | 16 | 0  |

- The critical path of the project is A-B-C-E-F and the project completion time is 16 days.