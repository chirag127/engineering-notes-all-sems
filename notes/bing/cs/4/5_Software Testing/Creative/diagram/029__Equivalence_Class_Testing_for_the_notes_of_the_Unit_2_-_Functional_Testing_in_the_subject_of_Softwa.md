Equivalence Class Testing is a technique of dividing the input data into classes that have similar behavior and characteristics. The idea is to test one value from each class and assume that the rest of the values will behave the same. This way, the number of test cases can be reduced without compromising the test coverage.

The following diagram illustrates the basic concept of Equivalence Class Testing:

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  Valid Class   |    |  Valid Class   |    | Invalid Class  |
|                |    |                |    |                |
|  Test one      |    |  Test one      |    |  Test one      |
|  value from    |    |  value from    |    |  value from    |
|  this class    |    |  this class    |    |  this class    |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
```

An example of Equivalence Class Testing for the notes of the Unit 2 - Functional Testing in the subject of Software Testing is:

Suppose we have a function that accepts a date as input and returns the next date as output. The input date should be in the format DD/MM/YYYY and the output date should be in the same format. The valid range of input dates is from 01/01/1900 to 31/12/2099.

The Equivalence Classes for this function are:

- Valid Class 1: Dates in the format DD/MM/YYYY where DD is between 01 and 31, MM is between 01 and 12, and YYYY is between 1900 and 2099.
- Valid Class 2: Dates in the format DD/MM/YYYY where DD is the last day of the month and MM is not 12.
- Valid Class 3: Dates in the format DD/MM/YYYY where DD is 31 and MM is 12.
- Invalid Class 1: Dates in the format DD/MM/YYYY where DD is not between 01 and 31, MM is not between 01 and 12, or YYYY is not between 1900 and 2099.
- Invalid Class 2: Dates in the format DD/MM/YYYY where DD is not a valid day for the given month and year (e.g. 29/02/1900, 31/04/2020, etc.).
- Invalid Class 3: Dates that are not in the format DD/MM/YYYY (e.g. 12-34-5678, ABCD/EFGH/IJKL, etc.).

The following diagram illustrates the Equivalence Classes for this function:

```
+----------------+    +----------------+    +----------------+    +----------------+
|                |    |                |    |                |    |                |
|  Valid Class 1 |    |  Valid Class 2 |    |  Valid Class 3 |    | Invalid Class 1|
|                |    |                |    |                |    |                |
|  Test one      |    |  Test one      |    |  Test one      |    |  Test one      |
|  value from    |    |  value from    |    |  value from    |    |  value from    |
|  this class    |    |  this class    |    |  this class    |    |  this class    |
|                |    |                |    |                |    |                |
|  Example:      |    |  Example:      |    |  Example:      |    |  Example:      |
|  15/06/2021    |    |  30/09/2021    |    |  31/12/2021    |    |  45/13/2021    |
|                |    |                |    |                |    |                |
+----------------+    +----------------+    +----------------+    +----------------+

+----------------+    +----------------+
|                |    |                |
| Invalid Class 2|    | Invalid Class 3|
|                |    |                |
|  Test one      |    |  Test one      |
|  value from    |    |  value from    |
|  this class    |    |  this class    |
|                |    |                |
|  Example:      |    |  Example:      |
|  29/02/1900    |    |  12-34-567