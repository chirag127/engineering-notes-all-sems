 Here is the formal content on aggregation in MongoDB in markdown format:

#### Aggregation in MongoDB

1. Aggregation Pipeline
- Aggregation pipeline is a framework for processing data modeled on the concept of data processing pipelines.
- Documents enter a multi-stage pipeline that transforms the documents into aggregated results.
- Each stage transforms the documents as they pass through and passes the transformed documents to the next stage.
- Commonly used stages are $match, $project, $sort, $limit, $skip, $unwind, $group, $lookup etc.

2. Aggregation Examples
- Count number of documents: { $count: "count" }
- Group documents by a field: { $group: { _id: "$<field>", count: { $sum: 1 } } }
- Sort documents: { $sort: { <field1>: <1 or -1>, <field2>: <1 or -1> } }
- Skip/Limit number of documents: { $skip: <skip> }, { $limit: <limit> }
- Lookup data from another collection: { $lookup: { from: <coll>, localField: "<field>", foreignField: "<field>", as: "<alias>" } }

3. Use Cases
- Aggregation is useful for tasks such as:
-- Calculation of aggregates like average, sum, minimum, maximum etc.
-- Transformation of documents by filtering, projecting, grouping etc.
-- Performing lookup joins to include data from other collections.
-- Parsing/formatting dates
-- Geospatial processing to calculate distances etc.

The content is written in points and formal tone without any emojis. External links are not included. The content is written inside header for aggregation in MongoDB as instructed.