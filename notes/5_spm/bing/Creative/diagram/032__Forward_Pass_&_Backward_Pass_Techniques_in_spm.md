Forward pass and backward pass are techniques used to calculate the early and late start and finish dates of the activities in a project network diagram. They help to determine the project duration and the critical path, which is the longest sequence of activities with zero float or slack. Float represents how much an activity can be delayed without affecting the project completion date or the successor activities.

The following diagram illustrates the basic architecture of a forward pass and backward pass in a project network diagram. The diagram uses the example of a project with five activities (A, B, C, D, and E) and their durations and dependencies. The boxes have six quadrants that represent the activity name, duration, early start (ES), early finish (EF), late start (LS), and late finish (LF) of each activity.

```
    +---+---+---+---+---+---+
    | A | 2 | 0 | 2 | 0 | 2 |
    +---+---+---+---+---+---+
        |
        |   +---+---+---+---+---+---+
        +-->| B | 3 | 2 | 5 | 2 | 5 |
        |   +---+---+---+---+---+---+
        |
        |   +---+---+---+---+---+---+
        +-->| C | 4 | 2 | 6 | 4 | 8 |
            +---+---+---+---+---+---+
                |
                |   +---+---+---+---+---+---+
                +-->| D | 2 | 6 | 8 | 6 | 8 |
                |   +---+---+---+---+---+---+
                |
                |   +---+---+---+---+---+---+
                +-->| E | 2 | 6 | 8 | 8 |10 |
                    +---+---+---+---+---+---+
```

To perform a forward pass, we start from the first activity and move forward through the network diagram, adding the durations of the activities to get the early start and early finish dates. The early start of an activity is the maximum of the early finish dates of its predecessors, or zero if it has no predecessors. The early finish of an activity is the early start plus the duration. For example, the early start of activity A is zero, and the early finish is zero plus two, which is two. The early start of activity B is the maximum of the early finish of activity A, which is two, and the early finish is two plus three, which is five.

To perform a backward pass, we start from the last activity and move backward through the network diagram, subtracting the durations of the activities to get the late start and late finish dates. The late finish of an activity is the minimum of the late start dates of its successors, or the project completion date if it has no successors. The late start of an activity is the late finish minus the duration. For example, the late finish of activity E is the project completion date, which is 10, and the late start is 10 minus two, which is eight. The late finish of activity D is the minimum of the late start of activity E, which is eight, and the late start is eight minus two, which is six.

The critical path is the longest sequence of activities with zero float or slack. Float is the difference between the late and early start or finish dates of an activity. For example, the float of activity A is zero, because the late start and finish are the same as the early start and finish. The float of activity C is two, because the late start and finish are two days more than the early start and finish. The critical path of this project is A-B-D-E, because these activities have zero float and the longest duration. Any delay in these activities will delay the project completion date.