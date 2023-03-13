### Test Cases for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing

- A test case is a specification of the inputs, execution conditions, testing procedure, and expected results that define a single test to be executed to achieve a particular software testing objective.
- Test cases are one of the most important aspects of software engineering, as they define the way in which the testing would be carried out. Test cases are carried out for a very simple reason, to check if the software actually works or not.
- The process of generating test cases helps to identify the problems that exist in the software requirements and design. For generating a test case, firstly the criterion to evaluate a set of test cases is specified and then the set of test cases satisfying that criterion is generated.
- Some of the advantages of writing test cases are:
  - They help to ensure the completeness and consistency of the testing process.
  - They help to reduce the ambiguity and confusion in the testing process.
  - They help to improve the communication and collaboration among the testing team and other stakeholders.
  - They help to document the testing process and provide evidence of the testing results.
  - They help to measure the quality and effectiveness of the testing process.
- Some of the types of test cases are:
  - Functional test cases: These test cases verify the functionality of the software or application according to the requirements and specifications.
  - Non-functional test cases: These test cases verify the non-functional aspects of the software or application, such as performance, usability, security, reliability, etc.
  - Structural test cases: These test cases verify the internal structure and design of the software or application, such as code coverage, data flow, control flow, etc.
  - Regression test cases: These test cases verify that the software or application does not have any new defects or errors after any changes or modifications are made.
  - Integration test cases: These test cases verify that the software or application works well with other components or systems that it interacts with.
  - User interface test cases: These test cases verify that the software or application has a user-friendly and intuitive interface that meets the user expectations and needs.
  - User acceptance test cases: These test cases verify that the software or application meets the user requirements and expectations and is ready for deployment or delivery.
- The format of a test case may vary depending on the testing methodology, tool, or standard used, but generally it consists of the following elements:
  - Test case ID: A unique identifier for the test case.
  - Test case name: A descriptive name for the test case.
  - Test case description: A brief summary of the test case objective and scope.
  - Test case preconditions: The conditions or assumptions that must be met before executing the test case.
  - Test case steps: The detailed steps or actions to be performed for executing the test case.
  - Test case inputs: The data or values to be used for the test case steps.
  - Test case expected results: The expected outcomes or outputs of the test case steps.
  - Test case actual results: The actual outcomes or outputs of the test case steps after execution.
  - Test case status: The result of the test case execution, such as pass, fail, skip, etc.
  - Test case comments: Any additional information or remarks about the test case.
- An example of a test case for a login functionality of a web application is:

| Test case ID | Test case name | Test case description | Test case preconditions | Test case steps | Test case inputs | Test case expected results | Test case actual results | Test case status | Test case comments |
|--------------|----------------|-----------------------|-------------------------|-----------------|------------------|-----------------------------|--------------------------|------------------|--------------------|
| TC-001       | Valid login    | Verify that the user can login with valid credentials | The user has a valid username and password | 1. Open the web browser and navigate to the web application URL <br> 2. Enter the username and password in the respective fields <br> 3. Click on the login button | Username: user1 <br> Password: pass1 | The user is logged in and redirected to the home page | The user is logged in and redirected to the home page | Pass | N/A |
| TC-002       | Invalid login  | Verify that the user cannot login with invalid credentials | The user has an invalid username or password | 1. Open the web browser and navigate to the web application