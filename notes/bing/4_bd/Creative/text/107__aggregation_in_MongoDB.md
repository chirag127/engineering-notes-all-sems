#### Aggregation in MongoDB

Aggregation in MongoDB is the process of selecting, grouping, and transforming data from a collection to produce computed results. Aggregation can be used for various purposes, such as:

- Calculating statistics and summaries of data
- Performing complex queries and filters
- Joining data from multiple collections
- Shaping and transforming data for different needs

MongoDB provides two methods to perform aggregation:

- Single-purpose aggregation operations: These are collection methods that perform a specific aggregation task, such as counting documents, finding the minimum or maximum value, or calculating the average. Examples of single-purpose aggregation operations are `count()`, `distinct()`, and `group()`.
- Aggregation pipeline: This is a more flexible and powerful way of performing aggregation. It allows you to create a sequence of stages that process documents in a collection. Each stage can perform a different operation on the input documents, such as filtering, grouping, sorting, projecting, or joining. The output of one stage becomes the input of the next stage, until the final result is produced. Examples of aggregation pipeline stages are `$match`, `$group`, `$sort`, and `$lookup`.

To use aggregation in MongoDB, you can use the `aggregate()` method on a collection. This method accepts an array of stages as an argument, and returns a cursor that iterates over the aggregated documents. You can also use the `db.collection.aggregate()` command in the MongoDB shell to run an aggregation pipeline.

Here is an example of using aggregation in MongoDB to find the average rating of movies by genre:

```javascript
// Create a collection of movies with title, genre, and rating fields
db.movies.insertMany([
  {title: "The Godfather", genre: "Crime", rating: 9.2},
  {title: "The Shawshank Redemption", genre: "Drama", rating: 9.3},
  {title: "The Dark Knight", genre: "Action", rating: 9.0},
  {title: "The Matrix", genre: "Sci-Fi", rating: 8.7},
  {title: "The Lord of the Rings: The Return of the King", genre: "Fantasy", rating: 8.9},
  {title: "The Lion King", genre: "Animation", rating: 8.5},
  {title: "Toy Story", genre: "Animation", rating: 8.3},
  {title: "The Silence of the Lambs", genre: "Thriller", rating: 8.6},
  {title: "The Sixth Sense", genre: "Thriller", rating: 8.1},
  {title: "Inception", genre: "Sci-Fi", rating: 8.8}
])

// Use aggregation to find the average rating of movies by genre
db.movies.aggregate([
  // Group the documents by genre and calculate the average rating
  {$group: {_id: "$genre", avg_rating: {$avg: "$rating"}}},
  // Sort the results by average rating in descending order
  {$sort: {avg_rating: -1}}
])
```

The output of the aggregation pipeline is:

```javascript
{ "_id" : "Drama", "avg_rating" : 9.3 }
{ "_id" : "Crime", "avg_rating" : 9.2 }
{ "_id" : "Action", "avg_rating" : 9 }
{ "_id" : "Fantasy", "avg_rating" : 8.9 }
{ "_id" : "Sci-Fi", "avg_rating" : 8.75 }
{ "_id" : "Thriller", "avg_rating" : 8.35 }
{ "_id" : "Animation", "avg_rating" : 8.4 }
```

This shows that the highest average rating belongs to the drama genre, followed by crime and action. The lowest average rating belongs to the thriller genre.