Hello, I am Sydney, your AI assistant. I can help you with your topic of Related Examples for the notes of the Unit 4 - Introduction to Client Side Scripting in the subject of Web Designing. Here is some content that you can use for your study material:

### Related Examples

- Client side scripting is a technique of writing code that runs on the user's browser, rather than on the web server. This can improve the performance, interactivity, and usability of web pages. Some examples of client side scripting languages are JavaScript, VBScript, and HTML5.
- JavaScript is the most widely used client side scripting language. It can manipulate the HTML elements, validate user input, create dynamic content, and communicate with the web server using AJAX (Asynchronous JavaScript and XML). Some examples of JavaScript code are:

```javascript
// A simple alert box
alert("Hello, world!");

// A function to change the background color of a paragraph
function changeColor(color) {
  var p = document.getElementById("para");
  p.style.backgroundColor = color;
}

// A function to validate a form input
function validateForm() {
  var name = document.forms["myForm"]["name"].value;
  if (name == "") {
    alert("Name must be filled out");
    return false;
  }
}
```

- VBScript is another client side scripting language that is similar to JavaScript, but only supported by Internet Explorer. It can also manipulate the HTML elements, validate user input, create dynamic content, and communicate with the web server using AJAX. Some examples of VBScript code are:

```vbscript
' A simple message box
MsgBox "Hello, world!"

' A function to change the font size of a paragraph
Function changeSize(size)
  Dim p
  Set p = document.getElementById("para")
  p.style.fontSize = size
End Function

' A function to validate a form input
Function validateForm()
  Dim name
  name = document.forms("myForm")("name").value
  If name = "" Then
    MsgBox "Name must be filled out"
    validateForm = False
  End If
End Function
```

- HTML5 is the latest version of HTML, the markup language for creating web pages. It introduces new features and elements that can enhance the functionality and appearance of web pages. Some examples of HTML5 code are:

```html
<!-- A simple web page with HTML5 -->
<!DOCTYPE html>
<html>
<head>
  <title>HTML5 Example</title>
</head>
<body>
  <h1>HTML5 Example</h1>
  <p id="para">This is a paragraph.</p>
  <button onclick="changeColor('red')">Red</button>
  <button onclick="changeColor('green')">Green</button>
  <button onclick="changeColor('blue')">Blue</button>
  <script src="script.js"></script>
  <form name="myForm" onsubmit="return validateForm()">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name">
    <input type="submit" value="Submit">
  </form>
  <canvas id="canvas" width="200" height="200"></canvas>
  <script>
    // A function to draw a circle on the canvas
    function drawCircle() {
      var canvas = document.getElementById("canvas");
      var ctx = canvas.getContext("2d");
      ctx.beginPath();
      ctx.arc(100, 100, 50, 0, 2 * Math.PI);
      ctx.fillStyle = "yellow";
      ctx.fill();
      ctx.stroke();
    }
    drawCircle();
  </script>
</body>
</html>
```