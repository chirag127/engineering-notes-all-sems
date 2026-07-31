# Equivalence Class Testing

Equivalence class testing is a black box testing technique that divides the input domain of a system into classes of data that are expected to behave similarly. The main idea is to select one representative value from each class as a test case, instead of testing all possible values. This reduces the number of test cases and increases the test coverage.

## Advantages of Equivalence Class Testing

- It helps to identify the optimal number of test cases that cover all the possible scenarios.
- It avoids redundant and unnecessary test cases that do not add value to the testing process.
- It saves time and resources by focusing on the most relevant and critical test cases.

## Steps to Perform Equivalence Class Testing

- Analyze the system requirements and specifications to identify the input parameters and output results.
- Partition the input domain into valid and invalid equivalence classes based on the expected behavior and functionality of the system.
- Select one representative value from each equivalence class as a test case.
- Execute the test cases and verify the output results with the expected results.
- Report any defects or discrepancies found during the testing process.

## Example of Equivalence Class Testing

Consider a system that accepts a user name and a password as input and validates them against a database. The system requirements are as follows:

- The user name should be a valid email address.
- The password should be between 8 and 16 characters long and should contain at least one uppercase letter, one lowercase letter, one digit, and one special character.
- The system should display a message indicating whether the login is successful or not.

The input domain can be partitioned into the following equivalence classes:

- Valid user name and valid password (valid class)
- Valid user name and invalid password (invalid class)
- Invalid user name and valid password (invalid class)
- Invalid user name and invalid password (invalid class)

The test cases can be selected as follows:

- Test case 1: user name = sydney@bing.com, password = Sydney@123 (valid class)
- Test case 2: user name = sydney@bing.com, password = sydney (invalid class)
- Test case 3: user name = sydney, password = Sydney@123 (invalid class)
- Test case 4: user name = sydney, password = sydney (invalid class)

The expected results are as follows:

- Test case 1: The system should display a message "Login successful".
- Test case 2: The system should display a message "Invalid password".
- Test case 3: The system should display a message "Invalid user name".
- Test case 4: The system should display a message "Invalid user name and password".