#### Indexing in MongoDB

- Indexing is a process that improves the performance of queries by creating data structures that store a small portion of the collection's data.
- Indexes support efficient execution of queries by reducing the number of documents that need to be scanned.
- MongoDB provides various types of indexes, such as single field, compound, multikey, text, geospatial, hashed, and wildcard indexes.
- Each index has a name, a key specification, and an optional set of properties, such as uniqueness, partial filter expression, collation, etc.
- By default, MongoDB creates a unique index on the `_id` field of each collection, which cannot be dropped.
- To create an index, use the `db.collection.createIndex()` method, which takes the key specification and the optional properties as arguments.
- To list the indexes of a collection, use the `db.collection.getIndexes()` method, which returns an array of index documents.
- To drop an index, use the `db.collection.dropIndex()` method, which takes the index name or the key specification as an argument.
- To drop all indexes of a collection, use the `db.collection.dropIndexes()` method, which takes no arguments.
- To modify an existing index, such as changing its properties or adding or removing fields, you need to drop the index and recreate it with the new specification.
- To monitor the performance of indexes, use the `db.collection.stats()` method, which returns various statistics about the collection and its indexes, such as size, count, access, etc.
- To analyze the execution plan of a query, use the `explain()` method, which returns information about the stages, indexes, and costs involved in the query execution.