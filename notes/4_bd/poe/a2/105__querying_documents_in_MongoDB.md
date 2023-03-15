 Here is the content in markdown format with formal tone and without external links or emojis:

#### Querying Documents in MongoDB

1. Basic Queries:
- **find()**: Retrieving documents from a collection. Used to fetch all documents or filter documents.
- **findOne()**: Retrieves a single document from a collection that matches the specified filter criteria.
2. Query Filters:
- **equal**: {<field>: <value>}
- **greater than**: {<field>: {$gt: <value>}}
- **less than**: {<field>: {$lt: <value>}}
- **greater than or equal**: {<field>: {$gte: <value>}}
- **less than or equal**: {<field>: {$lte: <value>}}
- **not equal**: {<field>: {$ne: <value>}}
3. Logical Operators:
- **and**: {$and: [query1, query2]}
- **or**: {$or: [query1, query2]}
- **not**: {<field>: {$not: {<operator>: <value>}}}
4. Element Operators:
- **exists**: {<field>: {$exists: <boolean>}}
- **type**: {<field>: {$type: <type>}}
- **mod**: {<field>: {$mod: [<dividend>, <divisor>]}}
- **regex**: {<field>: {$regex: /<pattern>/<options>}}