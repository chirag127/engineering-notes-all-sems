A class in Java is a blueprint that defines the attributes and behaviors of an object. A class can contain fields, which are variables that store data, and methods, which are functions that perform actions on the object. An object is an instance of a class that can be created and manipulated at runtime. A class can also have constructors, which are special methods that initialize the object when it is created.

#### Methods & Classes in Core Java

The following diagram shows a simple example of a class and an object in Java:

```
+---------------------+
|       Person        |  <-- This is a class
+---------------------+
| - name : String     |  <-- This is a field
| - age : int         |
+---------------------+
| + Person(name, age) |  <-- This is a constructor
| + getName() : String|  <-- This is a method
| + getAge() : int    |
| + setName(name)     |
| + setAge(age)       |
+---------------------+

+---------------------+
|       p1            |  <-- This is an object
+---------------------+
| - name : "Alice"    |  <-- This is a value
| - age : 25          |
+---------------------+
| + Person(name, age) |
| + getName() : String|
| + getAge() : int    |
| + setName(name)     |
| + setAge(age)       |
+---------------------+
```

The class Person has two fields, name and age, and five methods, a constructor and four getters and setters. The object p1 is created by using the new keyword and calling the constructor with the values "Alice" and 25. The object p1 can access the fields and methods of the class Person by using the dot operator (.). For example, p1.getName() will return "Alice" and p1.setAge(26) will change the value of the age field to 26.