#### Documents in JavaScript

- A document in JavaScript is an object that represents the HTML or XML content of a web page.
- A document object has properties and methods that allow access and manipulation of the page elements, such as text, images, forms, links, etc.
- A document object is created by the browser when a web page is loaded, and can be accessed by the global variable `document` in JavaScript code.
- A document object is part of the Document Object Model (DOM), which is a standard interface for representing and interacting with web documents.
- Some of the common properties and methods of a document object are:

  - `document.documentElement`: returns the root element of the document, usually the `<html>` element.
  - `document.head`: returns the `<head>` element of the document.
  - `document.body`: returns the `<body>` element of the document.
  - `document.title`: returns or sets the title of the document, which is the content of the `<title>` element.
  - `document.URL`: returns the URL of the document.
  - `document.getElementById(id)`: returns the element with the specified id attribute, or null if not found.
  - `document.getElementsByClassName(className)`: returns a collection of elements with the specified class attribute, or an empty collection if not found.
  - `document.getElementsByTagName(tagName)`: returns a collection of elements with the specified tag name, or an empty collection if not found.
  - `document.querySelector(selector)`: returns the first element that matches the specified CSS selector, or null if not found.
  - `document.querySelectorAll(selector)`: returns a collection of elements that match the specified CSS selector, or an empty collection if not found.
  - `document.createElement(tagName)`: creates and returns a new element with the specified tag name.
  - `document.createTextNode(data)`: creates and returns a new text node with the specified data.
  - `document.write(html)`: writes the specified HTML string to the document.
  - `document.close()`: closes the document after writing.

- A document object can also fire events, such as `load`, `unload`, `click`, `keydown`, etc., that can be handled by event listeners.
- A document object can also be modified by using methods such as `appendChild()`, `insertBefore()`, `removeChild()`, `replaceChild()`, `setAttribute()`, `removeAttribute()`, etc., that change the structure or attributes of the document elements.

- A mnemonic to remember some of the document properties and methods is:

  - **D**ocument **U**RL **T**itle **H**ead **B**ody **E**lement
  - **D**ocument **G**et **E**lement **B**y **I**d **C**lass **T**ag **Q**uery
  - **D**ocument **C**reate **E**lement **T**ext **N**ode
  - **D**ocument **W**rite **C**lose

- An example of using the document object in JavaScript is:

```javascript
// Get the element with id="demo" and change its text content
var demo = document.getElementById("demo");
demo.textContent = "Hello, world!";

// Create a new paragraph element and append it to the body
var p = document.createElement("p");
p.textContent = "This is a new paragraph.";
document.body.appendChild(p);

// Add an event listener to the document that logs the key pressed
document.addEventListener("keydown", function(event) {
  console.log("You pressed: " + event.key);
});
```