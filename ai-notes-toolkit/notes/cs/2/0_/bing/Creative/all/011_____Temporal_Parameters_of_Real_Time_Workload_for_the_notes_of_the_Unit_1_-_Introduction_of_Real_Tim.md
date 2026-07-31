# Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and behavior .
- The temporal parameters of a job are:
  - **Release time (r<sub>i</sub>)**: The earliest time at which a job can start execution. It may be known exactly or within a range [r<sub>i</sub>-, r<sub>i</sub>+], where r<sub>i</sub>- is the minimum release time and r<sub>i</sub>+ is the maximum release time. The difference between r<sub>i</sub>+ and r<sub>i</sub>- is called the **jitter** of the job.
  - **Absolute deadline (d<sub>i</sub>)**: The latest time by which a job must finish execution. It may be fixed or variable depending on the system and the job. A job that misses its absolute deadline is considered to have failed.
  - **Relative deadline (D<sub>i</sub>)**: The maximum time interval between the release time and the absolute deadline of a job. It is usually fixed and known in advance. A job that finishes within its relative deadline is considered to have succeeded.
  - **Feasible interval [(r<sub>i</sub>), (d<sub>i</sub>)]**: The time interval in which a job can be feasibly executed by the system. It is bounded by the release time and the absolute deadline of the job. A job that starts before its release time or finishes after its absolute deadline is considered to have violated its feasible interval.
- The temporal parameters of a job are important for the analysis and design of real time systems, as they determine the schedulability, performance, and correctness of the system .