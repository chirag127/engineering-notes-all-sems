### Dynamic HTML in Web Page Designing

Dynamic HTML, or DHTML, is a collection of technologies used together to create interactive and animated web sites by using a combination of a static markup language (such as HTML), a client-side scripting language (such as JavaScript), a presentation definition language (such as CSS), and the Document Object Model (DOM).

Here is an example of a simple DHTML code that changes the text color of a paragraph when the user clicks on a button:

```html
<!DOCTYPE html>
<html>
<head>
<style>
p {
  color: black;
}
</style>
</head>
<body>

<p id="myP">This is a paragraph.</p>

<button onclick="myFunction()">Click me</button>

<script>
function myFunction() {
  document.getElementById("myP").style.color = "red";
}
</script>

</body>
</html>
```

This code creates a paragraph with the text "This is a paragraph." and a button with the text "Click me". When the user clicks on the button, the JavaScript function `myFunction()` is called, which changes the color of the text in the paragraph to red by modifying the `style` property of the `p` element.
