#### Querying documents in MongoDB

- MongoDB is a document-oriented database that stores data in JSON-like format.
- To query documents in MongoDB, one can use the `find()` method on a collection, which returns a cursor object that can be iterated over to access the matching documents.
- The `find()` method can take two optional parameters: a query filter and a projection.
- A query filter is a document that specifies the criteria for selecting the documents. It can use various operators, such as `$eq`, `$gt`, `$in`, `$and`, `$or`, etc., to compare the values of the document fields with the specified values.
- A projection is a document that specifies which fields to include or exclude from the returned documents. It can use the value `1` to include a field, or `0` to exclude it. By default, the `_id` field is always included, unless explicitly excluded.
- For example, the following query finds all the documents in the `users` collection where the `age` field is greater than 25, and returns only the `name` and `email` fields:

```javascript
db.users.find({age: {$gt: 25}}, {name: 1, email: 1, _id: 0})
```

- To sort the results of a query, one can use the `sort()` method on the cursor object, which takes a document that specifies the sort order for each field. The value `1` means ascending order, and `-1` means descending order.
- For example, the following query sorts the results by the `name` field in ascending order, and then by the `age` field in descending order:

```javascript
db.users.find().sort({name: 1, age: -1})
```

- To limit the number of results returned by a query, one can use the `limit()` method on the cursor object, which takes a positive integer as the argument.
- For example, the following query returns only the first 10 documents from the `users` collection:

```javascript
db.users.find().limit(10)
```

- To skip some results from the beginning of a query, one can use the `skip()` method on the cursor object, which takes a positive integer as the argument.
- For example, the following query skips the first 5 documents and returns the next 10 documents from the `users` collection:

```javascript
db.users.find().skip(5).limit(10)
```

- To count the number of documents that match a query, one can use the `count()` method on the cursor object, which returns an integer.
- For example, the following query counts the number of documents in the `users` collection where the `gender` field is `"female"`:

```javascript
db.users.find({gender: "female"}).count()
```

- To update one or more documents that match a query, one can use the `updateOne()`, `updateMany()`, or `replaceOne()` methods on a collection, which take a query filter and an update document as the arguments.
- The update document can use various operators, such as `$set`, `$inc`, `$push`, `$pull`, etc., to modify the values of the document fields.
- The `updateOne()` method updates the first document that matches the query filter, while the `updateMany()` method updates all the documents that match the query filter.
- The `replaceOne()` method replaces the first document that matches the query filter with the update document.
- For example, the following query updates the `email` field of the first document in the `users` collection where the `name` field is `"Alice"`:

```javascript
db.users.updateOne({name: "Alice"}, {$set: {email: "alice@example.com"}})
```

- To delete one or more documents that match a query, one can use the `deleteOne()` or `deleteMany()` methods on a collection, which take a query filter as the argument.
- The `deleteOne()` method deletes the first document that matches the query filter, while the `deleteMany()` method deletes all the documents that match the query filter.
- For example, the following query deletes all the documents in the `users` collection where the `age` field is less than 18:

```javascript
db.users.deleteMany({age: {$lt: 18}})
```