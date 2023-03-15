### Precedence Constraints and Data Dependency

- Precedence constraints and data dependency are two types of constraints that may affect the execution order of jobs in real time systems.
- Precedence constraints are imposed by the logical or temporal dependencies among jobs, such as control flow or synchronization. For example, a job J1 may need to finish before another job J2 can start, or a job J3 may need to wait for a signal from another job J4.
- Data dependency is imposed by the communication or sharing of data among jobs, such as input/output or shared memory. For example, a job J5 may need to read the data produced by another job J6, or a job J7 may need to write the data to a shared buffer that is accessed by another job J8.
- Precedence constraints and data dependency may affect the feasibility and optimality of scheduling algorithms for real time systems, as they may limit the parallelism or flexibility of job execution.
- An efficient way to represent precedence constraints is by using a directed graph G = (J, <) where J is the set of jobs. This graph is known as the precedence graph. Jobs are represented by vertices of the graph and precedence constraints are represented using directed edges. For example, the following graph shows the precedence constraints among four jobs J1, J2, J3 and J4:

```
J1 -> J2
J1 -> J3
J2 -> J4
J3 -> J4
```

- Data dependency cannot be captured by a precedence graph, as it may depend on the runtime values or states of the data. For example, a job J9 may need to read the data from a sensor only if the data is above a certain threshold, or a job J10 may need to write the data to a file only if the file is not locked by another job. Data dependency may require additional mechanisms to ensure the consistency and correctness of the data, such as locks, semaphores, monitors, or message passing.