 Here is the formal content written in Markdown format without any emojis or external links for the topic "Querying for the notes of Unit 8 - MongoDB in the subject of Big Data":

### Querying for the notes of Unit 8 - MongoDB in the subject of Big Data

1. MongoDB queries:
- MongoDB uses a document-based query language that is nearly JSON-like.
- The basic syntax is: db.collection.find({query}, {projection})
- Equality Condition: {<field>: <value>} - searches for documents where the field equals the specified value.
- Comparison operators: >, <, >=, <=
- Logical operators: $or, $nor, $not, $and
- Element operators: $exists, $type
- Evaluation operators: $mod, $regex, $text, $where

2. Query by multiple conditions:
- db.collection.find({key1: value1, key2: value2})
- Both conditions must match for a document to be included in the results.
- Can combine conditions with logical operators $or, $nor, $not for more complex queries.

3. Query an array field:
- Check if field exists: db.collection.find({field: {$exists: true}})
- Check size of array: db.collection.find({field: {$size: <value>}})
- Check for specific element: db.collection.find({field: {$all: [<value1>, <value2>]}})

[ Additional points on updating, deleting data, indexes, aggregations, etc. can be added here in the same format. ]