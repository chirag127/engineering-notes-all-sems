#### Schedulers in Hadoop ecosystem

- Schedulers are algorithms that manage the execution of tasks on a Hadoop cluster, based on the requests from different clients and the availability of resources.
- Schedulers help in ensuring optimal utilization of the resources and the access to the unused level of capacity.
- There are mainly three types of schedulers in Hadoop: FIFO, Capacity, and Fair.

##### FIFO Scheduler
- FIFO (First In First Out) is the default scheduling policy used in Hadoop.
- FIFO Scheduler gives more preference to the application coming first than those coming later.
- It places the applications in a queue and executes them in the order of their submission (first in, first out).
- FIFO Scheduler is simple and easy to implement, but it does not consider the priority or the size of the applications.
- FIFO Scheduler can cause starvation for the applications that are submitted later, especially if the earlier applications are long-running or resource-intensive.

##### Capacity Scheduler
- Capacity Scheduler is designed to run multiple applications on a Hadoop cluster, with different resource requirements and service level agreements.
- Capacity Scheduler divides the cluster into multiple queues, each with a configurable capacity and maximum limit.
- Each queue can have sub-queues to further divide the resources among different users or groups.
- Capacity Scheduler allocates resources to the applications in a queue based on their priority, and also allows preemption of resources from low-priority applications to high-priority ones.
- Capacity Scheduler supports elasticity, security, and multi-tenancy.

##### Fair Scheduler
- Fair Scheduler is another scheduler that supports running multiple applications on a Hadoop cluster, with the goal of providing fair and efficient sharing of resources.
- Fair Scheduler assigns resources to applications such that each application gets an equal share of the cluster over time, regardless of the order of submission or the size of the applications.
- Fair Scheduler also allows the creation of multiple queues, each with a minimum and maximum share of resources, and a weight to indicate the relative importance of the queue.
- Fair Scheduler dynamically adjusts the resource allocation based on the demand and the availability of the cluster, and also supports preemption of resources from low-weight queues to high-weight ones.

##### Mnemonics and learning tricks
- A possible mnemonic to remember the three types of schedulers in Hadoop is **F**air **C**apacity **F**IFO, which sounds like a phrase "fair capacity fee for".
- A possible learning trick to compare the three types of schedulers in Hadoop is to use a real-life analogy of a restaurant. FIFO Scheduler is like a restaurant that serves customers in the order of arrival, without considering their preferences or the size of their orders. Capacity Scheduler is like a restaurant that has different sections for different types of customers, such as VIP, regular, or walk-in, and allocates resources to each section based on their capacity and priority. Fair Scheduler is like a restaurant that tries to balance the needs of all customers, by giving each customer an equal share of the resources over time, and adjusting the allocation based on the demand and the availability of the resources.