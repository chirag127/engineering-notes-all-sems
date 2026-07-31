#### Capped Collections in MongoDB

- Capped collections are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order.
- Capped collections work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection.
- You must create capped collections explicitly using the `db.createCollection()` method, which is a `mongosh` helper for the `create` command.
- When creating a capped collection you must specify the maximum size of the collection in bytes, which MongoDB will pre-allocate for the collection.
- Capped collection in MongoDB is basically used to store log information, the high volume of data, and cache information.
- After creation, if we try to add more than documents to their capacity, it overwrites the existing documents.