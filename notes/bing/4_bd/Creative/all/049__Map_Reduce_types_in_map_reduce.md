#### Map Reduce types in map reduce

Map Reduce is a programming model for processing large-scale data sets in parallel and distributed environments. It consists of two main phases: map and reduce. In the map phase, a user-defined function is applied to each input record (key-value pair) and produces a set of intermediate key-value pairs. In the reduce phase, another user-defined function is applied to all the intermediate values associated with the same key and produces a set of output key-value pairs.

There are different types of map reduce operations, depending on the nature of the input, output, and intermediate data. Some of the common types are:

- Identity map reduce: This is the simplest type of map reduce, where the map function does not change the input key-value pairs and the reduce function simply concatenates the values for each key. This type of map reduce can be used to copy or partition data across different machines or files.

- Filtering map reduce: This type of map reduce filters out some of the input records based on a condition. The map function checks the condition and either emits the input key-value pair or discards it. The reduce function is the same as the identity reduce function. This type of map reduce can be used to remove unwanted or invalid data from a data set.

- Aggregation map reduce: This type of map reduce performs some aggregation operation on the values for each key, such as sum, count, average, min, max, etc. The map function emits the input key-value pair or transforms it into a different key-value pair. The reduce function applies the aggregation function to the values for each key and emits a single key-value pair. This type of map reduce can be used to compute statistics or summaries from a data set.

- Join map reduce: This type of map reduce performs a join operation on two or more data sets based on a common key. The map function emits key-value pairs where the key is the join key and the value is the record from the input data set. The reduce function merges the records from different data sets that have the same key and emits a single key-value pair. This type of map reduce can be used to combine related data from different sources.

- Group by map reduce: This type of map reduce performs a group by operation on a data set based on one or more attributes. The map function emits key-value pairs where the key is the group by attribute(s) and the value is the record from the input data set. The reduce function collects the records from the same group and emits a single key-value pair. This type of map reduce can be used to organize data into different categories or clusters.

- Sorting map reduce: This type of map reduce sorts a data set based on one or more attributes. The map function emits key-value pairs where the key is the sort attribute(s) and the value is the record from the input data set. The reduce function is the same as the identity reduce function. The sorting is done by the framework based on the key order. This type of map reduce can be used to order data by some criteria.

- Inverted index map reduce: This type of map reduce creates an inverted index from a collection of documents. The map function emits key-value pairs where the key is a word from the document and the value is the document identifier. The reduce function collects the document identifiers for each word and emits a single key-value pair. This type of map reduce can be used to support text search or analysis.

- Word count map reduce: This is a classic example of map reduce, where the goal is to count the frequency of each word in a collection of documents. The map function emits key-value pairs where the key is a word from the document and the value is 1. The reduce function sums up the values for each word and emits a single key-value pair. This type of map reduce can be used to measure the popularity or importance of words in a corpus.

A mnemonic to remember these types of map reduce is:

- I F A J G S I W
- Identity, Filtering, Aggregation, Join, Group by, Sorting, Inverted index, Word count