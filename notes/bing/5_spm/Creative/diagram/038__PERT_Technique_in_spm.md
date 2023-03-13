PERT technique in spm is a method of project management that involves estimating the duration of each activity in a project based on three scenarios: optimistic, pessimistic and most likely. The technique also involves creating a network diagram that shows the sequence and dependencies of the activities, and calculating the critical path and the slack time for each activity. The PERT technique helps to plan and control complex projects with uncertainty and variability.

### PERT Technique in spm

The following is an example of a PERT network diagram for a project that has six activities: A, B, C, D, E and F. The diagram shows the activity names, the durations in parentheses, and the predecessors in brackets. The diagram also shows the critical path in bold, which is the longest path in the network and determines the minimum time required to complete the project. The diagram also shows the slack time for each activity, which is the difference between the earliest and latest start or finish times. The slack time indicates how much an activity can be delayed without affecting the project completion time.

```
    A(10)[-]    B(12)[A]    C(8)[B]    D(6)[C]
     |           |           |           |
     |           |           |           |
     |           |           |           |
     |           |           |           |
     |           |           |           |
     |           |           |           |
     |           |           |           |
     |           |           |           |
     |           |           |           |
     |           |           |           |
     |           |           |           |
     |           |           |           |
     +-----------+-----------+-----------+
     |           |           |           |
     |           |           |           |
     |           |           |           |
     |           |           |           |
     |           |           |           |
     E(4)[A]     F(5)[E]     G(7)[F,D]
     |           |           |
     |           |           |
     |           |           |
     |           |           |
     |           |           |
     |           |           |
     |           |           |
     |           |           |
     |           |           |
     +-----------+-----------+
     |           |
     |           |
     |           |
     |           |
     |           |
     |           |
     |           |
     |           |
     |           |
     H(9)[G]
     |
     |
     |
     |
     |
     |
     |
     |
     |
     End
```

The following table shows the calculations for the earliest start (ES), earliest finish (EF), latest start (LS), latest finish (LF) and slack time (SL) for each activity.

| Activity | Duration | Predecessors | ES | EF | LS | LF | SL |
|----------|----------|--------------|----|----|----|----|----|
| A        | 10       | -            | 0  | 10 | 0  | 10 | 0  |
| B        | 12       | A            | 10 | 22 | 10 | 22 | 0  |
| C        | 8        | B            | 22 | 30 | 22 | 30 | 0  |
| D        | 6        | C            | 30 | 36 | 30 | 36 | 0  |
| E        | 4        | A            | 10 | 14 | 14 | 18 | 4  |
| F        | 5        | E            | 14 | 19 | 18 | 23 | 4  |
| G        | 7        | F, D         | 36 | 43 | 36 | 43 | 0  |
| H        | 9        | G            | 43 | 52 | 43 | 52 | 0  |

The critical path is A-B-C-D-G-H and the project completion time is 52 days. The activities E and F have a slack time of 4 days, which means they can be delayed by up to 4 days without affecting the project completion time. The activities A, B, C, D, G and H have a slack time of 0 days, which means they cannot be delayed at all without affecting the project completion time.