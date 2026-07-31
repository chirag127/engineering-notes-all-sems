#### Map Reduce types in map reduce

- Map Reduce is a programming model for processing large-scale data sets in parallel and distributed manner.
- Map Reduce consists of two main functions: map and reduce, which operate on key-value pairs of data.
- The map function takes an input key-value pair and produces a list of intermediate key-value pairs as output. The intermediate keys do not have to be the same as the input keys.
- The reduce function takes an intermediate key and a list of values associated with that key, and merges them into a smaller set of values or a single value. The output value does not have to be the same type as the input values.
- The general form of the map and reduce functions in Java is:

```java
map: (K1, V1) -> list(K2, V2)
reduce: (K2, list(V2)) -> list(K3, V3)
```

- The types K1, V1, K2, V2, K3, and V3 are defined by the programmer and can be any Java class that implements the Writable interface, which is a common interface for serializable data types in Hadoop.
- The types K1 and V1 are the input types for the map function, and K3 and V3 are the output types for the reduce function. The types K2 and V2 are the intermediate types that are used to shuffle the data between the map and reduce phases.
- The input and output types of the map and reduce functions are not fixed, and can vary depending on the application logic and the data format. However, some common types are:

  - Text: a string of characters, encoded in UTF-8.
  - IntWritable: a 32-bit integer.
  - LongWritable: a 64-bit integer.
  - FloatWritable: a 32-bit floating-point number.
  - DoubleWritable: a 64-bit floating-point number.
  - BooleanWritable: a boolean value.
  - BytesWritable: a byte array.
  - NullWritable: a special type that has no value.

- In addition to the types defined by the programmer, Hadoop also provides some predefined types and formats for the input and output data of the Map Reduce job, such as:

  - TextInputFormat: reads each line of a text file as a key-value pair, where the key is the byte offset of the line and the value is the line content. The default input format for Map Reduce jobs.
  - KeyValueTextInputFormat: reads each line of a text file as a key-value pair, where the key and the value are separated by a tab character.
  - SequenceFileInputFormat: reads binary key-value pairs from a sequence file, which is a compressed and serialized file format for storing data in Hadoop.
  - TextOutputFormat: writes each key-value pair as a line of text, where the key and the value are separated by a tab character. The default output format for Map Reduce jobs.
  - SequenceFileOutputFormat: writes binary key-value pairs to a sequence file.
  - MultipleOutputFormat: allows writing different types of output to different files or directories, based on the key or the value of the output pair.

- A possible mnemonic to remember the types and formats of Map Reduce is:

  - Map: K1, V1 -> list(K2, V2)
  - Reduce: K2, list(V2) -> list(K3, V3)
  - Input: Text, Key-Value, Sequence
  - Output: Text, Sequence, Multiple