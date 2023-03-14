##### Serialization in Hadoop io

- Serialization is the process of converting structured data into a byte stream for transmission over the network or storage on disk.
- Deserialization is the process of converting the byte stream back into the original structured data.
- Serialization is used in Hadoop for interprocess communication between nodes using remote procedure calls (RPCs) and for storing data in different file formats.
- Hadoop provides a mechanism for using different serialization frameworks by defining a list of Serialization classes in the property `io.serializations`.
- A Serialization class knows how to create Serializer and Deserializer instances for a given type of data.
- A Serializer is an interface that defines a method `serialize(T t, DataOutput out)` that writes an object of type T to a DataOutput stream.
- A Deserializer is an interface that defines a method `deserialize(DataInput in)` that reads an object of type T from a DataInput stream.
- Hadoop comes with two built-in Serialization implementations: WritableSerialization and JavaSerialization.
- WritableSerialization is the default serialization framework in Hadoop that uses the Writable interface to serialize and deserialize data.
- Writable is an interface that defines two methods: `write(DataOutput out)` and `readFields(DataInput in)` that are similar to the Serializer and Deserializer methods.
- Writable also defines a static method `readFields(DataInput in, Writable... writables)` that reads multiple Writable objects from a DataInput stream.
- Hadoop provides many classes that implement the Writable interface, such as IntWritable, Text, LongWritable, etc. Users can also create their own custom Writable classes by implementing the interface and overriding the methods.
- WritableSerialization is efficient and compact, but it does not support schema evolution (changing the fields of a data type) or cross-language interoperability (using data in different programming languages).
- JavaSerialization is an experimental serialization framework in Hadoop that uses the Java Serializable interface to serialize and deserialize data.
- Serializable is an interface that marks a class as eligible for serialization by the Java ObjectOutputStream and ObjectInputStream classes.
- JavaSerialization is easy to use and supports schema evolution, but it is slow and verbose, and it does not support cross-language interoperability.
- Hadoop also supports other serialization frameworks, such as Avro and Parquet, that offer more features and benefits than the built-in ones.
- Avro is a serialization framework that uses a schema to define the structure and type of the data, and a binary format to encode the data.
- Avro supports schema evolution, cross-language interoperability, and advanced compression techniques, such as Snappy.
- Parquet is a columnar storage format that uses Avro schemas to define the data, and a binary format to store the data in columns rather than rows.
- Parquet is optimized for analytical queries, as it allows skipping irrelevant columns and applying efficient compression and encoding schemes to each column.

Here is an example of how to use WritableSerialization in Hadoop:

```java
// A custom Writable class that represents a person
public class Person implements Writable {
  private String name;
  private int age;
  private boolean married;

  // A default constructor is required for deserialization
  public Person() {
  }

  // A constructor that sets the fields
  public Person(String name, int age, boolean married) {
    this.name = name;
    this.age = age;
    this.married = married;
  }

  // A getter method for the name field
  public String getName() {
    return name;
  }

  // A setter method for the name field
  public void setName(String name) {
    this.name = name;
  }

  // A getter method for the age field
  public int getAge() {
    return age;
  }

  // A setter method for the age field
  public void setAge(int age) {
    this.age = age;
  }

  // A getter method for the married field
  public boolean isMarried() {
    return married;
  }

  // A setter method for the married field
  public void setMarried(boolean married) {
    this.married = married;
  }

  // The write method that serializes the object to a DataOutput stream
  @Override
  public void write(DataOutput out) throws IOException {
    // Write the name as a Text object
    Text.writeString(out, name);
    // Write the age as an int
    out.writeInt(age);
    // Write the married as a boolean
    out.writeBoolean(married);
  }

  // The readFields method that deserializes