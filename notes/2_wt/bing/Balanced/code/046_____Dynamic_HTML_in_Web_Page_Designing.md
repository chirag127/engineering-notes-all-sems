### Dynamic HTML in Web Page Designing

Dynamic HTML (DHTML) is a term that refers to the use of various web development technologies to create dynamic and interactive web pages. DHTML can work with HTML, JavaScript, XML, and CSS to manipulate the HTML elements and their styles, events, and behaviors. DHTML can also use the Document Object Model (DOM) to access and modify any part of the web page.

One of the advantages of DHTML is that it can create effects and animations that would otherwise be impossible or require a lot of server-side processing. For example, DHTML can make text and images move, change colors, resize, or disappear based on user input or other conditions. DHTML can also create responsive web design, which means that the web page can automatically adjust to different screen sizes and devices.

To create a simple DHTML web page, you need to write HTML code to define the structure and content of the web page, CSS code to define the style and layout of the web page, and JavaScript code to define the functionality and interactivity of the web page. Here is an example of a DHTML web page that changes the background color of the body element randomly when the user clicks a button:

```html
<html>
<head>
<style>
  body {
    font-family: Arial, sans-serif;
    text-align: center;
  }

  button {
    margin: 20px;
    padding: 10px;
    font-size: 20px;
  }
</style>
<script>
  // This function generates a random hexadecimal color code
  function getRandomColor() {
    var letters = "0123456789ABCDEF";
    var color = "#";
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  // This function changes the background color of the body element
  function changeColor() {
    var body = document.getElementsByTagName("body")[0];
    var color = getRandomColor();
    body.style.backgroundColor = color;
  }
</script>
</head>
<body>
<h1>Dynamic HTML Example</h1>
<p>Click the button to change the background color of the page.</p>
<button onclick="changeColor()">Change Color</button>
</body>
</html>
```