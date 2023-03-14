#### Documents in JavaScript

- A document in JavaScript is an object that represents the web page loaded in the browser and allows access and manipulation of its content.
- A document is part of the Document Object Model (DOM), which is a tree-like structure of nodes that represent the elements, attributes, text, and comments in the HTML document.
- The document object is the root node of the DOM tree and has various properties and methods to interact with the web page.
- Some of the common properties of the document object are:

  - `document.title`: returns or sets the title of the document
  - `document.URL`: returns the complete URL of the document
  - `document.body`: returns the `<body>` element of the document
  - `document.cookie`: returns or sets the cookie of the document
  - `document.documentElement`: returns the `<html>` element of the document
  - `document.head`: returns the `<head>` element of the document
  - `document.readyState`: returns the loading status of the document
  - `document.referrer`: returns the URL of the document that linked to the current document

- Some of the common methods of the document object are:

  - `document.getElementById(id)`: returns the element with the specified id
  - `document.getElementsByTagName(name)`: returns a collection of elements with the specified tag name
  - `document.getElementsByClassName(name)`: returns a collection of elements with the specified class name
  - `document.createElement(element)`: creates a new element with the specified tag name
  - `document.createTextNode(text)`: creates a new text node with the specified text
  - `document.querySelector(selector)`: returns the first element that matches the specified CSS selector
  - `document.querySelectorAll(selector)`: returns a collection of elements that match the specified CSS selector
  - `document.appendChild(element)`: adds a new child element to the end of the document
  - `document.removeChild(element)`: removes a child element from the document
  - `document.replaceChild(new, old)`: replaces a child element with a new element
  - `document.write(text)`: writes text into the document
  - `document.addEventListener(event, function)`: attaches an event handler function to the document

- A document in JavaScript can also be used to access and manipulate various browser features, such as tabs, windows, history, stylesheets, etc. These are discussed further in the HTML DOM API documentation.
- A document in JavaScript can also be used to create and manipulate various types of documents, such as XML, SVG, etc. These are discussed further in the XML DOM and SVG DOM documentation.

- A mnemonic to remember some of the common properties and methods of the document object is:

  - **D**ocument **U**RL **B**ody **C**ookie **H**ead **R**eadyState **R**eferrer
  - **G**et **E**lement **B**y **I**d **T**ag **C**lass **N**ame
  - **C**reate **E**lement **T**ext **N**ode
  - **Q**uery **S**elector **A**ll
  - **A**ppend **R**emove **R**eplace **C**hild
  - **W**rite
  - **A**dd **E**vent **L**istener

- An example of using the document object in JavaScript is:

```javascript
// get the title of the document
var title = document.title;
console.log(title); // prints the title of the document

// change the title of the document
document.title = "New Title";
console.log(document.title); // prints "New Title"

// get the element with id="demo"
var demo = document.getElementById("demo");
console.log(demo); // prints the element object

// change the text content of the element
demo.textContent = "Hello World";
console.log(demo.textContent); // prints "Hello World"

// create a new paragraph element
var p = document.createElement("p");
console.log(p); // prints the element object

// create a new text node
var text = document.createTextNode("This is a new paragraph");
console.log(text); // prints the text node object

// append the text node to the paragraph element
p.appendChild(text);
console.log(p); // prints the element object with the text node as a child

// append the paragraph element to the document body
document.body.appendChild(p);
console.log(document.body); // prints the body element object with the paragraph element as a