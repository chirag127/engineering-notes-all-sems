#### Updating documents in MongoDB

- MongoDB is a document-oriented database that stores data in JSON-like format.
- To update documents in MongoDB, we can use the `updateOne()`, `updateMany()`, or `replaceOne()` methods of the `db.collection` object.
- The `updateOne()` method updates the first document that matches the filter condition with the specified update operation.
- The `updateMany()` method updates all the documents that match the filter condition with the specified update operation.
- The `replaceOne()` method replaces the first document that matches the filter condition with the specified replacement document.
- The update operation can use the following operators:
  - `$set`: sets the value of a field or creates a new field if it does not exist.
  - `$unset`: removes the specified field from the document.
  - `$inc`: increments the value of a field by a specified amount.
  - `$mul`: multiplies the value of a field by a specified amount.
  - `$rename`: renames a field.
  - `$min`: updates the value of a field to the specified value if it is less than the current value.
  - `$max`: updates the value of a field to the specified value if it is greater than the current value.
  - `$currentDate`: sets the value of a field to the current date, either as a Date or a Timestamp.
  - `$addToSet`: adds a value to an array field only if it does not already exist in the array.
  - `$push`: appends a value to an array field.
  - `$pop`: removes the first or last element of an array field.
  - `$pull`: removes all instances of a value from an array field.
  - `$pullAll`: removes all instances of the specified values from an array field.
- The update methods return a `WriteResult` object that contains information about the number of matched and modified documents, as well as any errors or warnings.
- Example: To update the name and age of the first document in the `users` collection where the email is "user@example.com", we can use the following command:

```javascript
db.users.updateOne(
  { email: "user@example.com" }, // filter condition
  { $set: { name: "John", age: 25 } } // update operation
)
```