### Classes

- Classes are templates for defining the characteristics and operations of an object .
- Classes are used to create and manage new objects and support inheritance, which is a mechanism of reusing code.
- Classes are the building blocks of object-oriented system design.
- Classes can be represented by a class diagram, which shows the name, attributes, and methods of a class, as well as the relationships between classes.
- A class diagram can be drawn using the Unified Modeling Language (UML) notation, which consists of a rectangle with three compartments: the top one for the class name, the middle one for the attributes, and the bottom one for the methods.
- An example of a class diagram for a class named Student is shown below:

```
+----------------+
|    Student     |
+----------------+
| - name: String |
| - age: int     |
| - major: String|
+----------------+
| + getName(): String |
| + getAge(): int     |
| + getMajor(): String|
| + setName(String): void |
| + setAge(int): void     |
| + setMajor(String): void|
+----------------+
```

- The attributes and methods of a class can have different visibility levels, indicated by the symbols: + for public, - for private, # for protected, and ~ for package.
- Public attributes and methods can be accessed by any object, private attributes and methods can only be accessed by the object itself, protected attributes and methods can be accessed by the object and its subclasses, and package attributes and methods can be accessed by objects in the same package.
- A class can also have static attributes and methods, which belong to the class itself and not to any specific object. Static attributes and methods are marked with an underline.
- A class can also have abstract methods, which are methods that have no implementation and must be overridden by subclasses. Abstract methods are marked with an italic font.
- A class can also have constructors, which are special methods that are invoked when an object is created. Constructors have the same name as the class and no return type.
- A class can also have associations with other classes, which represent the relationships between objects. Associations can have different types, such as aggregation, composition, generalization, and realization.
- Aggregation is a type of association that represents a whole-part relationship, where the part can exist independently of the whole. Aggregation is denoted by a hollow diamond at the end of the association line that points to the whole.
- Composition is a type of association that represents a stronger whole-part relationship, where the part cannot exist without the whole. Composition is denoted by a solid diamond at the end of the association line that points to the whole.
- Generalization is a type of association that represents an inheritance relationship, where a subclass inherits the attributes and methods of a superclass. Generalization is denoted by a solid line with a hollow triangle at the end of the line that points to the superclass.
- Realization is a type of association that represents an implementation relationship, where a class implements the abstract methods of an interface. Realization is denoted by a dashed line with a hollow triangle at the end of the line that points to the interface.
- An example of a class diagram with different types of associations is shown below:

```
+----------------+       +----------------+
|    Student     |       |    Course      |
+----------------+       +----------------+
| - name: String |       | - code: String |
| - age: int     |       | - title: String|
| - major: String|       | - credits: int |
+----------------+       +----------------+
| + getName(): String |  | + getCode(): String |
| + getAge(): int     |  | + getTitle(): String|
| + getMajor(): String|  | + getCredits(): int |
| + setName(String): void |  | + setCode(String): void |
| + setAge(int): void     |  | + setTitle(String): void|
| + setMajor(String): void|  | + setCredits(int): void |
+----------------+       +----------------+
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |