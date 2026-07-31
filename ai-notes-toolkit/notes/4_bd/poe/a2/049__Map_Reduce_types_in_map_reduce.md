 Here is the formal content on the topic "Map Reduce types in map reduce" in markdown format without any emojis or external links:

#### Map Reduce types in map reduce

1. Map phase - The map phase takes input data and converts it into key-value pairs. The keys and values can be of any data type. This output of the map phase is input to the reduce phase.
2. Shuffle and Sort phase - The key-value pairs obtained from the map phase are shuffled and sorted based on their keys. This is done to group all the values having the same key together.
3. Reduce phase - The reduce phase takes the output from the shuffle and sort phase and combines the values having the same key. The number of reduce tasks to be executed can be specified before the MapReduce job runs. The output of the reduce phase is the final output of the MapReduce algorithm.

The MapReduce algorithm is useful for performing operations like counting occurrences of words, grouping data, computing aggregates, etc. on large datasets in a distributed fashion. The core tasks of splitting the input data, processing the splits in parallel and combining the output can be customized based on the use case. The power of MapReduce lies in its flexibility and scalability in processing huge volumes of data.