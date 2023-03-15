#### Hadoop I/O
- Hadoop comes with a set of primitives for data I/O.
- Some of these techniques are more general than Hadoop, such as data integrity and compression, but deserve special consideration when dealing with multi-terabyte datasets.
- Hadoop has its own compact and fast serialization format, Writables, that MapReduce programs use to generate keys and value types.
- Hadoop’s own Record I/O (found in the org.apache.hadoop.record package) has an IDL that is compiled into Writable objects, which makes it convenient for generating types that are compatible with MapReduce.
- However, Record I/O was not widely used, and has been deprecated in favor of Avro.