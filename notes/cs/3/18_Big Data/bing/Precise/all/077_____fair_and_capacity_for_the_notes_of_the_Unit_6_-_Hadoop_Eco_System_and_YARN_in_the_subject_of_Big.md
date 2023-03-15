# Unit 6 - Hadoop Eco System and YARN

### Fair and Capacity Scheduler

- There are mainly 3 types of Schedulers in Hadoop: FIFO (First In First Out) Scheduler, Capacity Scheduler, and Fair Scheduler .
- The Fair Scheduler is very much similar to that of the capacity scheduler. The priority of the job is kept in consideration .
- With the help of Fair Scheduler, the YARN applications can share the resources in the large Hadoop Cluster and these resources are maintained dynamically so no need for prior capacity .
- Fair scheduling is a method of assigning resources to applications such that all apps get, on average, an equal share of resources over time .
- The CapacityScheduler is designed to allow sharing a large cluster while giving each organization capacity guarantees .
- The central idea is that the available resources in the Hadoop cluster are shared among multiple organizations who collectively fund the cluster based on their computing needs .
- In Apache Hadoop YARN 3.x (YARN for short), switching to Capacity Scheduler has considerable benefits and only a few drawbacks .
- To bring these features to users who are currently using Fair Scheduler, a tool has been created with the upstream YARN community to help the migration process .