### Introduction to AJAX

- AJAX stands for **Asynchronous JavaScript and XML**  .
- AJAX is not a programming language, but a technique that uses a combination of:
  - A browser built-in **XMLHttpRequest object** (to request data from a web server)  .
  - **JavaScript** and **HTML DOM** (to display or use the data)  .
- AJAX allows web pages to be updated **asynchronously** by exchanging data with a web server **behind the scenes**  .
- This means that it is possible to update parts of a web page, without reloading the whole page  .
- AJAX is commonly used in popular web applications like Google Maps, Gmail, Facebook, and Twitter .
- An example of AJAX is the Google Autocomplete feature, which offers keyword suggestions, helping users complete their search query when typing into the search bar  .
- The changes happen in real-time, but the web page remains the same  .
- The basic steps of using AJAX are:
  - Create an XMLHttpRequest object
  - Send a request to a server using the open() and send() methods
  - Receive a response from the server
  - Process the response and update the web page using JavaScript and HTML DOM
- The following code snippet shows a simple example of using AJAX to get the content of a file called "demo.txt" and display it in a <div> element with id="demo":

```javascript
// Create an XMLHttpRequest object
var xhttp = new XMLHttpRequest();

// Define a function to handle the response
xhttp.onreadystatechange = function() {
  // Check if the request is complete and successful
  if (this.readyState == 4 && this.status == 200) {
    // Get the response text
    var txt = this.responseText;
    // Display the response text in the <div> element
    document.getElementById("demo").innerHTML = txt;
  }
};

// Open a GET request to the file "demo.txt"
xhttp.open("GET", "demo.txt", true);

// Send the request
xhttp.send();
```