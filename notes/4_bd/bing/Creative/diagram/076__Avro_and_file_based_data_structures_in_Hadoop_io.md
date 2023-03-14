Avro is a language-independent, schema-based data serialization system that is popular for big data processing. It stores data and schema in a binary file format, which can be split and compressed. Avro files can be used in Hadoop as input or output for MapReduce jobs.

The following ASCII diagram illustrates the basic structure of an Avro file:

```
+----------------+
|  Avro Header   |
+----------------+
|  Data Block 1  |
+----------------+
|  Data Block 2  |
+----------------+
|      ...       |
+----------------+
|  Data Block N  |
+----------------+
|  File Footer   |
+----------------+
```

The Avro header contains the file metadata, which includes the schema definition in JSON format, the codec name for compression, and a magic number to identify the file as Avro.

Each data block contains a count of the records in the block, the size of the block in bytes, the serialized records, and a synchronization marker to delimit the block.

The file footer contains the number of blocks in the file and the position of the first block, as well as any user-defined metadata.

The Avro schema defines the data types and structure of the records in the file. It can be a primitive type (such as int, string, boolean, etc.), a complex type (such as record, enum, array, map, union, or fixed), or a logical type (such as decimal, date, time, etc.).

The following ASCII diagram illustrates an example of an Avro schema for a record type:

```
{
  "type": "record",
  "name": "Employee",
  "namespace": "com.example.avro",
  "fields": [
    {
      "name": "id",
      "type": "int"
    },
    {
      "name": "name",
      "type": "string"
    },
    {
      "name": "salary",
      "type": "double"
    },
    {
      "name": "department",
      "type": {
        "type": "enum",
        "name": "Department",
        "symbols": ["HR", "IT", "SALES", "MARKETING"]
      }
    },
    {
      "name": "skills",
      "type": {
        "type": "array",
        "items": "string"
      }
    }
  ]
}
```

This schema defines a record type called Employee, with five fields: id, name, salary, department, and skills. The department field is an enum type, which can have one of the four predefined values. The skills field is an array type, which can have zero or more string values. The schema also specifies the namespace for the record type, which is com.example.avro.

The following ASCII diagram illustrates an example of a serialized record that conforms to the above schema:

```
+----------------+
|  id: 123      |
+----------------+
|  name: Alice  |
+----------------+
|  salary: 5000 |
+----------------+
|  department: IT|
+----------------+
|  skills:      |
+----------------+
|  - Java       |
+----------------+
|  - SQL        |
+----------------+
|  - Python     |
+----------------+
```

This record represents an employee with id 123, name Alice, salary 5000, department IT, and skills Java, SQL, and Python. The record is serialized in a binary format, but shown here in a human-readable form for illustration purposes. The actual binary representation depends on the encoding scheme used by Avro, which is based on variable-length integers and binary-encoded strings.