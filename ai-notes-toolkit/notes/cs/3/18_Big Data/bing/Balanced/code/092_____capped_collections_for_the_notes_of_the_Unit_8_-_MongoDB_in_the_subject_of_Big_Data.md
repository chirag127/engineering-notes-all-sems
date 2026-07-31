# Capped Collections

Capped collections are a special type of collections in MongoDB that have the following characteristics  :

- They are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order.
- They are created explicitly using the `db.createCollection()` method, which requires specifying the maximum size of the collection in bytes, and optionally the maximum number of documents that it can store.
- They pre-allocate the specified space on disk and do not support updates that increase the size of the documents.
- They automatically delete the oldest documents in the collection when the allocated space or the maximum number of documents is reached, making room for new documents.
- They do not support the `deleteOne()`, `deleteMany()`, or `remove()` methods to delete documents. However, they support the `drop()` method to drop the entire collection.
- They preserve the insertion order of the documents, and support queries that return documents in the order they were inserted.
- They support the `createIndex()` method to create indexes on the fields of the documents, except for the `_id` field, which is automatically indexed in the order of insertion.
- They support the `tailable` and `awaitData` cursor options, which allow applications to retrieve new documents as they are inserted, similar to a message queue.

Some of the use cases for capped collections are  :

- Storing log information, such as application logs, system logs, or audit logs.
- Storing high volume of data, such as sensor data, clickstream data, or real-time analytics data.
- Storing cache information, such as frequently accessed data or session data.
- Implementing pub/sub or message queue patterns, where producers insert documents and consumers retrieve them in a FIFO manner.