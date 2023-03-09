 Here is the content in markdown format for the topic ### Variables in JS for the notes of the Unit 4 - Introduction to Client Side Scripting in the subject of Web Designing:

Variables in JavaScript:
- Variables are containers for storing data values.
- In JavaScript, variables are declared with the var, let or const keywords.
- var: The var keyword is function-scoped. Variables declared with var can be updated and re-declared within their scope.
- let: The let keyword is block-scoped. Variables declared with let cannot be updated and re-declared in the same scope.
- const: The const keyword is block-scoped and variables declared with const cannot be updated (they are read-only).

Declaring Variables:
- To declare a variable, you use this format:
`let/var/const variableName = value;`
- For example:
`let age = 30;`
`var name = "John";`
`const interestRate = 0.3;`

Naming Variables:
- Variable names must begin with a letter, underscore (_), or dollar sign ($).
- Variable names can only contain alphanumeric characters and underscores (A-z, 0-9, and _).
- Variable names are case sensitive (age, Age and AGE are three different variables).
- Use descriptive and readable names (age is better than a).

Variable Scope:
- The scope of a variable defines where it can be accessed in your code.
- var has function scope - it can be accessed anywhere within the function in which it is declared.
- let and const have block scope - they can only be accessed within the block they are declared.

Advantages of using variables:
- Variables make the code more readable and easier to maintain.
- Variables allow you to store values and use them throughout your code.
- Updating the value of a variable will update it throughout the code, making the process of changing values more efficient.

Markdown table for comparing var, let and const:

| Variable Type | Scope     | Can be re-declared | Can be updated |
|