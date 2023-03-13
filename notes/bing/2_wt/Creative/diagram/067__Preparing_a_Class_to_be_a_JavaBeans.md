A JavaBean is a Java class that follows some conventions to be used as a reusable component. To prepare a class to be a JavaBean, it must:

- Implement the java.io.Serializable interface, which allows the object to be saved and restored.
- Have a public no-argument constructor, which allows the object to be instantiated by a bean container or a tool.
- Have private properties with public getter and setter methods, which follow the naming convention of getPropertyName and setPropertyName. This allows the object to be manipulated by a bean container or a tool.

The following diagram illustrates the basic structure of a JavaBean class:

```
+-----------------+
|  JavaBean Class |
+-----------------+
|                 |
| + private prop1 |<-------------------+
| + private prop2 |<-----------------+ |
| + ...           |<---------------+ | |
|                 |                | | |
| + public no-arg |                | | |
|   constructor() |                | | |
|                 |                | | |
| + public getProp1()             | | |
| + public setProp1(prop1)        | | |
|                 |                | | |
| + public getProp2()             | | |
| + public setProp2(prop2)        | | |
|                 |                | | |
| + ...                           | | |
+-----------------+                | | |
                                   | | |
+-----------------+                | | |
|  Bean Container |                | | |
|  or Tool        |                | | |
+-----------------+                | | |
|                 |                | | |
| + instantiate() |----------------> | |
|                 |                  | |
| + manipulate()  |------------------+ |
|                 |                    |
| + save()        |--------------------+
| + restore()     |
|                 |
+-----------------+
```