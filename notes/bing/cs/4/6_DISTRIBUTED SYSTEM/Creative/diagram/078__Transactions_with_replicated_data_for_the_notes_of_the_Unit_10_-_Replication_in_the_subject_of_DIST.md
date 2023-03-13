The following diagram illustrates the basic architecture of a transactional replication system, which is a type of data replication that automatically distributes frequent data changes amongst servers . It consists of three main components: the publisher, the distributor, and the subscriber. The publisher is the source of the data that is replicated to one or more subscribers. The distributor is a database that stores the replication metadata and the transactions that are marked for replication in the publisher's transaction log. The subscriber is the destination of the data that is replicated from the publisher. The replication agents are processes that perform the tasks of copying and applying the data changes, such as the Log Reader Agent, the Snapshot Agent, and the Distribution Agent.

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Publisher    |      |   Distributor  |      |   Subscriber   |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Data source   |      |  Metadata and  |      |  Data target   |
|                |      |  transactions  |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
| Transaction log|      |                |      |                |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
| Snapshot Agent |----->| Log Reader     |----->| Distribution   |
|                |      | Agent          |      | Agent          |
+----------------+      +----------------+      +----------------+
```