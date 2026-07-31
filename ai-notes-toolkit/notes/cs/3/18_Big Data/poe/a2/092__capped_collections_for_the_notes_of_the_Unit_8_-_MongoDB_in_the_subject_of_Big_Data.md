 Here are the notes for Capped Collections in MongoDB for Unit 8 - MongoDB in Big Data:

### Capped Collections

- Capped collections are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order.
- Once a capped collection reaches its maximum size, it makes room for new documents by overwriting the oldest documents in the collection.
- Capped collections are ideal for storing frequently accessed data in a predictable order. Examples include server logs and geospatial data.
- To create a capped collection, specify a maximum size for the collection (e.g. 100000 bytes) in the db.createCollection() method. MongoDB will pre-allocate the necessary space for the collection.
- Capped collections do not support indexes or validation.
- The _id field is automatically indexed in capped collections.
- Capped collections support the oplog, which is a special capped collection that holds a rolling record of all operations that modify the data stored in a MongoDB database.

- The key points to remember about capped collections are:
- Fixed size
- Documents are ordered by insertion order
- Older documents get overwritten when the size limit is reached
- Great for high throughput operations and streaming data access
- Used for oplog, logging, and caching data