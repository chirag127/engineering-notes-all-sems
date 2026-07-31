#### Schedulers in Hadoop Ecosystem

Schedulers in Hadoop are general purpose systems that allow the system to perform high level performance processing of data on distributed node sets known as Hadoop. They also help in ensuring optimum utilization of resources and access to unused levels of capacity .

There are mainly 3 types of Schedulers in Hadoop  :

1. **FIFO (First In First Out) Scheduler:** This scheduler schedules tasks in the order they are received.
2. **Capacity Scheduler:** This scheduler is designed to allow multiple tenants to share a large cluster while maximizing the utilization of the resources.
3. **Fair Scheduler:** This scheduler assigns resources to jobs in a way that all jobs get, on average, an equal share of resources over time.

These Schedulers are actually a kind of algorithm that is used to schedule tasks in a Hadoop cluster when requests are received from different clients .