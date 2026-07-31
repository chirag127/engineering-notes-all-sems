# Dynamic Versus Static Systems

- A **dynamic system** is one that changes its behavior or configuration in response to external events or inputs, such as workload, resource availability, or user requests.
- A **static system** is one that has a fixed and predetermined behavior or configuration that does not change during its operation, such as task set, task priorities, or resource allocation.
- Dynamic and static systems have different advantages and disadvantages for real-time scheduling, depending on the characteristics and requirements of the application domain.

## Advantages of Dynamic Systems

- Dynamic systems can adapt to changing conditions and unpredictable events, such as varying workload, resource failures, or user preferences.
- Dynamic systems can optimize the performance metrics of the system, such as response time, throughput, or utilization, by making scheduling decisions based on the current state of the system and the environment.
- Dynamic systems can handle a larger and more diverse set of tasks, as they do not need to know the task parameters or dependencies in advance.

## Disadvantages of Dynamic Systems

- Dynamic systems incur more overhead and complexity for making scheduling decisions at run-time, as they need to collect and process information about the system and the environment.
- Dynamic systems are harder to analyze and verify, as they may exhibit non-deterministic or unpredictable behavior, depending on the inputs and events that occur during the system operation.
- Dynamic systems may not guarantee the satisfaction of the timing constraints of the tasks, as they may not have enough information or resources to schedule all the tasks within their deadlines.

## Advantages of Static Systems

- Static systems have less overhead and complexity for making scheduling decisions, as they are done before the system runs, based on the known task parameters and dependencies.
- Static systems are easier to analyze and verify, as they exhibit deterministic and predictable behavior, regardless of the inputs and events that occur during the system operation.
- Static systems can guarantee the satisfaction of the timing constraints of the tasks, as they can check the feasibility of the schedule before the system runs, and reject any task set that is not schedulable.

## Disadvantages of Static Systems

- Static systems cannot adapt to changing conditions and unpredictable events, such as varying workload, resource failures, or user preferences.
- Static systems may not optimize the performance metrics of the system, such as response time, throughput, or utilization, as they may not exploit the opportunities or cope with the challenges that arise during the system operation.
- Static systems can handle a smaller and more restricted set of tasks, as they need to know the task parameters and dependencies in advance, and may not accept any task set that is not schedulable.