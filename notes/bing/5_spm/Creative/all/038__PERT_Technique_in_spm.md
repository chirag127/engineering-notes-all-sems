### PERT Technique in spm

- PERT stands for Program Evaluation and Review Technique. It is a project management planning tool used to calculate the amount of time it will take to realistically finish a project .
- PERT charts are used to plan tasks within a project, making it easier to schedule and coordinate team members. They also help in keeping track of the progress, or lack thereof, of the overall project  .
- PERT was first developed by the US Navy SPO (Special Projects Office) in 1967 during the Polaris missile development program then it was applied to the other industries. Both CPM and PERT are complementary tools and they are developed at roughly the same time .
- PERT is based on the concept of a network diagram, which is a graphical representation of the project activities and their interdependencies. A network diagram consists of nodes and arrows. Nodes represent the activities or tasks, and arrows represent the precedence relationships or dependencies among them.
- PERT uses a three-point estimating technique to calculate the expected time for each activity. The three points are: optimistic time (O), pessimistic time (P), and most likely time (M). The expected time (E) is calculated as follows :

  E = (O + 4M + P) / 6

- PERT also calculates the variance (V) and the standard deviation (SD) of each activity, which are measures of the uncertainty or risk involved in the time estimates. The variance is calculated as follows :

  V = ((P - O) / 6)^2

  SD = sqrt(V)

- PERT uses the expected time, variance, and standard deviation of each activity to determine the critical path of the project, which is the longest path of activities in the network diagram that determines the minimum duration of the project. The critical path is identified by adding the expected times of the activities along each path and finding the path with the maximum total time  .
- PERT also calculates the earliest start time (ES), earliest finish time (EF), latest start time (LS), and latest finish time (LF) of each activity, which are the time windows within which the activity can be performed without affecting the project duration. These are calculated as follows :

  ES = maximum EF of all immediate predecessors

  EF = ES + E

  LF = minimum LS of all immediate successors

  LS = LF - E

- PERT also calculates the slack or float of each activity, which is the amount of time that the activity can be delayed or advanced without affecting the project duration. There are two types of slack: total slack and free slack. Total slack is the difference between the latest and earliest times of the activity. Free slack is the difference between the earliest finish time of the activity and the earliest start time of the next activity. Slack is calculated as follows :

  Total slack = LF - EF = LS - ES

  Free slack = minimum ES of all immediate successors - EF

- PERT can be used to analyze the project work schedule by focusing on each task and calculate the minimum time required to complete the project. It can also be used to identify the critical activities that need more attention and resources, and the non-critical activities that have some flexibility and buffer. PERT can also be used to evaluate the impact of changes or delays in the project activities on the overall project duration  .
- Some advantages of PERT are  :

  - It helps in planning and controlling complex and uncertain projects.
  - It provides a visual and logical representation of the project activities and their dependencies.
  - It allows for the incorporation of uncertainty and risk in the time estimates.
  - It helps in identifying the critical path and the critical activities that determine the project duration.
  - It helps in optimizing the use of resources and time.
  - It helps in monitoring and tracking the project progress and performance.

- Some disadvantages of PERT are  :

  - It can be time-consuming and costly to collect and analyze the data for the three-point estimates.
  - It can be difficult to estimate the optimistic, pessimistic, and most likely