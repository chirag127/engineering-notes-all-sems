An object in JavaScript is a variable that contains multiple data values, which are called properties. Properties can be primitive values, such as strings, numbers, or booleans, or reference values, such as arrays, functions, or other objects. Properties are accessed using dot notation or bracket notation, such as `obj.name` or `obj["name"]`. Objects can also have methods, which are functions that belong to the object and can perform actions on it. Methods are invoked using parentheses, such as `obj.sayHello()`.

The following diagram illustrates the basic structure of an object in JavaScript using ASCII characters:

```
+---------------------+
|      Object         |
+---------------------+
| name: "John"        |
| age: 25             |
| hobbies: ["reading",|  +-----------------+
|          "gaming"]  |->|    Array       |
| sayHello: function()|  +-----------------+
| {                   |  | 0: "reading"    |
|   console.log("Hi, I|  | 1: "gaming"     |
|   am " + this.name);|  +-----------------+
| }                   |
+---------------------+
```

The object has four properties: `name`, `age`, `hobbies`, and `sayHello`. The `name` and `age` properties are primitive values, while the `hobbies` property is a reference to an array object, which has two elements. The `sayHello` property is a method, which is a function that prints a greeting message using the `name` property of the object. The `this` keyword refers to the current object.