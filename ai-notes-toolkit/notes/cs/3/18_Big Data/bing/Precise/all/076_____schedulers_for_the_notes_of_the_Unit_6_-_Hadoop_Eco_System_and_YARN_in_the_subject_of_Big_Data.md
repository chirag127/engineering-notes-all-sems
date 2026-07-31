### Schedulers for the notes of the Unit 6 - Hadoop Eco System and YARN in the subject of Big Data

Schedulers are responsible for allocating resources to applications in a fair and efficient manner. In the context of Hadoop and YARN, there are several schedulers available, each with its own set of features and capabilities.

1. **FIFO Scheduler**: The FIFO (First In, First Out) scheduler is the simplest scheduler available in YARN. It schedules jobs in the order in which they are submitted, without considering the size or complexity of the jobs.

2. **Capacity Scheduler**: The Capacity Scheduler is designed to allow multiple tenants to share a large cluster while ensuring that each tenant receives a guaranteed minimum share of the resources. It allows for the configuration of queues, each with its own set of resources and policies.

3. **Fair Scheduler**: The Fair Scheduler is designed to allocate resources to applications in a fair manner, such that all applications get an equal share of the resources over time. It supports hierarchical queues and allows for the configuration of minimum and maximum resource shares for each queue.

4. **Dominant Resource Fairness (DRF) Scheduler**: The DRF scheduler is an extension of the Fair Scheduler that takes into account the dominant resource when allocating resources to applications. This ensures that applications that require a large amount of a particular resource, such as memory or CPU, are not starved of that resource.

These are some of the schedulers available in the Hadoop ecosystem and YARN. Each scheduler has its own set of features and capabilities, and the choice of scheduler will depend on the specific requirements of the cluster and its users.