#### Aggregation in MongoDB

- Aggregation in MongoDB is the process of selecting data from a collection and performing operations on the data to return computed results.
- Aggregation can be used to group values from multiple documents, perform calculations on the grouped data, and analyze data changes over time.
- MongoDB provides two methods to perform aggregation: aggregation pipelines and single purpose aggregation methods.
- Aggregation pipelines are the preferred method for performing aggregations. They consist of one or more stages that process documents and pass them to the next stage. Each stage can perform an operation on the input documents, such as filtering, grouping, calculating, sorting, etc.
- Single purpose aggregation methods are simple but lack the capabilities of an aggregation pipeline. They are a collection of helper methods that apply to a collection to calculate a result, such as countDocuments(), distinct(), estimatedDocumentCount(), etc.
- Aggregation operations can be performed using the db.collection.aggregate() method or the aggregation framework in the MongoDB drivers.