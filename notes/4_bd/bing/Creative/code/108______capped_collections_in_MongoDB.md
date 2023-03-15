#### Capped Collections in MongoDB

- Capped collections are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order    .
- Capped collections work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection  .
- You must create capped collections explicitly using the `db.createCollection()` method, which is a mongosh helper for the create command .
- When creating a capped collection you must specify the maximum size of the collection in bytes, which MongoDB will pre-allocate for the collection  .
- You can also specify the maximum number of documents that the capped collection can store, but this is optional  .
- Capped collections have the following characteristics and limitations :
  - Capped collections guarantee preservation of the insertion order. As a result, queries do not need an index to return documents in insertion order. Without this indexing overhead, capped collections can support higher insertion throughput.
  - Capped collections automatically remove the oldest documents in the collection without requiring scripts or explicit remove operations.
  - Capped collections cannot be sharded. However, you can create a sharded cluster that contains replica sets, where each replica set has a capped collection.
  - You cannot delete documents from a capped collection. However, you can use the `db.collection.drop()` method to drop the entire collection, or the `db.collection.remove()` method to remove all documents from the collection.
  - You cannot update documents in a capped collection if the update operation causes the document to grow beyond its original size. However, you can perform update operations that do not increase the size of the document, such as using the `$inc` operator to increment a field value.
  - You can create indexes on a capped collection, but you cannot create a text index.
  - You can use capped collections for applications that require fast and frequent insertion and retrieval of documents, such as logging, caching, or real-time analytics  .