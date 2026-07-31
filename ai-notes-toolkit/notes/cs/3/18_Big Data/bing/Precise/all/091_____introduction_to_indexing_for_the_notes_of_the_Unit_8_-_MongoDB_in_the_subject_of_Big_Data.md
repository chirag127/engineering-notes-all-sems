# Introduction to Indexing

Indexing is a technique used to improve the performance of database queries. It works by creating a data structure that allows the database to quickly locate the records that match a query, without having to scan the entire collection.

Here are some key points to remember about indexing in MongoDB:

1. Indexes can be created on one or more fields in a collection.
2. Indexes can be created in ascending or descending order.
3. Indexes can be created on embedded fields and arrays.
4. Indexes can be created using the `createIndex()` method.
5. Indexes can be used to enforce uniqueness on a field or set of fields.
6. Indexes can be used to improve the performance of queries that use the indexed fields in the query condition, sort, or projection.
7. Indexes can be used to improve the performance of queries that use the `$geoNear`, `$near`, and `$nearSphere` operators.
8. Indexes can be used to improve the performance of queries that use the `$text` operator.
9. Indexes can be used to improve the performance of queries that use the `$lookup` and `$graphLookup` aggregation stages.
10. Indexes can be used to improve the performance of queries that use the `$group` aggregation stage, if the `$group` stage is preceded by a `$sort` stage that sorts the documents by the grouping key.
