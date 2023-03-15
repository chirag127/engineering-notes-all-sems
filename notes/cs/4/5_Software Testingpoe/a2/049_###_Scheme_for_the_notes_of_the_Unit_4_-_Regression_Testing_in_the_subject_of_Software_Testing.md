 Here is the content in markdown format for the notes of Unit 4 - Regression Testing in Software Testing:

### Scheme for the notes of the Unit 4 - Regression Testing in the subject of Software Testing

1. Introduction to Regression Testing
- Regression Testing is a type of software testing to confirm that a recent program or code change has not adversely affected existing features.
- It checks if the existing functionality works as expected after a change in the software.
- It is done whenever the code is modified to fix a bug or to add new functionality.
- Mnemonic: Regression testing is necessary to Regress bugs and Re-check features.

2. Types of Regression Testing
- Complete Regression Testing: All the test cases are re-executed.
- Partial Regression Testing: Only some of the test cases are re-executed based on priority or risk assessment.
- Progressive Regression Testing: Test cases are re-executed in a progressive way, starting with basic functionality test cases.
- Local and Global Regression Testing: Testing a specific changed module (local) or testing the entire system (global).

3. Techniques for Regression Testing
- Retest all: Rerun all the test cases.
- Regression test suite: Identify and run tests that target changed areas.
- Test case prioritization: Rerun test cases in priorities based on risk.
- Test case minimization: Reduce the test suite by removing redundant test cases.
- Test case selection: Choose a subset of test cases based on criteria.
- Impact analysis: Analyze the dependencies of the changes to identify impacted test cases.

4. Regression Testing Challenges
- Test suite maintenance: As code changes, impacted test cases should be identified and updated.
- Resource constraints: May not be feasible to rerun the entire test suite in every iteration.
- Determining what to test: Challenging to determine coverage and select right test cases to rerun.
- Test flakiness: Tests that sometimes pass and sometimes fail hinder regression testing.
- Alternate approaches: Data mining based techniques can be used to identify failures without rerunning test cases.

[Include diagrams and examples if required]