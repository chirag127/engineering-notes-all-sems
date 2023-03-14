#### Indexing in MongoDB

- Indexing is a process that improves the performance of queries by creating data structures that store a small portion of the collection's data.
- Indexes support the efficient execution of queries by reducing the number of documents that the database needs to scan.
- MongoDB provides various types of indexes, such as single field, compound, multikey, text, geospatial, hashed, and wildcard indexes.
- Each index type supports different query patterns and has different advantages and disadvantages.
- By default, MongoDB creates a unique index on the `_id` field of each collection, which prevents the insertion of duplicate documents with the same `_id` value.
- To create additional indexes, MongoDB provides the `createIndex()` method, which takes a document that specifies the field or fields to index and the index type.
- For example, to create a single field index on the `name` field of the `users` collection, the command would be:

```javascript
db.users.createIndex({name: 1})
```

- The value `1` indicates an ascending index, while `-1` indicates a descending index.
- To create a compound index on multiple fields, the command would be:

```javascript
db.users.createIndex({name: 1, age: -1})
```

- This creates an index on the `name` field in ascending order and the `age` field in descending order.
- Compound indexes can support queries that match on all or a prefix of the indexed fields.
- To create a multikey index on an array field, the command would be:

```javascript
db.users.createIndex({hobbies: 1})
```

- This creates an index on the `hobbies` field, which is an array of values.
- Multikey indexes can support queries that match on one or more elements of the array field.
- To create a text index on a field that contains string data, the command would be:

```javascript
db.users.createIndex({bio: "text"})
```

- This creates a text index on the `bio` field, which is a string of text.
- Text indexes can support queries that perform full-text search on the string data, using operators such as `$text` and `$search`.
- To create a geospatial index on a field that contains geospatial data, such as coordinates or polygons, the command would be:

```javascript
db.users.createIndex({location: "2dsphere"})
```

- This creates a 2dsphere index on the `location` field, which is a GeoJSON object that represents a point on the earth's surface.
- Geospatial indexes can support queries that perform geospatial operations, such as finding nearby points or intersecting regions, using operators such as `$near` and `$geoWithin`.
- To create a hashed index on a field that contains any type of data, the command would be:

```javascript
db.users.createIndex({email: "hashed"})
```

- This creates a hashed index on the `email` field, which is a string of email address.
- Hashed indexes can support queries that perform exact matches on the hashed value of the field, using operators such as `$eq` and `$in`.
- Hashed indexes are also useful for sharding collections, which is a process of distributing data across multiple servers.
- To create a wildcard index on all or a subset of fields in a collection, the command would be:

```javascript
db.users.createIndex({"$**": 1})
```

- This creates a wildcard index on all the fields in the `users` collection, which can support queries that match on any field.
- To create a wildcard index on a subset of fields, the command would be:

```javascript
db.users.createIndex({"name.$**": 1})
```

- This creates a wildcard index on all the subfields of the `name` field, which can support queries that match on any subfield of the `name` field.
- Wildcard indexes are useful for collections that have a dynamic schema, where the fields vary across documents.

- Some of the benefits of indexing are:

  - Faster query execution, as the database can use the index to quickly locate the matching documents, instead of scanning the entire collection.
  - Reduced disk I/O, as the database can read only the relevant portions of the data from the disk, instead of loading the entire collection into memory.
  - Improved sort performance, as the database can use the index to sort the results, instead of performing an in-memory sort.
  - Enhanced aggregation performance, as the database can use the index to optimize some stages of the aggregation pipeline, such as `$match` and `$group`.

- Some of the drawbacks of indexing are:

  - Increased disk