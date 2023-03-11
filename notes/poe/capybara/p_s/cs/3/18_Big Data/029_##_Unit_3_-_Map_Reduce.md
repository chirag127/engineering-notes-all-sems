## Unit 3 - Map Reduce

MapReduce is a programming model and an associated implementation for processing and generating big data sets with a parallel, distributed algorithm on a cluster.

### MapReduce Framework

MapReduce is a framework for processing large data sets across a cluster of machines. The framework consists of two main functions: Map and Reduce.

#### Map

Map function takes a set of data and converts it into another set of data, where individual elements are broken down into tuples (key-value pairs).

#### Reduce

Reduce function takes the output from a map as an input and combines those data tuples into a smaller set of tuples.

### Advantages of MapReduce

- Scalability: MapReduce is highly scalable and can process a large amount of data in parallel across a cluster of machines.

- Fault tolerance: MapReduce is fault-tolerant, which means that if a machine fails, the framework automatically redirects the work to another machine.

- Flexibility: MapReduce is flexible and can be used with different programming languages.

### Disadvantages of MapReduce

- Complexity: MapReduce is a complex framework that requires a significant amount of knowledge to use effectively.

- Development time: Developing MapReduce programs can be time-consuming because of its complexity.

### MapReduce Applications

- Log processing: MapReduce is commonly used in log processing, where large amounts of data need to be analyzed quickly.

- Search engines: MapReduce is used by search engines to perform indexing and data mining tasks.

- Machine learning: MapReduce is used in machine learning algorithms for processing large data sets.

### Example of MapReduce

The following is an example of MapReduce program that counts the number of occurrences of each word in a given text file:

```
Map(String key, String value):
  // key: document name
  // value: document contents
  for each word w in value:
    EmitIntermediate(w, "1");

Reduce(String key, Iterator values):
  // key: word
  // values: list of counts
  int sum = 0;
  for each v in values:
    sum += ParseInt(v);
  Emit(key, AsString(sum));
```

### Conclusion

MapReduce is a powerful framework for processing and generating large data sets. It is highly scalable, fault-tolerant, and flexible, making it a popular choice for many big data applications. However, it is also complex and requires a significant amount of knowledge to use effectively.