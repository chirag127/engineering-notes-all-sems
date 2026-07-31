#### Capped Collections in MongoDB

- Capped collections are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order    .
- Capped collections work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection  .
- You must create capped collections explicitly using the `db.createCollection()` method, which is a mongosh helper for the create command .
- When creating a capped collection you must specify the maximum size of the collection in bytes, which MongoDB will pre-allocate for the collection  .
- You can also specify the maximum number of documents that the capped collection can store, but this is optional  .
- Capped collections have the following characteristics and limitations :
  - Capped collections guarantee preservation of the insertion order. As a result, queries do not need an index to return documents in insertion order. Without this indexing overhead, capped collections can support higher insertion throughput.
  - Capped collections automatically remove the oldest documents in the collection without requiring scripts or explicit remove operations.
  - Capped collections cannot be sharded. However, you can create a sharded cluster that contains replica sets, where each replica set contains one or more capped collections.
  - You cannot delete documents from a capped collection. However, you can use the `db.collection.drop()` method to drop the entire collection, or you can use the `emptyCapped` command to remove all documents from a capped collection.
  - You cannot update documents in a capped collection if the update operation causes the document to grow in size. However, you can update documents in a capped collection if the update does not increase the document size, such as updating a field value from one integer to another.
  - You can use the `db.collection.convertToCapped()` method to convert a non-capped collection to a capped collection. However, this operation will empty the collection and you will lose the original documents. You can use the `cloneCollection` command to copy the documents to another collection before converting.
- Capped collections are typically used for storing log information, high volume of data, and cache information .