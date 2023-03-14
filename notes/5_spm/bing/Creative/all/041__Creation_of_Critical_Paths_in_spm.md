### Creation of Critical Paths in spm

- Critical Path Method (CPM) is an algorithm for planning, managing and analyzing the timing of a project.
- A critical path in project management is the longest sequence of activities that must be finished on time in order for the entire project to be complete  .
- The activities on the critical path have zero slack, meaning that any delay in them will cause a delay in the whole project.
- The critical path method helps to identify critical and non-critical tasks, estimate the project duration, allocate resources, monitor progress, and control risks.
- The steps to create a critical path in spm are:

  1. Activity specification: List all the activities required to complete the project and assign them an ID and a duration.
  2. Activity sequence establishment: Determine the logical order and dependencies of the activities. Use a precedence diagram to show the relationships between the activities.
  3. Network diagram: Draw a network diagram using the activity-on-node (AON) method, where each node represents an activity and each arrow represents a dependency. Label each node with its ID, duration, and early and late start and finish times. Calculate the early and late times using the forward and backward pass methods.
  4. Estimates for each activity: Estimate the best-case, most-likely, and worst-case durations for each activity using historical data, expert judgment, or other methods. Calculate the expected duration and the variance for each activity using the PERT formula: Expected duration = (Best + 4 x Most-likely + Worst) / 6; Variance = ((Worst - Best) / 6)^2
  5. Identification of the critical path: Identify the critical path by finding the longest path in the network diagram. The critical path is the path with the longest expected duration and the highest variance. The activities on the critical path have zero slack, meaning that their early and late times are equal.
  6. Critical path diagram to show project progresses: Draw a critical path diagram using a Gantt chart, where each activity is represented by a horizontal bar and the critical path is highlighted. Update the diagram as the project progresses by marking the actual start and finish times of each activity and adjusting the remaining durations and slack values.

- A mnemonic to remember the steps of creating a critical path in spm is: **A**ll **A**nts **N**eed **E**xtra **I**ce **C**ream. The first letter of each word corresponds to the first letter of each step.