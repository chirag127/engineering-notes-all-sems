### Layered structure of operating system

- The layered structure of operating system is an operating system architecture that divides the software components into different layers, where the hardware is at the bottom layer and the user interface is at the top layer.
- Each layer in the operating system is responsible for certain functions and services, and can only use the functions of the lower-level layers.
- The layered structure of operating system was proposed to improve the modularity, maintainability, and portability of the operating system, compared to the monolithic and simple structures.
- The advantages of the layered structure of operating system are:
  - Modularity: Each layer is independent and well-defined, and can be modified or replaced without affecting the other layers.
  - Easy debugging: Errors can be easily located and corrected in a specific layer, without affecting the rest of the system.
  - Portability: The hardware-dependent layer can be changed to adapt to different hardware platforms, without affecting the higher-level layers.
- The disadvantages of the layered structure of operating system are:
  - Overhead: Each layer adds some overhead to the system performance, as there are more function calls and data transfers between layers.
  - Difficulty in defining layers: It is not easy to decide how many layers are needed and what functions should be assigned to each layer, as there may be dependencies and interactions between layers.
  - Lack of flexibility: The rigid hierarchy of layers may limit the flexibility and functionality of the system, as some functions may need to access the higher-level layers directly.

- An example of the layered structure of operating system is the THE operating system, developed by Dijkstra and his team at the Technological University of Eindhoven in the 1960s. It had six layers, as shown below:

```
+-----------------+
|     Layer 5     |
|  User programs  |
+-----------------+
|     Layer 4     |
|  Input/Output   |
+-----------------+
|     Layer 3     |
|  Operator console|
+-----------------+
|     Layer 2     |
|  Memory manager |
+-----------------+
|     Layer 1     |
|  Processor manager|
+-----------------+
|     Layer 0     |
|     Hardware    |
+-----------------+
```

- Another example of the layered structure of operating system is the Windows NT operating system, developed by Microsoft in the 1990s. It had four layers, as shown below:

```
+-----------------+
|     Layer 3     |
|  User mode      |
|  Subsystems     |
+-----------------+
|     Layer 2     |
|  User mode      |
|  Executive      |
+-----------------+
|     Layer 1     |
|  Kernel mode    |
|  Executive      |
+-----------------+
|     Layer 0     |
|  Hardware       |
|  Abstraction    |
|  Layer (HAL)    |
+-----------------+
```

Some possible mnemonics and learning tricks for the topic are:

- To remember the six layers of the THE operating system, you can use the acronym UMPIRE, which stands for User programs, Memory manager, Processor manager, Input/Output, Operator console, and Hardware.
- To remember the four layers of the Windows NT operating system, you can use the acronym USEK, which stands for User mode Subsystems, User mode Executive, Kernel mode Executive, and Hardware Abstraction Layer (HAL).
- To remember the advantages and disadvantages of the layered structure of operating system, you can use the following sentences:

  - Advantages: Modularity makes debugging easy and portability possible.
  - Disadvantages: Overhead, difficulty, and lack of flexibility are the drawbacks of layers.