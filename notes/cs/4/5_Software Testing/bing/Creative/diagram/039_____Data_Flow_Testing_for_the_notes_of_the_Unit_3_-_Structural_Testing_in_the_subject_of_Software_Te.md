### Data Flow Testing

- Data flow testing is a **white-box testing** technique that examines the data flow with respect to the variables used in the code .
- It examines the initialization of variables and checks their values at each instance .
- It is a type of **structural testing** that uses the **control flow graph** of the program to find the test paths.
- It has nothing to do with data flow diagrams.
- It focuses on data variables and their values, rather than the control flow of the program.
- It aims to test the **def-use pairs** of variables, where a variable is defined at one point and used at another point in the program.
- It can detect errors such as **missing initialization**, **uninitialized variables**, **dead code**, **unused variables**, etc .
- It can be applied at different levels of testing, such as unit testing, integration testing, and system testing.
- It can be performed using different strategies, such as **all-definitions**, **all-uses**, **all-du-paths**, **all-p-uses**, and **all-c-uses** .
- It can be combined with other testing techniques, such as **data driven testing**, which stores test data in table or spreadsheet form.