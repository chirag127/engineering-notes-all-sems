#### Function Oriented Design in Software Design

Function Oriented Design is a method to software design where the model is decomposed into a set of interacting units or modules where each unit or module has a clearly defined function . Thus, the system is designed from a functional viewpoint.

One of the design notations used for Function Oriented Design is the Data Flow Diagram (DFD). A DFD maps out the flow of information for any process or system. It uses symbols to represent the entities, processes, data stores, and data flows in the system.

A DFD consists of four basic components:

- External entity: A source or destination of data, usually outside the system. It is represented by a rectangle with a name inside.
- Process: A function or a transformation of data, usually within the system. It is represented by a circle or a rounded rectangle with a name inside.
- Data store: A place where data is stored, usually within the system. It is represented by an open-ended rectangle with a name inside.
- Data flow: A movement of data from one place to another. It is represented by an arrow with a name or a label above.

Here is an example of a DFD for a student registration system:

```
+-----------------+             +-----------------+
|                 |             |                 |
| Student         |             | Registration    |
|                 |             |                 |
+-----------------+             +-----------------+
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |
       |                               |             +-----------------+
       |                               |             |                 |
       |                               +------------>| Course         |
       |                               |             |                 |
       |                               |             +-----------------+
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |             +-----------------+
       |                               |                    |             |                 |
       |                               |                    +------------>| Fee             |
       |                               |                    |             |                 |
       |                               |                    |             +-----------------+
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |             +-----------------+
       |                               |                    |             |                 |
       |                               |                    +------------>| Certificate     |
       |                               |                    |             |                 |
       |                               |                    |             +-----------------+
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |             +-----------------+
       |                               |                    |             |                 |
       |                               |                    +------------>| Report          |
       |                               |                    |             |                 |
       |                               |                    |             +-----------------+
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |                    |             +-----------------+
       |                               |                    |             |                 |
       |                               |                    +------------>| Transcript      |
       |                               |                    |             |                 |
       |                               |                    |             +-----------------+
       |                               |                    |
       |                               |                    |
       |                               |                    |
       |                               |

```
