##### Serialization in Hadoop IO

Serialization is the process of converting an object into a stream of bytes that can be stored or transmitted over a network. Deserialization is the reverse process of converting a stream of bytes back into an object.

Hadoop provides its own serialization framework, called Writable, that is optimized for performance and compactness. Writable is an interface that defines two methods: `write(DataOutput out)` and `readFields(DataInput in)`. Any class that implements Writable can be serialized and deserialized by Hadoop.

Here is an example of a custom Writable class that represents a pair of integers:

```java
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;
import org.apache.hadoop.io.Writable;

public class IntPair implements Writable {
  private int first;
  private int second;

  public IntPair() {
    // default constructor
  }

  public IntPair(int first, int second) {
    this.first = first;
    this.second = second;
  }

  public int getFirst() {
    return first;
  }

  public int getSecond() {
    return second;
  }

  public void setFirst(int first) {
    this.first = first;
  }

  public void setSecond(int second) {
    this.second = second;
  }

  @Override
  public void write(DataOutput out) throws IOException {
    // write the fields in binary format
    out.writeInt(first);
    out.writeInt(second);
  }

  @Override
  public void readFields(DataInput in) throws IOException {
    // read the fields in binary format
    first = in.readInt();
    second = in.readInt();
  }
}
```