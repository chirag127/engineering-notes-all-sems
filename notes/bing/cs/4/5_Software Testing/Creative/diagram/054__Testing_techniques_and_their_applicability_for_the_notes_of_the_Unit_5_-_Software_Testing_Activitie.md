The following is a detailed ASCII diagram for testing techniques and their applicability for the notes of the Unit 5 - Software Testing Activities in the subject of Software Testing.

### Testing techniques and their applicability

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Unit Testing   |    | Integration     |    | Acceptance      |
|                 |    | Testing         |    | Testing         |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  - Tests        |    | - Tests         |    | - Tests         |
|  individual     |    | software        |    | the whole       |
|  methods and    |    | components or   |    | system as       |
|  functions of   |    | functions       |    | intended        |
|  the classes,   |    | together        |    |                 |
|  components,    |    |                 |    |                 |
|  or modules     |    |                 |    |                 |
|                 |    |                 |    |                 |
|  - Helps to     |    | - Helps to      |    | - Helps to      |
|  validate the   |    | verify the      |    | verify the      |
|  functionality  |    | functionality   |    | functionality   |
|  and logic of   |    | and logic of    |    | and logic of    |
|  each unit      |    | each component  |    | each system     |
|                 |    | or function     |    |                 |
|                 |    |                 |    |                 |
|  - Can be       |    | - Can be        |    | - Can be        |
|  automated and  |    | automated or    |    | automated or    |
|  run quickly by |    | manual          |    | manual          |
|  a continuous   |    |                 |    |                 |
|  integration    |    | - Requires      |    | - Requires      |
|  server         |    | interfaces and  |    | user            |
|                 |    | dependencies    |    | acceptance      |
|                 |    | between         |    | criteria and    |
|                 |    | components or   |    | test cases      |
|                 |    | functions       |    |                 |
|                 |    |                 |    |                 |
|  - Applicable   |    | - Applicable    |    | - Applicable    |
|  to any type of |    | to any type of  |    | to any type of  |
|  software       |    | software that   |    | software that   |
|                 |    | has multiple    |    | has a defined   |
|                 |    | components or   |    | set of          |
|                 |    | functions       |    | requirements    |
|                 |    | interacting     |    |                 |
|                 |    | with each       |    |                 |
|                 |    | other           |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The diagram is based on the information from the following sources   .