### Java Script Loops

- Loops are used to execute a block of code repeatedly until a certain condition is met.
- JavaScript supports the following types of loops:
  - `for` loop: executes a block of code a specified number of times, based on a counter variable.
  - `while` loop: executes a block of code while a specified condition is true.
  - `do...while` loop: executes a block of code once, and then repeats it while a specified condition is true.
  - `for...in` loop: iterates over the properties of an object, in an arbitrary order.
  - `for...of` loop: iterates over the values of an iterable object, such as an array or a string.
- The syntax of a `for` loop is:

```javascript
for (initialization; condition; increment) {
  // code block to be executed
}
```

- The syntax of a `while` loop is:

```javascript
while (condition) {
  // code block to be executed
}
```

- The syntax of a `do...while` loop is:

```javascript
do {
  // code block to be executed
} while (condition);
```

- The syntax of a `for...in` loop is:

```javascript
for (variable in object) {
  // code block to be executed
}
```

- The syntax of a `for...of` loop is:

```javascript
for (variable of iterable) {
  // code block to be executed
}
```

- To break out of a loop, the `break` statement can be used.
- To skip the current iteration of a loop, the `continue` statement can be used.
- To label a loop, the `label` statement can be used, followed by a colon and the loop statement. The label can then be used with the `break` or `continue` statement to control the flow of the loop.
- Example of a `for` loop:

```javascript
// print the numbers from 1 to 10
for (let i = 1; i <= 10; i++) {
  console.log(i);
}
```

- Example of a `while` loop:

```javascript
// print the numbers from 1 to 10
let i = 1;
while (i <= 10) {
  console.log(i);
  i++;
}
```

- Example of a `do...while` loop:

```javascript
// print the numbers from 1 to 10
let i = 1;
do {
  console.log(i);
  i++;
} while (i <= 10);
```

- Example of a `for...in` loop:

```javascript
// print the properties and values of an object
let person = {name: "Alice", age: 25, occupation: "programmer"};
for (let prop in person) {
  console.log(prop + ": " + person[prop]);
}
```

- Example of a `for...of` loop:

```javascript
// print the elements of an array
let fruits = ["apple", "banana", "cherry"];
for (let fruit of fruits) {
  console.log(fruit);
}
```

- Example of a `break` statement:

```javascript
// print the numbers from 1 to 10, but stop at 5
for (let i = 1; i <= 10; i++) {
  if (i === 5) {
    break;
  }
  console.log(i);
}
```

- Example of a `continue` statement:

```javascript
// print the odd numbers from 1 to 10
for (let i = 1; i <= 10; i++) {
  if (i % 2 === 0) {
    continue;
  }
  console.log(i);
}
```

- Example of a `label` statement:

```javascript
// print the numbers from 1 to 10, but skip 5 and 6
outer: for (let i = 1; i <= 10; i++) {
  if (i === 5 || i === 6) {
    continue outer;
  }
  console.log(i);
}
```