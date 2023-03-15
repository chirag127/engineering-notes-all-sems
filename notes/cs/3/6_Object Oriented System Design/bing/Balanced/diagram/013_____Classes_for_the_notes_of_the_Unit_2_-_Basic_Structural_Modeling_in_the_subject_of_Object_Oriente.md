### Classes

- Classes are templates for defining the characteristics and operations of an object .
- Classes are used to create and manage new objects and support inheritance, which is a mechanism of reusing code.
- Classes are the building blocks of object-oriented system design.
- Classes can be represented by a class diagram, which shows the name, attributes, and methods of a class, as well as the relationships between classes.
- A class diagram can be drawn using the Unified Modeling Language (UML) notation, which consists of a rectangle with three compartments: the top one for the class name, the middle one for the attributes, and the bottom one for the methods.
- An example of a class diagram is shown below:

```
+-----------------+
|    Student      |
+-----------------+
| - name: String  |
| - age: int      |
| - major: String |
+-----------------+
| + getName(): String |
| + getAge(): int     |
| + getMajor(): String|
| + setName(String): void |
| + setAge(int): void    |
| + setMajor(String): void |
+-----------------+
```

- The class name is Student, and it has three attributes: name, age, and major, which are of type String, int, and String, respectively.
- The class also has six methods: getName, getAge, getMajor, setName, setAge, and setMajor, which are used to access and modify the attributes of the class.
- The methods have a return type and a parameter list, which are shown in parentheses after the method name.
- The symbols + and - indicate the visibility of the attributes and methods: + means public and - means private.
- Public attributes and methods can be accessed by any other class, while private attributes and methods can only be accessed by the class itself or its subclasses.