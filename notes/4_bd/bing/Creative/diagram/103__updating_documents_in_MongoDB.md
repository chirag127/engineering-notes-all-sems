To update documents in MongoDB, you can use the following methods:

- db.collection.updateOne(): This method updates the first document that matches a specified filter. You can use update operators, such as $set, to modify field values. You can also use the $currentDate operator to update the value of a field to the current date.
- db.collection.updateMany(): This method updates all the documents that match a specified filter. You can use the same update operators as in updateOne(). This method is useful for bulk updates.
- db.collection.replaceOne(): This method replaces the entire content of a document except for the _id field. You cannot use update operators in this method. You can only pass a new document that contains field/value pairs. The replacement document can have different fields from the original document.

#### Updating documents in MongoDB

The following diagram illustrates the basic architecture of updating documents in MongoDB using the updateOne() method:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Application   |     |   MongoDB       |     |   Collection    |
|                 |     |   Server        |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  db.collection. |     |                 |     |                 |
|  updateOne(     |     |                 |     |                 |
|  {filter},      |     |                 |     |                 |
|  {update},      |     |                 |     |                 |
|  {options}      |     |                 |     |                 |
|  )              |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|                 |---->|                 |     |                 |
|                 |     |                 |---->|                 |
|                 |     |                 |     |                 |
|                 |     |                 |<----|                 |
|                 |     |                 |     |                 |
|                 |<----|                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The application sends a request to the MongoDB server with the filter, update, and options parameters. The MongoDB server applies the filter to the collection and updates the first document that matches the filter. The MongoDB server returns a result object that contains information about the operation, such as the number of documents modified. The application receives the result object and can check the status of the update.