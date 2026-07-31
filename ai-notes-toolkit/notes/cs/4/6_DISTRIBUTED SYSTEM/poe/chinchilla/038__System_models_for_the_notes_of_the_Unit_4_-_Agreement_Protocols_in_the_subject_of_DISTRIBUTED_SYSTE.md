### System Models for the Notes of Unit 4 - Agreement Protocols in the Subject of Distributed System

In distributed systems, agreement protocols are critical for ensuring that all nodes in the system agree on a particular decision or outcome. These protocols help to prevent inconsistencies that can arise due to communication delays, node failures, or other factors. However, to understand agreement protocols, it is first necessary to understand the different system models that are used in distributed systems. 

The following are the different system models used in distributed systems:

1. Synchronous Model: In this model, there is a known bound on the time taken for message delivery, processing, and response. This model is easy to reason about and allows for straightforward implementation of agreement protocols. However, it assumes that all nodes in the system have clocks that are synchronized with each other.

2. Partially Synchronous Model: In this model, there is no known bound on the time taken for message delivery, processing, and response. However, the system is assumed to be synchronous for a certain period of time, after which it becomes asynchronous. This model allows for more flexibility in the system but makes the implementation of agreement protocols more challenging.

3. Asynchronous Model: In this model, there is no assumption about the time taken for message delivery, processing, and response. This model is the most challenging to reason about and requires the use of advanced techniques such as timeouts and failure detectors to implement agreement protocols.

It is important to note that the choice of system model depends on the specific requirements of the distributed system. For example, if the system requires high consistency guarantees, then the synchronous model may be more appropriate. On the other hand, if the system can tolerate some level of inconsistency, then the asynchronous model may be more suitable.

In conclusion, understanding the different system models used in distributed systems is essential for designing and implementing effective agreement protocols. Depending on the specific requirements of the system, different models may be more appropriate, and it is important to choose the right model for the job.