Code coverage prioritization technique is a method of ordering test cases based on their code coverage, which is the measure of how much of the source code is executed by the test cases. There are different types of code coverage, such as statement coverage, branch coverage, function coverage, and condition coverage. Each type of coverage has a different criterion for determining how much of the code is covered by the test cases. For example, statement coverage counts how many statements in the program have been executed, while branch coverage counts how many branches of the control structures (such as if statements) have been executed.

The following diagram illustrates the basic idea of code coverage prioritization technique using a simple example. The diagram shows a program with four statements (S1, S2, S3, S4) and two test cases (T1, T2). The test cases have different code coverage values for each type of coverage. For example, T1 has 100% statement coverage, but only 50% branch coverage, while T2 has 75% statement coverage and 100% branch coverage. The diagram also shows how the test cases can be prioritized based on different types of coverage. For example, if statement coverage is used as the criterion, then T1 will be executed before T2, but if branch coverage is used, then T2 will be executed before T1.

```
+-----------------+-----------------+-----------------+-----------------+
|                 | Statement       | Branch          | Function        |
|                 | Coverage        | Coverage        | Coverage        |
+-----------------+-----------------+-----------------+-----------------+
| Test Case       | S1 S2 S3 S4     | S1 S2 S3 S4     | S1 S2 S3 S4     |
+-----------------+-----------------+-----------------+-----------------+
| T1              | X  X  X  X      | X  X  X         | X               |
+-----------------+-----------------+-----------------+-----------------+
| T2              | X  X     X      | X  X     X  X   | X               |
+-----------------+-----------------+-----------------+-----------------+
| Coverage (%)    | 100 100  50  50 | 50  50  50  50  | 100             |
+-----------------+-----------------+-----------------+-----------------+
| Prioritization  | T1 T2           | T2 T1           | T1 T2           |
+-----------------+-----------------+-----------------+-----------------+
```

The program is:

```javascript
function foo(x) { // S1
  if (x > 0) { // S2
    return x + 1; // S3
  } else {
    return x - 1; // S4
  }
}

// Test cases
T1 = foo(1); // returns 2
T2 = foo(-1); // returns -2
```