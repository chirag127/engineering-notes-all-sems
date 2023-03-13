### Data Flow Testing for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

- Data Flow Testing is a type of structural testing that focuses on the data variables and their values in a program .
- It is a method that is used to find the test paths of a program according to the locations of definitions and uses of variables in the program .
- It has nothing to do with data flow diagrams .
- It is concerned with:
  - Statements where variables receive values (definitions)
  - Statements where variables are used (uses)
  - Paths from definitions to uses (du-paths)
- It makes use of the control flow graph to identify the test paths.
- It aims to cover all the possible du-paths for each variable in the program.
- It can reveal errors such as:
  - Variables used before being defined (uninitialized variables)
  - Variables defined but never used (dead code)
  - Variables defined multiple times before being used (redundant definitions)
- It can be classified into four strategies:
  - All-Defs: Every definition of every variable is executed at least once
  - All-Uses: Every use of every variable is executed at least once
  - All-c-Uses: Every computational use of every variable is executed at least once
  - All-p-Uses: Every predicate use of every variable is executed at least once
- A computational use of a variable is when the variable is used in a calculation or an assignment.
- A predicate use of a variable is when the variable is used in a conditional statement or a loop.
- An example of data flow testing is shown below:

```c
// A simple program to calculate the average of two numbers
#include <stdio.h>
int main()
{
  int a, b, sum, avg; // Line 1: Definition of variables
  printf("Enter two numbers: "); // Line 2: Use of variable printf
  scanf("%d %d", &a, &b); // Line 3: Definition of variables a and b
  sum = a + b; // Line 4: Definition of variable sum, use of variables a and b
  avg = sum / 2; // Line 5: Definition of variable avg, use of variable sum
  printf("The average is %d\n", avg); // Line 6: Use of variables printf and avg
  return 0; // Line 7: Use of variable return
}
```

- The control flow graph of the program is shown below:

```
  1
  |
  2
  |
  3
  |
  4
  |
  5
  |
  6
  |
  7
```

- The du-paths for each variable are shown below:

| Variable | Definition | Use | du-path |
|----------|------------|-----|---------|
| a        | Line 3     | Line 4 | 3-4     |
| b        | Line 3     | Line 4 | 3-4     |
| sum      | Line 4     | Line 5 | 4-5     |
| avg      | Line 5     | Line 6 | 5-6     |
| printf   | N/A        | Line 2, Line 6 | N/A   |
| scanf    | N/A        | Line 3 | N/A     |
| return   | N/A        | Line 7 | N/A     |

- The test cases for each strategy are shown below:

| Strategy | Test Case | Test Path | Coverage |
|----------|-----------|-----------|----------|
| All-Defs | (10, 20)  | 1-2-3-4-5-6-7 | 100%     |
| All-Uses | (10, 20)  | 1-2-3-4-5-6-7 | 100%     |
| All-c-Uses | (10, 20) | 1-2-3-4-5-6-7 | 100%     |
| All-p-Uses | N/A      | N/A       | N/A      |

- A possible mnemonic to remember the four strategies is **AD UP** (All-Defs, All-Uses, All