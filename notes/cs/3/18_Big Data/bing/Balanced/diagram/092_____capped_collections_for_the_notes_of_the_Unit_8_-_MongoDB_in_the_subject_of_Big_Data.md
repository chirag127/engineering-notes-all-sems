### Capped Collections

Capped collections are a type of collections in MongoDB that have the following characteristics  :

- They are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order.
- They work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection.
- They are created explicitly using the `db.createCollection()` method, which is a mongosh helper for the `create` command. When creating a capped collection, you must specify the maximum size of the collection in bytes, which MongoDB will pre-allocate for the collection.
- They do not support updates that increase the size of the documents. If you update a document in a capped collection with a larger document, MongoDB will remove the document from the collection.
- They do not support the `delete` operation. To remove all documents from a capped collection, use the `drop()` method.
- They automatically remove the oldest documents in the collection if the collection reaches its maximum size limit before it reaches the maximum document count limit.
- They maintain the insertion order of the documents. You can use the `natural` order to return documents in the order they were inserted.
- They support creating indexes on any field, but they do not support the `expireAfterSeconds` option for TTL indexes.
- They support the `createIndex()` method, but they do not support the `dropIndex()` or `dropIndexes()` methods. To drop an index from a capped collection, use the `drop()` method to drop the entire collection, including the indexes, and then recreate the collection and the indexes.
- They support the `tailable` cursor option, which allows clients to retrieve documents from the collection as they are inserted.

Some of the use cases for capped collections are :

- Storing log information, such as web server logs or application logs, that are frequently accessed and do not need to be persisted for a long time.
- Storing high volume of data, such as sensor data or real-time analytics, that are only relevant for a short period of time.
- Storing cache information, such as session data or temporary data, that can be easily regenerated if lost.