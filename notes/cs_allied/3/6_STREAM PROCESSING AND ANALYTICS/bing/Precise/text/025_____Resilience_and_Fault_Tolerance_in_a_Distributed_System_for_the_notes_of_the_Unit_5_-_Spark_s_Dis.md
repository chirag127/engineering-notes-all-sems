### Resilience and Fault Tolerance in a Distributed System

- **Resilience** is the use of strategies for improving a distributed system’s availability. One of the primary goals of resilience is to prevent situations where an issue with one microservice instance causes more issues, which escalate and eventually lead to distributed system failure. This is known as a cascading failure.

- **Fault tolerance** refers to the ability of a system to continue functioning in the event of a failure. In the context of distributed systems, this means that the system is able to continue operating even if one or more of its components fail.

- Fault tolerance in distributed systems is achieved through techniques such as process resilience, reliable multicasting, and others. Process resilience refers to techniques by which one or more processes can fail without seriously disturbing the rest of the system. Reliable multicasting, on the other hand, refers to the guaranteed transmission of messages to a collection of processes.

- The need for fault tolerance in distributed systems arises from the need for reliability, availability, and security. Reliability refers to the continuous working of the system without any issue, while availability refers to the feature of the system to have a continuous flow of data between the system and the user.

- Distributed systems are made up of both software and hardware components. The availability of both the underlying hardware and software components affects the resulting availability of the workload.