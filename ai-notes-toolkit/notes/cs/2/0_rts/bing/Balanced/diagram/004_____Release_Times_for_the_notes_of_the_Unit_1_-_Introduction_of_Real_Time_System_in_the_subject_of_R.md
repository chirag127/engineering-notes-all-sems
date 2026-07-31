### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real-time system is a system that must respond to events within a specified time interval, otherwise it may fail to meet its requirements or cause undesirable consequences.
- A real-time system can be classified into two types: hard real-time and soft real-time.
- A hard real-time system is a system that must meet its deadlines strictly, otherwise it may cause catastrophic failure or severe damage. For example, a nuclear reactor control system, a flight control system, or a pacemaker.
- A soft real-time system is a system that can tolerate some degree of deadline misses, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- A real-time task is a unit of work that must be executed by a real-time system. A real-time task has three main attributes: release time, execution time, and deadline.
- The release time of a real-time task is the earliest time that the task is ready to be executed by the system. The release time may be periodic, aperiodic, or sporadic.
- A periodic task is a task that has a fixed release time interval, which is also called the period. For example, a task that is released every 10 milliseconds.
- An aperiodic task is a task that has a variable release time interval, which may depend on external events or user inputs. For example, a task that is released whenever a user presses a button.
- A sporadic task is a task that has a minimum release time interval, which is also called the minimum inter-arrival time. For example, a task that is released at least 5 milliseconds apart, but may be longer.
- The execution time of a real-time task is the amount of time that the task needs to complete its work. The execution time may be deterministic, probabilistic, or unknown.
- A deterministic task is a task that has a fixed execution time, which is also called the worst-case execution time. For example, a task that always takes 3 milliseconds to finish.
- A probabilistic task is a task that has a variable execution time, which follows a certain probability distribution. For example, a task that takes 2 milliseconds with 90% probability, and 4 milliseconds with 10% probability.
- An unknown task is a task that has an unpredictable execution time, which may depend on the input data, the system state, or the environment. For example, a task that takes different time to process different images.
- The deadline of a real-time task is the latest time that the task must finish its execution, otherwise it may miss its deadline. The deadline may be implicit, explicit, or constrained.
- An implicit deadline is a deadline that is equal to the release time of the next instance of the same task. For example, a periodic task with a period of 10 milliseconds and an execution time of 3 milliseconds has an implicit deadline of 10 milliseconds.
- An explicit deadline is a deadline that is specified separately from the release time and the period. For example, an aperiodic task with a release time of 15 milliseconds and an execution time of 4 milliseconds has an explicit deadline of 25 milliseconds.
- A constrained deadline is a deadline that is less than or equal to the release time of the next instance of the same task. For example, a periodic task with a period of 10 milliseconds and an execution time of 3 milliseconds has a constrained deadline of 8 milliseconds.