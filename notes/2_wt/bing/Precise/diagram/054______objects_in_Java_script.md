#### Objects in JavaScript

An object in JavaScript is a collection of key-value pairs, where the keys are strings and the values can be any data type. Here is an example of an object representing a person:

```
let person = {
  firstName: "John",
  lastName: "Doe",
  age: 25,
  address: {
    street: "123 Main St",
    city: "Springfield",
    state: "IL",
    zip: "12345"
  }
};
```

In this example, the `person` object has four properties: `firstName`, `lastName`, `age`, and `address`. The `address` property is itself an object with four properties: `street`, `city`, `state`, and `zip`.

Here is an ASCII diagram representing the `person` object:

```
+-----------------+
|    person       |
| +-------------+ |
| | firstName:  | |
| | "John"      | |
| | lastName:   | |
| | "Doe"       | |
| | age:        | |
| | 25          | |
| | address:    | |
| | +---------+ | |
| | | street: | | |
| | | "123... | | |
| | | city:   | | |
| | | "Spr... | | |
| | | state:  | | |
| | | "IL"    | | |
| | | zip:    | | |
| | | "12345" | | |
| | +---------+ | |
| +-------------+ |
+-----------------+
```
