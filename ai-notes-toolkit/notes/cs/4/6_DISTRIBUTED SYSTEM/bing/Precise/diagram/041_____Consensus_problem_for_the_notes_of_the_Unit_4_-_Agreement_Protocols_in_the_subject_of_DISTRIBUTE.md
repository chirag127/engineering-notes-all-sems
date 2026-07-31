# Consensus Problem in Distributed Systems

The consensus problem is a fundamental problem in distributed computing and multi-agent systems. It is the problem of getting a set of nodes in a distributed system to agree on something. This something might be a value, a course of action, or a decision .

Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network . This is important for achieving overall system reliability in the presence of a number of faulty processes.

There are many ways in which processes in a distributed system can reach a consensus. However, there is usually a constant struggle between security and performance. The more we want our algorithm to be secure against ways in which failure can happen, the less performant it tends to become.