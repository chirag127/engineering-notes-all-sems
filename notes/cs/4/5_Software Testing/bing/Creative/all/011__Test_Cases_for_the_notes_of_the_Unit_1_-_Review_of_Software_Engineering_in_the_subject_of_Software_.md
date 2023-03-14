### Test Cases for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing

A test case is a set of actions executed to verify a particular feature or functionality of a software application. A test case contains test steps, test data, precondition, postcondition developed for specific test scenario to verify any requirement. Test cases are one of the most important aspects of software engineering, as they define the way in which the testing would be carried out.

Some of the benefits of writing test cases are:

- They help to ensure the quality and reliability of the software.
- They help to detect defects and errors in the software early in the development cycle.
- They help to reduce the cost and time of testing by avoiding unnecessary or redundant tests.
- They help to document the expected behavior and results of the software.
- They help to improve the communication and collaboration among the stakeholders of the software project.

The format of a standard test case may vary depending on the test management tool or the organization's guidelines, but it typically includes the following elements :

- Test Case ID: A unique identifier for the test case.
- Test Case Description: A brief summary of the test case objective or scenario.
- Test Steps: A detailed sequence of actions to be performed on the software under test.
- Test Data: The input data or parameters to be used for the test steps.
- Expected Results: The expected outcome or output of the test steps.
- Actual Results: The actual outcome or output of the test steps after execution.
- Pass/Fail: The status of the test case based on the comparison of the expected and actual results.
- Comments: Any additional information or remarks about the test case.

An example of a test case for the login functionality of a website is given below:

| Test Case ID | Test Case Description | Test Steps | Test Data | Expected Results | Actual Results | Pass/Fail | Comments |
|--------------|-----------------------|------------|-----------|------------------|----------------|-----------|----------|
| TC01 | Check login with valid credentials | 1. Go to the website https://example.com <br> 2. Enter valid username and password <br> 3. Click on the login button | Username: user1 <br> Password: pass1 | The user should be logged in and redirected to the home page | As expected | Pass | N/A |
| TC02 | Check login with invalid credentials | 1. Go to the website https://example.com <br> 2. Enter invalid username and password <br> 3. Click on the login button | Username: user2 <br> Password: pass2 | The user should not be logged in and an error message should be displayed | As expected | Pass | N/A |
| TC03 | Check login with empty username | 1. Go to the website https://example.com <br> 2. Leave the username field blank <br> 3. Enter valid password <br> 4. Click on the login button | Username: blank <br> Password: pass1 | The user should not be logged in and a validation message should be displayed | As expected | Pass | N/A |
| TC04 | Check login with empty password | 1. Go to the website https://example.com <br> 2. Enter valid username <br> 3. Leave the password field blank <br> 4. Click on the login button | Username: user1 <br> Password: blank | The user should not be logged in and a validation message should be displayed | As expected | Pass | N/A |

Some of the best practices for writing good test cases are  :

- Use clear and concise language that is easy to understand and follow.
- Use descriptive and meaningful names for the test cases and test steps.
- Use positive and negative scenarios to cover all the possible outcomes and edge cases.
- Use preconditions and postconditions to specify the initial and final states of the software under test.
- Use test data that is realistic and relevant to the test scenario.
- Use expected results that are specific and verifiable.
- Use comments to explain any assumptions or dependencies of the test case.
- Use traceability matrix to link the test cases to the software requirements.
- Use test management tools to organize, execute, and report the test cases.
- Review and update the test cases regularly to ensure their validity and completeness.

Some of the popular test management tools are:

- TestRail
- Z