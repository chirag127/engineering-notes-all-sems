 Here is the content written in Markdown format on the topic ## Unit 7 - NoSQL Databases:

## Unit 7 - NoSQL Databases

NoSQL databases are non-relational databases that do not require a fixed schema. They have scalable and flexible data models. The main types of NoSQL databases are:

1. Key-Value stores: Data is stored in an array of key-value pairs. Examples include Redis and DynamoDB.
- Keys are used to retrieve values.
- Keys and values are scalar data types like strings and integers.
- Useful for storing session data and cached data.

2. Document databases: Data is stored in documents (instead of rows/tables in a relational DB). Examples include MongoDB and CouchDB.
- Documents are organized in collections.
- Documents can be in JSON, XML, YAML, etc. format.
- Dynamic schemas - documents in a collection can have different fields.
- Useful for content management systems, blogging platforms, etc.

3. Wide-column stores: Stores data in columns instead of rows. Examples include Cassandra and HBase.
- Columns are grouped into column families.
- Each row can have a dynamic set of columns.
- Often optimized for range scans/queries.
- Useful for heavy write applications like analytics.

4. Graph databases: Stores data in graph structures with nodes, properties, and lines. Examples include Neo4J and JanusGraph.
- Fast for traversing and querying relationships.
- Useful for social networking applications, recommendation systems, etc.

Advantages of NoSQL databases:
- Scalable and distributed
- Open source
- Schema-less and flexible
- Performance with large data volumes and throughput

Disadvantages:
- Limited query capabilities (no SQL-like queries)
- Eventual consistency (data may not be consistent across nodes)
- Limited ACID transaction support

[Detailed diagrams, codes, tables, more examples, and applications can be included here if required.]