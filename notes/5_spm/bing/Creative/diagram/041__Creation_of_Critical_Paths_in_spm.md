The critical path method (CPM) is a technique where you identify tasks that are necessary for project completion and determine scheduling flexibilities. A critical path in project management is the longest sequence of activities that must be finished on time in order for the entire project to be complete  .

The following steps are involved in creating a critical path in SPM:

1. Activity specification: List all the activities required to complete the project and assign them an ID and a name.
2. Activity sequence establishment: Determine the logical order of the activities and identify any dependencies or constraints among them. Use arrows to show the direction of the flow and circles to represent the start and end points of the project.
3. Network diagram: Draw a network diagram that shows the relationships among the activities and their durations. Use the activity IDs and names to label the arrows and the circles. You can use a software tool or a spreadsheet to create the diagram.
4. Estimates for each activity: Estimate the time required to complete each activity and write it on the corresponding arrow. You can use historical data, expert opinions, or other methods to estimate the durations.
5. Identification of the critical path: Calculate the earliest start time (ES), earliest finish time (EF), latest start time (LS), and latest finish time (LF) for each activity using the following formulas:

- ES = maximum EF of all immediate predecessors
- EF = ES + duration
- LF = minimum LS of all immediate successors
- LS = LF - duration

The critical path is the path that has the longest total duration and the least amount of slack or float. Slack or float is the difference between the latest and earliest times of an activity. It indicates how much an activity can be delayed without affecting the project completion time. The activities on the critical path have zero slack or float.
6. Critical path diagram to show project progresses: Update the network diagram with the calculated times and highlight the critical path. You can also use colors or symbols to indicate the status of each activity, such as completed, in progress, or not started.

The following diagram illustrates the creation of a critical path in SPM using an example project of building a house:

```
    Start
     |
     |  A: Obtain permit (2 weeks)
     |
     V
    B: Prepare site (3 weeks)  -->  C: Pour foundation (2 weeks)  -->  D: Build frame (3 weeks)  -->  E: Install roof (2 weeks)  -->  F: Finish exterior (4 weeks)  -->  End
     |                                                                                       ^
     |                                                                                       |
     +---------------------------------------------------------------------------------------+
     |  G: Install plumbing (4 weeks)                                                        |
     |                                                                                       |
     +---------------------------------------------------------------------------------------+
     |  H: Install electrical (5 weeks)                                                      |
     |                                                                                       |
     +---------------------------------------------------------------------------------------+
     |  I: Install drywall (4 weeks)                                                         |
     |                                                                                       |
     +---------------------------------------------------------------------------------------+
     |  J: Paint interior (3 weeks)                                                          |
     |                                                                                       |
     +---------------------------------------------------------------------------------------+
     |  K: Install flooring (2 weeks)                                                        |
     |                                                                                       |
     +---------------------------------------------------------------------------------------+
     |  L: Install cabinets (3 weeks)                                                        |
     |                                                                                       |
     +---------------------------------------------------------------------------------------+
     |  M: Install appliances (1 week)                                                       |
     |                                                                                       |
     +---------------------------------------------------------------------------------------+
     |  N: Install fixtures (2 weeks)                                                        |
     |                                                                                       |
     +---------------------------------------------------------------------------------------+
     |  O: Landscape yard (3 weeks)                                                          |
     |                                                                                       |
     +---------------------------------------------------------------------------------------+
```

The critical path is A-B-C-D-E-F, which has a total duration of 16 weeks. The slack or float of each activity is shown below:

- A: 0
- B: 0
- C: 0
- D: 0
- E: 0
- F: 0
- G: 5
- H: 4
- I: 5
- J: 6
- K: 7
- L: 6
- M: 8
- N: 7
- O: 5

The diagram can be updated with the calculated times and the status of each activity as the project progresses. For example, after 5 weeks, the diagram might look like this:

```
    Start
     |
     |  A: Obtain permit (2 weeks) [Completed]
     |
     V
    B: Prepare