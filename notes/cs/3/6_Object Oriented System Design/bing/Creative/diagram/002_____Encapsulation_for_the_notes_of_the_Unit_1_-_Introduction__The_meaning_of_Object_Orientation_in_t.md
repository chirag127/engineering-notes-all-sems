### Encapsulation

- Encapsulation is a fundamental concept in object-oriented programming (OOP) that involves bundling data and the methods that operate on that data within a single unit, known as a class .
- This concept helps to protect the data and methods from outside interference, as it restricts direct access to them .
- Encapsulation separates the contractual interface of an abstraction and its implementation. The interface defines the behavior and properties of an object, while the implementation provides the details of how the object works internally.
- Encapsulation allows an object to hide its internal state and functionality from other objects, and only expose a public set of functions that can be used to interact with the object.
- Encapsulation enables modularity, reusability, and maintainability of code, as it reduces the coupling between different components of a system and allows for easy changes and updates.
- Encapsulation can be achieved by using access modifiers, such as public, private, protected, and internal, to control the visibility and accessibility of the data and methods within a class.
- Encapsulation can also be implemented by using properties, which are special methods that provide a way to read and write the values of private fields.
- Encapsulation can be illustrated by the following diagram:

![Encapsulation diagram](https://stackify.com/wp-content/uploads/2017/09/encapsulation-1-793x397.png)

The diagram shows a class called Employee, which has three private fields: name, age, and salary. These fields are not directly accessible from outside the class, but can be accessed through public properties: Name, Age, and Salary. The class also has a public method called GetInfo, which returns a string containing the information of the employee. The class encapsulates the data and methods related to an employee, and only exposes the necessary interface to interact with it.