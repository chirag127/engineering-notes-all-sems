## Unit 4 - Regression Testing

- Regression testing is the process of retesting a software system after changes have been made to ensure that the changes have not introduced new defects or adversely affected the existing functionality.
- Regression testing can be performed at different levels of testing, such as unit, integration, system, or acceptance testing.
- Regression testing can be done manually or automatically, depending on the availability of test cases, test tools, and resources.
- Regression testing can be classified into three types: retest all, selective, and test suite minimization.
  - Retest all is the simplest approach, where all the existing test cases are executed again after any change. This ensures complete coverage, but it is also time-consuming and costly.
  - Selective is the most common approach, where only a subset of test cases are executed based on some criteria, such as the impact of the change, the risk of the functionality, or the history of defects. This reduces the testing effort, but it also requires a good selection strategy and traceability between test cases and requirements.
  - Test suite minimization is the most advanced approach, where the test suite is reduced to the smallest possible size while maintaining the same coverage and effectiveness. This requires sophisticated techniques, such as slicing, dependency analysis, or prioritization, and it can significantly improve the efficiency and quality of regression testing.