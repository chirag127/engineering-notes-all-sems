 Here is the content in markdown format on the topic of ### constants for the notes of the Unit 4 - C++ Basics in the subject of Object Oriented System Design:

### Constants

- Constants refer to fixed values that do not change during the execution of a program.
- They are also known as literals.
- Constants can be of any of the basic data types like int, float, double, char, etc.
- Declaring constants:
	- `const int MAX = 100;`
	- `const float PI = 3.14;`
	- `const char NEWLINE = '\n';`
- The values of constants cannot be changed after they are defined. Trying to do so will result in a compilation error.
- Constants are usually defined with uppercase names to differentiate them from variables.
- Uses of constants:
	- To represent fixed values that are repeatedly used in a program like mathematical constants.
	- To enhance readability of the code by using descriptive names for fixed values.
	- To make the code more robust by avoiding hard-coded values which may need to be changed later. The change will be needed at only one place if constants are used.

**Advantages:**
- Readability
- Maintainability
- Robustness

**Disadvantages:**
- None

**Examples:**
`const int MAX_SIZE = 100;`
`const float PI = 3.14;`
`const char NEWLINE = '\n';`

**Applications:**
- Mathematical calculations
- Array size definitions
- String endings
- And more...