### Schedulers for the notes of the Unit 6 - Hadoop Eco System and YARN in the subject of Big Data

- Schedulers are algorithms that allocate resources to applications running on a Hadoop cluster based on some criteria  .
- Schedulers are pluggable components in YARN, the resource management layer of Hadoop .
- Schedulers can have different policies and configurations to achieve different goals, such as fairness, capacity, priority, etc   .
- There are mainly three types of schedulers in Hadoop: FIFO (First In First Out) Scheduler, Capacity Scheduler, and Fair Scheduler .
- FIFO Scheduler: This is the simplest and default scheduler in Hadoop. It assigns resources to applications in the order of their submission, without considering the resource requirements or the priority of the applications.
- Capacity Scheduler: This scheduler allows multiple queues to share the cluster resources, each with a configurable capacity and limit. The queues can be hierarchical and support access control and preemption .
- Fair Scheduler: This scheduler aims to provide equal and fair share of resources to all applications over time, regardless of the order of submission. It also supports hierarchical queues, access control, preemption, and weight-based shares .
- Schedulers can be configured and tuned by modifying the configuration files such as yarn-site.xml, capacity-scheduler.xml, and fair-scheduler.xml  .
- Schedulers are important for optimizing the performance, efficiency, and utilization of the cluster resources, as well as ensuring the quality of service and fairness for the applications  .