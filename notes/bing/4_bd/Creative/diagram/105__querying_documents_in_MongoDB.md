Querying documents in MongoDB is the process of retrieving data from a collection using the db.collection.find() method. This method takes two parameters: a filter object that specifies the criteria for selecting documents, and an optional projection object that specifies the fields to return. The method returns a cursor object that can be iterated to access the matching documents.

#### Querying documents in MongoDB

The following diagram illustrates the basic architecture of querying documents in MongoDB:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Application    |       |  MongoDB Shell  |       |  MongoDB Server |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Driver         |       |  Driver         |       |  Database       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  db.collection. |       |  db.collection. |       |  Collection     |
|  find()         |       |  find()         |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Cursor         |       |  Cursor         |       |  Documents      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The diagram shows the following steps:

- The application or the MongoDB shell uses a driver to connect to the MongoDB server and issue a db.collection.find() query.
- The driver sends the query to the MongoDB server and receives a cursor object that points to the first matching document in the collection.
- The application or the MongoDB shell iterates through the cursor to access the documents that satisfy the query criteria. The cursor can also apply additional methods such as sort(), limit(), or skip() to modify the result set.