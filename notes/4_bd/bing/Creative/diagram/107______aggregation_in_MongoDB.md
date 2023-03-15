#### Aggregation in MongoDB

- Aggregation is the process of selecting data from a collection in MongoDB and performing various operations on the selected data to produce computed results .
- Aggregation operations are expressions that can be used to reduce and summarize data in MongoDB.
- Aggregation operations can be performed using the **aggregation pipeline**, the **map-reduce function**, or the **single purpose aggregation methods**.
- The aggregation pipeline is a framework that allows you to create a sequence of stages, each performing a specific operation on the input documents, and outputting the modified documents to the next stage .
- The aggregation pipeline supports a variety of stages, such as `$match`, `$group`, `$sort`, `$project`, `$unwind`, `$lookup`, `$bucket`, `$facet`, and more .
- The aggregation pipeline can be used for various purposes, such as filtering, grouping, transforming, joining, aggregating, and analyzing data  .
- The aggregation pipeline can be created and executed using the `aggregate()` method in MongoDB.
- The map-reduce function is a way of performing aggregation by applying a map function to each document and then reducing the results by a key.
- The map-reduce function can be used for complex aggregation tasks that cannot be easily expressed by the aggregation pipeline.
- The map-reduce function can be created and executed using the `mapReduce()` method in MongoDB.
- The single purpose aggregation methods are simple methods that perform common aggregation tasks, such as counting, finding the minimum or maximum, or calculating the average of a field.
- The single purpose aggregation methods can be used for simple aggregation tasks that do not require the flexibility and power of the aggregation pipeline or the map-reduce function.
- The single purpose aggregation methods include `count()`, `distinct()`, `group()`, and `estimatedDocumentCount()`.