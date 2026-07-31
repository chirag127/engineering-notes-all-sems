# JS Popup Boxes

JavaScript provides three types of popup boxes: Alert box, Confirm box, and Prompt box.

1. **Alert Box:** An alert box is used to display a message to the user. It is often used to make sure that information comes through to the user. When an alert box pops up, the user will have to click "OK" to proceed.

```javascript
alert("This is an alert box!");
```

2. **Confirm Box:** A confirm box is used to verify or accept something. When a confirm box pops up, the user will have to click either "OK" or "Cancel" to proceed. If the user clicks "OK", the box returns true. If the user clicks "Cancel", the box returns false.

```javascript
var result = confirm("Do you want to continue?");
if (result == true) {
  alert("You pressed OK!");
} else {
  alert("You pressed Cancel!");
}
```

3. **Prompt Box:** A prompt box is used to prompt users to input a value before entering a page. When a prompt box pops up, the user will have to click either "OK" or "Cancel" to proceed after entering an input value. If the user clicks "OK" the box returns the input value. If the user clicks "Cancel" the box returns null.

```javascript
var name = prompt("Please enter your name", "Harry Potter");
if (name != null) {
  alert("Hello " + name + "! How are you today?");
}
```

These are the three types of popup boxes available in JavaScript. They can be used to interact with the user and provide information or receive input from the user.