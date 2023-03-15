# Introduction to Indexing

- Indexing is a technique that improves the performance of queries in MongoDB by creating data structures that store a subset of the collection's fields.
- Indexes can be created on one or more fields of a collection, and can be either ascending or descending.
- Indexes can also be compound, multikey, text, geospatial, hashed, or sparse, depending on the type and structure of the data.
- Indexes support various query operations, such as equality, range, sort, text search, geospatial queries, and aggregation.
- Indexes can also enforce uniqueness constraints on the collection, preventing duplicate values for a field or a combination of fields.
- Indexes are stored in a special collection called system.indexes, which is hidden from the user.
- Indexes use a B-tree data structure, which allows for efficient insertion, deletion, and retrieval of data.
- Indexes have some trade-offs, such as increased storage space and write operations, and should be used carefully and selectively to optimize the query performance.