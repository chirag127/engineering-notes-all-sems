#### Introduction to AJAX in JavaScript

AJAX stands for Asynchronous JavaScript and XML. It is a technique for creating fast and dynamic web pages without reloading the entire page. AJAX allows web pages to send and receive data from a server asynchronously, in the background, without interfering with the display and behavior of the existing page.

Here is an example of how to use AJAX in JavaScript to send a request to a server and receive a response:

```javascript
// Create a new XMLHttpRequest object
var xhr = new XMLHttpRequest();

// Open a new connection, using the GET request on the URL endpoint
xhr.open('GET', 'https://api.example.com/data', true);

// Set the request header
xhr.setRequestHeader('Content-Type', 'application/json');

// Send the request
xhr.send();

// This will be called after the response is received
xhr.onload = function() {
  if (xhr.status != 200) {
    // analyze HTTP response
    alert(`Error ${xhr.status}: ${xhr.statusText}`);
  } else {
    // parse JSON data
    let data = JSON.parse(xhr.response);
    // process the data
    // ...
  }
};

xhr.onerror = function() {
  alert("Request failed");
};
```