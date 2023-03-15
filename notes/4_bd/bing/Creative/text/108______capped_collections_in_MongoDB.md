#### Capped Collections in MongoDB

- Capped collections are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order .
- Capped collections work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection  .
- You must create capped collections explicitly using the `db.createCollection()` method, which is a mongosh helper for the create command .
- When creating a capped collection you must specify the maximum size of the collection in bytes, which MongoDB will pre-allocate for the collection  .
- You can also specify the maximum number of documents that the capped collection can store, but this is optional.
- Capped collections have the following characteristics and limitations :
  - Capped collections guarantee preservation of the insertion order. As a result, queries do not need an index to return documents in insertion order. Without this indexing overhead, capped collections can support higher insertion throughput.
  - Capped collections automatically remove the oldest documents in the collection without requiring scripts or explicit remove operations.
  - Capped collections cannot be sharded. However, you can create a sharded cluster that contains replica sets, where each replica set contains one or more capped collections.
  - Capped collections cannot use the $out aggregation pipeline stage.
  - You cannot remove documents from a capped collection. To remove all documents from a capped collection, use the drop() method.
  - You cannot delete a document and then insert a new document to replace the deleted document. However, you can use the update() method with the overwrite option to replace the contents of an existing document in a capped collection.
  - You cannot update a document in a capped collection if the update operation causes the document to grow beyond its original size. However, you can update a document in a capped collection if the update operation does not cause the document to grow beyond its original size.
  - You can create indexes on a capped collection, but you cannot create a text index.
  - You can create a capped collection that is also a time series collection. See Time Series Collections for more information.
- Capped collections are useful for storing log information, high volume of data, and cache information .