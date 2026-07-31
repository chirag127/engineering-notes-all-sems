#### Map Reduce types in map reduce

MapReduce is a programming model for processing large-scale data sets in parallel and distributed manner. It consists of two phases: map and reduce. The map function takes a key-value pair as input and produces a list of intermediate key-value pairs as output. The reduce function takes an intermediate key and a list of values associated with that key as input and produces a list of final key-value pairs as output.

The map and reduce functions in Hadoop MapReduce have the following general form :

```java
map: (K1, V1) → list (K2, V2)
reduce: (K2, list (V2)) → list (K3, V3)
```

In general, the map input key and value types (K1 and V1) are different from the map output types (K2 and V2). Similarly, the reduce input key and value types (K2 and V2) are different from the reduce output types (K3 and V3). The map output types and the reduce input types must match, but the Java compiler does not enforce it  .

Hadoop provides several built-in types for MapReduce, such as Text, IntWritable, LongWritable, FloatWritable, DoubleWritable, BooleanWritable, BytesWritable, etc. These types implement the Writable interface, which defines how the data is serialized and deserialized for network transmission and disk storage. Hadoop also provides the WritableComparable interface, which extends the Writable interface and adds a compareTo method for sorting the keys. Most of the built-in types implement the WritableComparable interface.

Hadoop also allows users to define their own custom types for MapReduce, as long as they implement the Writable and/or WritableComparable interfaces. For example, a user can define a Point class that represents a two-dimensional coordinate and implements the WritableComparable interface. Then, the user can use the Point class as a key or value type in MapReduce.