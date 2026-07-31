#### Objects in JavaScript

An object in JavaScript is a collection of properties, where each property has a name and a value. Properties can be primitive values, other objects, or functions. Here is an example of creating an object in JavaScript:

```javascript
let person = {
    firstName: "John",
    lastName: "Doe",
    age: 25,
    greet: function() {
        console.log("Hello, my name is " + this.firstName + " " + this.lastName);
    }
};
```

In this example, we create an object called `person` with four properties: `firstName`, `lastName`, `age`, and `greet`. The `greet` property is a function that logs a greeting to the console using the `firstName` and `lastName` properties of the `person` object.

You can access the properties of an object using dot notation or bracket notation. Here is an example of accessing the `firstName` property of the `person` object using both notations:

```javascript
console.log(person.firstName); // Output: John
console.log(person["firstName"]); // Output: John
```

You can also add new properties to an object or modify existing properties. Here is an example of adding a new property called `email` to the `person` object and modifying the `age` property:

```javascript
person.email = "john.doe@example.com";
person["age"] = 26;
```

After adding the `email` property and modifying the `age` property, the `person` object now looks like this:

```javascript
{
    firstName: "John",
    lastName: "Doe",
    age: 26,
    email: "john.doe@example.com",
    greet: function() {
        console.log("Hello, my name is " + this.firstName + " " + this.lastName);
    }
}
```
