#### Capped collections in MongoDB

- Capped collections are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order .
- Capped collections work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection .
- You must create capped collections explicitly using the `db.createCollection()` method, which is a mongosh helper for the create command .
- When creating a capped collection you must specify the maximum size of the collection in bytes, which MongoDB will pre-allocate for the collection .
- You can also specify the maximum number of documents that the capped collection can store, but this is optional.
- Capped collections have the following characteristics and limitations :
  - Capped collections guarantee preservation of the insertion order. As a result, queries do not need an index to return documents in insertion order. Without this indexing overhead, capped collections can support higher insertion throughput.
  - Capped collections only allow insertion at the end of the collection and in contiguously allocated space. Updates to a document must not increase the document’s size, to prevent the document from exceeding the allocated space. If a document size increases, MongoDB will remove the document from the capped collection and insert it as a new document at the end of the collection, if space is available.
  - Capped collections cannot be sharded. However, you can create a sharded system that writes to a non-sharded capped collection on a single shard. See Sharded Cluster with Non-Sharded Capped Collection for an example.
  - Capped collections automatically remove the oldest documents in the collection without requiring scripts or explicit remove operations.
  - Capped collections do not support the `db.collection.remove()` method. To remove all documents from a capped collection, use the `db.collection.drop()` method to drop the collection and recreate the capped collection.
  - Capped collections support createIndex() on any field, but only support dropIndex() on the _id field.
  - Capped collections support the `db.collection.renameCollection()` method with the dropTarget option set to true.
- Capped collections are useful for storing log information, high volume of data, and cache information.
- Capped collections can be converted to regular (uncapped) collections using the `db.collection.convertToCapped()` method, which takes the maximum size of the collection in bytes as a parameter.
- A possible mnemonic to remember the features of capped collections is: **C**ircular, **A**llocated, **P**reserved, **P**re-ordered, **E**nd-insertion, **D**eletion.