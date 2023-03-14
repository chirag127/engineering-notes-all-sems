### Basic Concept of Software Design

Software design is the process of envisioning and defining software solutions to one or more sets of problems, using a set of primitive components and subject to constraints.  Software design involves problem-solving and planning a software solution, which includes both a low-level component and algorithm design and a high-level architecture design. 

One of the main components of software design is the software requirements analysis (SRA), which is a part of the software development process that lists specifications used in software engineering.  The SRA document is the input for the software design phase, which produces the design document as the output. The design document describes the following aspects of the software:

- Different modules required and their functionalities.
- Control relationships among modules.
- Interfaces among different modules.
- Data structures among the different modules.
- Algorithms required to implement the individual modules.

The objectives of software design are:

- Correctness: The design should correctly implement all the functionalities of the system as specified in the SRA document.
- Efficiency: The design should address the resources, time, and cost optimization issues.
- Understandability: The design should be easily understandable, for which it should be modular and arranged in layers.
- Completeness: The design should have all the components like data structures, modules, and external interfaces, etc.
- Maintainability: The design should be easily amenable to change whenever a change request is made from the customer side.

The concepts of software design are the principles or ideas behind the design, which describe how the design is planned and solved. Some of the concepts of software design are:

- Abstraction: Abstraction means to hide the details to reduce complexity and increase efficiency. Different levels of abstraction are applied at each stage of the design process to refine the software solution. The solution is described in broad terms at a higher level of abstraction and in more detail at a lower level of abstraction.
- Modularity: Modularity means to divide the system into smaller parts to reduce complexity and increase reusability. Modularity in design means to subdivide the system into modules that can be created and tested independently and then used in different systems to perform different functions.
- Coupling: Coupling is the measure of the degree of interdependence between the modules. A good software design should have low coupling, which means the modules are loosely connected and can function independently without affecting other modules.
- Cohesion: Cohesion is the measure of the degree of intra-dependence within a module. A good software design should have high cohesion, which means the module performs a single well-defined task and has a clear purpose.
- Encapsulation: Encapsulation is the technique of hiding the internal details of a module from the outside world and providing a well-defined interface for communication. Encapsulation ensures that the module can be changed internally without affecting the external behavior of the module.
- Information hiding: Information hiding is the principle of hiding the details that are not essential for the user and exposing only the necessary information. Information hiding reduces complexity and increases security and maintainability of the software.
- Inheritance: Inheritance is the mechanism of reusing the properties and behaviors of an existing class or module by creating a new class or module that inherits from it. Inheritance allows the software to be extended and modified easily without affecting the existing functionality.
- Polymorphism: Polymorphism is the ability of a module to behave differently depending on the context or the input. Polymorphism allows the software to be flexible and adaptable to different situations and requirements.

A mnemonic to remember some of the concepts of software design is:

**A MICE PIC**

- **A**bstraction
- **M**odularity
- **I**nformation hiding
- **C**oupling
- **E**ncapsulation
- **P**olymorphism
- **I**nheritance
- **C**ohesion