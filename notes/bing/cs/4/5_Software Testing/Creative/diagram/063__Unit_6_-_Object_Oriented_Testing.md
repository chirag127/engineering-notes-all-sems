## Unit 6 - Object Oriented Testing

Object oriented testing is a method of software testing that focuses on the objects and classes of an object oriented system. Object oriented testing involves testing the behavior and interactions of the objects, as well as the functionality and quality of the system as a whole.

One way to represent object oriented testing is by using an object diagram, which is a type of UML diagram that shows the instances of the classes and their relationships in a system. An object diagram is similar to a class diagram, but it shows the actual objects and their values, rather than the abstract classes and their attributes.

An object diagram can be used to show the state of the system at a particular point in time, or to illustrate a test case or a scenario. An object diagram can also be used to verify the accuracy and completeness of a class diagram, by showing examples of data structures and object interactions.

An object diagram consists of the following elements:

- Objects: The instances of the classes in the system. They are represented by rectangles with the object name and the class name separated by a colon, such as `obj1:Class1`. The object name can be omitted if it is not relevant or important. The object can also show the values of its attributes, such as `obj1:Class1 (attr1 = 10, attr2 = "hello")`.
- Links: The connections between the objects that represent their associations or dependencies. They are represented by solid lines with optional labels or multiplicity indicators, such as `1..*` or `0..1`. A link can also show the value of its role or qualifier, such as `obj1 -role-> obj2` or `obj1 -[qual]-> obj2`.
- Messages: The communications between the objects that represent their operations or methods. They are represented by dashed lines with arrowheads and labels that indicate the name and parameters of the message, such as `obj1 -> obj2:method1(param1, param2)`. A message can also show the return value of the operation, such as `obj1 <- obj2:method1(param1, param2) = result`.

The following diagram illustrates the basic architecture of a object oriented testing system:

```
+------------------+       +------------------+       +------------------+
| Test Case        |       | Test Runner      |       | Test Report      |
|------------------|       |------------------|       |------------------|
| -name            |       | -testCases       |       | -results         |
| -description     |       | -testReport      |       | -summary         |
| -testSteps       |       | -run()           |       | -show()          |
| -expectedResults |       | -report()        |       |                  |
| -actualResults   |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        +----------------------->+                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        +----------------------->+
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        +<-----------------------+                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        +<-----------------------+
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |