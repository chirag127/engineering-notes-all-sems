Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for Unit 10 - Replication.

## Unit 10 - Replication

- Replication is the process of creating and maintaining multiple copies of the same data on different database servers.
- Replication can improve the availability, performance, and scalability of a database system.
- Replication can also provide data redundancy and backup, as well as facilitate data distribution and synchronization across different locations.
- Replication can be classified into different types based on the following criteria:

  - The direction of data flow: unidirectional, bidirectional, or multidirectional.
  - The timing of data transfer: synchronous, asynchronous, or semi-synchronous.
  - The granularity of data transfer: statement-based, row-based, or mixed.
  - The topology of replication: master-slave, master-master, peer-to-peer, or hierarchical.

- Replication can also be categorized into different modes based on the consistency level of the replicated data:

  - Snapshot replication: the data is copied from the source to the target at a specific point in time, and then remains unchanged until the next snapshot is taken.
  - Transactional replication: the data is copied from the source to the target as transactions are committed, and then applied in the same order and with the same atomicity and isolation properties as the source.
  - Merge replication: the data is copied from the source to the target initially, and then changes are tracked and merged periodically or on demand, allowing for updates to occur at both the source and the target.
  - Conflict detection and resolution: replication can encounter conflicts when the same data is updated by different sources or targets, or when the data is corrupted or lost due to network or system failures. Replication can use different methods to detect and resolve conflicts, such as timestamps, version numbers, primary keys, or user-defined rules.