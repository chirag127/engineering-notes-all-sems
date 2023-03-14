### Visibility for the notes of the Unit 7 - Use case 2 in the subject of Block chain Architecture Design

- Use case diagrams are a type of UML diagram that describe the functionality of a system from the perspective of the users and their goals.
- Use case diagrams can help to design processes and systems that are user-driven, simple, and trackable.
- Use case diagrams consist of the following elements:
  - Actors: the users or external systems that interact with the system. They are represented by stick figures or rectangles with the keyword <<actor>>.
  - Use cases: the actions or goals that the actors can perform with the system. They are represented by ovals with verb phrases.
  - Subject: the system boundary or the system under consideration that owns and performs the use cases. It is represented by a rectangle that encloses the use cases and has a noun phrase as the name.
  - Associations: the relationships between actors and use cases. They are represented by solid lines with optional multiplicity indicators.
  - Generalizations: the relationships between actors or use cases that indicate inheritance or specialization. They are represented by solid lines with hollow arrowheads pointing to the supertype or the generalized element.
  - Include: the relationships between use cases that indicate that one use case is always performed as part of another use case. They are represented by dashed lines with the keyword <<include>> and an arrowhead pointing to the included use case.
  - Extend: the relationships between use cases that indicate that one use case can optionally extend the behavior of another use case under certain conditions. They are represented by dashed lines with the keyword <<extend>> and an arrowhead pointing to the extended use case.
- Use case diagrams can also have use case specifications that provide more details about each use case, such as the name, scope, primary and secondary actors, stakeholders, preconditions, postconditions, trigger, main success scenario, and extensions.
- Use case diagrams can be used to model different scenarios or levels of abstraction for a system, such as the business, system, or subsystem level.
- Use case diagrams can be used to model different types of systems, such as web applications, software, or block chain architectures .
- A block chain architecture is a distributed ledger system that uses cryptography, consensus algorithms, and smart contracts to store and verify transactions without a central authority.
- A use case diagram for a block chain architecture can show the different actors and use cases involved in the block chain system, such as the nodes, miners, validators, clients, transactions, blocks, smart contracts, etc.
- Here is an example of a use case diagram for a block chain architecture that shows the basic functions of a block chain system:

```
+-----------------------------+
|       Block Chain System    |
|                             |
|  +-----------------------+  |
|  |     Create Block      |  |
|  +-----------------------+  |
|  +-----------------------+  |
|  |     Validate Block    |  |
|  +-----------------------+  |
|  +-----------------------+  |
|  |     Append Block      |  |
|  +-----------------------+  |
|  +-----------------------+  |
|  |     Execute Smart     |  |
|  |      Contract         |  |
|  +-----------------------+  |
|  +-----------------------+  |
|  |     Query Ledger      |  |
|  +-----------------------+  |
+-----------------------------+
    |             |     |     |
    |             |     |     |
    |             |     |     |
    |             |     |     |
    |             |     |     |
    |             |     |     |
    |             |     |     |
    |             |     |     |
    |             |     |     |
    |             |     |     |
    |             |     |     |
    |             |     |     |
    |             |     |     |
+---+---+     +---+---+ | +---+---+
| Node  |     | Node  | | | Node  |
+---+---+     +---+---+ | +---+---+
    |             |     |     |
    |             |     |     |
    |             |     |     |
    |             |     |     |
    |             |     |     |
    |             |     |     |
+---+---+     +