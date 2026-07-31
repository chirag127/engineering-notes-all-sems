### Updating and Deleting Documents in MongoDB

MongoDB is a popular NoSQL database that stores data in the form of documents. In this section, we will discuss how to update and delete documents in MongoDB.

#### Updating Documents

1. To update a document in MongoDB, you can use the `updateOne()` or `updateMany()` methods. The `updateOne()` method updates a single document that matches the specified filter, while the `updateMany()` method updates all documents that match the specified filter.

2. The `updateOne()` and `updateMany()` methods take two arguments: a filter that specifies the criteria for selecting the documents to update, and an update document that specifies the changes to be made to the selected documents.

3. The update document can contain update operators such as `$set`, `$inc`, and `$push` to modify the values of specific fields in the selected documents.

4. Here is an example that uses the `updateOne()` method to update the age of a user with the name "John Doe" in the `users` collection:

```javascript
db.users.updateOne(
   { name: "John Doe" },
   { $set: { age: 42 } }
)
```

#### Deleting Documents

1. To delete documents in MongoDB, you can use the `deleteOne()` or `deleteMany()` methods. The `deleteOne()` method deletes a single document that matches the specified filter, while the `deleteMany()` method deletes all documents that match the specified filter.

2. The `deleteOne()` and `deleteMany()` methods take a single argument: a filter that specifies the criteria for selecting the documents to delete.

3. Here is an example that uses the `deleteOne()` method to delete a user with the name "John Doe" from the `users` collection:

```javascript
db.users.deleteOne({ name: "John Doe" })
```

These are the basic operations for updating and deleting documents in MongoDB. It is important to carefully specify the filter criteria to ensure that the correct documents are selected for updating or deleting.