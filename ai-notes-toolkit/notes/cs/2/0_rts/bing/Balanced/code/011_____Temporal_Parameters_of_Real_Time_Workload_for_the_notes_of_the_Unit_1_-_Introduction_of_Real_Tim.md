### Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and characteristics.
- The temporal parameters of a job are :
  - Release time (r<sub>i</sub>): The time instant when the job becomes available for execution.
  - Absolute deadline (d<sub>i</sub>): The time instant by which the job must finish its execution.
  - Relative deadline (D<sub>i</sub>): The time interval between the release time and the absolute deadline of the job.
  - Feasible interval ([r<sub>i</sub>, d<sub>i</sub>]): The time interval during which the job can be executed.
- The temporal parameters of a job can be specified by the application or the system designer, or they can be derived from other parameters such as the period or the frequency of the job.
- The temporal parameters of a job can be used to determine the schedulability and the performance of the real time system.
- The temporal parameters of a job can be fixed or variable, depending on the nature of the application and the system. For example, a hard real time system may have fixed and known temporal parameters, while a soft real time system may have variable and uncertain temporal parameters.