#### Function Oriented Design in Software Design

- Function Oriented Design (FOD) is a method to software design where the model is decomposed into a set of interacting units or modules where each unit or module has a clearly defined function .
- The system is designed from a functional viewpoint, that is, the focus is on what the system does rather than how it does it.
- FOD follows a top-down approach, where the system is first described at a high level of abstraction, and then each part of the system is refined in greater detail until the design is complete.
- FOD uses various design notations to represent the system, such as data flow diagrams, data dictionaries, structure charts, and pseudo code .
- Data flow diagrams (DFDs) show how data flows through the system and how the output is derived from the input through a series of functional transformations . DFDs use symbols like rectangles, circles, and arrows to show data inputs, outputs, storage points, and the routes between each destination.
- Data dictionaries (DDs) are repositories to store information about all data items defined in DFDs . DDs include the name, aliases, description, related data items, range of values, and data structure definition of each data item.
- Structure charts (SCs) are hierarchical representations of the system that show the modules and their relationships . SCs use symbols like boxes and lines to show the modules, their functions, and their calls.
- Pseudo code (PC) is a system description in short English-like phrases that describe the function of each module . PC uses keywords and indentation to show the logic and structure of the code.

Some advantages of FOD are:

- It is easy to understand and communicate the system design using graphical and textual notations.
- It supports modularization and abstraction, which help to reduce complexity and enhance reusability.
- It facilitates top-down testing and debugging, as each module can be tested and verified independently.

Some disadvantages of FOD are:

- It does not capture the dynamic behavior and interactions of the system well, as it focuses on the static data flow and functions.
- It does not consider the object-oriented concepts such as encapsulation, inheritance, and polymorphism, which are widely used in modern software development.
- It may lead to poor data design and low cohesion, as the data is scattered across different modules and functions.

Some examples of FOD are:

- Structured design methods, such as Structured Analysis and Design Technique (SADT), Structured Systems Analysis and Design Method (SSADM), and Yourdon/Constantine method.
- Functional programming languages, such as Lisp, Scheme, Haskell, and Erlang.

Some applications of FOD are:

- FOD is suitable for designing systems that are data-intensive, sequential, and deterministic, such as batch processing systems, numerical computation systems, and text processing systems.
- FOD is also useful for prototyping and exploring the functionality of a system before implementing it in a more suitable design paradigm.