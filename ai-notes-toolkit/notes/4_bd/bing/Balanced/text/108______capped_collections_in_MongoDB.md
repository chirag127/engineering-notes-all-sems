#### Capped Collections in MongoDB

- Capped collections are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order    .
- Capped collections work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection  .
- You must create capped collections explicitly using the `db.createCollection()` method, which is a mongosh helper for the create command .
- When creating a capped collection you must specify the maximum size of the collection in bytes, which MongoDB will pre-allocate for the collection  .
- You can also specify the maximum number of documents that the capped collection can store, but this is optional.
- Capped collections have the following characteristics and limitations :
  - You cannot delete documents from a capped collection. To remove all documents from a capped collection, use the `db.collection.drop()` method to drop the collection and recreate the capped collection.
  - You cannot update documents in a way that increases their size. If you attempt to do so, MongoDB will return an error.
  - You can, however, update documents in a way that does not increase their size, such as changing the value of a field to a value of the same length.
  - You can use the `db.collection.remove()` method to remove the last document inserted into a capped collection, but this is not recommended as it may impact the performance of the collection.
  - You cannot shard a capped collection.
  - You can create indexes on a capped collection, but you cannot create a unique index on a capped collection unless the index is on the `_id` field.
  - You can use the `db.collection.isCapped()` method to check if a collection is capped.
- Capped collections are typically used to store log information, high volume of data, and cache information . They are also useful for implementing a queue or a stream of data that only retains recent information.