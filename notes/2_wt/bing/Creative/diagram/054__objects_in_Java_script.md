Objects in JavaScript are variables that contain multiple data values. The values within a JS object are known as properties. Objects use keys to name values, much like how is done with variables. Objects can be created using the Object () constructor or the object initializer / literal syntax . An object initializer is also called an object literal, and it is a comma-separated list of key-value pairs enclosed in curly braces.

The following diagram illustrates the basic structure of an object in JavaScript:

#### Objects in JavaScript
```
+-----------------+
|                 |
|  Object name    |
|                 |
+-----------------+
|                 |
|  key1: value1   |
|  key2: value2   |
|  ...            |
|  keyN: valueN   |
|                 |
+-----------------+
```

The keys can be identifiers, numbers, or strings, and the values can be any valid expression, including functions, which are called methods when they are properties of an object. For example, the following object literal defines a person object with four properties: name, age, gender, and sayHello.

#### Example of an object literal
```
const person = {
  name: "Alice",
  age: 25,
  gender: "female",
  sayHello: function() {
    console.log("Hello, I'm " + this.name);
  }
};
```

To access the properties of an object, you can use either dot notation or bracket notation. For example, person.name or person["name"] will return the value of the name property. To invoke a method of an object, you can use dot notation followed by parentheses. For example, person.sayHello() will call the sayHello function and print "Hello, I'm Alice" to the console.