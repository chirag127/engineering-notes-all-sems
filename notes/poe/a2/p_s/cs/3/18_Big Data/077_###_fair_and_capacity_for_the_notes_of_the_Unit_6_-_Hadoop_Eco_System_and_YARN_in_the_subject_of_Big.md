 Here is the content in markdown format for the topic ### fair and capacity for the notes of the Unit 6 - Hadoop Eco System and YARN in the subject of Big Data:

### Fair Scheduler and Capacity Scheduler

- Fair Scheduler: It is a scheduling algorithm for Hadoop YARN that aims for fairness and efficiency. It ensures that each application gets roughly equal allocation of resources over time. It allocates resources to applications based on the number of containers they are allowed or allocated.
- Capacity Scheduler: It is a multi-tenant scheduler for Hadoop YARN that supports multiple organizations, users, and applications with differing capacity guarantees and sharing policies. It allows organizations and users to be allocated a guaranteed minimum capacity that is isolated from others. It can deploy applications with differentiated capacities and supports priorities and preemption of lower priority applications.
- Comparison:
-- Fair Scheduler is good for single organisation with different users and teams with equal shares of resources. Capacity Scheduler is good for multi-tenant Hadoop cluster shared by different organisations.
-- Fair Scheduler uses a first-in-first-out (FIFO) queue whereas Capacity Scheduler uses hierarchical queues.
-- Fair Scheduler is simpler to configure while Capacity Scheduler provides more powerful resource management capabilities with complex configuration.

Examples and diagrams can be added to further explain the concepts. The advantages and disadvantages of each scheduler and their use cases can be discussed in detail. The applications of these schedulers in real-world big data problems can also be included. Overall, the content can be expanded with more details and examples to make it comprehensive for learning and exams.