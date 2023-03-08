 Here is the content written in Markdown format:

#### Introduction to NoSQL databases

NoSQL databases are non-relational databases that do not require a fixed schema and use JSON-like documents with key-value pairs. Some of the key points about NoSQL databases are:

- Schema-less: The schema can be dynamic in NoSQL databases. New columns can be added on the go. This provides flexibility and scalability.
- Distributed: The data in NoSQL databases is distributed across many nodes in a cluster. This provides high availability and horizontal scalability.
- Open source: Most of the popular NoSQL databases like MongoDB, CouchDB, Cassandra, HBase, etc. are open source.
- Diverse data models: There are four main types of NoSQL databases based on their data models:
    - Key-value store: Data is stored in an array of key-value pairs. Example: Redis
    - Document store: Data is stored in documents (instead of rows and columns in a table) like JSON/BSON documents. Example: MongoDB
    - Wide-column store: Data is stored in tables with columns, with columns stored together in column families. Example: Cassandra
    - Graph database: Data is stored in graph structures with relationships between data nodes. Example: Neo4J

Some of the advantages of NoSQL databases are:

- Scalability: NoSQL databases scale out easily by adding more servers into the cluster.
- Flexibility: The schema-less nature and different data models provide flexibility in evolving database needs.
- Performance: NoSQL databases can achieve fast read/write speeds with their distributed architecture and simpler data models.

However, some of the disadvantages are:

- Limited query capabilities: The query capabilities of NoSQL databases are limited as compared to SQL databases.
- Eventual consistency: The data in distributed NoSQL databases can become inconsistent temporarily until it gets replicated across all nodes.
- Lack of standards: There are no standard APIs or query languages for NoSQL databases. Each database uses its own methods.

NoSQL databases are gaining popularity due to their scalability and flexibility benefits. They are being used by many large companies for their data storage needs. However, they may not be a good fit if ACID transactions and complex joins are required. The choice between SQL and NoSQL databases depends on the use case and application requirements.