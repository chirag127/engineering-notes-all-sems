# Schedulers for the notes of the Unit 6 - Hadoop Eco System and YARN in the subject of Big Data

- Schedulers are algorithms that allocate resources to applications running on a Hadoop cluster based on some criteria, such as fairness, capacity, priority, etc.
- Schedulers are part of the Resource Manager component in YARN, which is the framework for managing and executing distributed applications on Hadoop.
- Schedulers are pluggable, meaning that different schedulers can be used depending on the needs and policies of the cluster.
- There are mainly three types of schedulers in Hadoop: FIFO, Capacity, and Fair.

## FIFO Scheduler
- FIFO (First In First Out) Scheduler is the simplest and default scheduler in Hadoop.
- It assigns resources to applications in the order of their submission, without considering any other factors.
- It is suitable for small clusters with homogeneous and short-lived applications.
- It does not support priorities, queues, preemption, or resource sharing.

## Capacity Scheduler
- Capacity Scheduler is a scheduler that allows multiple tenants to share a large cluster in a secure and scalable manner.
- It organizes applications into queues, each with a configurable capacity, maximum limit, priority, ACL, etc.
- It ensures that each queue gets its fair share of resources, while allowing for elasticity and over-allocation when there is spare capacity.
- It supports preemption, which means that it can reclaim resources from low-priority or under-utilized applications to satisfy the demand of high-priority or starved applications.
- It also supports hierarchical queues, which can be nested to create sub-queues with different properties.

## Fair Scheduler
- Fair Scheduler is a scheduler that aims to provide fair and equal allocation of resources to applications, regardless of their submission order or queue.
- It dynamically adjusts the resource share of each application based on the current demand and availability of resources, using a concept called weights.
- Weights are assigned to applications based on various factors, such as user, pool, priority, etc., and determine the fraction of resources that each application should receive.
- Fair Scheduler also supports preemption, hierarchical queues, and min/max shares, which can be used to enforce minimum and maximum resource guarantees for applications or pools.