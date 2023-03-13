### Test for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing

The following diagram illustrates the basic architecture of a software testing process, based on the information from the search results   . It shows the different types of testing, such as unit testing, integration testing, system testing, and acceptance testing, and how they are related to each other. The diagram also shows the roles of the developers, testers, and customers in the software testing process.

```
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
|   Unit Testing  |     | Integration     |     |  System Testing |     | Acceptance      |
|                 |     | Testing         |     |                 |     | Testing         |
|                 |     |                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
|   Developers    |     |   Developers    |     |   Testers       |     |   Customers     |
|                 |     |                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
|   Test each     |     |   Test the       |     |   Test the       |     |   Test the       |
|   component     |     |   interaction    |     |   functionality  |     |   usability      |
|   separately    |     |   of components  |     |   and reliability|     |   and suitability|
|                 |     |                 |     |   of the system  |     |   of the system  |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
|   Use test      |     |   Use test       |     |   Use test       |     |   Use test       |
|   automation    |     |   automation     |     |   automation     |     |   automation     |
|   tools         |     |   tools          |     |   tools          |     |   tools          |
|                 |     |                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
|   Find and fix  |     |   Find and fix   |     |   Find and report|     |   Find and report|
|   bugs in the   |     |   bugs in the    |     |   bugs in the    |     |   bugs in the    |
|   code          |     |   code           |     |   system         |     |   system         |
|                 |     |                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
|   Ensure the    |     |   Ensure the     |     |   Ensure the     |     |   Ensure the     |
|   quality of    |     |   quality of     |     |   quality of     |     |   quality of     |
|   each unit     |     |   the system     |     |   the system     |     |   the system     |
|                 |     |   design         |     |   performance    |     |   meets the      |
|                 |     |                 |     |                 |     |   customer       |
|                 |     |                 |     |                 |     |   requirements   |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
|   +----------+  |     |   +----------+  |     |   +----------+  |     |   +----------+  |
|   |          |  |     |   |          |  |     |   |          |  |     |   |          |  |
|   |  Input   |  |     |   |  Input   |