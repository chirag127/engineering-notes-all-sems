#### Aggregation in MongoDB

- Aggregation is the process of selecting data from a collection in MongoDB and performing various operations on the selected data to produce computed results .
- Aggregation operations are expressions that can be used to reduce and summarize data in MongoDB.
- Aggregation operations can be performed using the aggregation pipeline, the map-reduce function, or the single purpose aggregation methods.
- The aggregation pipeline is a framework that allows you to create a sequence of stages that process documents and output aggregated results .
- Each stage in the aggregation pipeline performs a specific operation on the input documents, such as filtering, grouping, sorting, projecting, or transforming them .
- The output documents of a stage are passed to the next stage as input, until the final stage produces the aggregated result .
- The aggregation pipeline can be created using the `aggregate()` method, which accepts one or more stage names as arguments.
- Some of the common aggregation stages are:
  - `$match`: Filters the documents that match a specified condition.
  - `$group`: Groups the documents by a specified expression and applies an accumulator function to each group.
  - `$sort`: Sorts the documents by a specified order.
  - `$project`: Specifies the fields to include or exclude in the output documents.
  - `$unwind`: Deconstructs an array field from the input documents and outputs a document for each element.
  - `$lookup`: Performs a left outer join with another collection and appends the joined documents to the output documents.
  - `$addFields`: Adds new fields to the output documents.
  - `$out`: Writes the output documents to a specified collection.
- Aggregation operations can be used for various purposes, such as data analysis, reporting, data transformation, or data enrichment .