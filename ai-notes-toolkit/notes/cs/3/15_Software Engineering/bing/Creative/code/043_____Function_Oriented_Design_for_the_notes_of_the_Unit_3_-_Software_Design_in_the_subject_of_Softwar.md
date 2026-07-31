# Function Oriented Design

- Function Oriented Design (FOD) is an approach to software design where the design is decomposed into a set of interacting units or modules where each unit or module has a clearly defined function .
- FOD is based on the idea of top-down decomposition, where the system is first viewed as a single function and then refined into smaller and smaller sub-functions until they are simple enough to be implemented.
- FOD focuses on the functionality of the system rather than the data or the objects involved. The data is treated as passive and the functions are treated as active.
- FOD is suitable for developing software systems that are algorithmic or computational in nature, where the main goal is to perform some calculations or transformations on the input data and produce the output data.

## FOD Strategies

- Some of the common strategies or techniques used in FOD are:

  - Data Flow Diagram (DFD): A DFD is a graphical representation of the flow of data and the functions that process the data in a system. It shows the sources and destinations of the data, the data stores, the external entities, and the processes that transform the data. A DFD can be drawn at different levels of abstraction, from the context level (level 0) to the detailed level (level n).
  - Data Dictionary: A data dictionary is a repository of information about the data items defined in the DFDs. It specifies the name, description, type, format, range, and other attributes of each data item. It also shows the relationships and dependencies among the data items.
  - Structured English: Structured English is a subset of natural language that is used to describe the logic and functionality of a process in a DFD. It follows some rules and conventions to avoid ambiguity and confusion. It uses keywords, indentation, and punctuation to structure the sentences.
  - Decision Table: A decision table is a tabular representation of the conditions and actions of a process in a DFD. It shows the possible combinations of inputs and outputs and the corresponding actions to be performed. It helps to simplify complex logic and handle multiple cases.
  - Decision Tree: A decision tree is a graphical representation of the conditions and actions of a process in a DFD. It shows the branching structure of the logic and the sequence of decisions and actions. It helps to visualize the flow of control and the alternatives.

## FOD Advantages and Disadvantages

- Some of the advantages of FOD are :

  - It is easy to understand and communicate, as it uses natural language and graphical notations.
  - It is systematic and disciplined, as it follows a top-down approach and a step-by-step procedure.
  - It is modular and hierarchical, as it divides the system into smaller and manageable units and levels.
  - It is independent of the programming language and the hardware platform, as it focuses on the functionality rather than the implementation.

- Some of the disadvantages of FOD are :

  - It is not suitable for developing software systems that are object-oriented or data-driven, where the main goal is to model the real-world entities and their behaviors and interactions.
  - It does not capture the dynamic aspects of the system, such as the states, events, and transitions.
  - It does not support reusability and maintainability, as it does not emphasize the data abstraction and encapsulation.
  - It may lead to poor data quality and integrity, as it does not enforce the data consistency and security.