# Stateless and Stateful Processing

- Stream processing is the process of analyzing and processing data streams in real time.
- Stream processing can be stateless or stateful, depending on whether the current data/events are processed independently of previous ones or not.
- Stateless stream processing is when the data is evaluated as it arrives without consideration for the prior state or knowledge . For example, if you want to count the number of words in a stream of text, you can do it in a stateless way by simply adding one to a counter for each word you see.
- Stateful stream processing is when the data is analyzed with regard to the overall state of the data, which is maintained and updated over time . For example, if you want to calculate the average word length in a stream of text, you need to keep track of the total number of words and the total number of characters seen so far, and update them as new words arrive.
- Stateful stream processing allows for more complex and accurate analysis of data streams, but it also requires more memory and computation resources than stateless stream processing.
- Stateful stream processing can be implemented using various techniques, such as windows, aggregations, joins, and checkpoints.