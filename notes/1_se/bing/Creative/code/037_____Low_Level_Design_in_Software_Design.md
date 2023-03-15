### Low Level Design in Software Design

Low level design (LLD) is a detailed and specific description of how a software system will be implemented. It includes the following components:

- Class diagrams: These show the classes, attributes, methods, and relationships of the software system.
- Sequence diagrams: These show the interactions and messages between the classes and objects of the software system.
- Data flow diagrams: These show the flow of data and information between the components of the software system.
- State diagrams: These show the states and transitions of the objects of the software system.
- Pseudocode or algorithms: These show the logic and steps of the methods and functions of the software system.

An example of low level design for a calculator software system is given below:

```markdown
Class Diagram:

+-----------------+
|   Calculator    |
+-----------------+
| - result: int   |
+-----------------+
| + add(x: int, y: int): int    |
| + subtract(x: int, y: int): int |
| + multiply(x: int, y: int): int |
| + divide(x: int, y: int): int   |
| + getResult(): int              |
+-----------------+

Sequence Diagram:

User -> Calculator: add(5, 10)
Calculator -> Calculator: result = 5 + 10
Calculator -> User: return result
User -> Calculator: subtract(15, 5)
Calculator -> Calculator: result = 15 - 5
Calculator -> User: return result
User -> Calculator: multiply(3, 4)
Calculator -> Calculator: result = 3 * 4
Calculator -> User: return result
User -> Calculator: divide(12, 4)
Calculator -> Calculator: result = 12 / 4
Calculator -> User: return result
User -> Calculator: getResult()
Calculator -> User: return result

Data Flow Diagram:

+------+     +------------+     +------+
| User | --> | Calculator | --> | User |
+------+     +------------+     +------+
              | result    |
              +------------+

State Diagram:

+---------+     add      +---------+
| Initial | ----------> | Result  |
+---------+             +---------+
                         | result  |
                         +---------+
                         ^    |    ^
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    v    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    v    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    v    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    v    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    v    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    v    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    |    |
                         |    v    |
                         |    |    |
                         |    |    |
                         |