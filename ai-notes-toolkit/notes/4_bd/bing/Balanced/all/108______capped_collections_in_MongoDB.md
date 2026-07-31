#### Capped Collections in MongoDB

- Capped collections are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order   .
- Capped collections work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection   .
- You must create capped collections explicitly using the `db.createCollection()` method, which is a mongosh helper for the create command .
- When creating a capped collection you must specify the maximum size of the collection in bytes, which MongoDB will pre-allocate for the collection  .
- You can also optionally specify the maximum number of documents that the capped collection can store  .
- Capped collections have some advantages and limitations compared to regular collections   :
  - Advantages:
    - Capped collections guarantee preservation of the insertion order, which means that queries can return documents in the order they were inserted by using the natural sort order  .
    - Capped collections support tailable cursors, which are special cursors that remain open after returning the final results of the query, and continue to return new documents as they are inserted into the collection   .
    - Capped collections are more efficient for high-volume inserts and updates, as they do not require index updates or document moves  .
  - Limitations:
    - Capped collections cannot be sharded, which means they cannot be distributed across multiple servers  .
    - Capped collections do not support the `remove()` method, which means documents can only be deleted by dropping the collection or by deleting the database  .
    - Capped collections do not allow updates that increase the size of the documents, as this would cause the documents to exceed the allocated space  .
- Capped collections are useful for some use cases, such as   :
  - Storing log data, such as web server logs or application logs, as they provide fast insertion and retrieval of the most recent entries   .
  - Implementing a queue or a buffer, as they allow consumers to process documents in the order they were produced by the producers   .
  - Streaming data, such as real-time analytics or notifications, as they enable tailable cursors to continuously fetch new documents as they arrive   .