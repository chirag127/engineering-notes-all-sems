### Issues for the notes of the Unit 6 - Object Oriented Testing in the subject of Software Testing

- Object Oriented Testing (OOT) is a software testing process that is conducted to test the software using object oriented paradigms like encapsulation, inheritance, polymorphism, etc.  
- OOT presents specific challenges to the testing teams, as the object oriented software contains the OO methodology and its different components, such as classes, objects, methods, messages, etc.  
- Some of the issues that are faced in OOT are:

  - **Encapsulation**: Encapsulation is the mechanism of hiding the internal details of an object from the outside world. It provides data abstraction and information hiding. However, it also makes it difficult to test the internal state and behavior of an object, as they are not directly accessible.   
    - One possible solution is to use **white-box testing** techniques, such as code coverage, data flow analysis, etc., to test the internal logic of an object.  
    - Another possible solution is to use **test drivers** or **stubs** to simulate the interactions between objects and test their interfaces.  

  - **Inheritance**: Inheritance is the mechanism of deriving new classes from existing ones, and inheriting their attributes and methods. It provides code reuse and specialization. However, it also introduces complexity and ambiguity in testing, as the derived classes may have different or overridden behaviors from the base classes.   
    - One possible solution is to use **regression testing** techniques, such as retesting, test selection, test prioritization, etc., to test the changes and impacts of inheritance on the software.  
    - Another possible solution is to use **class testing** techniques, such as class hierarchy analysis, class interaction testing, etc., to test the relationships and dependencies between classes.  

  - **Polymorphism**: Polymorphism is the mechanism of having different implementations of the same method or operator for different types of objects. It provides flexibility and dynamic binding. However, it also increases the uncertainty and variability in testing, as the actual behavior of an object may depend on its runtime type and context.   
    - One possible solution is to use **black-box testing** techniques, such as equivalence partitioning, boundary value analysis, etc., to test the input and output of an object based on its specification.  
    - Another possible solution is to use **dynamic testing** techniques, such as runtime monitoring, debugging, etc., to test the actual behavior of an object at runtime.  

- Some of the mnemonics and learning tricks for the issues in OOT are:

  - **EIP**: Encapsulation, Inheritance, Polymorphism - the three main OO concepts that cause issues in OOT. 
  - **WRT**: White-box, Regression, Test drivers - the possible solutions for testing encapsulation.  
  - **RCT**: Regression, Class testing, Test selection - the possible solutions for testing inheritance.  
  - **BDD**: Black-box, Dynamic testing, Debugging - the possible solutions for testing polymorphism.