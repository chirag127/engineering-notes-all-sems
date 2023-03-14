Advanced indexing in HBase is a technique to improve the performance of queries that are not based on the primary row key. HBase does not provide built-in support for secondary indexes, so they have to be implemented manually or using third-party libraries. One way to implement secondary indexes is to create a separate table that stores the mapping between the secondary key and the primary row key, and then use a join or a lookup to retrieve the original records. Another way is to use coprocessors, which are custom code that runs on the HBase region servers, to maintain the secondary indexes and intercept the queries.

The following diagram illustrates the basic architecture of a secondary index table in HBase:

```
+-----------------+     +-----------------+
| Secondary Index |     | Original Table  |
| Table           |     |                 |
+-----------------+     +-----------------+
| Secondary Key   |     | Primary Row Key |
| (e.g. col_1)    |     | (e.g. row_id)   |
+-----------------+     +-----------------+
| val_1 | row_1   |     | row_1 | ...     |
| val_1 | row_2   |     | row_2 | ...     |
| val_2 | row_3   |     | row_3 | ...     |
| val_2 | row_4   |     | row_4 | ...     |
| ...   | ...     |     | ...   | ...     |
+-----------------+     +-----------------+
```

To query the original table based on the secondary key, one can scan the secondary index table for the matching values, and then use the row keys to get the records from the original table. For example, to get the rows whose column 'col_1' has value 'val_1', one can scan the secondary index table for 'val_1' and get the row keys 'row_1' and 'row_2', and then use a multi-get operation to fetch the records from the original table. Alternatively, one can use a join operation to combine the two tables based on the row key. However, both methods may incur network overhead and latency, as the secondary index table and the original table may be stored on different region servers. Therefore, secondary indexing in HBase should be used with caution and only when the benefits outweigh the costs.