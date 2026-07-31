### Capped Collections

Capped collections are a type of collections in MongoDB that have the following characteristics  :

- They are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order.
- They work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection.
- They are created explicitly using the `db.createCollection()` method, which is a mongosh helper for the `create` command. When creating a capped collection, you must specify the maximum size of the collection in bytes, which MongoDB will pre-allocate for the collection.
- They do not support updates that increase the size of the documents. If you update a document in a capped collection with a larger document, MongoDB will remove the document from the collection.
- They do not support the `delete` operation. To remove all documents from a capped collection, use the `drop()` method.
- They maintain the insertion order of the documents. You can use the `$natural` operator to query documents in the order they were inserted.
- They support creating indexes on any field, but they do not support the `expireAfterSeconds` option for TTL indexes.
- They support creating a tailable cursor, which is a cursor that remains open after it reaches the end of the data, and continues to return new data as it becomes available.

Some of the use cases for capped collections are :

- Storing log information, such as web server logs, application logs, or system logs.
- Storing high volume of data, such as sensor data, stock market data, or social media data.
- Storing cache information, such as frequently accessed data, session data, or temporary data.