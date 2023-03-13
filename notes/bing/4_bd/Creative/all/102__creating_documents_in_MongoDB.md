#### Creating documents in MongoDB

- MongoDB is a document-oriented database that stores data in collections of JSON-like documents.
- To create a document in MongoDB, you can use the `insertOne()` or `insertMany()` methods of the collection object.
- The `insertOne()` method takes a single document as an argument and inserts it into the collection. It returns a result object that contains the `_id` field of the inserted document.
- The `insertMany()` method takes an array of documents as an argument and inserts them into the collection. It returns a result object that contains an array of `_id` fields of the inserted documents.
- If you do not specify an `_id` field for a document, MongoDB will automatically generate a unique ObjectId value for it.
- You can also use the `db.collection.insert()` method, which is a wrapper for `insertOne()` and `insertMany()`, depending on the argument type.
- To insert a document into a collection that does not exist, MongoDB will create the collection for you.
- Example: Inserting a document into the `users` collection using `insertOne()`:

```javascript
db.users.insertOne({
  name: "Alice",
  age: 25,
  email: "alice@example.com"
})
```

- Result:

```javascript
{
  "acknowledged" : true,
  "insertedId" : ObjectId("60f9f0b4a4f9c1f4f4f4f4f4")
}
```

- Example: Inserting multiple documents into the `users` collection using `insertMany()`:

```javascript
db.users.insertMany([
  {
    name: "Bob",
    age: 28,
    email: "bob@example.com"
  },
  {
    name: "Charlie",
    age: 30,
    email: "charlie@example.com"
  }
])
```

- Result:

```javascript
{
  "acknowledged" : true,
  "insertedIds" : [
    ObjectId("60f9f0b5a4f9c1f4f4f4f4f5"),
    ObjectId("60f9f0b5a4f9c1f4f4f4f4f6")
  ]
}
```

- Mnemonic: To remember the methods for creating documents in MongoDB, you can use the acronym **I'M IN**:

  - **I**nsertOne
  - **M**any
  - **I**nsert
  - **N**o collection, no problem