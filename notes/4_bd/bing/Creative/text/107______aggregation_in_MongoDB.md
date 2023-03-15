#### Aggregation in MongoDB

- Aggregation is the process of selecting data from a collection in MongoDB and performing various operations on the selected data to produce computed results .
- Aggregation operations are expressions that can be used to reduce and summarize data in MongoDB.
- Aggregation operations can be performed using the **aggregation pipeline**, the **map-reduce function**, or the **single purpose aggregation methods**.
- The aggregation pipeline is a framework that allows you to create a sequence of stages, each of which performs an operation on the input documents and outputs the modified documents to the next stage .
- The aggregation pipeline supports various stages, such as `$match`, `$group`, `$sort`, `$project`, `$unwind`, `$lookup`, and more .
- The aggregation pipeline can be used for various purposes, such as filtering, grouping, transforming, joining, sorting, and aggregating data  .
- The aggregation pipeline can be created using the `aggregate()` method, which accepts one or more stage names as arguments.
- The map-reduce function is a way of performing aggregation by applying a map function to each document and then reducing the results by a key.
- The map-reduce function can be used for complex aggregation tasks that cannot be easily expressed by the aggregation pipeline.
- The map-reduce function can be created using the `mapReduce()` method, which accepts a map function, a reduce function, and an output collection as arguments.
- The single purpose aggregation methods are simple methods that perform specific aggregation tasks, such as counting, finding the minimum or maximum value, or calculating the average.
- The single purpose aggregation methods can be used for simple aggregation tasks that do not require multiple stages or complex logic.
- The single purpose aggregation methods include `count()`, `distinct()`, `group()`, and more.