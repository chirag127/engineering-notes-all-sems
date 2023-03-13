## Unit 5 - Software Testing Activities

Software testing activities are the tasks or steps that are performed during the software testing life cycle. These activities include checking the developed software to see if it meets specific requirements, identifying and reporting defects, and ensuring the quality of the product. Software testing activities can be divided into six major phases:

- Requirement Analysis: In this phase, the testers analyze the requirements of the software and identify the scope, objectives, and risks of testing. They also define the test criteria, such as test coverage, test data, and test environment.
- Test Planning: In this phase, the testers plan the test strategy, test schedule, test resources, and test tools. They also define the test levels, test types, and test techniques to be used. They also prepare the test plan document that describes the overall approach and scope of testing.
- Test Case Development: In this phase, the testers design and write the test cases based on the test criteria and test techniques. They also create the test data and test scripts to execute the test cases. They also review and verify the test cases for completeness and accuracy.
- Test Environment Setup: In this phase, the testers set up and configure the test environment, such as hardware, software, network, and database, to execute the test cases. They also verify that the test environment is ready and meets the test requirements.
- Test Execution: In this phase, the testers execute the test cases and test scripts in the test environment. They also monitor and record the test results, such as pass, fail, or error. They also log and report the defects found during testing to the development team.
- Test Cycle Closure: In this phase, the testers evaluate the test results and the test process. They also measure the test metrics, such as defect density, test coverage, and test effectiveness. They also prepare the test summary report that summarizes the test activities, test outcomes, and test recommendations.

The following diagram illustrates the software testing activities and their relationships using the Unified Modeling Language (UML) activity diagram notation. The diagram shows the flow of control among the different activities of the software testing life cycle. The diagram also shows the entry and exit criteria, activities, and deliverables for each phase of testing.

```
+-----------------+
| Entry Criteria  |
+-----------------+
| - Requirements  |
| - Test Plan     |
+-----------------+
        |
        V
+-----------------+
| Requirement     |
| Analysis        |
+-----------------+
| Activities:     |
| - Analyze       |
|   requirements  |
| - Define test   |
|   criteria      |
| - Identify      |
|   risks         |
| Deliverables:   |
| - Test          |
|   Requirements  |
| - Traceability  |
|   Matrix        |
+-----------------+
        |
        V
+-----------------+
| Test Planning   |
+-----------------+
| Activities:     |
| - Plan test     |
|   strategy      |
| - Define test   |
|   levels, types,|
|   and techniques|
| - Estimate test |
|   resources     |
| - Schedule test |
|   activities    |
| - Select test   |
|   tools         |
| Deliverables:   |
| - Test Plan     |
| - Test Strategy |
+-----------------+
        |
        V
+-----------------+
| Test Case       |
| Development     |
+-----------------+
| Activities:     |
| - Design test   |
|   cases         |
| - Write test    |
|   cases         |
| - Create test   |
|   data          |
| - Write test    |
|   scripts       |
| - Review test   |
|   cases         |
| Deliverables:   |
| - Test Cases    |
| - Test Data     |
| - Test Scripts  |
+-----------------+
        |
        V
+-----------------+
| Test Environment|
| Setup           |
+-----------------+
| Activities:     |
| - Setup test    |
|   hardware      |
| - Install test  |
|   software      |
| - Configure     |
|   test network  |
| - Verify test   |
|   environment   |
| Deliverables:   |
| - Test          |
|   Environment   |
+-----------------+
        |
        V
+-----------------+
| Test Execution  |
+-----------------+
| Activities:     |
| - Execute test  |
|   cases         |
| - Record test   |
|   results       |
| - Log defects   |
| - Report        |
|   defects       |
| Deliverables