Equivalence Class Testing is a software testing technique that divides the input data of a software unit into partitions of equivalent data from which test cases can be derived. This technique tries to define test cases that uncover classes of errors, thereby reducing the total number of test cases that must be developed.

The following diagram illustrates the basic concept of Equivalence Class Testing:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Valid Class 1  |     |  Valid Class 2  |     |  Valid Class 3  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Invalid Class  |     |  Invalid Class  |     |  Invalid Class  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

Each valid class represents a set of input values that are expected to produce the same output or behavior from the software unit. Each invalid class represents a set of input values that are expected to produce an error or an invalid output from the software unit. The test cases are designed to cover each valid and invalid class at least once, thus ensuring that all possible scenarios are tested.

For the notes of the Unit 2 - Functional Testing in the subject of Software Testing, a possible example of Equivalence Class Testing is the Next Date Problem, which is stated as follows:

Given a day in the format of day-month-year, you need to find the next date for the given date. Perform Equivalence Class Testing for this. Conditions : D: 1<Day<31 M: 1<Month<12 Y: 1800 <Year <2048

The input classes for this problem are:

Day: 
- D1: day between 1 to 28 
- D2: 29 
- D3: 30 
- D4: 31 

Month: 
- M1: Month has 30 days 
- M2: Month has 31 days 
- M3: Month is February 

Year: 
- Y1: Year is a leap year 
- Y2: Year is a normal year 

The output classes for this problem are:

- Increment Day 
- Reset Day and Increment Month 
- Increment Year 
- Invalid Date 

The following diagram illustrates the Equivalence Class Testing for the Next Date Problem:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     D1-M1-Y1    |     |     D1-M2-Y1    |     |     D1-M3-Y1    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
| Increment Day   |     | Increment Day   |     | Increment Day   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+

+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     D2-M1-Y1    |     |     D2-M2-Y1    |     |     D2-M3-Y1    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                      |                      |
        |                      |                      |