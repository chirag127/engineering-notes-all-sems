Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here are the notes for Unit 3 - Scripting:

# Unit 3 - Scripting

Scripting is a technique of writing programs that are executed by an interpreter at runtime, rather than being compiled into machine code. Scripting languages are often used for web development, as they can interact with web browsers, servers, databases, and other web technologies. Some examples of scripting languages are JavaScript, PHP, Python, Ruby, and Perl.

## Learning Outcomes

By the end of this unit, you should be able to:

- Explain the difference between scripting and programming languages
- Identify the advantages and disadvantages of scripting languages
- Compare and contrast various scripting languages and their features
- Write basic scripts using JavaScript, PHP, Python, Ruby, and Perl
- Use scripting languages to create dynamic web pages and applications

## Topics

The following topics are covered in this unit:

- Introduction to scripting languages
- JavaScript
- PHP
- Python
- Ruby
- Perl

## Introduction to scripting languages

Scripting languages are high-level languages that are interpreted by another program, rather than compiled into machine code. They are often used for tasks that require user interaction, such as web development, automation, data analysis, and testing. Scripting languages have some common characteristics, such as:

- They are easy to learn and use, as they have simple syntax and semantics
- They are portable, as they can run on different platforms and environments
- They are flexible, as they can be embedded into other languages and applications
- They are dynamic, as they can change their behavior and data types at runtime
- They are expressive, as they can perform complex operations with less code

However, scripting languages also have some drawbacks, such as:

- They are slower, as they have to be interpreted every time they run
- They are less secure, as they can be easily modified and accessed by unauthorized users
- They are less reliable, as they can have errors and bugs that are not detected until runtime
- They are less efficient, as they consume more memory and resources

## JavaScript

JavaScript is a scripting language that is widely used for web development, especially for creating dynamic and interactive web pages. It can run on both the client-side (in the web browser) and the server-side (using platforms such as Node.js). JavaScript has some features, such as:

- It is based on the ECMAScript standard, which defines the syntax and semantics of the language
- It is object-oriented, which means it can create and manipulate objects that have properties and methods
- It is event-driven, which means it can respond to user actions and other events that occur in the web page
- It is asynchronous, which means it can perform multiple tasks without blocking the execution flow
- It supports multiple paradigms, such as functional, imperative, and declarative programming

Some examples of JavaScript code are:

```javascript
// Declare a variable and assign a value
var name = "Sydney";

// Define a function and call it
function greet() {
  console.log("Hello, " + name);
}
greet();

// Create an object and access its properties and methods
var person = {
  name: "Sydney",
  age: 21,
  greet: function() {
    console.log("Hello, I am " + this.name);
  }
};
person.greet();

// Add an event listener to a button element
var button = document.getElementById("button");
button.addEventListener("click", function() {
  alert("You clicked the button!");
});
```

## PHP

PHP is a scripting language that is mainly used for server-side web development, as it can interact with web servers, databases, and other web technologies. It can also run on the command-line and as a standalone application. PHP has some features, such as:

- It is embedded into HTML, which means it can mix PHP code and HTML tags in the same file
- It is loosely typed, which means it does not require variable declarations or data type specifications
- It is procedural, which means it can execute a series of statements in a specific order
- It is also object-oriented, which means it can create and manipulate objects that have properties and methods
- It supports multiple paradigms, such as functional, imperative, and declarative programming

Some examples of PHP code are:

```php
<?php
// Declare a variable and assign a value
$name = "Sydney";

// Define a function and call it
function greet() {
  global $name; // Use the global keyword to access the variable outside the function
  echo "Hello, " . $name;
}
greet();

// Create an

```
