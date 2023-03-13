Dynamic HTML (DHTML) is a term that describes the use of various web technologies to create dynamic and interactive web pages. DHTML can work with HTML, JavaScript, XML, and CSS to manipulate the HTML elements and their styles, events, and behaviors .

The basic architecture of a DHTML web page consists of four components:

- The HTML document, which contains the structure and content of the web page.
- The CSS style sheet, which defines the presentation and layout of the HTML elements.
- The JavaScript code, which provides the functionality and interactivity of the web page.
- The Document Object Model (DOM), which is a representation of the HTML document as a tree of objects that can be accessed and modified by JavaScript.

The following diagram illustrates the basic architecture of a DHTML web page:

```
+-----------------+    +-----------------+
| HTML document   |    | CSS style sheet |
|                 |    |                 |
| <html>          |    | body {          |
|   <head>        |    |   background:   |
|     <title>     |    |   linear-       |
|     </title>    |    |   gradient(...);|
|     <link>      |    | }               |
|     </link>     |    | h1 {            |
|   </head>       |    |   color: red;   |
|   <body>        |    | }               |
|     <h1>        |    | button {        |
|     </h1>       |    |   border: none; |
|     <button>    |    |   cursor:       |
|     </button>   |    |   pointer;      |
|   </body>       |    | }               |
| </html>         |    +-----------------+
+-----------------+              |
         |                       |
         |                       |
         +-----------------------+
         |
         v
+-----------------+    +-----------------+
| JavaScript code |    | Document Object |
|                 |    | Model (DOM)     |
| function change |    |                 |
| Title() {       |    | document        |
|   var title =   |    |   .querySelector|
|   document      |    |   ("h1");       |
|   .querySelector|    | title           |
|   ("h1");       |    |   .textContent  |
|   title         |    |   = "Hello";    |
|   .textContent  |    | title           |
|   = "Hello";    |    |   .style        |
| }               |    |   .color        |
|                 |    |   = "blue";     |
| var button =    |    | var button      |
| document        |    |   = document    |
|   .querySelector|    |   .querySelector |
|   ("button");   |    |   ("button");   |
| button          |    | button          |
|   .onclick      |    |   .onclick      |
|   = changeTitle;|    |   = changeTitle;|
+-----------------+    +-----------------+
```

: DHTML Tutorial - Javatpoint
: What is Dynamic HTML? - Code Institute Global
: How Dynamic HTML (DHTML) Is Used to Create Interactive Pages - ThoughtCo