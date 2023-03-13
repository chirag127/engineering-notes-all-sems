#### Deleting Documents in MongoDB

MongoDB is a popular NoSQL database management system that stores data in collections of documents. Deleting documents is an essential operation when it comes to managing data in a MongoDB database. In this section, we will explore how to delete documents in MongoDB.

#### Syntax for Deleting Documents in MongoDB

The following is the syntax for deleting documents in MongoDB:

```
db.collection.deleteOne(<filter>)
```

The above command deletes the first document that matches the specified filter. If you want to delete all documents that match the filter, you can use the following command:

```
db.collection.deleteMany(<filter>)
```

#### Parameters for Deleting Documents in MongoDB

The following are the parameters for deleting documents in MongoDB:

- `db`: The name of the database that contains the collection.
- `collection`: The name of the collection that contains the documents.
- `filter`: The criteria to select the documents to delete.

#### Mnemonic Trick for Deleting Documents in MongoDB

A useful mnemonic for remembering the syntax for deleting documents in MongoDB is "deleteOne for one document, and deleteMany for many documents."

#### Example for Deleting Documents in MongoDB

Consider the following example where we have a collection named "students" that contains documents with information about students:

```
db.students.insertMany([
   {"name": "Alice", "age": 20},
   {"name": "Bob", "age": 22},
   {"name": "Charlie", "age": 21},
   {"name": "David", "age": 23}
])
```

To delete the document for the student named "Bob," we can use the following command:

```
db.students.deleteOne({"name": "Bob"})
```

To delete all documents for students who are 21 years old, we can use the following command:

```
db.students.deleteMany({"age": 21})
```

#### Conclusion

Deleting documents in MongoDB is a straightforward process that can be accomplished using the `deleteOne` and `deleteMany` commands. By specifying the appropriate filter, you can delete individual documents or multiple documents that match a specific criteria. Remembering the syntax for deleting documents in MongoDB is easy with the mnemonic "deleteOne for one document, and deleteMany for many documents."