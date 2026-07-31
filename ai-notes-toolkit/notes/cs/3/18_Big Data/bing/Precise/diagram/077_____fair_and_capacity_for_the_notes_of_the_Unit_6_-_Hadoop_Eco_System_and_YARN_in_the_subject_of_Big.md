# Unit 6 - Hadoop Eco System and YARN

### Fair and Capacity Scheduler

- There are mainly 3 types of Schedulers in Hadoop: FIFO (First In First Out) Scheduler, Capacity Scheduler, and Fair Scheduler .
- These Schedulers are actually a kind of algorithm that we use to schedule tasks in a Hadoop cluster when we receive requests from different clients .
- The Fair Scheduler is very much similar to that of the capacity scheduler. The priority of the job is kept in consideration .
- With the help of Fair Scheduler, the YARN applications can share the resources in the large Hadoop Cluster and these resources are maintained dynamically so no need for prior capacity .
- The resources are distributed in such a manner that all applications within a cluster get an equal amount of time .
- Fair scheduling is a method of assigning resources to applications such that all apps get, on average, an equal share of resources over time .
- Hadoop NextGen is capable of scheduling multiple resource types. By default, the Fair Scheduler bases scheduling fairness decisions only on memory .
- In Apache Hadoop YARN 3.x (YARN for short), switching to Capacity Scheduler has considerable benefits and only a few drawbacks .
- To bring these features to users who are currently using Fair Scheduler, a tool with the upstream YARN community was created to help the migration process .
- The maximum number of applications in the system which can be concurrently active both running and pending is determined by `yarn.scheduler.capacity.maximum-applications` or `yarn.scheduler.capacity.<queue-path>.maximum-applications` .
- Limits on each queue are directly proportional to their queue capacities and user limits .