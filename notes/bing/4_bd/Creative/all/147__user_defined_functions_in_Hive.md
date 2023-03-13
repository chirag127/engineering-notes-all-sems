#### User defined functions in Hive

- User defined functions (UDFs) are custom functions that can be created and used in Hive queries to perform specific tasks that are not supported by the built-in functions.
- UDFs can be written in Java, Python, or any other scripting language that supports the Hive UDF interface.
- UDFs can be categorized into three types: scalar, generic, and table.
- Scalar UDFs take one or more input values and return a single output value. For example, a UDF that converts Fahrenheit to Celsius.
- Generic UDFs are similar to scalar UDFs, but they can handle complex data types such as arrays, maps, and structs. For example, a UDF that extracts the first element of an array.
- Table UDFs take one or more input values and return a table of values. For example, a UDF that splits a string into multiple rows based on a delimiter.
- To create a UDF in Java, the following steps are required:
  - Define a class that extends the UDF, GenericUDF, or GenericUDTF class, depending on the type of the UDF.
  - Implement the evaluate method that contains the logic of the UDF.
  - Compile the class into a JAR file and add it to the Hive classpath using the ADD JAR command.
  - Register the UDF using the CREATE FUNCTION command with the name and class of the UDF.
  - Use the UDF in the Hive queries with the registered name.
- To create a UDF in Python, the following steps are required:
  - Define a function that contains the logic of the UDF.
  - Save the function in a Python script file and add it to the Hive distributed cache using the ADD FILE command.
  - Register the UDF using the CREATE FUNCTION command with the name and the path of the Python script file.
  - Use the UDF in the Hive queries with the registered name.
- A mnemonic to remember the types of UDFs is: **S**calar, **G**eneric, and **T**able UDFs are **S**imple, **G**eneral, and **T**abular functions.
- An example of a scalar UDF in Java that converts Fahrenheit to Celsius is:

```java
import org.apache.hadoop.hive.ql.exec.UDF;
import org.apache.hadoop.io.DoubleWritable;

public class FahrenheitToCelsius extends UDF {
  public DoubleWritable evaluate(DoubleWritable fahrenheit) {
    if (fahrenheit == null) {
      return null;
    }
    double celsius = (fahrenheit.get() - 32) * 5.0 / 9.0;
    return new DoubleWritable(celsius);
  }
}
```

- An example of a generic UDF in Java that extracts the first element of an array is:

```java
import org.apache.hadoop.hive.ql.exec.UDFArgumentException;
import org.apache.hadoop.hive.ql.exec.UDFArgumentLengthException;
import org.apache.hadoop.hive.ql.metadata.HiveException;
import org.apache.hadoop.hive.ql.udf.generic.GenericUDF;
import org.apache.hadoop.hive.serde2.objectinspector.ListObjectInspector;
import org.apache.hadoop.hive.serde2.objectinspector.ObjectInspector;

public class FirstElement extends GenericUDF {
  private ListObjectInspector listOI;

  @Override
  public ObjectInspector initialize(ObjectInspector[] arguments) throws UDFArgumentException {
    if (arguments.length != 1) {
      throw new UDFArgumentLengthException("The function FIRST_ELEMENT takes exactly one argument.");
    }
    if (!(arguments[0] instanceof ListObjectInspector)) {
      throw new UDFArgumentException("The function FIRST_ELEMENT takes an array as input.");
    }
    listOI = (ListObjectInspector) arguments[0];
    return listOI.getListElementObjectInspector();
  }

  @Override
  public Object evaluate(DeferredObject[] arguments) throws HiveException {
    Object list = arguments[0].get();
    if (list == null) {
      return null;
    }
    int size = listOI.getListLength(list);
    if (size == 0) {
      return null;
    }
    return listOI.getListElement(list, 0);
  }

  @Override
  public String getDisplayString(String[] children) {
    return "first_element(" + children[0] + ")";
  }
}
```

- An example of a table UDF in Java that splits a string into multiple rows based on a delimiter is:

```java
import java.util.ArrayList;
import org.apache.hadoop.hive.ql.exec.UDFArgumentException;
import org.apache.hadoop.hive.ql.exec.UDFArgument