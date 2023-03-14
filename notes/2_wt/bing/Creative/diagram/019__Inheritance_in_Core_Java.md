Inheritance in Core Java is a mechanism that allows a class to inherit the features and behavior of another class. The class that inherits is called the subclass or child class, and the class that is inherited is called the superclass or parent class. The subclass can access the non-private and non-static members of the superclass, and can also add its own members. The keyword extends is used to indicate inheritance in Java.

#### Inheritance in Core Java

```
+----------------+       +----------------+
|   Superclass   |       |   Subclass     |
|----------------|       |----------------|
| - privateField |       | - privateField |
| + publicField  |       | + publicField  |
| # protectedField|      | # protectedField|
| ~ defaultField |       | ~ defaultField |
|----------------|       |----------------|
| + publicMethod()|      | + publicMethod()|
| - privateMethod()|     | - privateMethod()|
| # protectedMethod()|   | # protectedMethod()|
| ~ defaultMethod() |    | ~ defaultMethod() |
|----------------|       |----------------|
|                |       |                |
|                |       |                |
|                |       |                |
|                |       |                |
|                |       |                |
|                |       |                |
|                |       |                |
|                |       |                |
+----------------+       +----------------+
         ^                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         |                      |
         +----------------------+
                extends
```

The diagram above shows the basic structure of inheritance in Core Java. The superclass and subclass have their own fields and methods, which are indicated by different symbols:

- `-` means private
- `+` means public
- `#` means protected
- `~` means default (package-private)

The subclass inherits the public, protected, and default members of the superclass, but not the private ones. The subclass can also override the inherited methods or add new ones. The arrow with the word extends shows the inheritance relationship between the two classes.