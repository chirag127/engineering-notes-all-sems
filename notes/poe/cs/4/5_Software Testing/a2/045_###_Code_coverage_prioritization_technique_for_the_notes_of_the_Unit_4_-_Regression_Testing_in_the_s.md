 Here is the content in markdown format for the topic -

### Code coverage prioritization technique for the notes of the Unit 4 - Regression Testing in the subject of Software Testing

Code coverage prioritization technique is a technique used in Regression Testing to prioritize the test cases. In this technique, the test cases are prioritized in the descending order of the code coverage they achieve. The test cases covering more code are given higher priority and the test cases covering less code are given lower priority.

Some key points about Code coverage prioritization technique -

- It focuses on maximizing the code coverage in limited time and resources.
- The test cases providing maximum code coverage have higher chances of detecting maximum number of bugs. So, they are executed first.
- The test cases with less code coverage are executed later if time and resources permit.
- It is easier to implement as code coverage data can be easily obtained using code coverage tools.
- The demerits of this technique are -
    - It does not consider the severity and criticality of bugs. A test case with less coverage may detect a critical bug.
    - The coverage metric may not always relate to fault detection capability. Some statements/branches may not be related to the functionality. Their coverage may not mean much.

**Examples** -

Suppose there are 6 test cases TC1, TC2, ...., TC6 with code coverage as follows -

TC1 - 50%
TC2 - 60%
TC3 - 40%
TC4 - 70%
TC5 - 30%
TC6 - 80%

Then, the prioritized order of test cases will be -

TC6 -> TC4 -> TC2 -> TC1 -> TC5 -> TC3

This technique focuses on maximizing cumulative code coverage in the prioritized test suite.

**Applications** - When time and resources are limited for Regression Testing and it is desired to maximize code coverage. The criticality/severity of bugs is not a primary consideration. The code coverage data is easily available which makes this technique easier to implement.