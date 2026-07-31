Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of temporal parameters of real time workload for the unit 1 - introduction of real time system.

### Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and characteristics.
- The temporal parameters of a job are :
  - **Release time (r<sub>i</sub>)**: The earliest time at which a job can start execution. It may be known exactly or within a range [r<sub>i</sub>-, r<sub>i</sub>+].
  - **Absolute deadline (d<sub>i</sub>)**: The latest time by which a job must finish execution. It may be hard or soft, depending on the consequences of missing it.
  - **Relative deadline (D<sub>i</sub>)**: The maximum time allowed for a job to finish execution after its release time. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - **Feasible interval [(r<sub>i</sub>), (d<sub>i</sub>)]**: The time interval in which a job can be feasibly executed, i.e., it can meet its deadline.
- The temporal parameters of a job can be represented graphically as follows:

![Temporal parameters of a job](https://benchpartner.com/sites/default/files/inline-images/Real%20Time%20Workload%20Parameters.png)

- The temporal parameters of a job can be used to analyze the schedulability and performance of a real time system. For example, a real time system is said to be feasible if it can execute all the jobs in the workload without missing any deadlines.