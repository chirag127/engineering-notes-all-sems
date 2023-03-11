### Fair and Capacity for the Notes of Unit 6 - Hadoop Eco System and YARN in the Subject of Big Data

In the Hadoop ecosystem, managing resources efficiently is crucial to ensure optimal performance. Fair and Capacity Scheduler are two scheduling algorithms used in the Hadoop ecosystem that help in managing resources effectively.

#### Fair Scheduler

The Fair Scheduler is a scheduling algorithm used in Hadoop's YARN (Yet Another Resource Negotiator) that allocates resources based on the application's need. It ensures that each application gets an equal share of resources, regardless of the application's priority. Here are some key features of the Fair Scheduler:

- Fairness: The Fair Scheduler ensures that all applications get an equal share of resources, regardless of their priority.
- Preemption: The Fair Scheduler supports preemption, which allows the scheduler to interrupt a running application if a higher-priority application needs resources.
- Hierarchical Queues: The Fair Scheduler allows the creation of hierarchical queues, which helps in organizing and prioritizing jobs based on their importance.
- Configurable: The Fair Scheduler is highly configurable and can be customized to suit specific requirements.

#### Capacity Scheduler

The Capacity Scheduler is another scheduling algorithm used in Hadoop's YARN that allocates resources based on the application's priority. It allows for the creation of multiple queues, each with a specific capacity. Here are some key features of the Capacity Scheduler:

- Prioritization: The Capacity Scheduler allows for prioritization of applications based on their importance.
- Resource Guarantees: The Capacity Scheduler guarantees a minimum amount of resources for each queue, ensuring that no queue is starved of resources.
- Overcommitment: The Capacity Scheduler supports overcommitment, which allows for more resources to be allocated to an application if they are available.
- Configurable: The Capacity Scheduler is highly configurable and can be customized to suit specific requirements.

#### Fair Scheduler vs. Capacity Scheduler

- Fairness: The Fair Scheduler ensures that all applications get an equal share of resources, while the Capacity Scheduler prioritizes applications based on their importance.
- Preemption: The Fair Scheduler supports preemption, while the Capacity Scheduler does not.
- Resource Guarantees: The Capacity Scheduler guarantees a minimum amount of resources for each queue, ensuring that no queue is starved of resources, while the Fair Scheduler does not.
- Overcommitment: The Capacity Scheduler supports overcommitment, while the Fair Scheduler does not.

In conclusion, both the Fair Scheduler and Capacity Scheduler are important scheduling algorithms used in Hadoop's YARN. The choice of scheduling algorithm depends on the specific requirements of the application. The Fair Scheduler is ideal for applications that require fairness in resource allocation, while the Capacity Scheduler is ideal for applications that require prioritization based on importance.