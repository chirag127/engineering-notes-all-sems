 Here is the content in markdown format:

### Dynamic Versus Static Systems

- **Dynamic systems:** In dynamic systems, the task sets and their characteristics may change with time. The scheduler has to adapt to these changes by re-scheduling tasks. This requires computation and may introduce scheduling overhead and latency. Example: Soft real-time systems where task sets may vary dynamically.
- **Static systems:** In static systems, the task sets and their characteristics are known a priori and do not change with time. The scheduler can pre-compute an optimal schedule off-line. There is no scheduling overhead at run-time. Example: Hard real-time systems where task sets are typically static.

Advantages of static systems:

- No run-time overhead since scheduling is pre-computed.
- Can achieve optimal schedules.

Disadvantages of static systems:

- Inflexible to changes in task sets or their characteristics.
- Schedule must be re-computed if there are any changes.

Advantages of dynamic systems:

- Can adapt to changes in task sets or their characteristics.
- No re-computation of schedule required if tasks are added or removed.

Disadvantages of dynamic systems:

- Run-time scheduling overhead may lead to latency.
- Difficult to achieve optimal schedules.

Applications:

- Static systems: Hard real-time systems, control systems.
- Dynamic systems: Soft real-time systems, multimedia systems.

[Detailed diagrams and examples can be added if required.]