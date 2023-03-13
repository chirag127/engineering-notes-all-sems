To update documents in MongoDB, you can use different methods depending on whether you want to update a single document, multiple documents, or replace a document. You also need to specify a filter condition to match the documents you want to update, and an update document that contains the new values or update operators.

#### Updating documents in MongoDB

The following diagram illustrates the basic steps of updating documents in MongoDB using the MongoDB shell:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Connect to     |     |  Get the        |     |  Use update     |
|  MongoDB        |     |  database and   |     |  methods with   |
|  instance       |     |  collection     |     |  filter and     |
|                 |     |                 |     |  update         |
|                 |     |                 |     |  document       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       V                       V                       V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  db             |     |  db.comets      |     |  db.comets.     |
|                 |     |                 |     |  updateOne(     |
|                 |     |                 |     |  {name: "Halley"},|
|                 |     |                 |     |  {$set: {year: 1986}})|
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The above example updates one document in the comets collection where the name field is "Halley" and sets the year field to 1986. You can use other update methods, such as updateMany() or replaceOne(), to update multiple documents or replace a document respectively. You can also use other update operators, such as $inc, $push, $rename, etc., to modify the fields in different ways. For more details, please refer to the MongoDB documentation.