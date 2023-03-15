#### Querying Documents in MongoDB

- MongoDB is a document-oriented database that stores data in JSON-like format.
- To query data from MongoDB collection, you need to use MongoDB's `find()` method.
- The basic syntax of `find()` method is as follows:

```javascript
db.collection_name.find(query, projection)
```

- The `query` parameter is an optional document that specifies the criteria for selecting documents. If omitted, all documents in the collection are returned.
- The `projection` parameter is an optional document that specifies the fields to include or exclude in the result set. If omitted, all fields are included.
- The `find()` method returns a cursor object that can be iterated to access the documents.
- To query documents by their unique identifier `_id`, you need to use the `ObjectId()` function to convert the string value to an `ObjectId` type.
- For example, the following query returns the document with `_id` equal to `"60c9b5e9d6e6b9f9c0d7c8b9"`:

```javascript
db.books.find({_id: ObjectId("60c9b5e9d6e6b9f9c0d7c8b9")})
```

- To query documents by their embedded or nested fields, you need to use the dot notation to specify the path to the field.
- For example, the following query returns the documents where the field `author.name` equals `"J.K. Rowling"`:

```javascript
db.books.find({"author.name": "J.K. Rowling"})
```

- To query documents by multiple criteria, you can use logical operators such as `$and`, `$or`, `$not`, etc. to combine the conditions.
- For example, the following query returns the documents where the field `genre` equals `"Fantasy"` and the field `price` is less than or equal to `20`:

```javascript
db.books.find({$and: [{genre: "Fantasy"}, {price: {$lte: 20}}]})
```

- To query documents by using comparison, logical, or array operators, you need to use the `$` prefix to indicate the operator name.
- For example, the following query returns the documents where the field `rating` is greater than `4` or the field `reviews` contains an element that matches the subdocument `{user: "Alice", comment: "Great book!"}`:

```javascript
db.books.find({$or: [{rating: {$gt: 4}}, {reviews: {$elemMatch: {user: "Alice", comment: "Great book!"}}}]})
```

- To query documents by using regular expressions, you need to use the `$regex` operator to specify the pattern and the `$options` operator to specify the flags.
- For example, the following query returns the documents where the field `title` starts with `"Harry Potter"` and is case-insensitive:

```javascript
db.books.find({title: {$regex: "^Harry Potter", $options: "i"}})
```

- To query documents by using text search, you need to create a text index on the fields that contain text data and use the `$text` operator to specify the search term and the `$language` operator to specify the language.
- For example, the following query returns the documents that contain the term `"magic"` in the `title` or `description` fields:

```javascript
db.books.find({$text: {$search: "magic", $language: "en"}})
```

- To query documents by using geospatial data, you need to create a geospatial index on the fields that contain location data and use the geospatial operators such as `$near`, `$geoWithin`, `$geoIntersects`, etc. to specify the geometry or the distance.
- For example, the following query returns the documents that are within 10 kilometers of the point with coordinates `[40.7589, -73.9851]`:

```javascript
db.stores.find({location: {$near: {$geometry: {type: "Point", coordinates: [40.7589, -73.9851]}, $maxDistance: 10000}}})
```

- To query documents by using aggregation, you need to use the `aggregate()` method and specify the pipeline of stages that transform the documents.
- For example, the following query returns the average rating and the number of books for each genre:

```javascript
db.books.aggregate([
  {$group: {_id: "$genre", avg_rating: {$avg: "$rating"}, count: