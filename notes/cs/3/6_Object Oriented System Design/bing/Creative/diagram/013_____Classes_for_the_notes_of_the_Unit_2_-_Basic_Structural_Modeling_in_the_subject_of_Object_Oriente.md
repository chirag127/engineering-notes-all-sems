Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of classes for the unit 2 - basic structural modeling in the subject of object oriented system design.

### Classes
- A class is a template or blueprint that defines the properties and behaviors of objects that belong to that class.
- A class can have attributes, which are data members that store the state or characteristics of the objects, and operations, which are methods or functions that perform actions on the objects or manipulate their attributes.
- A class can also have relationships with other classes, such as inheritance, association, aggregation, composition, or dependency, which specify how the classes are connected or interact with each other.
- A class can be represented by a rectangle with three compartments in a UML class diagram. The top compartment shows the name of the class, the middle compartment shows the attributes of the class, and the bottom compartment shows the operations of the class.
- The attributes and operations can have different visibility or access modifiers, such as public (+), private (-), protected (#), or package (~), which indicate who can access them. The visibility can be shown by a symbol before the name of the attribute or operation in the class diagram.
- The attributes and operations can also have different properties or stereotypes, such as static, abstract, final, or derived, which indicate how they behave or are implemented. The properties can be shown by a keyword in curly braces after the name of the attribute or operation in the class diagram.
- An example of a class diagram for a class named Student is shown below:

```markdown
+----------------+
|    Student     |
+----------------+
| - name: String |
| - age: int     |
| - id: String   |
+----------------+
| + getName(): String |
| + getAge(): int     |
| + getId(): String   |
| + setName(name: String): void |
| + setAge(age: int): void     |
| + setId(id: String): void   |
+----------------+
```