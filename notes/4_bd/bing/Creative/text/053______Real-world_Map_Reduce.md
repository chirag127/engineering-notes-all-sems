#### Real-world Map Reduce

- MapReduce is a programming model and an associated implementation for processing and generating large data sets in parallel and distributed manner.
- MapReduce consists of two phases: map and reduce. The map phase applies a user-defined function to each input key/value pair and produces a set of intermediate key/value pairs. The reduce phase merges all intermediate values associated with the same intermediate key using another user-defined function.
- MapReduce is designed to handle large-scale data processing on clusters of commodity hardware, and provides fault tolerance, load balancing, data locality, scalability and simplicity.
- MapReduce can be used for various applications, such as word count, inverted index, web link analysis, machine learning, data mining, etc.
- One real-world example of MapReduce is how Twitter manages its tweets. Twitter receives around 500 million tweets per day, which is nearly 3000 tweets per second. To analyze the tweets, Twitter uses MapReduce to perform tasks such as filtering, aggregating, counting, sorting, etc.
- The following illustration shows how Twitter uses MapReduce to count the number of tweets per user:

![MapReduce example](https://www.tutorialspoint.com/map_reduce/images/map_reduce_example.jpg)

- In the map phase, each tweet is mapped to a key/value pair, where the key is the user name and the value is 1. The map output is then shuffled and sorted by the key, and sent to the reduce phase.
- In the reduce phase, each reducer receives a list of values for each key, and sums up the values to get the total number of tweets per user. The reduce output is then stored in a file system or a database.