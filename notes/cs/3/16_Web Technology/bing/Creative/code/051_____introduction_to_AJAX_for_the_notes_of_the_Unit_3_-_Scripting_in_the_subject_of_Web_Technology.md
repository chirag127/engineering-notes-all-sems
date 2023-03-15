# Introduction to AJAX

- AJAX stands for **Asynchronous JavaScript and XML**  .
- AJAX is not a programming language, but a technique that uses a combination of existing web technologies .
- AJAX allows you to send and receive data **asynchronously** without reloading the web page .
- AJAX improves the user experience and performance of web applications by reducing the server's "think time" and the bandwidth consumption.
- AJAX uses the **XMLHttpRequest** object to communicate with the server using HTTP requests and responses  .
- AJAX can handle different types of data formats, such as XML, JSON, HTML, text, etc .
- AJAX follows a basic workflow as shown below:

![AJAX workflow](https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX/Getting_Started/ajax_diagram.png)

- The steps involved in the AJAX workflow are:
  - A user event triggers a JavaScript function to create an XMLHttpRequest object.
  - The XMLHttpRequest object sends an HTTP request to the server with optional data.
  - The server processes the request and sends back an HTTP response with the requested data.
  - The XMLHttpRequest object receives the response and passes it to a JavaScript callback function.
  - The callback function updates the web page with the new data.