Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of JavaScript loops for the unit 4 - Introduction to Client Side Scripting in the subject of Web Designing.

# JavaScript Loops

- Loops are used to execute a block of code repeatedly until a certain condition is met.
- Loops can reduce the amount of code and make it easier to maintain and debug.
- JavaScript supports the following types of loops:

## for loop

- A for loop repeats a block of code for a specified number of times.
- A for loop has the following syntax:

```javascript
for (initialization; condition; update) {
  // code to be executed
}
```

- The initialization statement is executed only once before the loop starts. It is usually used to declare and initialize a loop counter variable.
- The condition statement is evaluated before each iteration of the loop. If the condition is true, the loop continues; if the condition is false, the loop ends.
- The update statement is executed after each iteration of the loop. It is usually used to increment or decrement the loop counter variable.
- Example:

```javascript
// print the numbers from 1 to 10
for (let i = 1; i <= 10; i++) {
  console.log(i);
}
```

## while loop

- A while loop repeats a block of code as long as a specified condition is true.
- A while loop has the following syntax:

```javascript
while (condition) {
  // code to be executed
}
```

- The condition statement is evaluated before each iteration of the loop. If the condition is true, the loop continues; if the condition is false, the loop ends.
- Example:

```javascript
// print the numbers from 1 to 10
let i = 1;
while (i <= 10) {
  console.log(i);
  i++;
}
```

## do...while loop

- A do...while loop is similar to a while loop, except that the block of code is executed at least once before the condition is checked.
- A do...while loop has the following syntax:

```javascript
do {
  // code to be executed
} while (condition);
```

- The condition statement is evaluated after each iteration of the loop. If the condition is true, the loop continues; if the condition is false, the loop ends.
- Example:

```javascript
// print the numbers from 1 to 10
let i = 1;
do {
  console.log(i);
  i++;
} while (i <= 10);
```

## break and continue statements

- The break statement can be used to terminate a loop prematurely, and jump to the next statement after the loop.
- The continue statement can be used to skip the current iteration of the loop, and jump to the next iteration.
- Example:

```javascript
// print the odd numbers from 1 to 10
for (let i = 1; i <= 10; i++) {
  if (i % 2 == 0) {
    continue; // skip even numbers
  }
  console.log(i);
  if (i == 7) {
    break; // stop the loop when i is 7
  }
}
```