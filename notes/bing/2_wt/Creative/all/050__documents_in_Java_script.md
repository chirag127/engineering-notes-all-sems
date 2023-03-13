#### Documents in JavaScript

- A document in JavaScript is an object that represents the web page loaded in the browser and provides access to its content and functionality.
- A document is part of the Document Object Model (DOM), which is a tree-like structure of nodes that represent the elements, attributes, text, comments, etc. of the web page .
- A document object has many properties and methods that can be used to manipulate the DOM tree, such as `document.getElementById()`, `document.createElement()`, `document.body`, `document.title`, etc.
- A document object can be obtained by using the global variable `document` or by calling the `window.document` property, which refers to the same object.
- A document object can also be created by using the `document.implementation.createDocument()` method, which returns a new XML or HTML document.
- A document object can be used to perform various tasks, such as:
  - Getting and setting the content of elements, attributes, text, etc. by using methods like `document.querySelector()`, `document.getElementsByClassName()`, `document.setAttribute()`, `document.textContent`, etc.
  - Creating and deleting elements, attributes, text, etc. by using methods like `document.createElement()`, `document.createAttribute()`, `document.createTextNode()`, `document.removeChild()`, etc.
  - Modifying the style and layout of elements by using methods like `document.getElementById().style`, `document.getElementById().className`, `document.getElementById().offsetWidth`, etc.
  - Adding and removing event listeners to elements by using methods like `document.getElementById().addEventListener()`, `document.getElementById().removeEventListener()`, etc.
  - Loading and saving data from and to the web page by using methods like `document.cookie`, `document.location`, `document.write()`, `document.open()`, etc.
  - Validating and parsing the document by using methods like `document.doctype`, `document.documentElement`, `document.compatMode`, `document.querySelector()`, etc.

- A document object can be helpful to learn and read from for exams because it allows you to understand and manipulate the web page content and functionality using JavaScript.
- A possible mnemonic to remember some of the document methods is:

  - **G**et **E**lements **B**y **I**d, **C**lass, **N**ame, **T**ag, **S**elector: `document.getElementById()`, `document.getElementsByClassName()`, `document.getElementsByName()`, `document.getElementsByTagName()`, `document.querySelector()`.
  - **C**reate **E**lement, **A**ttribute, **T**ext: `document.createElement()`, `document.createAttribute()`, `document.createTextNode()`.
  - **R**emove **C**hild, **A**ttribute: `document.removeChild()`, `document.removeAttribute()`.
  - **A**dd **E**vent **L**istener, **R**emove **E**vent **L**istener: `document.addEventListener()`, `document.removeEventListener()`.
  - **W**rite, **O**pen, **C**ookie, **L**ocation: `document.write()`, `document.open()`, `document.cookie`, `document.location`.

- A possible ASCII diagram to illustrate the document object and the DOM tree is:

```
+-----------------+       +-----------------+
| window object   |       | document object |
|                 |       |                 |
| document        | ----> | doctype         |
|                 |       | documentElement |
|                 |       | body            |
|                 |       | title           |
|                 |       | cookie          |
|                 |       | location        |
+-----------------+       | ...             |
                          +-----------------+
                                 |
                                 |
                                 v
                          +-----------------+
                          | DOM tree        |
                          |                 |
                          | <html>          |
                          |   <head>        |
                          |     <title>     |
                          |     ...         |
                          |   </head>       |
                          |   <body>        |
                          |     <div>       |
                          |       <p>       |
                          |       ...       |
                          |     </div>      |
                          |     ...         |
                          |   </body>       |
                          | </html>         |
                          +-----------------+
```