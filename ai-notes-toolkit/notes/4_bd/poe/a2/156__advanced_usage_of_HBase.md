 Here is the content in Markdown format with formal tone and without any emojis or external links:

#### Advanced usage of HBase

1. Secondary Indexes

- HBase tables are indexed by row key. Secondary indexes can be created on other columns to speed up queries on those columns.
- These indexes are maintained separately from the main table data and require additional storage space.
- Common secondary index patterns include:
-- Index on a column to allow sorted access
-- Multi-valued index for fast instance-of type queries
-- Full-text search index

2. Bloom Filters

- Bloom filters are a space-efficient probabilistic data structure to test whether an element is a member of a set.
- They are often used in HBase to check if a row exists in a table before doing a full lookup, thereby saving read time.
- The filter may return false positives but will never return false negatives, so the row existence check may have to be followed by an actual get operation.
- Bloom filters are ideal for cases where the number of keys is very large and the chance of false positives is within acceptable limits.

3. Compression

- HBase provides facilities to compress data in columns to save space and increase performance.
- Supported compression algorithms include:
-- Gzip
-- Lzo
-- Snappy

- The choice of algorithm depends on the characteristics of the data like size of values, frequency of updates, CPU overhead of compression/decompression, etc.
- Compression works on a per-column family basis and all columns in a family are compressed using the same algorithm.

[The content continues in the same formal tone with headings and points.]