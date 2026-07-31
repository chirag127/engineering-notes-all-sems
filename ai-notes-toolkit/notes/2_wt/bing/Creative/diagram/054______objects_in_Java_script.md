Objects in JavaScript are standalone entities that can store various keyed data and functions. They can be created using the Object() constructor or the object literal syntax. Here is an example of an object literal syntax:

```javascript
var person = {
  name: "Alice",
  age: 25,
  greet: function() {
    console.log("Hello, my name is " + this.name);
  }
};
```

This object has three properties: name, age, and greet. The name and age properties are data values, while the greet property is a function (also called a method). The object can access its own properties using the this keyword.

Here is a possible ASCII diagram for this object:

```
+-----------------+
|    person       |
+-----------------+
| name: "Alice"   |
| age: 25         |
| greet: function |
+-----------------+
```

The diagram shows the object name, the properties, and their values. The function value is not shown in detail, but it could be represented by a curly brace or a symbol. The diagram can be extended to show more properties or nested objects.