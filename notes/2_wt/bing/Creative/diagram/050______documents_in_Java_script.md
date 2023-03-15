A document in JavaScript is an object that represents a web page and provides access to its content and functionality. A document is part of the Document Object Model (DOM), which is a tree-like structure of nodes that represent elements, attributes, text, comments, etc. The document object has many properties and methods that can be used to manipulate the DOM tree, such as document.getElementById, document.createElement, document.querySelector, etc.

Here is an example of a document object in JavaScript:

```javascript
// The document object is a global variable in the browser
console.log(document); // Prints the document object

// The document object has a property called documentElement that refers to the root element of the document, usually the <html> element
console.log(document.documentElement); // Prints the <html> element

// The document object has a property called head that refers to the <head> element of the document
console.log(document.head); // Prints the <head> element

// The document object has a property called body that refers to the <body> element of the document
console.log(document.body); // Prints the <body> element

// The document object has a method called getElementById that returns the element with the specified id attribute, or null if not found
var element = document.getElementById("myDiv"); // Returns the element with id="myDiv" or null
console.log(element); // Prints the element or null

// The document object has a method called createElement that creates a new element with the specified tag name
var newElement = document.createElement("p"); // Creates a new <p> element
console.log(newElement); // Prints the <p> element

// The document object has a method called querySelector that returns the first element that matches the specified CSS selector, or null if not found
var anotherElement = document.querySelector(".myClass"); // Returns the first element with class="myClass" or null
console.log(anotherElement); // Prints the element or null
```

Here is a possible ASCII diagram for the document object in JavaScript:

```
+-----------------+
| document object |
+-----------------+
|                 |
| +---------------+-----------------+
| | documentElement                |
| +---------------+-----------------+
| |                               |
| | +-----------+ +-------------+ |
| | | head      | | body        | |
| | +-----------+ +-------------+ |
| | |           | |             | |
| | | +-------+ | | +---------+ | |
| | | | title | | | | myDiv   | | |
| | | +-------+ | | +---------+ | |
| | |           | |             | |
| | +-----------+ +-------------+ |
| |                               |
| +-------------------------------+
|                 |
| +---------------+-----------------+
| | getElementById                 |
| +---------------+-----------------+
| |                               |
| | +-----------------------------+
| | | Returns the element with the |
| | | specified id attribute, or  |
| | | null if not found           |
| | +-----------------------------+
| |                               |
| +-------------------------------+
|                 |
| +---------------+-----------------+
| | createElement                 |
| +---------------+-----------------+
| |                               |
| | +-----------------------------+
| | | Creates a new element with  |
| | | the specified tag name      |
| | +-----------------------------+
| |                               |
| +-------------------------------+
|                 |
| +---------------+-----------------+
| | querySelector                 |
| +---------------+-----------------+
| |                               |
| | +-----------------------------+
| | | Returns the first element   |
| | | that matches the specified  |
| | | CSS selector, or null if    |
| | | not found                   |
| | +-----------------------------+
| |                               |
| +-------------------------------+
|                 |
+-----------------+
```