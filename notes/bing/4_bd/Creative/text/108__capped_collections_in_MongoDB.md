#### Capped Collections in MongoDB

- Capped collections are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order .
- Capped collections work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection .
- You must create capped collections explicitly using the `db.createCollection()` method, which is a mongosh helper for the create command .
- When creating a capped collection you must specify the maximum size of the collection in bytes, which MongoDB will pre-allocate for the collection .
- You can also optionally specify the maximum number of documents that the collection can store.
- Capped collections are typically used to store log information, high volume of data, and cache information .
- Capped collections have the following advantages and limitations :
  - Advantages:
    - Capped collections guarantee preservation of the insertion order. As a result, queries do not need an index to return documents in insertion order. Without this indexing overhead, capped collections can support higher insertion throughput.
    - Capped collections automatically remove the oldest documents in the collection without requiring scripts or explicit remove operations.
    - Capped collections support createIndex () operations to create indexes on any field of the documents in the collection.
    - Capped collections support tailable cursors, which can remain open after returning the final result of the initial query and continue to return new documents as they are inserted into the collection.
  - Limitations:
    - You cannot delete documents from a capped collection. To remove all documents from a capped collection, use the drop () method to drop the collection and recreate the collection.
    - You cannot update documents in a capped collection if the update operation causes the document to grow beyond its original size. However, you can perform update operations that do not increase the size of the document, such as using the $inc operator to increment a field value.
    - You cannot shard a capped collection. However, you can create a capped collection on a shard by connecting directly to the shard mongod instance and using the db.createCollection () method.
    - You cannot change the size of a capped collection after creation. However, you can use the collMod command with the convertToCapped option to convert a non-capped collection to a capped collection and specify a new size. This operation will delete any documents that do not fit in the new size.