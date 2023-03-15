#### Capped Collections in MongoDB

- Capped collections are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order   .
- Capped collections work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection   .
- You must create capped collections explicitly using the `db.createCollection()` method, which is a mongosh helper for the create command .
- When creating a capped collection you must specify the maximum size of the collection in bytes, which MongoDB will pre-allocate for the collection  .
- You can also optionally specify the maximum number of documents that the capped collection can store  .
- Capped collections have the following characteristics and limitations  :
  - You cannot delete documents from a capped collection.
  - You cannot update documents in a capped collection if the update increases the document size.
  - You cannot use the `db.collection.drop()` method to drop a capped collection. You must use the `db.collection.drop()` method instead.
  - You cannot shard a capped collection.
  - You can create indexes on a capped collection, but you cannot create a unique index unless the _id field is the only indexed field.
- Capped collections are useful for scenarios where you need to store and access recent data, such as logs, metrics, or notifications    .
- Capped collections provide natural ordering of documents, which means you do not need to create an index to sort the documents by insertion order  .
- Capped collections guarantee preservation of insertion order, which means that queries will return documents in the order they were inserted  .
- Capped collections support tailable cursors, which are special cursors that remain open after returning the final document in a query and continue to return new documents as they are inserted into the collection  .