#### User Defined Functions in Pig

- User defined functions (UDFs) are custom functions that can be written in Java, Python, Ruby, or Groovy and used in Pig scripts to perform specific tasks that are not supported by the built-in functions.
- UDFs can be used to manipulate data, perform complex calculations, call external services, or interact with other systems.
- UDFs can be classified into four types: eval, filter, load/store, and aggregate functions.
- Eval functions take one or more input values and return a single output value. For example, a UDF that converts temperature from Celsius to Fahrenheit is an eval function.
- Filter functions take a single input value and return a boolean value indicating whether the input satisfies a certain condition. For example, a UDF that checks if a string contains a specific word is a filter function.
- Load/store functions are used to read and write data from and to various sources and formats. For example, a UDF that reads data from a JSON file or writes data to a MongoDB collection is a load/store function.
- Aggregate functions take a bag of values and return a single output value that summarizes the input. For example, a UDF that calculates the average or the standard deviation of a bag of numbers is an aggregate function.
- To use a UDF in a Pig script, the UDF class must be registered using the REGISTER statement, and the UDF name must be aliased using the DEFINE statement. For example, to use a UDF called MyUDF that is defined in a Java class called com.example.MyUDF, the following statements are needed:

```
REGISTER com.example.MyUDF.jar;
DEFINE MyUDF com.example.MyUDF;
```

- Then, the UDF can be invoked using the alias name and the appropriate arguments. For example, to use the UDF MyUDF on a relation called A, the following statement can be used:

```
B = FOREACH A GENERATE MyUDF($0, $1);
```

- UDFs can also be written in scripting languages such as Python, Ruby, or Groovy using the Pig streaming feature. To use a UDF written in a scripting language, the script file must be registered using the REGISTER statement, and the UDF name must be aliased using the DEFINE statement with the STREAM keyword. For example, to use a UDF called my_udf that is defined in a Python script called my_udf.py, the following statements are needed:

```
REGISTER 'my_udf.py' USING streaming_python AS my_udf;
DEFINE my_udf STREAM my_udf;
```

- Then, the UDF can be invoked using the alias name and the appropriate arguments. For example, to use the UDF my_udf on a relation called A, the following statement can be used:

```
B = FOREACH A GENERATE FLATTEN(my_udf($0, $1));
```

- UDFs can be tested and debugged using the PigUnit framework, which allows writing unit tests for Pig scripts and UDFs using JUnit. PigUnit provides methods to create mock input data, run Pig scripts, and verify the output data. For example, to test a UDF called MyUDF that is defined in a Java class called com.example.MyUDF, the following code snippet can be used:

```
import org.apache.pig.pigunit.PigTest;
import org.apache.pig.tools.parameters.ParseException;
import org.junit.Test;

public class MyUDFTest {
  @Test
  public void testMyUDF() throws IOException, ParseException {
    String[] input = {
      "1\t10",
      "2\t20",
      "3\t30"
    };

    String[] output = {
      "(11)",
      "(22)",
      "(33)"
    };

    PigTest test = new PigTest("my_script.pig");

    test.assertOutput("data", input, "result", output);
  }
}
```

- The PigTest class takes the name of the Pig script file as an argument. The assertOutput method takes the name of the input and output relations, the input and output data arrays, and compares the actual output of the script with the expected output. If the output matches, the test passes; otherwise, the test fails.