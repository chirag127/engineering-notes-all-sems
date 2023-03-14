#### Introduction to AJAX in JavaScript

- AJAX stands for **Asynchronous JavaScript and XML**  .
- AJAX is not a programming language, but a technique for creating dynamic and interactive web pages .
- AJAX uses a combination of a browser built-in **XMLHttpRequest object** (to request data from a web server) and **JavaScript and HTML DOM** (to display or use the data) .
- AJAX allows web pages to be updated **asynchronously** by exchanging data with a web server behind the scenes. This means that it is possible to update parts of a web page, without reloading the whole page .
- AJAX can use different formats to transport data, such as **XML, plain text, or JSON** .
- AJAX can improve the user experience and performance of web applications by reducing the bandwidth and latency.
- AJAX works by following these steps :
  1. An event occurs in a web page (the page is loaded, a button is clicked, etc.)
  2. An XMLHttpRequest object is created by JavaScript
  3. The XMLHttpRequest object sends a request to a web server
  4. The server processes the request
  5. The server sends a response back to the web page
  6. The response is read by JavaScript
  7. Proper action (like page update) is performed by JavaScript
- Modern browsers can use **Fetch API** instead of the XMLHttpRequest object. The Fetch API interface allows web browser to make HTTP requests to web servers in a simpler way.