### Multilevel Inheritance

Multilevel inheritance is a type of inheritance in which a derived class is created by inheriting properties from another derived class. In this type of inheritance, a class can inherit properties from its parent class, which in turn can inherit properties from its own parent class.

#### Syntax

The syntax for creating a multilevel inheritance class is as follows:

```
class Base_Class
{
    //code
};

class Derived_Class1 : public Base_Class
{
    //code
};

class Derived_Class2 : public Derived_Class1
{
    //code
};
```

#### Advantages of Multilevel Inheritance

- It provides a clear and simple hierarchy of classes.
- It allows for code reusability by inheriting properties from parent classes.
- It allows for the creation of complex systems by breaking down complex classes into smaller, more manageable classes.

#### Disadvantages of Multilevel Inheritance

- It can be difficult to manage and maintain a large hierarchy of classes.
- It can lead to code duplication if properties are inherited from multiple classes.
- It can lead to tight coupling between classes, making it difficult to make changes or modifications to the code.

#### Example

Consider the following example:

```
class Vehicle
{
    public:
        void start()
        {
            cout << "Vehicle started" << endl;
        }
};

class Car : public Vehicle
{
    public:
        void drive()
        {
            cout << "Car is being driven" << endl;
        }
};

class Sports_Car : public Car
{
    public:
        void race()
        {
            cout << "Sports car is racing" << endl;
        }
};
```

In this example, the `Sports_Car` class is derived from the `Car` class, which in turn is derived from the `Vehicle` class. The `Sports_Car` class inherits the `drive()` method from the `Car` class and the `start()` method from the `Vehicle` class. Additionally, the `Sports_Car` class has its own unique method, `race()`.