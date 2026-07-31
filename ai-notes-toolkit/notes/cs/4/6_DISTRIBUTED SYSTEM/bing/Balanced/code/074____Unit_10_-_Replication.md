## Unit 10 - Replication

- Replication is the process of creating and maintaining multiple copies of the same data on different database servers.
- Replication provides benefits such as high availability, fault tolerance, load balancing, and scalability.
- Replication can be classified into different types based on the direction, timing, and location of data transfer.
- The main types of replication are:
  - Snapshot replication: A snapshot of the data is taken at a point in time and copied to the subscribers. The data is not synchronized until the next snapshot is taken.
  - Transactional replication: Changes made to the data at the publisher are captured and sent to the subscribers as they occur. The data is synchronized in near real time.
  - Merge replication: Changes made to the data at the publisher and the subscribers are tracked and merged periodically. The data is synchronized based on a predefined schedule or on demand.
  - Peer-to-peer replication: Changes made to the data at any node in a peer-to-peer topology are propagated to all other nodes. The data is synchronized in near real time and all nodes are equal.
- Replication involves the following components:
  - Publisher: The database server that publishes the data to be replicated.
  - Distributor: The database server that stores the replication metadata and distributes the data to the subscribers.
  - Subscriber: The database server that receives the data from the publisher or the distributor.
  - Publication: The set of data that is published by the publisher.
  - Subscription: The request for the data that is made by the subscriber.
  - Article: The smallest unit of data that can be replicated, such as a table, a view, or a stored procedure.
  - Agent: The software component that performs the replication tasks, such as copying, distributing, merging, or monitoring the data.