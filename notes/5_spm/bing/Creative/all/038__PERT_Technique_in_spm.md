### PERT Technique in spm

- PERT stands for Program Evaluation and Review Technique. It is a project management tool that helps to estimate the time and resources required to complete a project. It also helps to identify the critical path and possible risks of the project.   
- PERT uses a network diagram to represent the project activities and their dependencies. Each activity is assigned an optimistic, pessimistic, and most likely time estimate based on the uncertainty and variability of the task.   
- PERT calculates the expected time for each activity using a weighted average formula: Expected time = (Optimistic time + 4 x Most likely time + Pessimistic time) / 6.   
- PERT also calculates the variance and standard deviation for each activity using the formula: Variance = ((Pessimistic time - Optimistic time) / 6) ^ 2. Standard deviation = Square root of variance.   
- PERT identifies the critical path of the project, which is the longest sequence of activities that determines the minimum duration of the project. The critical path has zero slack or float, which means any delay in the critical activities will delay the project completion.   
- PERT also identifies the non-critical activities, which have some slack or float, which means they can be delayed without affecting the project completion. The slack or float of an activity is the difference between its latest finish time and its earliest finish time, or between its latest start time and its earliest start time.   
- PERT can be used to calculate the probability of completing the project within a given time frame, using the normal distribution curve and the z-score formula. The z-score is the number of standard deviations that a given value is away from the mean. The z-score formula is: z = (Target time - Expected time) / Standard deviation.   
- PERT can also be used to perform sensitivity analysis, which is the process of evaluating how changes in one or more variables affect the outcome of the project. For example, PERT can be used to determine how much the project duration will change if the optimistic, pessimistic, or most likely time estimates of some activities are changed.   
- PERT has some advantages and disadvantages as a project management tool. Some of the advantages are:   
  - It helps to plan and control complex and uncertain projects.
  - It helps to identify the critical activities and the slack or float of the non-critical activities.
  - It helps to estimate the expected time and variance of the project.
  - It helps to calculate the probability of completing the project within a given time frame.
  - It helps to perform sensitivity analysis and risk management.
- Some of the disadvantages are:   
  - It requires a lot of data and calculations, which can be time-consuming and error-prone.
  - It assumes a normal distribution of the activity times, which may not be realistic in some cases.
  - It does not consider the resource availability and allocation, which may affect the project duration and cost.
  - It does not account for the interdependencies and feedback loops among the activities, which may cause changes in the project scope and quality.

- Here is an example of a PERT network diagram for a project that has six activities: A, B, C, D, E, and F. The optimistic, pessimistic, and most likely time estimates for each activity are given in parentheses. The expected time, variance, and standard deviation for each activity are calculated using the formulas mentioned above. The critical path is highlighted in red. The slack or float of the non-critical activities are shown in brackets.

```
    A(2,4,3)    B(3,9,6)    C(4,16,10)
    E(2,2,2)    F(5,11,8)
    |----3----|----6----|----10----|
    |         |         |          |
    |         |         |