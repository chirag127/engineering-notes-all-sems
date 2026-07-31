#### Fair and Capacity in Hadoop Ecosystem

Hadoop is a batch processing ecosystem that cannot analyze data on-the-fly. In Hadoop, there are mainly 3 types of Schedulers: FIFO (First In First Out) Scheduler, Capacity Scheduler, and Fair Scheduler. These Schedulers are actually a kind of algorithm that we use to schedule tasks in a Hadoop cluster when we receive requests from different-different clients.

Fair Scheduler allows YARN applications to justly share resources in large Hadoop clusters. With this scheduler, there is no need for reserving a set amount of capacity because it will dynamically balance resources between all running applications. The priority of the job is kept in consideration.

Fair scheduling is a method of assigning resources to jobs such that all jobs get, on average, an equal share of resources over time. When there is a single job running, that job uses the entire cluster. When other jobs are submitted, tasks slots that free up are assigned to the new jobs, so that each job gets roughly the same amount of CPU time.

The two top tools to schedule a job in Hadoop are Capacity and Fair.