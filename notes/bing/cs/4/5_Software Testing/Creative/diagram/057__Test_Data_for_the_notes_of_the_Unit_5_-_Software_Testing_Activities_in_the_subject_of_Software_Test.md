According to , test data in software testing is the input given to a software program during test execution. It represents data that affects or affected by software execution while testing. Test data is used for both positive testing to verify that functions produce expected results for given inputs and for negative testing to test software ability to handle unusual, exceptional or unexpected inputs.

A possible diagram for test data for the notes of the unit 5 - software testing activities in the subject of software testing is:

```
+----------------------+     +----------------------+     +----------------------+
|                      |     |                      |     |                      |
|   Test Data Source   |     |   Test Data Format   |     |   Test Data Usage    |
|                      |     |                      |     |                      |
+----------------------+     +----------------------+     +----------------------+
|                      |     |                      |     |                      |
| - Production cloning |     | - CSV                |     | - Positive testing   |
| - Data generation    |     | - XML                |     | - Negative testing   |
| - Data extraction    |     | - JSON               |     | - Boundary testing   |
| - Data masking       |     | - SQL                |     | - Equivalence testing|
|                      |     |                      |     |                      |
+----------------------+     +----------------------+     +----------------------+
```

The diagram shows the different aspects of test data, such as the source, format and usage. The source is where the test data comes from, such as copying from production servers, generating new data, extracting data from existing sources or masking sensitive data. The format is how the test data is structured, such as comma-separated values, extensible markup language, JavaScript object notation or structured query language. The usage is how the test data is applied, such as positive testing to verify expected results, negative testing to check error handling, boundary testing to test the limits of the input range or equivalence testing to test different classes of input values.