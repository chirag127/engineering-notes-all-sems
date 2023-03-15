# Time diagram for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- Object Oriented System Design is a process of defining the architecture, modules, interfaces, and data for a system that uses objects as the basic units of abstraction.
- Basic Structural Modeling is a part of Object Oriented System Design that focuses on the static structure of the system, such as the classes, attributes, operations, and relationships among them.
- A time diagram is a type of UML interaction diagram that shows the interactions of objects along a linear time axis, with a focus on the conditions changing within and among the objects.
- A time diagram consists of the following elements:
  - Lifelines: vertical dashed lines that represent the existence of an object over time. Each lifeline has a name and an optional classifier.
  - States: horizontal segments on a lifeline that indicate the state or condition of the object during a period of time. A state can have a name and an optional value expression.
  - Transitions: vertical lines or arrows that connect states and show the changes in state or condition of the object. A transition can have an event name and an optional event occurrence expression.
  - Constraints: horizontal brackets that span across one or more lifelines and specify a condition or restriction on the timing of events or states. A constraint can have a name and a value expression.
  - Occurrence specifications: points on a lifeline that denote the occurrence of an event, such as sending or receiving a message, creating or destroying an object, or changing a state. An occurrence specification can have a name and an optional event occurrence expression.
  - Messages: horizontal arrows that connect occurrence specifications and show the communication or interaction between objects. A message can have a name, a sequence number, and an optional argument list.
  - Destruction occurrences: X marks on a lifeline that indicate the end of the existence of an object. A destruction occurrence can have a name and an optional event occurrence expression.

- An example of a time diagram for a basic structural modeling of a system that manages books in a library is shown below:

![time diagram example](https://www.visual-paradigm.com/servlet/editor-content/tutorials/what-is-timing-diagram/timing-diagram-example.png)

- The diagram shows the lifelines of three objects: a library, a book, and a borrower. The library object has two states: available and borrowed. The book object has three states: new, old, and damaged. The borrower object has one state: registered. The diagram also shows the transitions, constraints, occurrence specifications, messages, and destruction occurrences that occur during the interaction of the objects. For example, the library object sends a message to the book object to check its state, and the book object replies with its state value. The library object then sends a message to the borrower object to create it, and the borrower object replies with a registered state. The library object then sends a message to the book object to borrow it, and the book object changes its state from new to old. The diagram also shows a constraint that specifies that the book object must be returned within 30 days, and a destruction occurrence that indicates that the book object is destroyed when it is damaged.