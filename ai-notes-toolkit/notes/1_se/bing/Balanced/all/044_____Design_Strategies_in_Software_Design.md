### Design Strategies in Software Design

- Design strategies are the approaches that are taken to design a software system that meets the requirements and specifications of the problem domain.
- Design strategies help to outline the product's architecture, interfaces, data, and modules in a systematic and coherent way.
- Design strategies also help to improve the quality, maintainability, reusability, and scalability of the software system.
- There are three major types of design strategies in software engineering: structured design, function-oriented design, and object-oriented design.

#### Structured Design
- Structured design is a design strategy that focuses on the decomposition of the software system into smaller, independent, and well-defined modules that communicate with each other through well-defined interfaces.
- Structured design follows the top-down design approach, which starts with a high-level view of the system and gradually breaks it down into lower-level components.
- Structured design is based on the principle of information hiding, which means that each module should hide its internal details and expose only the necessary information to other modules.
- Structured design is suitable for simple and linear software systems that have clear and stable requirements and specifications.
- Structured design has some limitations, such as:
  - It does not support the concepts of inheritance, polymorphism, and encapsulation, which are essential for modeling complex and dynamic software systems.
  - It does not handle the changes in the requirements and specifications well, as it requires modifying the entire system structure and interfaces.
  - It does not facilitate the reuse of existing modules, as they are tightly coupled with the system structure and interfaces.

#### Function-Oriented Design
- Function-oriented design is a design strategy that focuses on the identification and organization of the software system's functions and data.
- Function-oriented design follows the bottom-up design approach, which starts with the identification of the basic functions and data of the system and gradually combines them into higher-level functions and data structures.
- Function-oriented design is based on the principle of functional abstraction, which means that each function should perform a single and well-defined task and hide the details of how it is implemented.
- Function-oriented design is suitable for software systems that have complex and dynamic functions and data, and that require high performance and efficiency.
- Function-oriented design has some limitations, such as:
  - It does not support the concepts of classes, objects, and methods, which are essential for modeling the real-world entities and behaviors of the software system.
  - It does not handle the changes in the functions and data well, as it requires modifying the existing functions and data structures.
  - It does not facilitate the reuse of existing functions and data, as they are not modular and independent.

#### Object-Oriented Design
- Object-oriented design is a design strategy that focuses on the identification and organization of the software system's classes, objects, and methods.
- Object-oriented design follows the iterative and incremental design approach, which starts with the identification of the most important classes, objects, and methods of the system and gradually refines and extends them.
- Object-oriented design is based on the principle of object abstraction, which means that each class should represent a real-world entity or concept and hide the details of how it is implemented.
- Object-oriented design supports the concepts of inheritance, polymorphism, and encapsulation, which are essential for modeling complex and dynamic software systems.
- Object-oriented design is suitable for software systems that have complex and dynamic requirements and specifications, and that require high modularity, reusability, and scalability.
- Object-oriented design has some limitations, such as:
  - It requires more analysis and design effort, as it involves identifying and defining the classes, objects, and methods of the system.
  - It requires more testing and debugging effort, as it involves testing and debugging the interactions and behaviors of the classes, objects, and methods of the system.
  - It requires more memory and processing power, as it involves creating and managing the instances of the classes and objects of the system.

#### Mnemonics and Learning Tricks
- A possible mnemonic to remember the three types of design strategies is **SFO** (Structured, Function-oriented, Object-oriented).
- A possible learning trick to remember the differences between the three types of design strategies is to use the analogy of building a house:
  - Structured design is like building a house by dividing it into rooms and connecting them with doors and windows. Each room has a specific purpose and hides its internal details from other rooms. This works well for simple and linear houses, but not for complex and dynamic ones.
  - Function-oriented design is like building a house by identifying and organizing the functions and data that are needed in the house.