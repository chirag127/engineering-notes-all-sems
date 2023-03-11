### Updating and Deleting Documents in MongoDB

MongoDB is a popular NoSQL database that provides flexible data modeling and document-oriented storage. In this section, we will learn about updating and deleting documents in MongoDB.

#### Updating Documents

Updating documents in MongoDB is straightforward. We can use the `updateOne()` or `updateMany()` methods to update one or multiple documents, respectively. The syntax of the `updateOne()` method is as follows:

```
db.collection.updateOne(
   <filter>,
   <update>,
   {
      upsert: <boolean>,
      writeConcern: <document>
   }
)
```

Here, `<filter>` specifies the criteria for selecting the document to update, and `<update>` specifies the modifications to make. The `upsert` option is optional and specifies whether to insert a new document if no document matches the filter. The `writeConcern` option is also optional and specifies the level of acknowledgement requested from MongoDB for write operations.

For example, to update the name of a document with a specific `_id` value, we can use the following command:

```
db.collection.updateOne({_id: ObjectId("...")}, {$set: {name: "John Doe"}})
```

This command sets the value of the `name` field to "John Doe" for the document with the specified `_id` value.

#### Deleting Documents

Deleting documents in MongoDB is also straightforward. We can use the `deleteOne()` or `deleteMany()` methods to delete one or multiple documents, respectively. The syntax of the `deleteOne()` method is as follows:

```
db.collection.deleteOne(<filter>)
```

Here, `<filter>` specifies the criteria for selecting the document to delete.

For example, to delete a document with a specific `_id` value, we can use the following command:

```
db.collection.deleteOne({_id: ObjectId("...")})
```

This command deletes the document with the specified `_id` value.

In conclusion, updating and deleting documents in MongoDB is essential for data management and maintenance. With the help of the `updateOne()`, `updateMany()`, `deleteOne()`, and `deleteMany()` methods, we can manipulate the data in our MongoDB collections efficiently.