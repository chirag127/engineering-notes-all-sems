## Unit 2 - Web Page Designing

In this unit, you will learn how to design and create web pages using HTML, CSS, and JavaScript. You will also learn about the basic principles of web design, such as layout, color, typography, and responsiveness.

HTML stands for HyperText Markup Language. It is the standard language for creating web pages and web applications. HTML describes the structure and content of a web page using tags and attributes.

CSS stands for Cascading Style Sheets. It is a language that describes how HTML elements are styled and arranged on a web page. CSS can control the appearance, layout, and behavior of web pages.

JavaScript is a scripting language that can add interactivity and functionality to web pages. JavaScript can manipulate HTML elements, respond to user events, and communicate with web servers.

To create a web page, you need to write HTML, CSS, and JavaScript code in a text editor and save it as a file with the .html extension. You can then open the file in a web browser to see the result.

Here is an example of a simple web page that displays a greeting message and the current date and time:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My Web Page</title>
  <style>
    /* CSS code goes here */
    body {
      font-family: Arial, sans-serif;
      background-color: lightblue;
    }

    h1 {
      color: white;
      text-align: center;
    }

    p {
      color: black;
      text-align: center;
    }
  </style>
</head>
<body>
  <h1>Welcome to my web page!</h1>
  <p id="date"></p>
  <script>
    // JavaScript code goes here
    // Get the element with id="date"
    var dateElement = document.getElementById("date");
    // Get the current date and time
    var date = new Date();
    // Format the date and time as a string
    var dateString = date.toLocaleString();
    // Display the date and time in the element
    dateElement.innerHTML = dateString;
  </script>
</body>
</html>
```