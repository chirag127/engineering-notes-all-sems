 Here is the formal content on how to build applications with Zookeeper:

#### How to build applications with Zookeeper

1. Choose a use case for Zookeeper
Zookeeper is suited for applications that require:
- Coordination between processes or machines. For example, ensuring only one process performs a task at a time.
- Reliably storing and retrieving small amounts of configuration or synchronization data.
- Detecting failed nodes or processes and maintaining availability in the event of failures.

Some example use cases include:

- electing a leader from a set of machines to perform a task
- distributing work queues
- naming and configuration services
- detecting node failures

2. Design your data model
Data in Zookeeper is structured in a hierarchical namespace, much like a file system. You will need to design a suitable path structure to store your application data.
Some guidelines:

- Keep paths short and name nodes meaningfully
- Avoid deeply nested paths
- Consider using sequential nodes to avoid conflicts
- Store small amounts of data - Zookeeper is not a database

3. Choose a client library
There are Zookeeper client libraries available for many programming languages. These will handle the low-level connectivity and server interaction for you.
Some options include:

- Java: ZooKeeper
- Python: kazoo
- C: libzookeeper

The client will allow you to:

- Connect to a Zookeeper cluster
- Create, read, update and delete nodes
- Handle watches and notifications
- Deal with errors and connection loss gracefully

4. Handle errors and edge cases
When building a robust Zookeeper application, you must handle various error scenarios and edge cases, including:

- Connection loss to the Zookeeper cluster
- Network partitions isolating part of the cluster
- Nodes being deleted or modified unexpectedly
- Session expiration

By handling these scenarios gracefully, you can build an application that is resilient to the types of issues that can occur in distributed systems.