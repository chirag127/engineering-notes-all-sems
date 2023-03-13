
#### Output Formats in Map Reduce

- **Text Output Format**: The default output format of MapReduce is a plain text file. The output of the mapper is written to the local disk of the machine and is then transferred to the reducer. It is the simplest output format and is useful for debugging purposes.

- **Sequence File Output Format**: Sequence file is a flat file consisting of binary key/value pairs. It is widely used as an input to MapReduce jobs. It is advantageous over text output format as it is compressed and splittable.

- **Avro Data File Output Format**: Avro is a serialization system that provides rich data structures, a compact binary format, and a container file for sequence files. It is a row-oriented storage format and is used to store large amounts of data.

- **Map File Output Format**: Map file is a container file for storing data in a key/value format. It is a sequence file with an index at the end. It is used to store large amounts of data and is splittable.

- **JSON Output Format**: JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is used to store and exchange data. It is a popular output format for MapReduce jobs as it is easy to read and write.

- **HBase Output Format**: HBase is a NoSQL database that stores data in the form of tables. It is used to store large amounts of data. HBase Output Format is used to write data to an HBase table.