 Here is the content in markdown format for the given topic:

### Priority Driven Approach

- In priority driven approach, each task is assigned a priority. The priority can be either fixed priority or dynamic priority.
- In fixed priority approach, the priorities are assigned to tasks statically based on task criticality or importance. The task with highest priority is executed first. If two tasks have same priority, then they are scheduled using priority inheritance, priority ceiling or Rate Monotonic scheduling algorithm.
- In dynamic priority approach, the priorities of tasks are changed dynamically based on factors like deadline, execution time, etc. The Earliest Deadline First (EDF) algorithm is a dynamic priority based algorithm.
- Priority driven approach has advantage of handling tasks with varying criticality but it suffers from priority inversion problem. The high priority task may have to wait for low priority task to complete execution.
- Appropriate priority assignment and use of priority inheritance protocols can reduce the priority inversion problem in priority driven approach.
- Examples of priority driven scheduling are Rate Monotonic scheduling, Earliest Deadline First scheduling, etc. They are used in hard real time systems to schedule tasks with varying criticality and deadlines.

The above content summarizes the key points about priority driven approach for real time scheduling. It covers both fixed and dynamic priority, pros and cons, examples and applications. The points are written in brief for easy understanding and learning. Please let me know if you would like me to elaborate on any of the points or add more details and examples.