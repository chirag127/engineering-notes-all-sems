Object models in web page designing are a way of representing the structure and content of a web document using objects, properties, methods, and events. Objects are the elements or components that make up a web page, such as the window, document, form, link, anchor, etc. Properties are the attributes or characteristics of the objects, such as the title, href, value, etc. Methods are the actions or functions that the objects can perform, such as open, close, submit, etc. Events are the occurrences or interactions that trigger the methods, such as click, load, change, etc.

One of the most common and widely used object models in web page designing is the Document Object Model (DOM), which is a standard interface for accessing and manipulating web documents. The DOM represents the web document as a tree of nodes, where each node is an object that corresponds to an HTML element, attribute, text, comment, etc. The DOM provides methods and properties for traversing and modifying the tree, as well as events for handling user input and other changes.

The following diagram illustrates the basic object model of a web page using the DOM:

### Object Models in Web Page Designing

```
+-----------------+
| Window Object   |<----------------+
|                 |                 |
| +-------------+ |                 |
| | Document    | |                 |
| | Object      | |                 |
| +-------------+ |                 |
|                 |                 |
+-----------------+                 |
                                   |
+-----------------+                 |
| Browser Window  |                 |
|                 |                 |
| +-------------+ |                 |
| | HTML        | |                 |
| | Document    | |                 |
| +-------------+ |                 |
|                 |                 |
+-----------------+                 |
                                   |
+-----------------+                 |
| HTML Document   |                 |
|                 |                 |
| +-------------+ |                 |
| | <html>      | |                 |
| | Element     | |                 |
| +-------------+ |                 |
|                 |                 |
+-----------------+                 |
                                   |
+-----------------+                 |
| <html> Element  |                 |
|                 |                 |
| +-------------+ |                 |
| | <head>      | |                 |
| | Element     | |                 |
| +-------------+ |                 |
|                 |                 |
| +-------------+ |                 |
| | <body>      | |                 |
| | Element     | |                 |
| +-------------+ |                 |
|                 |                 |
+-----------------+                 |
                                   |
+-----------------+                 |
| <head> Element  |                 |
|                 |                 |
| +-------------+ |                 |
| | <title>     | |                 |
| | Element     | |                 |
| +-------------+ |                 |
|                 |                 |
| +-------------+ |                 |
| | <link>      | |                 |
| | Element     | |                 |
| +-------------+ |                 |
|                 |                 |
| +-------------+ |                 |
| | <script>    | |                 |
| | Element     | |                 |
| +-------------+ |                 |
|                 |                 |
+-----------------+                 |
                                   |
+-----------------+                 |
| <body> Element  |                 |
|                 |                 |
| +-------------+ |                 |
| | <h1>        | |                 |
| | Element     | |                 |
| +-------------+ |                 |
|                 |                 |
| +-------------+ |                 |
| | <form>      | |                 |
| | Element     | |                 |
| +-------------+ |                 |
|                 |                 |
| +-------------+ |                 |
| | <p>         | |                 |
| | Element     | |                 |
| +-------------+ |                 |
|                 |                 |
+-----------------+                 |
                                   |
+-----------------+                 |
| <form> Element  |                 |
|                 |                 |
| +-------------+ |                 |
| | <input>     | |                 |
| | Element     | |                 |
| +-------------+ |                 |
|                 |                 |
| +-------------+ |                 |
| | <button>    | |                 |
| | Element     | |                 |
| +-------------+ |                 |
|                 |                 |
+-----------------+-----------------+
```