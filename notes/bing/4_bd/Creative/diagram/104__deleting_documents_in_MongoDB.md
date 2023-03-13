#### Deleting documents in MongoDB

MongoDB provides several methods to delete documents from a collection. The most common ones are:

- `db.collection.remove()` : This method deletes one or more documents that match a given filter condition. It can take an optional parameter to specify whether to delete just one document or all matching documents. It returns a write result object that contains the number of deleted documents and other information.
- `db.collection.deleteOne()` : This method deletes a single document that matches a given filter condition. It returns a delete result object that contains the number of deleted documents and other information.
- `db.collection.deleteMany()` : This method deletes all documents that match a given filter condition. It returns a delete result object that contains the number of deleted documents and other information.
- `delete` : This is a command that can be used in the mongo shell to delete documents from a collection. It takes a query document as a parameter and deletes all matching documents. It returns a command result object that contains the number of deleted documents and other information.

The following diagram illustrates the basic architecture of deleting documents in MongoDB using ASCII art:

```
+-----------------+      +-----------------+      +-----------------+
| mongo shell     |      | mongod server   |      | database        |
|                 |      |                 |      |                 |
|                 |      |                 |      |                 |
|                 |      |                 |      |                 |
| +-------------+ |      | +-------------+ |      | +-------------+ |
| | delete      | |      | | delete      | |      | | delete      | |
| | command     | |----->| | command     | |----->| | operation   | |
| +-------------+ |      | +-------------+ |      | +-------------+ |
|                 |      |                 |      |                 |
| +-------------+ |      | +-------------+ |      | +-------------+ |
| | db.collection| |      | | db.collection| |      | | collection  | |
| | .remove()   | |----->| | .remove()   | |----->| |             | |
| +-------------+ |      | +-------------+ |      | +-------------+ |
|                 |      |                 |      |                 |
| +-------------+ |      | +-------------+ |      | +-------------+ |
| | db.collection| |      | | db.collection| |      | | collection  | |
| | .deleteOne()| |----->| | .deleteOne()| |----->| |             | |
| +-------------+ |      | +-------------+ |      | +-------------+ |
|                 |      |                 |      |                 |
| +-------------+ |      | +-------------+ |      | +-------------+ |
| | db.collection| |      | | db.collection| |      | | collection  | |
| | .deleteMany()| |----->| | .deleteMany()| |----->| |             | |
| +-------------+ |      | +-------------+ |      | +-------------+ |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```