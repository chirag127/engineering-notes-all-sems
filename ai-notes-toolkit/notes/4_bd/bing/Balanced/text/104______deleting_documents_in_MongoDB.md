#### Deleting documents in MongoDB

- MongoDB is a document-oriented database that stores data in collections of JSON-like documents.
- To delete documents from a collection, MongoDB provides the following methods:
  - `db.collection.deleteOne(filter, options)`: Deletes a single document that matches the filter condition. If multiple documents match the filter, only the first one is deleted. The options parameter can specify write concern and collation settings.
  - `db.collection.deleteMany(filter, options)`: Deletes all documents that match the filter condition. The options parameter can specify write concern and collation settings.
  - `db.collection.remove(query, justOne)`: Deprecated. Deletes documents from a collection that match the query condition. The justOne parameter can be set to true to delete only one document. This method is equivalent to `db.collection.deleteOne()` or `db.collection.deleteMany()` depending on the value of justOne.
- To delete an entire collection, MongoDB provides the following methods:
  - `db.collection.drop()`: Drops the collection from the database, along with its indexes. Returns true if the collection is dropped successfully, or false if the collection does not exist.
  - `db.dropCollection(name, options)`: Drops the collection with the specified name from the database, along with its indexes. The options parameter can specify write concern settings. Returns a document that contains the status of the operation.
- To delete a database, MongoDB provides the following methods:
  - `db.dropDatabase()`: Drops the current database, along with all its collections and indexes. Returns a document that contains the status of the operation.
  - `use <database>` and `db.dropDatabase()`: Switches to the specified database and drops it, along with all its collections and indexes. Returns a document that contains the status of the operation.