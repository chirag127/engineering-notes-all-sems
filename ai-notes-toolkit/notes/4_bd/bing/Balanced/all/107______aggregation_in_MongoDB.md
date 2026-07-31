#### Aggregation in MongoDB

- Aggregation is the process of selecting data from a collection in MongoDB and performing various operations on the selected data to return a computed result .
- Aggregation operations are expressions that can be used to produce reduced and summarized results in MongoDB.
- Aggregation operations can be performed using the aggregation pipeline, the map-reduce function, or the single purpose aggregation methods.
- The aggregation pipeline is a framework that allows you to create a sequence of stages that process documents and transform them as they pass from one stage to another.
- Each stage in the aggregation pipeline performs a specific operation on the input documents, such as filtering, grouping, sorting, projecting, or aggregating.
- The output documents of a stage are passed to the next stage as input, and the final result is returned at the end of the pipeline.
- The aggregation pipeline can be used for various purposes, such as data analysis, reporting, data transformation, or data enrichment.
- The aggregation pipeline can be created using the `aggregate()` method, which accepts one or more stage names as arguments .
- Some of the common stages in the aggregation pipeline are:

  - `$match`: This stage filters the documents that match a specified condition and passes them to the next stage.
  - `$group`: This stage groups the documents by a specified expression and applies an accumulator function to each group to compute a value.
  - `$sort`: This stage sorts the documents by a specified order and passes them to the next stage.
  - `$project`: This stage reshapes the documents by adding, removing, or renaming fields and passes them to the next stage.
  - `$unwind`: This stage deconstructs an array field from the input documents and outputs a document for each element in the array.
  - `$lookup`: This stage performs a left outer join with another collection and adds a new array field to the input documents.
  - `$out`: This stage writes the output documents to a specified collection.

- The map-reduce function is a way of performing aggregation by applying a map function to each document and then reducing the results by a key.
- The map function emits key-value pairs, and the reduce function combines the values for each key and returns a single value.
- The map-reduce function can be used for complex aggregation tasks that cannot be done by the aggregation pipeline.
- The map-reduce function can be created using the `mapReduce()` method, which accepts a map function, a reduce function, and an output specification as arguments.
- The single purpose aggregation methods are simple methods that perform specific aggregation tasks on a collection.
- Some of the single purpose aggregation methods are:

  - `count()`: This method returns the number of documents in a collection or that match a query.
  - `distinct()`: This method returns an array of distinct values for a specified field in a collection or that match a query.
  - `group()`: This method groups documents by a specified key and applies a reduce function to each group.