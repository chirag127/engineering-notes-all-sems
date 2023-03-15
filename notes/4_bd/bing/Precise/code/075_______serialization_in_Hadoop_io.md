##### Serialization in Hadoop IO

Serialization is the process of converting data structures or objects into a binary or textual format that can be stored or transmitted and later deserialized back into its original form. In Hadoop, serialization is used to transfer data between nodes and to write data to disk.

Here is an example of how to implement a custom `Writable` class in Hadoop for serialization:

```java
import org.apache.hadoop.io.Writable;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

public class MyWritable implements Writable {
    private int myInt;
    private String myString;

    public MyWritable() {}

    public MyWritable(int myInt, String myString) {
        this.myInt = myInt;
        this.myString = myString;
    }

    @Override
    public void write(DataOutput out) throws IOException {
        out.writeInt(myInt);
        out.writeUTF(myString);
    }

    @Override
    public void readFields(DataInput in) throws IOException {
        myInt = in.readInt();
        myString = in.readUTF();
    }
}
```

This class implements the `Writable` interface and overrides the `write` and `readFields` methods to define how the data should be serialized and deserialized. The `write` method writes the data to the `DataOutput` stream, and the `readFields` method reads the data from the `DataInput` stream.
