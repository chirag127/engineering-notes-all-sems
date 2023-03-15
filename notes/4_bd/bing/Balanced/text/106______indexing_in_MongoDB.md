#### Indexing in MongoDB

- Indexing is a process that improves the performance of queries by creating data structures that store a small portion of the collection's data.
- Indexes support efficient execution of queries by reducing the number of documents that need to be scanned.
- MongoDB provides various types of indexes, such as single field, compound, multikey, text, geospatial, hashed, and wildcard indexes.
- Each index has a unique name and a specification that defines the fields to be indexed and the order of the index keys.
- By default, MongoDB creates a unique index on the `_id` field of each collection, which prevents the insertion of duplicate documents with the same `_id` value.
- To create an index, use the `db.collection.createIndex()` method, which takes an index key specification and an optional index options document as parameters.
- To list the indexes of a collection, use the `db.collection.getIndexes()` method, which returns an array of index documents.
- To drop an index, use the `db.collection.dropIndex()` method, which takes an index name or an index key specification as a parameter.
- To drop all indexes of a collection, use the `db.collection.dropIndexes()` method, which takes no parameters.
- To modify an existing index, such as changing its options or adding or removing fields, you need to drop the index and recreate it with the new specification.