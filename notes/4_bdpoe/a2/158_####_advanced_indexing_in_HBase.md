 Here is the content in markdown format on #### advanced indexing in HBase:

#### Advanced Indexing in HBase

- Secondary Indexes: In addition to the row key, HBase also supports secondary indexes on column values. These secondary indexes are stored in separate HBase tables and can be queried to fetch data. Some of the popular secondary index approaches in HBase are:
- ** Prefix Tree Index:** Built using prefix tree data structure where each node represents a character. It is efficient for indexing strings with common prefixes.
- ** Suffix Array Index:** Built using suffix arrays and is efficient for indexing strings with common suffixes.
- ** Bitmap Index:** Compresses the base data and uses bitmaps to index the columns. It is efficient for low cardinality data (few unique values) like boolean, sex, status etc.
- ** Connection Table Index:** Uses a separate small table to store index info and a connection table to point to the base data. It is flexible but has an additional hop to fetch the final data.

Advantages:
- Enable fast searches and filters on column values
- Can be tailored to different data patterns

Disadvantages:
- Additional storage required for indexes
- Additional complexity to maintain consistency between data and indexes
- Not suitable for highly dynamic data

[Detailed diagrams, examples, codes, etc. can be added here if required to explain the concepts]

Some mnemonics/tricks to remember:
- Prefix tree: Good for prefixes, tree structure
- Suffix array: Good for suffixes, array structure
- Bitmap: Low cardinality, bitmaps
- Connection table: Flexible, extra hop

Applications:
- Prefix tree index: Geo-spatial data, time-series data
- Suffix array index: Keyword search
- Bitmap index: Filtering outliers
- Connection table index: Generic secondary indexing