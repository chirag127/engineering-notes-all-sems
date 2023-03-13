Decision table testing is a software testing technique used to test system behavior for different input combinations. It is a tabular representation of input conditions and resulting actions, showing the causes and effects of different scenarios. It is useful for testing complex business logic that involves multiple inputs and outputs.

A decision table consists of four quadrants: condition stubs, condition entries, action stubs, and action entries. Condition stubs are the input conditions that affect the system behavior, such as user inputs, system states, or environmental factors. Condition entries are the possible values or ranges of values for each condition stub, such as true or false, yes or no, or numeric values. Action stubs are the expected system behavior or output for each combination of condition entries, such as displaying a message, performing a calculation, or updating a database. Action entries are the indicators of whether an action stub is executed or not for each combination of condition entries, such as X or blank, or 1 or 0.

A decision table can be represented in ASCII format using the following symbols:

- | for vertical lines
- - for horizontal lines
- + for line intersections
- X for action entries that are executed
- blank for action entries that are not executed
- T for true condition entries
- F for false condition entries
- Y for yes condition entries
- N for no condition entries
- other symbols for other condition entries

An example of a decision table for testing the login functionality of a software application is given below:

| Condition Stubs | Condition Entries | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|-----------------|-------------------|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| Username        | Valid             | T | T | T | T | F | F | F | F |   |   |   |   |   |   |   |   |
| Password        | Valid             | T | T | F | F | T | T | F | F |   |   |   |   |   |   |   |   |
| Captcha         | Valid             | T | F | T | F | T | F | T | F |   |   |   |   |   |   |   |   |
|-----------------|-------------------|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| Action Stubs    | Action Entries    | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| Login success   |                   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Login failure   |                   |   | X | X | X | X | X | X | X |   |   |   |   |   |   |   |   |
| Captcha refresh |                   |   | X | X | X | X | X | X | X |   |   |   |   |   |   |   |   |
| Error message   |                   |   |   |   |   | X | X | X | X |   |   |   |   |   |   |   |   |
|-----------------|-------------------|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

The above decision table can be interpreted as follows:

- If the username, password, and captcha are all valid, then the login is successful and no other actions are performed.
- If any of the username, password, or captcha is invalid, then the login fails, the captcha is refreshed, and an error message is displayed.