 Here is the content in markdown format for the topic ##### Avro and file based data structures in Hadoop io:

##### Avro and file based data structures in Hadoop io

Avro is a data serialization system that provides rich data structures and a compact binary data format with JSON-like schemas. Avro files are splittable, allowing MapReduce to process them efficiently.

Some key points about Avro data format:

- Schemas are defined using JSON. This allows easy integration with languages/systems that already use JSON.
- Supports complex data structures like records, arrays, enumerations, maps, unions, and fixed length binary data.
- Data is always accompanied by a schema that describes the data structure. This allows systems to dynamically understand the data without any additional information.
- Data is serialized in a compact binary format. This makes it efficient for storage and data transfer.
- Has support for dynamic schemas i.e. schemas can evolve over time and Avro data can be read by code generated for earlier schemas.

Some advantages of Avro:

- Schema evolution: Avro has support for backward and forward compatibility of schemas. This means old data can be read by new programs and new data can be read by old programs.
- Language independence: Avro data and schemas are language agnostic. Many languages have Avro libraries to serialize/deserialize data.
- Performance: Avro's binary format is compact and fast to serialize/deserialize.
- Dynamic typing: Avro schemas are defined with types but the actual data format is dynamic. This allows gradual schema migrations.

Some disadvantages of Avro:

- Heavyweight: Avro needs to maintain schemas with data and this adds some overhead.
- Code generation: Avro requires code generation from schemas to read/write data. This can be cumbersome for some use cases.
- JSON schemas: Although JSON is popular, it can be verbose for defining complex schemas.

Applications of Avro:

- Serialization in Hadoop for storing and processing data.
- Messaging in Apache Kafka. Kafka has first class support for Avro data format.
- Data transfer between heterogeneous systems/languages. The language independence and schema support makes this easy with Avro.

[Include diagrams/images/codes/tables if required to explain the concepts]

[Additional points/examples/applications can be added if required]