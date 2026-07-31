#### Creating documents in MongoDB

- MongoDB is a document-oriented database that stores data in collections of JSON-like documents.
- A document is a set of key-value pairs, where the value can be any of the supported BSON data types, such as strings, numbers, arrays, objects, etc.
- To create documents in MongoDB, you can use one of the following methods: `insertOne()`, `insertMany()`, or `insert()`.
- The `insertOne()` method inserts a single document into a collection, using the following syntax:

  ```javascript
  db.collection.insertOne(document, options)
  ```

  - The `document` parameter is the document to insert.
  - The `options` parameter is an optional object that specifies additional settings, such as write concern, bypass document validation, etc.
  - The method returns a `WriteResult` object that contains information about the operation, such as the number of documents inserted, the `_id` field of the inserted document, etc.

- The `insertMany()` method inserts multiple documents into a collection, using the following syntax:

  ```javascript
  db.collection.insertMany(documents, options)
  ```

  - The `documents` parameter is an array of documents to insert.
  - The `options` parameter is an optional object that specifies additional settings, such as write concern, bypass document validation, ordered or unordered insertion, etc.
  - The method returns a `WriteResult` object that contains information about the operation, such as the number of documents inserted, the `_id` fields of the inserted documents, etc.

- The `insert()` method inserts one or more documents into a collection, using the following syntax:

  ```javascript
  db.collection.insert(document or array of documents, options)
  ```

  - The `document or array of documents` parameter is either a single document or an array of documents to insert.
  - The `options` parameter is an optional object that specifies additional settings, such as write concern, bypass document validation, etc.
  - The method returns a `WriteResult` object that contains information about the operation, such as the number of documents inserted, the `_id` fields of the inserted documents, etc.

- To create a collection in MongoDB, you can either explicitly use the `create()` command or implicitly create it when inserting the first document into a non-existing collection.
- The `create()` command creates a collection with the specified name and options, using the following syntax:

  ```javascript
  db.createCollection(name, options)
  ```

  - The `name` parameter is the name of the collection to create.
  - The `options` parameter is an optional object that specifies additional settings, such as capped collection, validation rules, indexes, etc.
  - The command returns an object that contains information about the operation, such as the name of the created collection, the ok status, etc.

- To implicitly create a collection, you can use any of the insert methods on a non-existing collection, and MongoDB will create the collection automatically with the default options.
- For example, the following command will create a collection named `movie` and insert a document into it:

  ```javascript
  db.movie.insertOne({"name":"Avengers: Endgame"})
  ```

- To view the documents in a collection, you can use the `find()` method, which returns a cursor to the matching documents, using the following syntax:

  ```javascript
  db.collection.find(query, projection)
  ```

  - The `query` parameter is an optional object that specifies the criteria for selecting documents.
  - The `projection` parameter is an optional object that specifies the fields to include or exclude in the returned documents.
  - The method returns a cursor object that allows you to iterate over the documents or apply additional methods, such as `sort()`, `limit()`, `skip()`, etc.

- For example, the following command will return all the documents in the `movie` collection:

  ```javascript
  db.movie.find()
  ```

- To view the collections in a database, you can use the `show collections` command in the mongo shell, which lists the names of the collections in the current database.
- For example, the following command will show the collections in the `test` database:

  ```javascript
  use test
  show collections
  ```