MongoDB is a document-oriented database that stores data in JSON-like format. It is designed to meet the demands of modern applications with a distributed and scalable architecture. MongoDB consists of the following components:

- **mongod**: The core database process that handles data requests, manages data access, and performs background management operations.
- **mongos**: The query router that provides access to a sharded cluster.
- **config server**: The metadata store that holds the configuration information and the shard key ranges for a sharded cluster.
- **replica set**: A group of mongod instances that maintain the same data set and provide high availability and data redundancy.
- **shard**: A partition of data in a sharded cluster, which is stored on a replica set.
- **document**: The basic unit of data in MongoDB, which is composed of field-value pairs.
- **collection**: A grouping of documents that have a similar or related purpose.
- **database**: A logical container for collections that can have different access control and configuration settings.

The following diagram illustrates the basic architecture of a MongoDB sharded cluster:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  config server  |     |  config server  |     |  config server  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
          |                     |                     |
          +---------------------+---------------------+
                            |
                            |
                            v
+---------------------------------------------------------------+
|                                                               |
|                          mongos                               |
|                                                               |
+---------------------------------------------------------------+
          |                     |                     |
          |                     |                     |
          v                     v                     v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    shard 1      |     |    shard 2      |     |    shard 3      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  replica set 1  |     |  replica set 2  |     |  replica set 3  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```