Test Drivers and Test Stubs are two types of test harnesses that are used in software testing to simulate the behavior of missing or incomplete modules. They help to test the functionality and integration of different modules in a system.

A Test Driver is a program that calls and passes test data to another module that is under test. It is used in bottom-up testing approach, when the lower-level modules are ready but the higher-level modules are not. A Test Driver acts as a temporary substitute for the higher-level modules and provides the necessary inputs and outputs for the lower-level modules.

A Test Stub is a program that receives and returns test data from another module that is under test. It is used in top-down testing approach, when the higher-level modules are ready but the lower-level modules are not. A Test Stub acts as a temporary substitute for the lower-level modules and provides the expected outputs and responses for the higher-level modules.

Here is an example of a Test Driver and a Test Stub in Java:

```java
// A Test Driver for the Calculator class
public class CalculatorDriver {

    public static void main(String[] args) {
        // Create a Calculator object
        Calculator calculator = new Calculator();

        // Call the add method and pass some test data
        int result = calculator.add(10, 20);

        // Print the result
        System.out.println("The result of adding 10 and 20 is " + result);
    }
}

// A Test Stub for the Database class
public class DatabaseStub {

    // A method that returns some test data for the query
    public ResultSet executeQuery(String query) {
        // Create a ResultSet object
        ResultSet resultSet = new ResultSet();

        // Populate the ResultSet with some test data
        resultSet.add("John", "Doe", 25);
        resultSet.add("Jane", "Doe", 23);
        resultSet.add("Jack", "Doe", 21);

        // Return the ResultSet
        return resultSet;
    }
}
```