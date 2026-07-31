### JS Objects

- An object is a collection of properties that store data and functions that perform actions.
- An object can be created using an object literal, which is a pair of curly braces `{}` that enclose a list of properties and values separated by commas.
- A property is a key-value pair, where the key is a name or identifier and the value can be any valid JavaScript expression, such as a string, a number, a boolean, an array, a function, or another object.
- A property can be accessed using dot notation `object.property` or bracket notation `object["property"]`.
- A function that is stored as a property of an object is called a method. A method can be invoked using parentheses `object.method()`.
- A method can access the object that it belongs to using the keyword `this`, which refers to the current object.
- An object can be modified by adding, updating, or deleting properties and methods. To add or update a property, use an assignment statement `object.property = value`. To delete a property, use the `delete` operator `delete object.property`.
- An object can be iterated over using a `for...in` loop, which loops through the keys of the object. To access the value of each property, use bracket notation `object[key]`.
- An object can be compared to another object using the `===` operator, which checks if they refer to the same object in memory. Two objects that have the same properties and values are not equal unless they are the same object.
- An object can be copied using the `Object.assign()` method, which takes a target object and one or more source objects as arguments and copies the properties and values from the source objects to the target object. The target object is returned and modified, while the source objects are not changed.