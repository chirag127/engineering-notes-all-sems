#### Documents in JavaScript

Here is an example of how to create, access, and modify a document in JavaScript:

```javascript
// Create a new document
let doc = document.implementation.createHTMLDocument("New Document");

// Access the document's body
let body = doc.body;

// Create a new element
let p = doc.createElement("p");

// Set the element's text content
p.textContent = "This is some text.";

// Append the element to the body
body.appendChild(p);

// Modify the element's text content
p.textContent = "This is some updated text.";
```