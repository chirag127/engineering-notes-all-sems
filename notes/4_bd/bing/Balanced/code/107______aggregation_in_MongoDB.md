#### Aggregation in MongoDB

- Aggregation is the process of selecting data from a collection in MongoDB and performing various operations on the selected data to return a computed result .
- Aggregation operations are expressions that can be used to produce reduced and summarized results in MongoDB.
- Aggregation operations can be performed using the aggregation pipeline, which is a framework that allows you to create a sequence of stages that process documents.
- Each stage in the aggregation pipeline performs a specific operation on the input documents, such as filtering, grouping, sorting, projecting, etc.
- The output documents of each stage are passed to the next stage as input, until the final result is produced.
- Aggregation pipelines can be used for various purposes, such as data analysis, data transformation, data enrichment, etc.
- Aggregation pipelines can be created using the `aggregate()` method, which accepts one or more stage names as arguments.
- Some of the common aggregation stages are:
  - `$match`: filters the documents that match a specified condition.
  - `$group`: groups the documents by a specified expression and applies an accumulator function to each group.
  - `$sort`: sorts the documents by a specified order.
  - `$project`: modifies the documents by adding, removing, or renaming fields.
  - `$unwind`: splits an array field into multiple documents, one for each element.
  - `$lookup`: performs a left outer join with another collection and adds the joined documents to an array field.
  - `$out`: writes the output documents to a specified collection.