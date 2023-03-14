A document in JavaScript is an object that represents the web page loaded in the browser. It provides access to the content and structure of the page, such as the elements, attributes, styles, and events. The document object is part of the Document Object Model (DOM), which is a tree-like representation of the HTML document.

A possible ASCII diagram for documents in JavaScript is:

#### documents in JavaScript
```
+-----------------+
| document object |
+-----------------+
| properties      |
| methods         |
+-----------------+
        |
        |
        v
+-----------------+
| documentElement |
+-----------------+
| <html> element  |
+-----------------+
        |
        |
        v
+-----------------+     +-----------------+
| head            |     | body            |
+-----------------+     +-----------------+
| <head> element  |     | <body> element  |
+-----------------+     +-----------------+
        |                       |
        |                       |
        v                       v
+-----------------+     +-----------------+
| title           |     | images          |
+-----------------+     +-----------------+
| <title> element |     | <img> elements  |
+-----------------+     +-----------------+
```