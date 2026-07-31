#### Schema design in HBase

- HBase is a NoSQL database that stores data in a tabular format, where each row has a unique key and each column belongs to a column family.
- HBase does not support joins, but it allows denormalization and nested entities, which are columns that store complex values as serialized bytes .
- HBase schema design is driven by the access patterns and performance requirements of the application, rather than the structure and relationships of the data.
- Some general principles for HBase schema design are  :
  - Choose a row key that is unique, short, and sortable, and that supports the most frequent queries.
  - Use column families to group related columns together, and keep the number of column families low (usually less than five).
  - Use column qualifiers to store dynamic or sparse attributes, and avoid using them as secondary indexes.
  - Use filters, scanners, and coprocessors to optimize read performance and reduce network traffic.
  - Use compression, bloom filters, and block cache to reduce disk and memory usage.
  - Use versioning, TTL, and compaction to manage data lifecycle and garbage collection.