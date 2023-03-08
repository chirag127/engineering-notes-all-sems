### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a computer system that responds to events within a specified time interval .
- A real time system consists of a set of tasks or jobs that need to be executed periodically or aperiodically.
- Each task or job has a release time, an execution time and a deadline.
- The release time of a job is the time at which the job becomes ready for execution.
- The release time may not be exact, but may have some jitter, which is the variation in the release time of a job.
- The release time may depend on the occurrence of external events, such as sensor inputs, user commands, network messages, etc.
- The release time may also depend on the completion of other jobs, such as data dependencies, resource sharing, synchronization, etc.
- A job can be scheduled and executed at any time at or after its release time, provided its resource dependency conditions are met.
- The release time of a job determines its eligibility for execution and its priority for scheduling.
- The release time of a job may affect its deadline, which is the time by which the job should finish its execution.
- The deadline may be absolute, which means it is fixed with respect to a reference point, such as the start of the system or the occurrence of an event.
- The deadline may also be relative, which means it is fixed with respect to the release time of the job.
- The deadline may be hard, which means missing the deadline may cause catastrophic consequences, such as system failure, loss of life, etc.
- The deadline may also be soft, which means missing the deadline may cause degraded performance, reduced quality, etc.
- The deadline of a job determines its urgency for execution and its priority for scheduling.
- The deadline of a job may affect its execution time, which is the time taken by the job to finish its execution.
- The execution time may depend on the characteristics of the job, such as the algorithm, the input data, the output data, etc.
- The execution time may also depend on the characteristics of the system, such as the processor speed, the memory size, the cache size, the bus bandwidth, etc.
- The execution time may also depend on the characteristics of the environment, such as the workload, the interference, the noise, etc.
- The execution time may not be constant, but may have some variation, which is the difference between the worst-case execution time (WCET) and the best-case execution time (BCET) of a job.
- The execution time of a job determines its resource requirement and its feasibility for scheduling.
- The execution time of a job may affect its release time and deadline, which are the timing constraints of a job.
- The timing constraints of a job specify the temporal behavior and the quality of service of a job.
- The timing constraints of a job may be specified by the application developer, the system designer, the user, or the environment.
- The timing constraints of a job may be static, which means they are known and fixed before the execution of the system, or dynamic, which means they may change during the execution of the system.
- The timing constraints of a job may be explicit, which means they are explicitly given as parameters of the job, or implicit, which means they are implicitly derived from the semantics of the job.
- The timing constraints of a job may be deterministic, which means they are predictable and repeatable, or stochastic, which means they are probabilistic and random.
- The timing constraints of a job may be independent, which means they do not depend on the timing constraints of other jobs, or dependent, which means they may depend on the timing constraints of other jobs.
- The timing constraints of a job may be strict, which means they must be satisfied exactly, or lax, which means they may be satisfied approximately.
- The timing constraints of a job may be mandatory, which means they must be satisfied for the correctness of the system, or optional, which means they may be satisfied for the optimality of the system.
- The release time of a job is one

Some possible mnemonics and learning tricks for the topic are:

- To remember the difference between hard and soft deadlines, think of hard as harsh and soft as smooth.
- To remember the difference between absolute and relative deadlines, think of absolute as fixed and relative as flexible.
- To remember the difference between static and dynamic timing constraints, think of static as stable and dynamic as changing.
- To remember the difference between explicit and implicit timing constraints, think of explicit as clear and implicit as hidden.
- To remember the difference between deterministic and stochastic timing constraints, think of deterministic as certain and stochastic as uncertain.
- To remember the difference between independent and dependent timing constraints, think of independent as isolated and dependent as connected.
- To remember the difference between strict and lax timing constraints, think of strict as precise and lax as approximate.
- To remember the difference between mandatory and optional timing constraints, think of mandatory as required and optional as desired.