 Here is the content in Markdown format with formal tone and without any emojis or external links:

#### Advanced Indexing in HBase

1. Secondary Indexes
- HBase supports secondary indexes on column values. This speeds up the query performance as you don't have to scan the entire row to fetch the data.
- The secondary index table stores the main table row key and the column value on which the index is created.
- During querying, the secondary index table is scanned first to get the row keys and then the main table is accessed using the row keys to fetch the data.

2. Filtering using PrefixTree
- HBase provides a PrefixTree based row filtering option which efficiently filters the rows when the filter criteria is based on the row key prefix.
- This avoids full table scan and provides a fast way to fetch the rows having row key matching a certain prefix.

3. Bloom Filters
- Bloom filters can be used to check if a given row exists in the table or not.
- These are space-efficient probabilistic data structures to test the existence of an element.
- They may result in false positives but never false negatives. So, if a Bloom filter says a row may exist, it definitely exists.
- This can speed up the queries where you want to check the existence of a row in the table.

4. Coprocessors
- HBase provides Coprocessors framework to run the user code on Region Servers to operate on data locality.
- This enables you to implement your own indexing logic or other custom functionality on the Region Server to get high throughput and performance.
- The Coprocessors are pluggable modules which can be loaded/unloaded dynamically on a table to provide advanced capabilities beyond the native HBase functionality.