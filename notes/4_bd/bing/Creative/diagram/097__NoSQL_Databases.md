NoSQL databases are databases that do not use the standard tabular relations used in relational databases. They are designed to handle large volumes of unstructured or semi-structured data in a scalable and fast way. They also offer more flexibility and control over data consistency and availability. There are different types of NoSQL databases, such as key-value, document, wide column, and graph databases. Each type has its own data model, query language, and use cases.

### NoSQL Databases

```
+----------------+----------------+----------------+----------------+
| Key-Value      | Document       | Wide Column    | Graph          |
+----------------+----------------+----------------+----------------+
| Data model:    | Data model:    | Data model:    | Data model:    |
| A collection   | A collection   | A collection   | A collection   |
| of key-value   | of documents,  | of rows        | of nodes and   |
| pairs, where   | where each     | organized into | edges, where   |
| each key is    | document is a  | column         | each node is   |
| unique and     | JSON-like      | families,      | an entity and  |
| maps to a      | object with    | where each     | each edge is a |
| value.         | fields and     | column family  | relationship   |
|                | values.        | is a group of  | between nodes. |
|                |                | related        |                |
|                |                | columns.       |                |
+----------------+----------------+----------------+----------------+
| Query          | Query          | Query          | Query          |
| language:      | language:      | language:      | language:     |
| Simple         | JSON-based     | CQL (Cassandra | Graph-based    |
| operations     | queries or     | Query          | queries such   |
| such as GET,   | MongoDB Query  | Language) or   | as Gremlin or  |
| PUT, DELETE    | Language       | HBase API      | Cypher         |
| based on keys. |                |                |                |
+----------------+----------------+----------------+----------------+
| Use cases:     | Use cases:     | Use cases:     | Use cases:     |
| Caching,       | Content        | Time series    | Social         |
| session        | management,    | data,          | networks,      |
| management,    | e-commerce,    | analytics,     | recommendation |
| user           | IoT,           | log data       | engines, fraud |
| preferences,   | personalization|                | detection      |
| etc.           | etc.           |                | etc.           |
+----------------+----------------+----------------+----------------+
| Examples:      | Examples:      | Examples:      | Examples:      |
| Redis,         | MongoDB,       | Cassandra,     | Neo4j,         |
| Memcached,     | Couchbase,     | HBase,         | JanusGraph,    |
| DynamoDB,      | CouchDB,       | Bigtable       | ArangoDB       |
| Riak           | Cosmos DB      |                |                |
+----------------+----------------+----------------+----------------+
```