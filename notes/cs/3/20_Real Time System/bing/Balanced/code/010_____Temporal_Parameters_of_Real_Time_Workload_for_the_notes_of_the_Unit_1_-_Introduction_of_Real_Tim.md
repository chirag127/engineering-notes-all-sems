### Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and characteristics .
- The temporal parameters of a job are :
  - Release time (r<sub>i</sub>): The time instant when the job becomes available for execution.
  - Absolute deadline (d<sub>i</sub>): The time instant by which the job must finish its execution.
  - Relative deadline (D<sub>i</sub>): The maximum allowed time between the release time and the absolute deadline of the job. D<sub>i</sub> = d<sub>i</sub> - r<sub>i</sub>.
  - Feasible interval ([r<sub>i</sub>, d<sub>i</sub>]): The time interval in which the job can be executed.
- The temporal parameters of a job may be fixed, variable, or unknown, depending on the nature of the real time system and the workload .
- The temporal parameters of a job may be specified by the application, the system, or the user .
- The temporal parameters of a job may be expressed in absolute or relative terms, depending on the reference point of the time measurement .
- The temporal parameters of a job may be hard or soft, depending on the consequences of missing the deadline .
- The temporal parameters of a job may be periodic or aperiodic, depending on the regularity of the job arrival pattern .
- The temporal parameters of a job may be independent or dependent, depending on the existence of precedence or synchronization constraints among jobs .