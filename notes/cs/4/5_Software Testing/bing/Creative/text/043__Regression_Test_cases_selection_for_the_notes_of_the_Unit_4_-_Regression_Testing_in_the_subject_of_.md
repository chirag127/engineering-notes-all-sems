### Regression Test cases selection

- Regression testing is the process of retesting the modified parts of a software system and ensuring that no new errors have been introduced by the changes.
- Regression test cases are the test cases that are executed during regression testing to verify the functionality and performance of the software system after the modifications.
- Regression test cases selection is the process of choosing a subset of test cases from the existing test suite that are relevant and effective for regression testing.
- Regression test cases selection can be done based on various criteria, such as:
  - The coverage of the modified code or functionality by the test cases.
  - The severity or priority of the test cases.
  - The historical data of the test cases, such as their failure rate, execution time, or defect detection rate.
  - The dependencies or relationships among the test cases, such as their order of execution, data flow, or control flow.
  - The feedback or recommendations from the developers, testers, or stakeholders.
- Regression test cases selection can be done manually or automatically, using various techniques, such as:
  - Retest all: This technique involves executing all the test cases in the existing test suite, regardless of their relevance or effectiveness for regression testing. This technique ensures complete coverage and reliability, but it is also time-consuming, costly, and redundant.
  - Retest modified: This technique involves executing only the test cases that cover the modified code or functionality. This technique reduces the testing effort and cost, but it may miss some defects that are caused by the interactions or side effects of the modifications.
  - Retest risky: This technique involves executing only the test cases that have a high risk of failure or defect detection. This technique focuses on the critical and important aspects of the software system, but it may neglect some less risky or less important aspects.
  - Retest optimal: This technique involves executing a subset of test cases that maximizes the coverage and effectiveness of regression testing, while minimizing the testing effort and cost. This technique requires sophisticated algorithms and tools to select the optimal subset of test cases, based on various criteria and constraints.