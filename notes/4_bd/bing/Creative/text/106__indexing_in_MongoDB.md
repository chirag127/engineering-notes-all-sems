#### Indexing in MongoDB

Indexing is a process that improves the efficiency of query execution in MongoDB. Without indexes, MongoDB has to scan every document in a collection to find the matching documents for a query. With indexes, MongoDB can use special data structures that store a subset of the collection's data in an ordered form, making it easier to locate the relevant documents.

Some of the main points about indexing in MongoDB are:

- MongoDB creates a unique index on the _id field by default for every collection. This index prevents duplicate values for the _id field and cannot be dropped.
- MongoDB supports user-defined indexes on single fields, compound fields (multiple fields in one index), multikey fields (fields that contain arrays), text fields (fields that contain string values), geospatial fields (fields that contain location data), hashed fields (fields that are hashed for sharding purposes), and wildcard fields (fields that match a filter expression).
- MongoDB also supports partial indexes (indexes that only include documents that match a filter expression), sparse indexes (indexes that only include documents that have the indexed field), TTL indexes (indexes that expire documents after a specified time), and hidden indexes (indexes that are invisible to the query planner).
- To create an index, use the db.collection.createIndex() method, which takes a document that specifies the field(s) to index and the index direction (1 for ascending, -1 for descending), and an optional document that specifies the index options (such as name, unique, background, etc.).
- To drop an index, use the db.collection.dropIndex() method, which takes a document that specifies the index name or the index specification. To drop all indexes except the _id index, use the db.collection.dropIndexes() method.
- To view the indexes on a collection, use the db.collection.getIndexes() method, which returns an array of index documents. To view the index statistics, use the db.collection.stats() method, which returns a document that contains information such as the index size, the number of index entries, and the index access operations.