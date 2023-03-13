#### Cohesion Measures in Software Design

Cohesion is an essential concept in software design that refers to the degree to which the elements of a module or a component are related to each other. In simple words, cohesion measures how well the individual parts of a software module, class or method work together to perform a single, well-defined task.

There are different types of cohesion measures that software designers can use to evaluate the quality of their software components. Here are some of the most commonly used cohesion measures:

1. **Functional cohesion**: This type of cohesion exists when all the elements of a module contribute to the same well-defined task or function. In other words, all the methods or procedures within a module work together to achieve a single, specific goal. 

2. **Sequential cohesion**: This type of cohesion exists when the elements of a module are arranged in a specific order, and each element depends on the output of the previous element. For example, a module that performs a sequence of mathematical calculations in a specific order is said to exhibit sequential cohesion.

3. **Communicational cohesion**: This type of cohesion exists when the elements of a module perform related tasks and share the same data. For example, a module that performs operations on a shared data structure can be said to exhibit communicational cohesion.

4. **Procedural cohesion**: This type of cohesion exists when the elements of a module are related to each other because they are part of the same procedural sequence. For example, a module that performs a series of steps in a specific order to accomplish a task can be said to exhibit procedural cohesion.

5. **Temporal cohesion**: This type of cohesion exists when the elements of a module are related to each other because they are executed at the same time. For example, a module that performs a series of operations at a specific time or in response to a particular event can be said to exhibit temporal cohesion.

6. **Logical cohesion**: This type of cohesion exists when the elements of a module are related to each other because they all contribute to a specific, logical goal. For example, a module that performs a set of operations to validate user input can be said to exhibit logical cohesion.

Cohesion is an essential quality attribute of software, as it affects the maintainability, testability, and reusability of a software system. A well-cohesive software component is easier to understand, modify, and extend than a poorly-cohesive one. 

#### Learning Tricks and Mnemonics

While there are no specific mnemonics or learning tricks for remembering the different types of cohesion measures, it may be helpful to associate each type of cohesion with a specific scenario or example that illustrates its characteristics. For example, you could associate functional cohesion with a module that performs a specific mathematical operation, sequential cohesion with a module that performs a series of calculations in a specific order, and so on. This can help you remember the different types of cohesion measures and their characteristics more easily. 

It is important to note that cohesion measures are not mutually exclusive, and a software component can exhibit more than one type of cohesion. However, it is generally desirable to aim for high cohesion in software design, as it can lead to more maintainable, testable, and reusable software components.