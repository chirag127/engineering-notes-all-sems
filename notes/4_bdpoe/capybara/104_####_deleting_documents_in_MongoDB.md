#### Deleting Documents in MongoDB

In MongoDB, documents can be deleted using the `deleteOne()` and `deleteMany()` methods. These methods allow you to remove one or multiple documents that match a specified filter criteria.

##### `deleteOne()`

The `deleteOne()` method deletes a single document that matches the specified filter criteria. If multiple documents match the filter, only the first document that is found will be deleted.

The basic syntax of the `deleteOne()` method is as follows:

```
db.collection.deleteOne(filter, options)
```

- `filter`: The filter criteria to match the document(s) to delete.
- `options`: Optional parameters such as `collation`, `writeConcern`, etc.

###### Example

Suppose we have a collection named `users` with the following documents:

```
{ "_id" : ObjectId("602c0f1a7ec80d1e1c3955c5"), "name" : "John", "age" : 25 }
{ "_id" : ObjectId("602c0f1a7ec80d1e1c3955c6"), "name" : "Jane", "age" : 30 }
{ "_id" : ObjectId("602c0f1a7ec80d1e1c3955c7"), "name" : "Bob", "age" : 35 }
```

To delete the document with `name` equal to "John", we can use the following command:

```
db.users.deleteOne({ name: "John" })
```

This will delete the first document that matches the filter criteria.

##### `deleteMany()`

The `deleteMany()` method deletes all documents that match the specified filter criteria.

The basic syntax of the `deleteMany()` method is as follows:

```
db.collection.deleteMany(filter, options)
```

- `filter`: The filter criteria to match the document(s) to delete.
- `options`: Optional parameters such as `collation`, `writeConcern`, etc.

###### Example

Suppose we have a collection named `users` with the following documents:

```
{ "_id" : ObjectId("602c0f1a7ec80d1e1c3955c5"), "name" : "John", "age" : 25 }
{ "_id" : ObjectId("602c0f1a7ec80d1e1c3955c6"), "name" : "Jane", "age" : 30 }
{ "_id" : ObjectId("602c0f1a7ec80d1e1c3955c7"), "name" : "Bob", "age" : 35 }
{ "_id" : ObjectId("602c0f1a7ec80d1e1c3955c8"), "name" : "Alice", "age" : 40 }
```

To delete all documents with `age` greater than or equal to 35, we can use the following command:

```
db.users.deleteMany({ age: { $gte: 35 } })
```

This will delete the following documents:

```
{ "_id" : ObjectId("602c0f1a7ec80d1e1c3955c7"), "name" : "Bob", "age" : 35 }
{ "_id" : ObjectId("602c0f1a7ec80d1e1c3955c8"), "name" : "Alice", "age" : 40 }
```

##### Mnemonic

A mnemonic for remembering the difference between `deleteOne()` and `deleteMany()` is "One and Done" for `deleteOne()`, meaning it deletes one document, and "Many and Gone" for `deleteMany()`, meaning it deletes many documents.

##### Advantages

- Allows you to delete one or multiple documents that match a specified filter criteria.
- Supports the use of optional parameters such as `collation`, `writeConcern`, etc.

##### Disadvantages

- Deleting documents permanently removes them from the database, and there is no way to retrieve them.
- Deleting large amounts of data can be time-consuming and may impact the performance of the database.

##### Applications

- Cleaning up outdated or irrelevant data.
- Removing duplicate or erroneous data.
- Managing data retention policies.