### System Models for the Notes of the Unit 4 - Agreement Protocols in the Subject of Distributed System

In order to achieve agreement among multiple nodes in a distributed system, various system models have been developed. These system models are designed to ensure that all nodes in the system are in agreement with each other, even in the presence of failures and network delays. Some of the commonly used system models are:

1. **Crash-recovery model**: In this model, a node can fail by crashing and then recover after some time. The system ensures that all nodes agree on a particular decision, even if some nodes fail and then recover. This is achieved by having the non-faulty nodes reach a consensus on the decision and then propagating it to the recovering nodes.

2. **Byzantine-fault-tolerant model**: This model is designed to handle arbitrary failures, including malicious ones. In this model, some nodes may behave incorrectly, but the system ensures that all correct nodes agree on a particular decision. This is achieved by having the correct nodes reach a consensus on the decision while ignoring the faulty ones.

3. **Synchronous model**: In this model, all nodes have access to a common clock and can execute operations in a synchronized manner. This model is useful for systems where precise timing is important, such as real-time systems.

4. **Asynchronous model**: In this model, nodes do not have access to a common clock and communication delays are unpredictable. This model is useful for systems where timing is less important, but fault tolerance is crucial.

5. **Leader-based model**: In this model, one node is designated as the leader and is responsible for making decisions on behalf of the system. The other nodes simply accept the decisions made by the leader. This model is useful for systems where a centralized authority is required.

In conclusion, understanding the different system models used for achieving agreement in distributed systems is crucial for developing reliable and fault-tolerant systems. Each model has its own advantages and disadvantages, and the choice of model depends on the specific requirements of the system.