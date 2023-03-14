### Prioritization guidelines for the notes of the Unit 4 - Regression Testing in the subject of Software Testing

- Regression testing is the process of testing parts of an already tested application after it undergoes any changes like a new software addition, a feature update, a code change, a defect fix etc. to ensure that no existing functionality is impacted due to the latest changes.
- Regression testing is required for the unification of software and is especially important now with so many companies adopting continuous delivery.
- Regression testing can be time-consuming, costly and tedious if done manually for large and complex applications. Therefore, automation and prioritization of regression test cases are essential to increase the efficiency and effectiveness of regression testing activities .
- Prioritization of regression test cases is the process of ordering a regression test suite to execute higher priority test cases before lower priority ones based on some criterion.
- Prioritization of regression test cases can help in detecting and correcting errors as early as possible, saving time and resources, reducing the test execution phase cost, managing the risks associated with software delivery, and improving the quality of the product.
- There are different methods and techniques for prioritizing regression test cases, such as risk-based testing, code coverage analysis, fault severity analysis, test case execution history, test case complexity, test case dependency, etc.
- Some of the best practices in identifying and prioritizing test cases for regression testing are:

  - Select test cases with frequent defects: Based on the previous regression test cycle experience and learnings, select test cases that resulted in generating frequent defects.
  - Choose test cases with critical functionalities: Identify and prioritize test cases that cover the core and essential features of the application that have a high business impact and user value.
  - Select test cases with frequent code changes: Analyze the code changes and their impact on the application and select test cases that cover the areas that are most likely to be affected by the code changes.
  - Cover end-to-end test flows: Include test cases that cover the complete and integrated functionality of the application from the user's perspective and verify the expected outcomes.
  - Cover field validation test cases: Include test cases that check the input validation, error handling, and boundary conditions of the application fields and forms.
  - Select a risk-based testing approach: Assess the probability and impact of failure for each test case and prioritize them based on the risk level (high, medium, low).

- A possible mnemonic to remember the best practices for prioritizing regression test cases is **FCCFERS** (Frequent defects, Critical functionalities, Code changes, Field validations, End-to-end flows, Risk-based testing, and Selective testing).