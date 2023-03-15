#### Introduction to AJAX in JavaScript

AJAX stands for Asynchronous JavaScript and XML. It is a technique that allows you to send and receive data from a web server without reloading the web page. It uses a combination of the following technologies:

- JavaScript: to make the request and handle the response
- XMLHttpRequest: a browser object that can communicate with the server
- DOM: to manipulate the HTML elements on the page
- XML, JSON, or plain text: to format the data that is exchanged

A typical AJAX process involves the following steps:

1. The user interacts with the web page, such as clicking a button or entering some input.
2. The JavaScript code creates an XMLHttpRequest object and sends a request to the server, passing some parameters if needed.
3. The server processes the request and sends back a response, usually in XML, JSON, or plain text format.
4. The JavaScript code receives the response and updates the web page accordingly, using the DOM methods.

The following diagram illustrates the AJAX process:

```
+-----------------+               +-----------------+
|                 |               |                 |
|    Web Page     |               |    Web Server   |
|                 |               |                 |
+-----------------+               +-----------------+
       |   |                           |   |
       |   |  User interaction        |   |
       |   +------------------------->|   |
       |                               |   |
       |  XMLHttpRequest object       |   |
       |  Request                     |   |
       +------------------------------>|   |
       |                               |   |
       |                               |   |
       |                               |   |  Process request
       |                               |   |  Response
       |                               |   +------------------------->|
       |                               |   |                          |
       |  XMLHttpRequest object       |   |                          |
       |  Response                    |   |                          |
       |<------------------------------+   |                          |
       |                               |   |                          |
       |  JavaScript code              |   |                          |
       |  Update web page             |   |                          |
       +------------------------------>|   |                          |
       |                               |   |                          |
       |   |                           |   |                          |
       |   |  User interaction        |   |                          |
       |   +------------------------->|   |                          |
       |                               |   |                          |
       |                               |   |                          |
       |                               |   |                          |
       |                               |   |                          |
       |                               |   |                          |
       |                               |   |                          |
       |                               |   |                          |
       |                               |   |                          |
       |                               |   |                          |
       |                               |   |                          |
       |                               |   |                          |
       |                               |   |                          |
       +-----------------+               +-----------------+
```