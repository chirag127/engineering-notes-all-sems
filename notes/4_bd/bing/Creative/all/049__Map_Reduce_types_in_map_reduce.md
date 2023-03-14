#### Map Reduce types in map reduce

Map Reduce is a programming model for processing large-scale data sets in parallel and distributed environments. It consists of two main phases: map and reduce. In the map phase, a user-defined function is applied to each input record to produce intermediate key-value pairs. In the reduce phase, another user-defined function is applied to all the values associated with the same key to produce the final output.

There are different types of map reduce operations, depending on the input and output formats, the number of map and reduce tasks, and the data partitioning and shuffling strategies. Some of the common types are:

- **Identity map reduce**: This is the simplest type of map reduce, where the map function does not change the input records and the reduce function just copies the values to the output. This type of map reduce can be used for data copying, filtering, or sampling.

- **Word count map reduce**: This is a classic example of map reduce, where the map function emits each word in the input record as a key and 1 as a value, and the reduce function sums up the values for each key and emits the word and its frequency as the output. This type of map reduce can be used for text analysis, such as finding the most common words in a document or a corpus.

- **Inverted index map reduce**: This is another common type of map reduce, where the map function emits each word in the input record as a key and the record identifier as a value, and the reduce function concatenates the values for each key and emits the word and its list of record identifiers as the output. This type of map reduce can be used for building an index for a search engine, such as finding all the documents that contain a given word or phrase.

- **Join map reduce**: This is a type of map reduce that performs a join operation on two or more input data sets, based on a common key attribute. The map function emits the key and the record as a value, along with a tag to indicate the source data set. The reduce function groups the values for each key and performs the join logic, such as inner join, outer join, or cross join, and emits the joined records as the output. This type of map reduce can be used for data integration, such as combining information from different sources or tables.

- **Aggregation map reduce**: This is a type of map reduce that performs an aggregation operation on the input data set, such as sum, average, count, min, max, or median. The map function emits the key and the value to be aggregated, and the reduce function applies the aggregation function to the values for each key and emits the key and the aggregated value as the output. This type of map reduce can be used for data analysis, such as finding the total sales, average rating, or median age of a group of records.

- **Matrix multiplication map reduce**: This is a type of map reduce that performs a matrix multiplication operation on two input matrices, A and B, to produce an output matrix, C. The map function emits the row and column indices of the output matrix as the key and the product of the corresponding elements of the input matrices as the value. The reduce function sums up the values for each key and emits the key and the sum as the output. This type of map reduce can be used for linear algebra, such as solving systems of equations, performing transformations, or computing eigenvalues and eigenvectors.

A possible mnemonic to remember these types of map reduce is:

- I WISH I JAM
- Identity, Word count, Inverted index, Sum, Join, Aggregation, Matrix multiplication