#### Introduction to NoSQL databases

- NoSQL databases are databases that do not use the SQL language or the relational model for data storage and retrieval.
- NoSQL stands for "not only SQL" or "non-relational" to emphasize the differences from the traditional relational databases that use tables, rows, and columns.
- NoSQL databases are designed to handle large volumes of unstructured, semi-structured, or structured data that may change rapidly or frequently.
- NoSQL databases offer flexible schemas, high scalability, high performance, and easy distribution across multiple nodes or servers.
- NoSQL databases can be classified into four main types based on their data model: document, key-value, wide-column, and graph.
- Document databases store data as documents, which are collections of key-value pairs that can have nested structures. Each document has a unique identifier and can have different fields and values. Examples of document databases are MongoDB, CouchDB, and Elasticsearch.
- Key-value databases store data as pairs of keys and values, where the key is a unique identifier and the value can be any type of data. Key-value databases are simple and fast, but do not support complex queries or relationships. Examples of key-value databases are Redis, DynamoDB, and Couchbase.
- Wide-column databases store data as columns, which are collections of key-value pairs that share the same key. Each column can have different attributes and values, and columns can be grouped into column families or tables. Wide-column databases are suitable for sparse, large, or dynamic data sets. Examples of wide-column databases are Cassandra, HBase, and Bigtable.
- Graph databases store data as nodes, which are entities with properties and values, and edges, which are relationships between nodes. Graph databases are ideal for modeling complex networks, hierarchies, or connections. Examples of graph databases are Neo4j, OrientDB, and ArangoDB.