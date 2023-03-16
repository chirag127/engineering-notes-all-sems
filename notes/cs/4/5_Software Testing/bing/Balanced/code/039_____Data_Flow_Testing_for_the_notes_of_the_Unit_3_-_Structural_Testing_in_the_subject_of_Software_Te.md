### Data Flow Testing

- Data flow testing is a **white-box testing** technique that examines the data flow with respect to the variables used in the code .
- White-box testing is a software testing technique that examines the internal working of the software code being developed.
- Data flow testing is a type of **structural testing**. It is a method that is used to find the test paths of a program according to the locations of definitions and uses of variables in the program.
- Data flow testing has nothing to do with data flow diagrams.
- Data flow testing makes use of the **control flow graph**. A control flow graph is a graphical representation of the flow of execution of a program. It consists of nodes and edges, where nodes represent statements or blocks of code, and edges represent the possible paths of execution .
- Data flow testing focuses on data variables and their values. It examines the initialization of variables and checks their values at each instance .
- Data flow testing aims to detect errors such as **missing initialization**, **uninitialized variables**, **dead code**, **unused variables**, and **incorrect variable values** .
- Data flow testing can be performed at different levels of granularity, such as **statement level**, **block level**, or **procedure level**.
- Data flow testing can be applied to different types of software, such as **sequential programs**, **concurrent programs**, or **object-oriented programs**.
- Data flow testing can be performed using different strategies, such as **all-defs**, **all-uses**, **all-du-paths**, **all-p-uses**, **all-c-uses**, or **all-pot-uses**. These strategies differ in the criteria for selecting test paths based on the definitions and uses of variables in the program.
- Data flow testing is different from **data driven testing**, which is a software testing technique that stores test data in table or spreadsheet form and uses a single test script that can run tests for all test data from a table and anticipate the test output in the same table. Data driven testing does not examine the data flow within the code, but rather the input and output data of the code.