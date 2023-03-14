### Issues for the notes of the Unit 6 - Object Oriented Testing in the subject of Software Testing

Object-oriented programming (OOP) has become the predominant paradigm for software development. Therefore, testing object-oriented software is essential to ensure its quality and reliability. However, testing object-oriented software poses some unique challenges that need to be addressed to achieve effective testing. Here are some of the issues that you need to keep in mind while testing object-oriented software.

1. **Inheritance**: Inheritance is a fundamental feature of OOP, but it can make testing challenging. Inheritance can lead to code reuse, but it also introduces complexity and dependencies between classes. Testing inherited code requires testing the base class and all its derived classes. It is essential to ensure that the derived classes maintain the behavior of the base class, and the base class does not break the derived classes.

2. **Polymorphism**: Polymorphism is another crucial feature of OOP, which can make testing complex. Polymorphism allows objects of different classes to be treated as if they were the same class. Testing polymorphic code requires testing all the possible types of objects that can be passed to a method.

3. **Encapsulation**: Encapsulation is a mechanism that hides the implementation details of a class from other classes. Testing encapsulated code requires accessing the internal state of the class. This can be done using accessor methods or reflection. However, accessing the internal state of a class can break encapsulation, leading to fragile tests.

4. **Dependency Injection**: Dependency injection is a technique used to manage dependencies between objects in OOP. It enables objects to be tested in isolation by replacing their dependencies with mock objects. Testing code that uses dependency injection requires creating mock objects, which can be time-consuming and error-prone.

5. **Testing Exceptions**: Exceptions are used in OOP to handle error conditions. Testing exception handling code requires testing the code's behavior when an exception is thrown. It is essential to ensure that the code handles the exception correctly and does not leave the system in an inconsistent state.

6. **Code Coverage**: Code coverage is a metric used to measure how much of the code is executed during testing. Testing object-oriented software requires achieving high code coverage to ensure that all the paths through the code are tested. However, achieving high code coverage can be challenging, especially if the code has complex control flow.

Mnemonic: "I PEE on the DECK" (Inheritance, Polymorphism, Encapsulation, Dependency Injection, Testing Exceptions, Code Coverage) can help you remember the issues to keep in mind while testing object-oriented software.

In conclusion, testing object-oriented software is a challenging task that requires careful planning and execution. By keeping these issues in mind, you can ensure that your tests are effective and reliable, and your software is of high quality.