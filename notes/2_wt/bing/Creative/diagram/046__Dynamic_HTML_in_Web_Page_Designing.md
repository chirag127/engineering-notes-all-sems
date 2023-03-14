Dynamic HTML (DHTML) is a term that refers to the combination of HTML, CSS, JavaScript and other web technologies to create dynamic and interactive web pages. Dynamic HTML allows developers to manipulate the content, style and behavior of web pages without reloading the page. For example, DHTML can be used to create animations, menus, forms, pop-ups, etc.

### Dynamic HTML in Web Page Designing

The following diagram illustrates the basic architecture of a dynamic HTML web page:

```
+-----------------+        +-----------------+
|                 |        |                 |
|  Web Browser    |        |  Web Server     |
|                 |        |                 |
|  +-----------+  |        |  +-----------+  |
|  |           |  |        |  |           |  |
|  |  HTML     |  |        |  |  HTML     |  |
|  |           |  |        |  |           |  |
|  +-----------+  |        |  +-----------+  |
|  +-----------+  |        |  +-----------+  |
|  |           |  |        |  |           |  |
|  |  CSS      |  |        |  |  CSS      |  |
|  |           |  |        |  |           |  |
|  +-----------+  |        |  +-----------+  |
|  +-----------+  |        |  +-----------+  |
|  |           |  |        |  |           |  |
|  |  JS       |  |        |  |  JS       |  |
|  |           |  |        |  |           |  |
|  +-----------+  |        |  +-----------+  |
|  +-----------+  |        |  +-----------+  |
|  |           |  |        |  |           |  |
|  |  DOM      |  |        |  |  DOM      |  |
|  |           |  |        |  |           |  |
|  +-----------+  |        |  +-----------+  |
|                 |        |                 |
+-----------------+        +-----------------+
       |  ^                       |  ^
       |  |                       |  |
       v  |                       v  |
+-----------------+        +-----------------+
|                 |        |                 |
|  User Input    |        |  Server Output  |
|                 |        |                 |
+-----------------+        +-----------------+
```

The web browser is the client-side application that renders the web page and executes the JavaScript code. The web server is the server-side application that hosts the web page and responds to the requests from the browser. The HTML, CSS and JS files are the resources that define the structure, style and behavior of the web page. The DOM (Document Object Model) is the representation of the web page in the browser's memory that can be accessed and modified by JavaScript. The user input and the server output are the events that trigger the changes in the web page using DHTML.