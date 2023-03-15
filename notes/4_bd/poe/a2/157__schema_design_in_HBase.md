 Here is the content in markdown format with formal tone and without external links or emojis:

#### Schema Design in HBase

1. Row key design:
- Row keys should be designed in a way that enables efficient scanning, sorting and pagination. They should be unique and sparse.
- Good options for row keys are:
-- Sequential numbers: Easy to scan but prone to hotspotting
-- Incrementing timestamps: Avoid hotspotting but scanning in reverse chronological order is inefficient
-- Hashed values: Even distribution of keys but range scans are not possible
- Row keys should be kept relatively short, ideally less than 100 bytes for performance

2. Column family design:
- Data should be organized into column families based on access patterns. Columns that are often accessed together should be placed in the same column family.
- The number of column families should be kept relatively low, ideally less than 3-5. Having too many column families affects performance.
- Column family names should be descriptive as they define the schema and are part of the row key. They should be kept relatively short, less than 30 characters.

3. Data modeling:
- HBase is a schemaless database so data does not have to conform to a rigid schema. However, some logical structuring of data is important for efficient querying and scanning.
- Good options for data modeling include:
-- Using column qualifiers to denote versions or types
-- Using TTLs (time-to-live) to expire old data
-- Using counters for atomic increments
-- Leveraging HBase's support for sparse data through deleting columns when values are empty

The content summarizes key considerations and best practices regarding schema design in HBase focusing on row keys, column families and data modeling. The points are written concisely in bullets with minimal flair. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.