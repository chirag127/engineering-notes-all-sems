Unit tests with MR unit are a way of testing Hadoop MapReduce jobs in isolation, without running them on a cluster. MR unit is a Java library that extends JUnit and allows you to create test cases for mappers, reducers, and map-reduce chains. A typical unit test with MR unit involves creating a driver object, setting up the input and expected output, and running the test. Here is a possible diagram of a unit test with MR unit:

#### Unit tests with MR unit

```
+-----------------+     +-----------------+     +-----------------+
| Test input      |     | Mapper          |     | Expected output |
| (key-value pair)| --> | (key-value pair)| --> | (key-value pair)|
+-----------------+     +-----------------+     +-----------------+
          |                     |                         |
          |                     |                         |
          |                     |                         |
          |                     |                         |
          |                     |                         |
          |                     |                         |
          |                     |                         |
          |                     |                         |
          |                     |                         |
          |                     |                         |
          |                     |                         |
          |                     |                         |
          v                     v                         v
+-----------------+     +-----------------+     +-----------------+
| MapDriver       |     | Test case       |     | Assert          |
| (driver object) | --> | (JUnit method)  | --> | (JUnit method)  |
+-----------------+     +-----------------+     +-----------------+
```