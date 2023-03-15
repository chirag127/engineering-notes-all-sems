##### Serialization in Hadoop IO

Serialization is the process of converting an object into a stream of bytes that can be stored or transmitted over a network. Deserialization is the reverse process of converting a stream of bytes back into an object.

Hadoop provides its own serialization framework, called Writable, that is optimized for performance and compactness. Writable is an interface that defines two methods: write(DataOutput out) and readFields(DataInput in). Any class that implements Writable can be serialized and deserialized by Hadoop.

An example of a Writable class is IntWritable, which represents an integer value. The code for IntWritable is:

```java
public class IntWritable implements WritableComparable<IntWritable> {

  private int value;

  public IntWritable() {}

  public IntWritable(int value) {
    set(value);
  }

  public void set(int value) {
    this.value = value;
  }

  public int get() {
    return value;
  }

  @Override
  public void write(DataOutput out) throws IOException {
    out.writeInt(value);
  }

  @Override
  public void readFields(DataInput in) throws IOException {
    value = in.readInt();
  }

  @Override
  public int compareTo(IntWritable o) {
    return Integer.compare(value, o.value);
  }

  @Override
  public boolean equals(Object o) {
    if (o instanceof IntWritable) {
      return value == ((IntWritable) o).value;
    }
    return false;
  }

  @Override
  public int hashCode() {
    return value;
  }

  @Override
  public String toString() {
    return Integer.toString(value);
  }
}
```

Hadoop also provides a generic serialization framework, called Serialization, that allows users to plug in their own serialization libraries, such as Avro, Thrift, or Protobuf. Serialization is an interface that defines two methods: getSerializer(Class<T> c) and getDeserializer(Class<T> c). These methods return instances of Serializer and Deserializer, respectively, which are responsible for serializing and deserializing objects of type T.

An example of a Serialization implementation is AvroSerialization, which uses Avro to serialize and deserialize objects. The code for AvroSerialization is:

```java
public class AvroSerialization<T> implements Serialization<T> {

  public static final String AVRO_SCHEMA_KEY = "avro.schema";

  @Override
  public boolean accept(Class<?> c) {
    return SpecificRecord.class.isAssignableFrom(c) ||
           GenericContainer.class.isAssignableFrom(c);
  }

  @Override
  public Serializer<T> getSerializer(Class<T> c) {
    return new AvroSerializer<T>();
  }

  @Override
  public Deserializer<T> getDeserializer(Class<T> c) {
    return new AvroDeserializer<T>(c);
  }

  private static class AvroSerializer<T> implements Serializer<T> {

    private DatumWriter<T> writer;
    private BinaryEncoder encoder;
    private OutputStream out;

    @Override
    public void open(OutputStream out) throws IOException {
      this.out = out;
      this.encoder = EncoderFactory.get().binaryEncoder(out, null);
    }

    @Override
    public void serialize(T t) throws IOException {
      if (writer == null) {
        writer = createDatumWriter(t);
      }
      writer.write(t, encoder);
    }

    @Override
    public void close() throws IOException {
      encoder.flush();
      out.close();
    }

    private DatumWriter<T> createDatumWriter(T t) {
      if (t instanceof SpecificRecord) {
        return new SpecificDatumWriter<T>((SpecificRecord) t);
      } else if (t instanceof GenericContainer) {
        return new GenericDatumWriter<T>(((GenericContainer) t).getSchema());
      } else {
        throw new RuntimeException("Unknown Avro type: " + t);
      }
    }
  }

  private static class AvroDeserializer<T> implements Deserializer<T> {

    private DatumReader<T> reader;
    private BinaryDecoder decoder;
    private InputStream in;
    private Class<T> type;

    public AvroDeserializer(Class<T> type) {
      this.type = type;
    }

    @Override
    public void open(InputStream in) throws IOException {
      this.in = in;
      this.decoder = DecoderFactory.get().binaryDecoder(in, null);
    }

    @Override
    public T deserialize(T t) throws IOException {
      if (reader == null) {
        reader = createDatumReader();
      }
      return reader.read(t, decoder);
    }

    @Override
    public void close() throws IOException {
      in.close();
    }

    private DatumReader<T> createDatumReader() {
      Schema schema = getSchema(type);
      if