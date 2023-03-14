An oracle is a mechanism, different from the program itself, that can be used to check the correctness of the output of the program for the test cases. A test oracle can be a human, a specification, another program, or a combination of these. A test oracle can be used to compare the actual output of the system under test with the expected output for a given test case input.

The following diagram illustrates the basic architecture of a test oracle:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Test case     |---->|  System under  |---->|  Actual output |
|  input         |     |  test          |     |                |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        +---------------------+---------------------+
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              v
                     +----------------+
                     |                |
                     |  Test oracle  |
                     |                |
                     +----------------+
                           |     |
                           |     |
                           |     |
                           |     |
                           |     |
                           |     |
                           |     |
                           |     |
                           |     |
                           |     |
                           |     |
                           |     |
                           |     |
                           |     |
                           |     |
                           |     |
                           |     |
                           v     v
                  +----------------+     +----------------+
                  |                |     |                |
                  |  Expected      |<----|  Test result   |
                  |  output        |     |                |
                  |                |     |                |
                  +----------------+     +----------------+
```