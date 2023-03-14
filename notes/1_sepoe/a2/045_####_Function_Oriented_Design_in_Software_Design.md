 Here is the content in markdown format for the topic #### Function Oriented Design in Software Design:

#### Function Oriented Design in Software Design

- In Function Oriented Design, the software is designed in terms of functions. The primary focus is on functions, their inputs, outputs, and their relationships with other functions.
- Key points:
    - The system is viewed as a collection of functions that transform inputs into outputs.
    - Each function is an independent and self-contained module that performs a specific task.
    - Functions are interconnected and the output of one function can be the input to another function.
    - Global data is minimized and shared among functions. Most data is local to functions.
    - The architecture is hierarchical with higher-level functions calling lower-level functions.
- Mnemonics:
    - Think of a function as a black box that takes in inputs and gives out outputs.
    - The system is made up of interconnected function boxes.
    - Isolate functions and minimize shared data.
    - Hierarchical decomposition into high and low level functions.
- Advantages:
    - Modularity - Functions are independent modules that can be reused.
    - Readability - The system logic is easier to follow as it is split into manageable functions.
    - Maintainability - Changes to one function does not affect other functions. Functions can be modified or replaced easily.
    - Scalability - The function oriented architecture can handle increasing complexity by adding more functions.
- Disadvantages:
    - Inefficiency - Repeated data inputs/outputs and function call overheads can lead to inefficiencies.
    - Debugging - It can be harder to debug due to many function calls and data being localized.
    - Complex interactions - Complex interactions between functions can make the system logic hard to follow.
- Examples: Numerical methods, signal processing systems.
- Applications: Software that can be decomposed into functional components like calculators, billing systems, etc.

[Detailed diagrams and code examples can be added here if required to understand the concepts better.]