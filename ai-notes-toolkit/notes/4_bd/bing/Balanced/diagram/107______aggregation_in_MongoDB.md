#### Aggregation in MongoDB

- Aggregation is the process of selecting data from a collection in MongoDB and performing various operations on the selected data to return a computed result .
- Aggregation operations are expressions that can be used to produce reduced and summarized results in MongoDB.
- Aggregation operations can be performed using the **aggregation pipeline**, the **map-reduce function**, or the **single purpose aggregation methods**.
- The aggregation pipeline is a framework that allows you to create a sequence of stages, each performing a specific operation on the input documents, and outputting the modified documents to the next stage .
- The aggregation pipeline supports a variety of stages, such as `$match`, `$group`, `$sort`, `$project`, `$unwind`, `$lookup`, `$out`, etc .
- The aggregation pipeline can be used for various purposes, such as filtering, grouping, transforming, joining, sorting, and updating documents  .
- The map-reduce function is a way of performing aggregation by applying a map function to each document and then reducing the results by a key.
- The map-reduce function can be used for complex aggregation tasks that cannot be easily expressed by the aggregation pipeline.
- The single purpose aggregation methods are simple methods that perform common aggregation tasks, such as counting, finding the minimum or maximum value, or calculating the average.
- The single purpose aggregation methods are faster and easier to use than the aggregation pipeline or the map-reduce function, but they are less flexible and expressive.
- Some examples of single purpose aggregation methods are `count()`, `distinct()`, `group()`, and `aggregate()`.