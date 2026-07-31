#### Updating documents in MongoDB

- MongoDB is a document-oriented database that stores data in JSON-like format.
- To update documents in MongoDB, you need to use one of the following methods:
  - `db.collection.updateOne()` to update a single document that matches a filter condition.
  - `db.collection.updateMany()` to update multiple documents that match a filter condition.
  - `db.collection.replaceOne()` to replace a single document that matches a filter condition with a new document.
- To specify which fields to update, you need to use update operators, such as `$set`, `$inc`, `$push`, etc. Update operators modify the values of the existing fields or add new fields to the document.
- To specify the filter condition, you can use query operators, such as `$eq`, `$gt`, `$in`, etc. Query operators compare the values of the fields with the given criteria.
- To view the result of the update operation, you can use the `acknowledged`, `matchedCount`, and `modifiedCount` properties of the result object. These properties indicate whether the operation was successful, how many documents matched the filter, and how many documents were actually updated.
- To check the updated documents, you can use the `db.collection.find()` method to query the collection.

- Here are some examples of updating documents in MongoDB using the MongoDB shell:

  - Update the `name` field of the first document in the `users` collection where the `age` field is greater than 30:

    ```javascript
    db.users.updateOne(
      { age: { $gt: 30 } }, // filter condition
      { $set: { name: "Alice" } } // update operator
    )
    ```

  - Update the `email` and `phone` fields of all the documents in the `users` collection where the `name` field is equal to "Bob":

    ```javascript
    db.users.updateMany(
      { name: { $eq: "Bob" } }, // filter condition
      { $set: { email: "bob@example.com", phone: "123-456-7890" } } // update operator
    )
    ```
  - Replace the first document in the `users` collection where the `name` field is equal to "Charlie" with a new document:

    ```javascript
    db.users.replaceOne(
      { name: { $eq: "Charlie" } }, // filter condition
      { name: "Charles", age: 25, gender: "male" } // new document
    )
    ```