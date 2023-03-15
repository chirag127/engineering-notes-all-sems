#### Deleting documents in MongoDB

MongoDB is a document-oriented database that stores data in collections of JSON-like documents. To delete documents from a collection, MongoDB provides several methods and commands that can be used in the mongo shell or in a driver. Here are some of the ways to delete documents in MongoDB:

- The `db.collection.remove()` method: This method takes a query filter as a parameter and deletes all the documents that match the filter from the collection. Optionally, you can pass a second parameter as `true` to delete only one document that matches the filter. This method is deprecated in MongoDB 4.2 and newer versions.  
- The `delete` command: This command can also be used to delete documents from a collection. Internally, the `remove` method also uses the `delete` command. To use this command, you need to run it with the `db.runCommand()` method and pass an object to it. The object must have the following fields: `delete`, which is the name of the collection; `deletes`, which is an array of objects that specify the query filters and the limit for each deletion; and `writeConcern`, which is an optional field that specifies the level of acknowledgment for the write operation.  
- The `db.collection.deleteOne()` method: This method deletes at most one document that matches a given filter from the collection. It returns an object that contains the status of the operation, the number of documents deleted, and the `_id` of the deleted document. This method is preferred over the `remove` method with the second parameter as `true`.  
- The `db.collection.deleteMany()` method: This method deletes all the documents that match a given filter from the collection. It returns an object that contains the status of the operation and the number of documents deleted. This method is preferred over the `remove` method with the second parameter as `false` or omitted.  

Here are some examples of using these methods and commands to delete documents in MongoDB:

- To delete all the documents from the `users` collection, you can use any of the following:

  ```js
  // Using the remove method
  db.users.remove({})

  // Using the delete command
  db.runCommand({
    delete: "users",
    deletes: [{ q: {}, limit: 0 }],
  })

  // Using the deleteMany method
  db.users.deleteMany({})
  ```

- To delete only one document that has the `name` field as `"Alice"` from the `users` collection, you can use any of the following:

  ```js
  // Using the remove method
  db.users.remove({ name: "Alice" }, true)

  // Using the delete command
  db.runCommand({
    delete: "users",
    deletes: [{ q: { name: "Alice" }, limit: 1 }],
  })

  // Using the deleteOne method
  db.users.deleteOne({ name: "Alice" })
  ```

- To delete all the documents that have the `age` field greater than `30` from the `users` collection, you can use any of the following:

  ```js
  // Using the remove method
  db.users.remove({ age: { $gt: 30 } })

  // Using the delete command
  db.runCommand({
    delete: "users",
    deletes: [{ q: { age: { $gt: 30 } }, limit: 0 }],
  })

  // Using the deleteMany method
  db.users.deleteMany({ age: { $gt: 30 } })
  ```

: https://database.guide/4-ways-to-delete-a-document-in-mongodb/

: https://www.mongodb.com/docs/mongodb-shell/crud/delete/

: https://www.knowledgehut.com/blog/web-development/deleting-document-in-mongodb

: https://docs.mongodb.com/manual/reference/command/delete/

: https://docs.mongodb.com/manual/tutorial/remove-documents/