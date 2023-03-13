## Unit 4 - Regression Testing

- Regression testing is the process of retesting a software system after changes have been made to it, such as bug fixes, new features, or configuration updates.
- The purpose of regression testing is to ensure that the changes have not introduced any new defects or adversely affected the existing functionality of the system.
- Regression testing can be performed at different levels of testing, such as unit testing, integration testing, system testing, or acceptance testing.
- Regression testing can be done manually or automatically, depending on the availability of test cases, test tools, and resources.
- Regression testing can be classified into three types: retest all, selective, and test suite minimization.

### Retest All
- Retest all is the simplest and most comprehensive type of regression testing, where all the test cases in the test suite are executed after every change.
- Retest all ensures maximum test coverage and detects any regression defects in the system.
- However, retest all is also the most expensive and time-consuming type of regression testing, as it requires a lot of resources and effort to execute all the test cases repeatedly.
- Retest all is suitable for systems that have frequent and critical changes, or systems that have a small and stable test suite.

### Selective
- Selective regression testing is the type of regression testing where only a subset of test cases in the test suite are executed after every change.
- Selective regression testing reduces the cost and time of regression testing, as it avoids executing unnecessary or redundant test cases.
- However, selective regression testing also reduces the test coverage and increases the risk of missing some regression defects in the system.
- Selective regression testing requires a criterion or a strategy to select the relevant test cases from the test suite, such as:

  - Test case prioritization: ranking the test cases based on their importance, such as severity, frequency, or impact of defects.
  - Test case dependency: identifying the test cases that are affected by the changes, such as direct, indirect, or transitive dependencies.
  - Test case coverage: selecting the test cases that cover the most code or functionality of the system, such as statement, branch, or path coverage.

### Test Suite Minimization
- Test suite minimization is the type of regression testing where the test suite is reduced to the smallest possible size without compromising the test coverage or quality of the system.
- Test suite minimization aims to eliminate the redundant or obsolete test cases from the test suite, such as duplicate, subsumed, or outdated test cases.
- Test suite minimization improves the efficiency and effectiveness of regression testing, as it reduces the cost and time of executing the test suite, and increases the fault detection rate of the test cases.
- Test suite minimization requires a technique or a tool to minimize the test suite, such as:

  - Greedy algorithm: selecting the test cases that cover the most uncovered code or functionality of the system, until the desired coverage is achieved.
  - Genetic algorithm: applying the principles of natural selection and evolution to generate and optimize the test suite, based on a fitness function and a set of operators.
  - Clustering algorithm: grouping the test cases based on their similarity or dissimilarity, and selecting one representative test case from each cluster.