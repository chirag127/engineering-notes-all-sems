### Unit 3 - Map Reduce

MapReduce is a programming model and an associated implementation for processing and generating large data sets. There are two main types of MapReduce:

1. **Hadoop MapReduce:** This is an open-source implementation of the MapReduce programming model, developed by the Apache Software Foundation. It is written in Java and is commonly used for processing large data sets on a cluster of computers.

2. **Google MapReduce:** This is the original implementation of the MapReduce programming model, developed by Google. It is proprietary software and is used internally by Google for processing large data sets.

Both types of MapReduce have the same basic structure, consisting of a Map function that processes a key/value pair to generate a set of intermediate key/value pairs, and a Reduce function that merges all intermediate values associated with the same intermediate key. However, there are some differences in the implementation details and the specific features offered by each type of MapReduce. For example, Hadoop MapReduce provides a more flexible and customizable framework, while Google MapReduce is optimized for performance and scalability.