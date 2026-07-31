### Dynamic HTML in Web Page Designing

Dynamic HTML (DHTML) is a term that refers to the use of various web development technologies to create dynamic and interactive web pages. DHTML can work with HTML, JavaScript, XML, and CSS to create effects such as animation, interactivity, and responsiveness. DHTML is not a markup or programming language, but a combination of features that can be applied to HTML elements using the Document Object Model (DOM) and scripts.

The main components of DHTML are:

- HTML: The markup language that defines the structure and content of the web page.
- CSS: The style sheet language that defines the presentation and layout of the web page.
- JavaScript: The scripting language that enables the manipulation and interaction of the web page elements using the DOM.
- XML: The markup language that defines the data and structure of the web page, which can be loaded and parsed by JavaScript.

An example of a simple DHTML web page that changes the background color of the body element when a button is clicked is:

```html
<html>
<head>
  <style>
    body {
      background-color: white;
    }
  </style>
  <script>
    function changeColor() {
      var color = document.getElementById("color").value;
      document.body.style.backgroundColor = color;
    }
  </script>
</head>
<body>
  <h1>DHTML Example</h1>
  <p>Enter a color name or a hexadecimal code and click the button to change the background color.</p>
  <input type="text" id="color" value="red">
  <button onclick="changeColor()">Change Color</button>
</body>
</html>
```