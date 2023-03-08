### Updating and Deleting Documents in MongoDB

MongoDB is a widely used NoSQL database system that provides a flexible and scalable approach to storing and managing data. In MongoDB, data is stored in collections, which contain documents. These documents can be updated or deleted as required. In this section, we will discuss how to update and delete documents in MongoDB.

#### Updating Documents

Updating documents in MongoDB involves using the `update()` method. This method allows you to modify the contents of a document in a collection. There are several operators you can use to update documents, including:

- `$set`: Sets the value of a field in a document
- `$inc`: Increments the value of a numeric field in a document
- `$push`: Adds an element to an array field in a document
- `$pull`: Removes an element from an array field in a document

Here is an example of using the `$set` operator to update the value of a field in a document:

```
db.collection.update(
   { _id: ObjectId("5f876e4c1d4e9f0a3d49fc3b") },
   { $set: { status: "completed" } }
)
```

This command updates the `status` field in the document with the specified `_id` to `"completed"`.

#### Deleting Documents

Deleting documents in MongoDB involves using the `remove()` method. This method allows you to delete one or more documents from a collection. There are several ways to specify which documents to delete, including:

- Deleting a specific document by its `_id` field
- Deleting all documents that match a specific condition

Here is an example of deleting a specific document by its `_id` field:

```
db.collection.remove({ _id: ObjectId("5f876e4c1d4e9f0a3d49fc3b") })
```

This command deletes the document with the specified `_id`.

In conclusion, updating and deleting documents in MongoDB is a crucial aspect of managing data in a NoSQL database system. The `update()` and `remove()` methods provide powerful ways to modify and delete data as required. Understanding how to use these methods is essential for anyone working with MongoDB in the field of Big Data.