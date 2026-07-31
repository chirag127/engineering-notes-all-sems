##### Avro and file based data structures in Hadoop io

Avro is a data serialization system that is used to encode data into a compact binary format. It is commonly used in Hadoop to store and process large amounts of data. Avro data is stored in a file-based data structure, which means that the data is stored in files on the Hadoop Distributed File System (HDFS).

Here is an example of how to write Avro data to a file in Hadoop:

```java
import org.apache.avro.file.DataFileWriter;
import org.apache.avro.io.DatumWriter;
import org.apache.avro.specific.SpecificDatumWriter;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;

// Create a configuration object
Configuration conf = new Configuration();

// Set the Hadoop file system
conf.set("fs.defaultFS", "hdfs://localhost:9000");

// Create a Hadoop file system object
FileSystem fs = FileSystem.get(conf);

// Create a path for the Avro file
Path path = new Path("/user/hadoop/avrodata.avro");

// Create an output stream to write to the Avro file
FSDataOutputStream out = fs.create(path);

// Create a datum writer to write the Avro data
DatumWriter<MyAvroRecord> writer = new SpecificDatumWriter<>(MyAvroRecord.class);

// Create a data file writer to write the Avro data to the file
DataFileWriter<MyAvroRecord> dataFileWriter = new DataFileWriter<>(writer);

// Open the data file writer
dataFileWriter.create(MyAvroRecord.SCHEMA$, out);

// Write the Avro data to the file
dataFileWriter.append(myAvroRecord);

// Close the data file writer
dataFileWriter.close();
```
