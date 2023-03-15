 Here is the content in markdown format with formal tone and without any emojis or external links:

### HBase

1. HBase is a distributed, scalable, big data store.
2. It is an open-source, non-relational, distributed database modeled after Google's Bigtable.
3. It is written in Java and runs on top of Hadoop, providing BigTable-like capabilities for Hadoop.
4. HBase uses Hadoop's distributed file system (HDFS) to store data on multiple machines and employs a master-slave architecture.
5. The master server assigns regions to region servers and coordinates load balancing and recovery.
6. Region servers manage subsets of rows in tables and handle read/write requests and hold the in-memory caches of recently accessed data.
7. HBase provides random real-time read/write access to Big Data. The rows are lexicographically sorted by row key.
8. HBase scaling is horizontal (by adding more machines to the cluster). It distributes and partitions data across machines.
9. HBase has strong consistency and is typically specified as having single-version concurrency control (KV). The latest update to a cell always overrides any previous updates.
10. HBase supports sparse data structures, ordered access, and range scans. Queries can be expressed through SQL-like languages (HiveQL), Maps Reduce, or via Java API.

Does this meet your requirements? Let me know if you would like me to modify or expand the content in any way.