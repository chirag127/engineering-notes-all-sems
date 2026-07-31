#### Updating documents in MongoDB

- MongoDB is a document-oriented database that stores data in collections of JSON-like documents.
- To update documents in MongoDB, you need to use the update methods provided by the MongoDB shell or the drivers for different programming languages.
- The update methods take a filter parameter that specifies which documents to match, and an update parameter that specifies how to modify the matched documents.
- The update methods also take an optional options parameter that can specify additional settings, such as whether to insert a new document if no match is found, or whether to return the modified document.
- The update methods return a result object that contains information about the operation, such as the number of matched and modified documents, and any errors that occurred.
- The update methods are:

  - `db.collection.updateOne(filter, update, options)`: Updates a single document that matches the filter. If multiple documents match, only the first one is updated.
  - `db.collection.updateMany(filter, update, options)`: Updates all the documents that match the filter. If no documents match, no updates are performed.
  - `db.collection.replaceOne(filter, replacement, options)`: Replaces a single document that matches the filter with the given replacement document. If multiple documents match, only the first one is replaced. The replacement document must not contain any update operators.
- To use the update methods, you need to pass an update document that contains update operators, such as `$set`, `$inc`, `$push`, etc. These operators modify the values of the fields in the matched documents.
- For example, to update the name and age of a document in the users collection with the _id of "123", you can use the following command:

  ```javascript
  db.users.updateOne(
    { _id: "123" }, // filter
    { $set: { name: "Alice", age: 25 } }, // update
    { upsert: true } // options
  )
  ```
- This command will update the name and age fields of the matched document, or insert a new document with the given _id, name, and age if no match is found. The upsert option specifies that a new document should be inserted if no match is found.
- To see the result of the update operation, you can use the `db.collection.findOne()` method to query the document by its _id:

  ```javascript
  db.users.findOne({ _id: "123" })
  ```
- This command will return the updated or inserted document, such as:

  ```json
  {
    "_id": "123",
    "name": "Alice",
    "age": 25
  }
  ```
- To update multiple documents in the users collection with the same name, you can use the following command:

  ```javascript
  db.users.updateMany(
    { name: "Bob" }, // filter
    { $inc: { age: 1 } } // update
  )
  ```
- This command will increment the age field of all the documents that have the name "Bob" by 1. The update document does not need to specify the $set operator, as it is implied by default.
- To see the result of the update operation, you can use the `db.collection.find()` method to query the documents by their name:

  ```javascript
  db.users.find({ name: "Bob" })
  ```
- This command will return the updated documents, such as:

  ```json
  {
    "_id": "456",
    "name": "Bob",
    "age": 31
  }
  {
    "_id": "789",
    "name": "Bob",
    "age": 28
  }
  ```
- To replace a document in the users collection with a new document, you can use the following command:

  ```javascript
  db.users.replaceOne(
    { _id: "456" }, // filter
    { name: "Charlie", age: 30, hobbies: ["reading", "writing"] } // replacement
  )
  ```
- This command will replace the document with the _id of "456" with the given replacement document. The replacement document must not contain any update operators, and it will have the same _id as the original document.
- To see the result of the replace operation, you can use the `db.collection.findOne()` method to query the document by its _id:

  ```javascript
  db.users.findOne({ _id: "456" })
  ```
- This command will return the replaced document, such as:

  ```json

```
