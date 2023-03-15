#### Querying Documents in MongoDB

MongoDB is a NoSQL database that stores data in the form of documents. These documents are stored in collections, which are similar to tables in a relational database. To query documents in MongoDB, you can use the `find()` method. Here are some key points to remember when querying documents in MongoDB:

1. The `find()` method is used to query documents in a collection. It takes a query filter as an argument and returns a cursor to the documents that match the query.
2. You can specify the fields to return in the query results by passing a projection document as the second argument to the `find()` method.
3. You can use query operators such as `$gt`, `$lt`, `$in`, and `$or` to specify conditions in the query filter.
4. You can use the `sort()`, `skip()`, and `limit()` methods to control the order and number of documents returned by the query.
5. You can use the `count()` method to count the number of documents that match a query.
6. You can use the `explain()` method to obtain information about the query execution plan.
