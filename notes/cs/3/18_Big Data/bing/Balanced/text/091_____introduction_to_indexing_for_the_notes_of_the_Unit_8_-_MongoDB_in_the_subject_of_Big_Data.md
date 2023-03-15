### Introduction to Indexing

- Indexing is a technique that improves the performance of queries in MongoDB by creating data structures that store a subset of the document fields.
- Indexes can be created on any field or combination of fields in a collection, and they support various types of queries, such as equality, range, text, geospatial, and array operations.
- Indexes also enable MongoDB to sort the query results efficiently, without using additional memory or disk space.
- MongoDB provides several types of indexes, such as:

  - Single field indexes: index only one field of the document.
  - Compound indexes: index multiple fields of the document in a specified order.
  - Multikey indexes: index the content of array fields, where each element of the array is a separate index entry.
  - Text indexes: index the content of string fields and support text search queries.
  - Hashed indexes: index the hash of the field value, and support equality queries and sharding.
  - Geospatial indexes: index the coordinates of points, lines, polygons, and other geometries, and support geospatial queries.
  - Wildcard indexes: index all the fields or a subset of the fields in a document, and support dynamic schemas.

- Indexes are stored in a special collection called `system.indexes`, and they use the same BSON format as the documents in the collection.
- Indexes are created using the `db.collection.createIndex()` method, which takes an index specification document and an optional options document as arguments.
- Indexes can be dropped using the `db.collection.dropIndex()` method, which takes an index name or an index specification document as an argument.
- Indexes can be listed using the `db.collection.getIndexes()` method, which returns an array of index specification documents.
- Indexes can be modified using the `db.collection.reIndex()` method, which rebuilds all the indexes in a collection, or the `collMod` command, which allows changing some index options.