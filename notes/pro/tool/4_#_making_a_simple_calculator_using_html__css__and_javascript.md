# making A Simple Calculator using HTML, CSS, and JavaScript

Sure, here's a sample code for a simple calculator website using HTML, CSS, and JavaScript:

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Calculator</title>
    <style>
      /* Add your CSS styles here */
      .calculator {
        width: 400px;
        margin: 0 auto;
        text-align: center;
        padding: 20px;
        background-color: #f2f2f2;
        border-radius: 10px;
      }
      .calculator input[type="text"] {
        width: 100%;
        padding: 10px;
        font-size: 18px;
        border: none;
        border-bottom: 2px solid #ccc;
        margin-bottom: 20px;
      }
      .calculator button {
        width: 100%;
        padding: 10px;
        font-size: 18px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 20px;
      }
    </style>
  </head>
  <body>
    <div class="calculator">
      <form>
        <input type="text" id="expression" disabled>
        <br>
        <button type="button" class="num" value="1">1</button>
        <button type="button" class="num" value="2">2</button>
        <button type="button" class="num" value="3">3</button>
        <button type="button" class="op" value="+">+</button>
        <br>
        <button type="button" class="num" value="4">4</button>
        <button type="button" class="num" value="5">5</button>
        <button type="button" class="num" value="6">6</button>
        <button type="button" class="op" value="-">-</button>
        <br>
        <button type="button" class="num" value="7">7</button>
        <button type="button" class="num" value="8">8</button>
        <button type="button" class="num" value="9">9</button>
        <button type="button" class="op" value="*">x</button>
        <br>
        <button type="button" class="clear" value="clear">C</button>
        <button type="button" class="num" value="0">0</button>
        <button type="button" class="eval" value="=">=</button>
        <button type="button" class="op" value="/">÷</button>
      </form>
    </div>
    <script>
      // Add your JavaScript code here
      const expression = document.getElementById("expression");
      const buttons = document.querySelectorAll("button");
      buttons.forEach(function(button) {
        button.addEventListener("click", function() {
          if (button.classList.contains("num")) {
            expression.value += button.value;
          } else if (button.classList.contains("op")) {
            expression.value += " " + button.value + " ";
          } else if (button.classList.contains("clear")) {
            expression.value = "";
          } else if (button.classList.contains("eval")) {
            try {
              expression.value = eval(expression.value);
            } catch (error) {
              expression.value = "Error";
            }
          }
        });
      });
    </script>
  </body>
</html>
```

This code creates a simple calculator with buttons for numbers, basic arithmetic operations, a clear button, and an equal button. The JavaScript code listens for button clicks and updates the expression in the input field accordingly. The CSS styles the calculator to look professional and beautiful.
