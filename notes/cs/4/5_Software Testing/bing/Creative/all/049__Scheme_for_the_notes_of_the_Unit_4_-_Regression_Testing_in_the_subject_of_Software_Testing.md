### Scheme for the notes of the Unit 4 - Regression Testing in the subject of Software Testing

- Regression testing is a software testing practice that ensures an application still functions as expected after any code changes, updates, or improvements.
- Regression testing is responsible for the overall stability and functionality of the existing features.
- Regression testing is applied to guarantee that after each update, the system stays sustainable under continuous improvements.
- Regression testing is the final step, as it verifies the product behaviors as a whole.
- Regression testing is needed whenever the code is changed, and you need to determine whether the modified code will affect other parts of the software application.
- Regression testing is also needed when a new feature is added to the software application or when a functional or performance defect/issue is fixed.
- Regression testing can be carried out using the following techniques:
  - Retest All: This is a method in which all the tests in the existing test suite are re-executed. This is very expensive as it requires huge time and resources.
  - Regression Test Selection: This is a technique in which some selected test cases from test suite are executed to test whether the modified code affects the software application or not. Test cases are categorized into two parts, reusable test cases which can be used in further regression cycles and obsolete test cases which can not be used in succeeding cycles.
  - Prioritization of Test Cases: This is a technique in which test cases are prioritized depending on business impact, critical & frequently used functionalities. Selection of test cases based on priority will greatly reduce the regression test suite.
- Regression testing can be automated using various tools, such as Katalon, Selenium, TestComplete, etc. Automation can save time and resources, as well as increase test coverage and accuracy.
- Regression testing is an integral part of the extreme programming software development method. In this method, design documents are replaced by extensive, repeatable, and automated testing of the entire software package throughout each stage of the software development process.
- A mnemonic to remember the steps of regression testing is: **DPPR**
  - **D**etect changes in the source code
  - **P**rioritize those changes and product requirements
  - **P**erform regression testing using the selected technique and tool
  - **R**eport and analyze the test results