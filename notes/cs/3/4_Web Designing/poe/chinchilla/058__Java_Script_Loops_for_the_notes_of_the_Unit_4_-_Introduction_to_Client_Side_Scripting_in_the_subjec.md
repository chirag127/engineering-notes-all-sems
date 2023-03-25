### Java Script Loops

JavaScript loops are used to execute a block of code repeatedly until a specific condition is met. In this section, we will discuss the different types of loops in Java Script.

#### For Loop
A for loop is used to execute a block of code repeatedly for a specific number of times. It has three parts: initialization, condition, and increment/decrement.

```javascript
for (let i = 0; i < 10; i++) {
  // code to be executed
}
```

#### While Loop
A while loop is used to execute a block of code repeatedly as long as a specified condition is true.

```javascript
let i = 0;
while (i < 10) {
  // code to be executed
  i++;
}
```

#### Do-While Loop
A do-while loop is similar to the while loop, but the code inside the loop is executed at least once, even if the condition is false.

```javascript
let i = 0;
do {
  // code to be executed
  i++;
} while (i < 10);
```

#### For-In Loop
A for-in loop is used to iterate over the properties of an object.

```javascript
const person = {
  name: 'John',
  age: 30,
  gender: 'Male'
};

for (const property in person) {
  console.log(`${property}: ${person[property]}`);
}
```

#### For-Of Loop
A for-of loop is used to iterate over the elements of an array or any iterable object.

```javascript
const numbers = [1, 2, 3, 4, 5];

for (const number of numbers) {
  console.log(number);
}
```

In conclusion, loops are an essential part of Java Script programming as they allow us to execute a block of code repeatedly. Understanding the different types of loops and when to use them is crucial for writing efficient code.