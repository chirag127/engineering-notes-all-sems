#### Creating documents in MongoDB

- MongoDB is a document-oriented database that stores data in JSON-like format.
- A document is a set of key-value pairs that represents a single entity or object in the application domain.
- A collection is a group of documents that share a common schema or structure.
- To create documents in MongoDB, you can use the following methods:

  - `insertOne()`: This method inserts a single document into a collection. If the collection does not exist, it will be created automatically. The syntax is:

    ```javascript
    db.collection.insertOne(document)
    ```

    where `db` is the database name, `collection` is the collection name, and `document` is the document to be inserted. For example:

    ```javascript
    db.users.insertOne({name: "Alice", age: 25, email: "alice@example.com"})
    ```

  - `insertMany()`: This method inserts multiple documents into a collection. If the collection does not exist, it will be created automatically. The syntax is:

    ```javascript
    db.collection.insertMany(documents)
    ```

    where `db` is the database name, `collection` is the collection name, and `documents` is an array of documents to be inserted. For example:

    ```javascript
    db.users.insertMany([
      {name: "Bob", age: 30, email: "bob@example.com"},
      {name: "Charlie", age: 35, email: "charlie@example.com"}
    ])
    ```

  - `insert()`: This method is a legacy method that can insert either a single document or multiple documents into a collection. It is equivalent to `insertOne()` or `insertMany()` depending on the input. The syntax is:

    ```javascript
    db.collection.insert(document or documents)
    ```

    where `db` is the database name, `collection` is the collection name, and `document or documents` is either a single document or an array of documents to be inserted. For example:

    ```javascript
    db.users.insert({name: "David", age: 40, email: "david@example.com"})
    db.users.insert([
      {name: "Eve", age: 45, email: "eve@example.com"},
      {name: "Frank", age: 50, email: "frank@example.com"}
    ])
    ```

- When inserting documents, MongoDB will automatically assign a unique `_id` field to each document if it is not provided. The `_id` field acts as a primary key for the collection and must be unique within the collection.
- To verify the insertion of documents, you can use the `find()` method to query the collection. The syntax is:

  ```javascript
  db.collection.find(query)
  ```

  where `db` is the database name, `collection` is the collection name, and `query` is an optional filter to specify the criteria for the documents to be returned. For example:

  ```javascript
  db.users.find()
  db.users.find({age: {$gt: 30}})
  ```

- To learn more about creating documents in MongoDB, you can refer to the following sources:

  - [How to Create Documents in MongoDB - MUO](https://www.makeuseof.com/how-to-create-documents-in-mongodb/)
  - [Create Documents — MongoDB for VS Code](https://www.mongodb.com/docs/mongodb-vscode/create-document-playground/)
  - [MongoDB - Create a Document - Quackit](https://www.quackit.com/mongodb/tutorial/mongodb_create_a_document.cfm)
  - [Documents — MongoDB Manual](https://www.mongodb.com/docs/manual/core/document/)
  - [create — MongoDB Manual](https://www.mongodb.com/docs/manual/reference/command/create/)