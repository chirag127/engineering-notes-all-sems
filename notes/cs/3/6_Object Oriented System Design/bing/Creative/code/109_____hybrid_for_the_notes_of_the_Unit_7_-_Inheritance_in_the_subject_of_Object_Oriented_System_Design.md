# Hybrid Inheritance

- Hybrid inheritance is a concept that combines multiple inheritance, multilevel inheritance, and hierarchical inheritance altogether .
- It is an important part of Object Oriented Programming (OOPs) concepts, which allows developers to create complex programs with robust features .
- Multiple inheritance is when a class inherits from more than one base class.
- Multilevel inheritance is when a class inherits from another class, which in turn inherits from another class.
- Hierarchical inheritance is when a class has more than one subclass.
- Hybrid inheritance is a mixture of these types of inheritance, where a class can inherit from multiple base classes, and those base classes can also inherit from a common base class .
- For example, consider the following class diagram:

![hybrid inheritance example](https://miro.medium.com/max/700/1*ZxQ2X9f0Z1g0f6kZl6Q2Lg.png)

- In this diagram, class D inherits from both class B and class C, which are subclasses of class A. This is a hybrid inheritance pattern, where multiple inheritance and hierarchical inheritance are combined.
- Hybrid inheritance can be used to achieve greater code reusability, modularity, and polymorphism .
- However, hybrid inheritance can also introduce complexity, ambiguity, and conflicts in the program.
- For example, if class B and class C have a method with the same name and signature, and class D calls that method, it is not clear which method should be executed. This is called the diamond problem.
- To resolve this problem, some programming languages, such as C#, use the concept of interfaces, which are abstract classes that only declare methods without providing any implementation .
- Interfaces can be used to specify the common behavior of multiple classes, without inheriting any state or implementation details .
- For example, in C#, the following code snippet shows how to use interfaces to implement hybrid inheritance:

```csharp
// An interface that declares a method called Display()
interface IDisplay
{
    void Display();
}

// A base class that implements the IDisplay interface
class A : IDisplay
{
    public void Display()
    {
        Console.WriteLine("Class A");
    }
}

// A subclass of A that also implements the IDisplay interface
class B : A, IDisplay
{
    public void Display()
    {
        Console.WriteLine("Class B");
    }
}

// Another subclass of A that also implements the IDisplay interface
class C : A, IDisplay
{
    public void Display()
    {
        Console.WriteLine("Class C");
    }
}

// A class that inherits from both B and C using multiple interface inheritance
class D : B, C, IDisplay
{
    public void Display()
    {
        Console.WriteLine("Class D");
    }
}

// A class that tests the hybrid inheritance pattern
class Test
{
    static void Main(string[] args)
    {
        // Create an object of class D
        D d = new D();

        // Call the Display() method of class D
        d.Display(); // Output: Class D

        // Call the Display() method of class B using explicit casting
        ((B)d).Display(); // Output: Class B

        // Call the Display() method of class C using explicit casting
        ((C)d).Display(); // Output: Class C

        // Call the Display() method of class A using explicit casting
        ((A)d).Display(); // Output: Class A
    }
}
```

- In this code snippet, class D inherits from both class B and class C, which are subclasses of class A. All these classes implement the IDisplay interface, which declares a method called Display().
- To avoid the diamond problem, the Display() method of each class can be called using explicit casting, which specifies the type of the object to be used.
- This way, hybrid inheritance can be achieved using interfaces, without causing any ambiguity or conflicts in the program.