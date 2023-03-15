### Forward Pass & Backward Pass Techniques in SPM

Forward Pass and Backward Pass are two techniques used in the critical path method (CPM) of scheduling in project management. These techniques are used to determine the earliest and latest possible start and finish times for each activity in a project.

#### Forward Pass

The Forward Pass technique is used to determine the earliest possible start and finish times for each activity in a project. This is done by moving forward through the project network diagram, starting from the first activity and calculating the earliest start and finish times for each subsequent activity.

The earliest start time (ES) for the first activity is usually set to zero. The earliest finish time (EF) for an activity is calculated by adding its duration to its earliest start time (ES). The earliest start time (ES) for a subsequent activity is the maximum of the earliest finish times (EF) of all its predecessor activities.

#### Backward Pass

The Backward Pass technique is used to determine the latest possible start and finish times for each activity in a project. This is done by moving backward through the project network diagram, starting from the last activity and calculating the latest start and finish times for each preceding activity.

The latest finish time (LF) for the last activity is usually set to its earliest finish time (EF). The latest start time (LS) for an activity is calculated by subtracting its duration from its latest finish time (LF). The latest finish time (LF) for a preceding activity is the minimum of the latest start times (LS) of all its successor activities.

These techniques are useful for determining the critical path of a project, which is the sequence of activities that must be completed on time for the project to be completed on schedule. Activities on the critical path have zero float, meaning that any delay in their completion will delay the completion of the entire project. Activities not on the critical path have some float, meaning that they can be delayed without delaying the completion of the entire project.