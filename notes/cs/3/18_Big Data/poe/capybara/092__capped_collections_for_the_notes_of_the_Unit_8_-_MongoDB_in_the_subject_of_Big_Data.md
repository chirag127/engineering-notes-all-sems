### Capped Collections for the Notes of the Unit 8 - MongoDB in the Subject of Big Data

Capped collections in MongoDB are fixed-size collections that maintain the order of documents based on the insertion order. They are useful for creating a collection of a fixed size that can be used as a buffer or cache. Here are some key points to keep in mind when working with capped collections in MongoDB:

- Capped collections have a fixed size and can only contain a certain number of documents. Once the collection reaches its maximum size, new documents will overwrite the oldest documents in the collection.
- Capped collections are created with the `db.createCollection()` method and the `capped` option set to `true`.
- Capped collections do not allow updates that increase the size of a document. If you need to update a document, you must replace it with a new document of the same size or smaller.
- Capped collections support a subset of query functionality compared to regular collections. For example, they do not support the `$near` operator or the `$text` operator.
- Capped collections can be used for a variety of purposes, such as logging, auditing, and real-time data processing.
- Capped collections are often used in conjunction with the Tailable Cursor feature in MongoDB, which allows you to create a cursor that remains open after returning the last document in a collection. This makes it possible to continuously stream data from a capped collection as new documents are inserted.
- When creating a capped collection, you can specify the maximum size of the collection in bytes using the `size` option. You can also specify the maximum number of documents the collection can hold using the `max` option.
- Capped collections can be queried and indexed just like regular collections. However, if you plan to query a capped collection frequently, it's a good idea to create an index on the field you plan to query on to improve performance.

In conclusion, capped collections are a useful feature of MongoDB that can be used to create fixed-size collections for a variety of purposes. By keeping these key points in mind, you can effectively use capped collections in your MongoDB projects.