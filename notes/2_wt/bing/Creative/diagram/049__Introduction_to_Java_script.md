#### Introduction to JavaScript

JavaScript is a scripting language that is used to create and manage dynamic web pages, basically anything that moves on your screen without requiring you to refresh your browser. It can be anything from animated graphics to an automatically generated Facebook timeline.

JavaScript was initially created to “make web pages alive”. The programs in this language are called scripts. They can be written right in a web page’s HTML and run automatically as the page loads. Scripts are provided and executed as plain text. They don’t need special preparation or compilation to run.

JavaScript is a cross-platform, object-oriented scripting language used to make webpages interactive (e.g., having complex animations, clickable buttons, popup menus, etc.). There are also more advanced server side versions of JavaScript such as Node.js, which allow you to add more functionality to a website than downloading files (such as realtime collaboration between multiple computers).

JavaScript contains a standard library of objects, such as Array, Date, and Math, and a core set of language elements such as operators, control structures, and statements. Core JavaScript can be extended for a variety of purposes by supplementing it with additional objects; for example:

- Client-side JavaScript extends the core language by supplying objects to control a browser and its Document Object Model (DOM). For example, client-side extensions allow an application to place elements on an HTML form and respond to user events such as mouse clicks, form input, and page navigation.
- Server-side JavaScript extends the core language by supplying objects relevant to running JavaScript on a server. For example, server-side extensions allow an application to communicate with a database, provide continuity of information from one invocation to another of the application, or perform file manipulations on a server.

The following diagram illustrates the basic architecture of a web application that uses JavaScript on both the client and the server side:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Web Browser   |     |   Web Server    |     |   Database      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  HTML/CSS/JS    |     |  Node.js/JS     |     |  SQL/NoSQL      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  DOM/JS Engine  |     |  JS Engine      |     |  DB Engine      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Browser Engine |     |  Server Engine  |     |  Storage Engine |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

: https://javascript.info/intro
: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction
: https://www.simplilearn.com/tutorials/javascript-tutorial/introduction-to-javascript