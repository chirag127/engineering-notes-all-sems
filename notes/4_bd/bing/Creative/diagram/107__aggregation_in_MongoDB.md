Aggregation in MongoDB is the process of selecting data from a collection and performing various operations on the grouped data, such as sum, average, minimum, maximum, etc. to return a computed result. MongoDB provides two methods to perform aggregation: aggregation pipelines and single-purpose aggregation methods. Aggregation pipelines are the preferred method for performing complex aggregations, as they allow you to specify multiple stages of operations on the input documents. Single-purpose aggregation methods are simple but lack the capabilities of an aggregation pipeline.

#### Aggregation in MongoDB

The following ASCII diagram illustrates the basic architecture of an aggregation pipeline in MongoDB:

```
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  Input         |     |  Stage 1       |     |  Stage 2       |     |  Output        |
|  Documents     |     |  (e.g. $match) |     |  (e.g. $group) |     |  Documents     |
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  { _id: 1,     |     |  { _id: 1,     |     |  { _id: "A",   |     |  { _id: "A",   |
|    type: "A",  | --> |    type: "A",  | --> |    count: 2,   | --> |    count: 2,   |
|    value: 10 } |     |    value: 10 } |     |    total: 30 } |     |    total: 30 } |
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  { _id: 2,     |     |  { _id: 2,     |     |  { _id: "B",   |     |  { _id: "B",   |
|    type: "A",  |     |    type: "A",  |     |    count: 1,   |     |    count: 1,   |
|    value: 20 } |     |    value: 20 } |     |    total: 15 } |     |    total: 15 } |
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  { _id: 3,     |     |                |     |                |     |                |
|    type: "B",  |     |                |     |                |     |                |
|    value: 15 } |     |                |     |                |     |                |
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
```

In this example, the input documents are from a collection that stores some data about different types of items. The first stage of the aggregation pipeline is a $match stage, which filters the documents by the type field and passes only the documents with type "A" to the next stage. The second stage of the aggregation pipeline is a $group stage, which groups the documents by the type field and calculates the count and total of the value field for each group. The output documents are the result of the aggregation pipeline, which contain the grouped and aggregated data.