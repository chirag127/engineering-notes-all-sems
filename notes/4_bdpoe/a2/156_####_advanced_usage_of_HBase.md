 Here is the content in markdown format for #### advanced usage of HBase:

#### Advanced usage of HBase

-   Secondary Indexes: HBase supports secondary indexes on column families which can speed up queries. These are basically additional HTables which store the main rowkey and a secondary key. Queries can be made on the secondary key and then the main rowkey can be obtained to get the final data.
-   Bloom Filters: Bloom filters are a space-efficient probabilistic data structure which can be used to check if a certain rowkey exists in a HTable or not. This can save a lot of I/O operations and increase speed. They give false positives but no false negatives.
-   Bulk Loading: HBase provides a bulk loader utility which can be used to load a large amount of data into HBase very fast. The data must be in HBase format. This bypasses a lot of normal constraints to achieve high speed.
-   Coprocessors: These are like user-defined functions which can operate on HBase tables. They are used to achieve custom processing on HBase tables, something beyond the normal get, put and scan operations. Examples include data validation, secondary indexing maintenance, etc.
-   Multi-Version Concurrency Control: HBase supports multiple versions of data to be stored together with timestamps. This enables concurrency as multiple people can edit and commit data simultaneously as long as the versions are distinguished by timestamps. The latest version can always be seen.
-   HBase on Top of Other Databases: Although HBase is a database on its own, it can also be run on top of other databases to take advantage of their features. For example, HBase on top of Hadoop provides scalability while HBase on a relational database provides ACID compliance.

Here are some Mnemonics and learning tricks for the advanced usage of HBase:

- Secondary Indexes: Think of a normal index in a book. HBase secondary indexes work similarly by containing rowkeys and secondary keys for fast lookup.
- Bloom Filters: Think of a filter which may let some false positives pass through (wrong data) but will never give false negatives (miss correct data). This is how HBase Bloom filters work to save I/O.
- Coprocessors: Think of co-processors in a CPU. HBase Coprocessors also work alongside the main table processing to provide custom processing.

The above points, diagrams, examples, etc. can help in learning and understanding the advanced usage of HBase in depth for exams and study purposes. Please let me know if you would like me to elaborate on any of the points or add additional details.