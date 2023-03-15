### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two algorithms for scheduling preemptive jobs on one processor in real time systems.
- EDF assigns the highest priority to the job with the earliest absolute deadline, and preempts the current job if a higher priority job arrives.
- LST assigns the highest priority to the job with the least slack (or laxity), which is the difference between the deadline and the remaining execution time, and preempts the current job if a higher priority job arrives.
- Both EDF and LST are optimal for scheduling independent jobs, meaning that if there exists a feasible schedule that meets all the deadlines, then EDF and LST will also produce a feasible schedule that meets all the deadlines .
- EDF and LST are also optimal for scheduling jobs with precedence constraints, meaning that some jobs depend on the completion of other jobs, as long as the precedence graph is a forest (a collection of trees) and the jobs have implicit deadlines (equal to their periods) .
- EDF and LST have different advantages and disadvantages in terms of performance and implementation.
  - EDF is easier to implement than LST, as it only requires sorting the jobs by their deadlines, while LST requires calculating the slack of each job at every scheduling point.
  - EDF has better average response time than LST, as it tends to finish the jobs earlier than their deadlines, while LST may delay some jobs until close to their deadlines.
  - LST has better worst-case response time than EDF, as it minimizes the maximum tardiness (the amount of time a job misses its deadline) of any job, while EDF may have large tardiness for some jobs if the system is overloaded.
  - LST is more robust than EDF to variations in execution times and arrival times, as it adapts to the changing slack of the jobs, while EDF may fail to meet some deadlines if the jobs take longer or arrive earlier than expected  .