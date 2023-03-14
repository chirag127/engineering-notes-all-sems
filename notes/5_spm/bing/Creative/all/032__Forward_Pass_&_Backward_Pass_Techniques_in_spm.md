### Forward Pass & Backward Pass Techniques in spm

- Forward pass and backward pass are techniques used to move through a project network diagram to determine the project duration, the critical path, and the float or slack of each activity.
- A project network diagram is a graphical representation of the project activities and their dependencies. It shows the sequence and duration of each activity, as well as the start and finish dates of the project.
- A forward pass is a technique to move forward from the project start date to the project end date, calculating the early start (ES) and early finish (EF) values for each activity. The ES is the earliest date that an activity can start, considering the dependencies and durations of the preceding activities. The EF is the earliest date that an activity can finish, which is equal to the ES plus the activity duration.
- A backward pass is a technique to move backward from the project end date to the project start date, calculating the late start (LS) and late finish (LF) values for each activity. The LF is the latest date that an activity can finish, without delaying the project completion date. The LS is the latest date that an activity can start, which is equal to the LF minus the activity duration.
- The forward pass and backward pass can be applied using the following formulas:

  - ES = Maximum EF of immediate predecessors
  - EF = ES + Duration
  - LF = Minimum LS of immediate successors
  - LS = LF - Duration

- The forward pass and backward pass can also be used to calculate the total float (TF) and free float (FF) of each activity. The TF is the amount of time that an activity can be delayed without affecting the project completion date. The FF is the amount of time that an activity can be delayed without affecting the start of any successor activity. The TF and FF can be calculated using the following formulas:

  - TF = LS - ES or LF - EF
  - FF = Minimum ES of immediate successors - EF

- The critical path is the longest sequence of activities in the project network diagram that has zero TF. It represents the shortest possible duration of the project. Any delay on the critical path will cause the project to be delayed.

- The forward pass and backward pass techniques can be illustrated using an example. Suppose we have a project with five activities (A, B, C, D, and E) and their durations and dependencies as follows:

  | Activity | Duration | Predecessors |
  | -------- | -------- | ------------ |
  | A        | 2 days   | None         |
  | B        | 3 days   | A            |
  | C        | 4 days   | A            |
  | D        | 5 days   | B, C         |
  | E        | 6 days   | D            |

- We can draw a project network diagram using boxes with six quadrants for each activity, as shown below:

  ```
  +----+----+----+
  | ES |    | EF |
  +----+----+----+
  |    | A  | 2  |
  +----+----+----+
  | LS |    | LF |
  +----+----+----+
  ```

- The ES and EF values are calculated using the forward pass, starting from the project start date (day 0). The LF and LS values are calculated using the backward pass, starting from the project end date (day 20). The TF and FF values are calculated using the formulas above. The results are shown below:

  ```
  +----+----+----+     +----+----+----+     +----+----+----+
  | 0  |    | 2  |     | 2  |    | 5  |     | 2  |    | 6  |
  +----+----+----+     +----+----+----+     +----+----+----+
  |    | A  | 2  | --> |    | B  | 3  | --> |    | C  | 4  |
  +----+----+----+     +----+----+----+     +----+----+----+
  | 0  |    | 2  |     | 2  |    | 5  |     | 2  |    | 6  |
  +----+----+----+     +----+----+----+     +----+----+----+
                             |                   |
                             |                   |
                             V                   V