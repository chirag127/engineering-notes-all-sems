#### Deleting documents in MongoDB

- MongoDB is a NoSQL database that stores data in collections of documents.
- Documents are JSON-like objects that can have different fields and values.
- To delete documents from a collection, MongoDB provides the `deleteOne()`, `deleteMany()`, and `bulkWrite()` methods.
- The `deleteOne()` method deletes the first document that matches a given filter condition.
- The `deleteMany()` method deletes all documents that match a given filter condition.
- The `bulkWrite()` method performs multiple write operations, such as insert, update, or delete, in a single request.
- To use these methods, you need to specify the collection name and the filter condition as arguments.
- For example, to delete a document with the `_id` field equal to `1` from the `users` collection, you can use the following syntax:

```javascript
db.users.deleteOne({_id: 1})
```

- To delete all documents with the `age` field greater than `30` from the `users` collection, you can use the following syntax:

```javascript
db.users.deleteMany({age: {$gt: 30}})
```

- To delete multiple documents with different conditions from the `users` collection, you can use the following syntax:

```javascript
db.users.bulkWrite([
  {deleteOne: {filter: {_id: 1}}},
  {deleteOne: {filter: {name: "Alice"}}},
  {deleteMany: {filter: {age: {$lt: 20}}}}
])
```

- The methods return a result object that contains information about the deletion, such as the number of documents deleted, the write concern, and any errors.
- To view the result object, you can use the `pretty()` method or assign the result to a variable and print it.
- For example, to view the result of the `deleteMany()` method, you can use the following syntax:

```javascript
db.users.deleteMany({age: {$gt: 30}}).pretty()
```

- To assign the result to a variable and print it, you can use the following syntax:

```javascript
var result = db.users.deleteMany({age: {$gt: 30}})
print(result)
```

- To delete all documents from a collection, you can use the `drop()` method on the collection object.
- The `drop()` method returns `true` if the collection is dropped successfully, or `false` if the collection does not exist.
- For example, to delete all documents from the `users` collection, you can use the following syntax:

```javascript
db.users.drop()
```