#### Introduction to AJAX in JavaScript

AJAX stands for Asynchronous JavaScript and XML. It is a technique that allows you to send and receive data from a web server without reloading the web page. It uses a combination of the following technologies:

- JavaScript: to make the request and handle the response
- XMLHttpRequest: a browser object that can send and receive HTTP requests
- DOM: to manipulate the HTML elements on the web page
- XML, JSON, or plain text: to format the data that is exchanged between the client and the server

A typical AJAX workflow is as follows:

1. The user interacts with the web page, such as clicking a button or entering some input.
2. JavaScript creates an XMLHttpRequest object and sends an HTTP request to the server, passing some data if needed.
3. The server processes the request and sends back an HTTP response, containing some data if needed.
4. JavaScript receives the response and updates the web page accordingly, using the DOM.

A diagram of the AJAX workflow is shown below:

```
+-----------------+        +-----------------+
|                 |        |                 |
|     Browser     |        |     Server      |
|                 |        |                 |
+-----------------+        +-----------------+
       |   ^                     |   ^
       |   |                     |   |
       |   |                     |   |
       |   |                     |   |
       |   |                     |   |
       |   |                     |   |
       |   |                     |   |
       |   |                     |   |
       |   |                     |   |
       |   |                     |   |
       |   |                     |   |
       |   |                     |   |
       |   |                     |   |
       |   +---------------------+   |
       |       HTTP response         |
       |                             |
       +-----------------------------+
           HTTP request
```