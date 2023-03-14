To create documents in MongoDB, you can use the insertOne(), insertMany(), or insert() methods. These methods insert one or more documents into a collection. Each document is provided as a parameter or an array of parameters. For example, to insert a single document into a collection named "users", you can use the following command:

db.users.insertOne({name: "Alice", age: 25, email: "alice@example.com"})

To insert multiple documents into the same collection, you can use the following command:

db.users.insertMany([
  {name: "Bob", age: 30, email: "bob@example.com"},
  {name: "Charlie", age: 35, email: "charlie@example.com"}
])

To insert one or more documents using the insert() method, you can use the following command:

db.users.insert({name: "David", age: 40, email: "david@example.com"})
db.users.insert([
  {name: "Eve", age: 45, email: "eve@example.com"},
  {name: "Frank", age: 50, email: "frank@example.com"}
])

The following diagram illustrates the basic architecture of creating documents in MongoDB:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Application    |       |  MongoDB Shell  |       |  MongoDB Server |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  insertOne()    | ----> |  insertOne()    | ----> |  insertOne()    |
|  insertMany()   | ----> |  insertMany()   | ----> |  insertMany()   |
|  insert()       | ----> |  insert()       | ----> |  insert()       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```