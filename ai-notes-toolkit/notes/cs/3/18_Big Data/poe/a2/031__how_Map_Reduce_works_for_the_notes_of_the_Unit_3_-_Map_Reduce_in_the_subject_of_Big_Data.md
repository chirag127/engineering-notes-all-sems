 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### How Map Reduce works

1. Map phase:

- The input data is divided into splits which are processed by the map tasks in parallel.
- The map task processes the input and outputs key-value pairs.
- The framework sorts the output of the maps by keys.

2. Shuffle phase:

- The framework transfers the map output to the reducers via network based on the key.
- The reducers receive all the values for a given key.

3. Reduce phase:

- The reduce task processes the sorted key-value pairs and outputs the final result.
- The number of reducers is configurable and they run in parallel.
- Combiner can be used to pre-aggregate the map output and reduce the network traffic.

The Map Reduce framework handles all the complexities of distributing the data, processing in parallel and handling faults. The user only needs to provide the map and reduce functions to process the data. Map Reduce is scalable and fault tolerant and provides a distributed programming model to process large data sets.

How's this? I have written the content in points in a formal tone without any emojis or external links as you requested. Let me know if you would like me to modify or expand the content in any way.