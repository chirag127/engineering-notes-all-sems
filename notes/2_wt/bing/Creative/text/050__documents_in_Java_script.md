#### Documents in JavaScript

- A document in JavaScript is an object that represents the web page loaded in the browser and provides access to its content and functionality.
- The document object is the owner of all other objects in the web page and the entry point to the Document Object Model (DOM), which is a tree-like structure of nodes that represent the elements, attributes, and text of the document .
- The document object has various properties and methods that can be used to find, create, modify, or delete HTML elements, attributes, styles, events, and cookies .
- The document object also has information about the document's URL, title, encoding, last modified date, and other metadata .
- The document object can be accessed using the global variable `document` or as a property of the `window` object .
- The document object is defined by the HTML specification and extended by other specifications such as SVG and XML.
- The document object is not part of the core JavaScript language, but a web API that interacts with JavaScript.

Some examples of using the document object are:

- To get the title of the document: `document.title`
- To get the element with a specific id: `document.getElementById(id)`
- To get all the elements with a specific tag name: `document.getElementsByTagName(name)`
- To get all the elements with a specific class name: `document.getElementsByClassName(name)`
- To create a new element: `document.createElement(element)`
- To append a child element to a parent element: `parent.appendChild(child)`
- To set an attribute of an element: `element.setAttribute(attribute, value)`
- To change the inner HTML of an element: `element.innerHTML = newHtml`
- To add an event listener to an element: `element.addEventListener(event, function)`
- To write text to the document: `document.write(text)`
- To get or set the document's cookie: `document.cookie`