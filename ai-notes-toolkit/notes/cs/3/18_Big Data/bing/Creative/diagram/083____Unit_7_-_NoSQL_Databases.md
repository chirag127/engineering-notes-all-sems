Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for Unit 7 - NoSQL Databases.

## Unit 7 - NoSQL Databases

- NoSQL stands for Not Only SQL, which means that it is a type of database that does not use the relational model or SQL language.
- NoSQL databases are designed to handle large volumes of unstructured, semi-structured, or dynamic data, such as social media posts, documents, graphs, or key-value pairs.
- NoSQL databases offer advantages such as scalability, flexibility, performance, and availability over relational databases, especially for big data applications.
- NoSQL databases can be classified into four main categories: document, key-value, column, and graph databases.

### Document databases
- Document databases store data as documents, which are self-describing collections of fields and values, usually in JSON or XML format.
- Document databases allow complex and nested data structures, and support dynamic schemas, which means that documents in the same collection can have different fields and types.
- Document databases are suitable for applications that need to store and query semi-structured data, such as e-commerce, content management, or blogging platforms.
- Examples of document databases are MongoDB, CouchDB, and DynamoDB.

### Key-value databases
- Key-value databases store data as pairs of keys and values, where the key is a unique identifier and the value can be any type of data, such as a string, a number, a file, or a binary object.
- Key-value databases are simple and fast, as they only support basic operations such as get, put, and delete by key.
- Key-value databases are suitable for applications that need to store and retrieve large amounts of simple data, such as caching, session management, or user preferences.
- Examples of key-value databases are Redis, Memcached, and Riak.

### Column databases
- Column databases store data as columns, which are collections of values that share the same attribute, rather than as rows, which are collections of attributes that describe the same entity.
- Column databases allow efficient storage and retrieval of sparse and wide data, as they only store the values that are present and compress the data by column.
- Column databases are suitable for applications that need to perform analytical queries on large and structured data sets, such as data warehousing, business intelligence, or recommendation systems.
- Examples of column databases are Cassandra, HBase, and Bigtable.

### Graph databases
- Graph databases store data as nodes and edges, which are entities and relationships, respectively, that form a graph structure.
- Graph databases allow complex and rich data modeling, and support traversal and path-finding queries, which are operations that explore the connections between nodes and edges.
- Graph databases are suitable for applications that need to store and query highly connected and networked data, such as social networks, fraud detection, or knowledge graphs.
- Examples of graph databases are Neo4j, OrientDB, and Titan.