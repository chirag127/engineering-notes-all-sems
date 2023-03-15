## Between 90-100%-----Print ‘A’

- This is a common programming task that involves using conditional statements to assign grades based on numerical scores.
- A conditional statement is a block of code that executes only if a certain condition is true.
- In most programming languages, the syntax for a conditional statement is:

```
if (condition) {
  // do something
} else {
  // do something else
}
```

- The condition is usually a logical expression that evaluates to either true or false, such as `score >= 90`.
- The `else` block is optional and executes only if the condition is false.
- To assign grades based on numerical scores, we can use a series of nested conditional statements, such as:

```
if (score >= 90) {
  // print 'A'
} else if (score >= 80) {
  // print 'B'
} else if (score >= 70) {
  // print 'C'
} else if (score >= 60) {
  // print 'D'
} else {
  // print 'F'
}
```

- This code checks the score from highest to lowest and prints the corresponding grade.
- The first condition, `score >= 90`, matches the requirement of printing 'A' for scores between 90 and 100.
- If the score is less than 90, the code moves on to the next condition, `score >= 80`, and so on, until it finds a matching condition or reaches the default case of printing 'F'.
- Note that the code assumes that the score is a valid number between 0 and 100. If the score is outside this range, the code may not work as expected.