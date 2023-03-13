##### Avro and file based data structures in Hadoop io

- Avro is a data serialization framework that is widely supported throughout Hadoop and its ecosystem  .
- Avro creates a data file where it keeps data along with schema in its metadata section, which makes the file self-describing .
- Avro data files support compression and are splittable, which is crucial for a MapReduce data input format.
- Avro data files are line-oriented, meaning the value of each row in the file are stored consecutively.
- Avro provides a rich data structure which makes it more popular than other similar solutions.
- Avro is the best fit for Big Data processing and is quite popular in Hadoop and Kafka world for its faster processing.
- Avro is best suited to Spark processing, whereas Hadoop supports other file formats such as ORC and Parquet.
- Avro supports schema evolution, which means changing the schema without breaking the compatibility with older data.