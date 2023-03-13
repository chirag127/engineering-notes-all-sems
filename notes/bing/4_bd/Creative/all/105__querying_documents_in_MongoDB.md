#### Querying documents in MongoDB

- MongoDB is a document-oriented database that stores data in JSON-like format.
- To query documents in MongoDB, you can use the `find()` method on a collection, which returns a cursor to the matching documents.
- The `find()` method takes two optional parameters: a query filter and a projection.
- The query filter specifies the conditions that the documents must match to be returned. It is a JSON object that can contain various operators, such as `$eq`, `$gt`, `$in`, `$or`, etc.
- The projection specifies which fields of the documents to include or exclude in the result. It is also a JSON object that can contain either 1 or 0 values for each field, indicating inclusion or exclusion, respectively. By default, the `_id` field is always included, unless explicitly excluded.
- For example, to find all documents in the `users` collection where the `age` field is greater than 25 and the `name` field starts with "A", you can use the following query:

```javascript
db.users.find(
  { age: { $gt: 25 }, name: { $regex: "^A" } }, // query filter
  { name: 1, age: 1, _id: 0 } // projection
)
```

- The result will be a cursor that can be iterated over to access the matching documents, such as:

```javascript
{ "name" : "Alice", "age" : 30 }
{ "name" : "Adam", "age" : 28 }
{ "name" : "Anna", "age" : 26 }
```

- To limit the number of documents returned by the `find()` method, you can use the `limit()` method on the cursor, which takes a positive integer as an argument.
- To skip some documents before returning the result, you can use the `skip()` method on the cursor, which also takes a positive integer as an argument.
- To sort the documents by one or more fields, you can use the `sort()` method on the cursor, which takes a JSON object as an argument, where the keys are the field names and the values are either 1 or -1, indicating ascending or descending order, respectively.
- For example, to find the first 10 documents in the `users` collection where the `age` field is greater than 25, sorted by the `name` field in ascending order, you can use the following query:

```javascript
db.users.find(
  { age: { $gt: 25 } }, // query filter
  { name: 1, age: 1, _id: 0 } // projection
).sort(
  { name: 1 } // sort by name ascending
).limit(10) // limit to 10 documents
```

- The result will be a cursor that can be iterated over to access the matching documents, such as:

```javascript
{ "name" : "Adam", "age" : 28 }
{ "name" : "Alice", "age" : 30 }
{ "name" : "Anna", "age" : 26 }
{ "name" : "Bob", "age" : 27 }
{ "name" : "Carol", "age" : 29 }
{ "name" : "David", "age" : 31 }
{ "name" : "Eve", "age" : 32 }
{ "name" : "Frank", "age" : 33 }
{ "name" : "Grace", "age" : 34 }
{ "name" : "Helen", "age" : 35 }
```

- To count the number of documents that match a query filter, you can use the `count()` method on the cursor, which returns an integer.
- For example, to count the number of documents in the `users` collection where the `age` field is greater than 25, you can use the following query:

```javascript
db.users.find(
  { age: { $gt: 25 } } // query filter
).count()
```

- The result will be an integer, such as:

```javascript
15
```

- To update one or more documents that match a query filter, you can use the `update()` method on a collection, which takes three parameters: a query filter, an update document, and an optional options object.
- The update document specifies the changes to be applied to the matching documents. It can contain various operators, such as `$set`, `$inc`, `$push`, `$pull`, etc.
- The options object can contain various flags, such as `multi`, `up