Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on JS Popup Boxes for the Unit 4 - Introduction to Client Side Scripting in the subject of Web Designing.

# JS Popup Boxes

- JS popup boxes are used to display information or get user input in a web page.
- There are three types of popup boxes in JS: alert, confirm, and prompt.
- Alert boxes are used to show a message and an OK button. They are useful for displaying warnings or notifications to the user.
- Confirm boxes are used to show a message and an OK and a Cancel button. They are useful for getting the user's confirmation or consent before performing an action.
- Prompt boxes are used to show a message and an input field and an OK and a Cancel button. They are useful for getting the user's input or feedback.
- To create a popup box, we use the `window` object and its methods: `alert()`, `confirm()`, and `prompt()`.
- The `window` object represents the browser window and provides access to various properties and methods related to the web page.
- The syntax for creating a popup box is:

```js
window.method(message, default);
```

- The `method` can be `alert`, `confirm`, or `prompt`.
- The `message` is a string that will be displayed in the popup box.
- The `default` is an optional parameter that specifies the default value for the input field in the prompt box.
- The `alert()` method returns `undefined`.
- The `confirm()` method returns `true` if the user clicks OK and `false` if the user clicks Cancel.
- The `prompt()` method returns the user's input if the user clicks OK and `null` if the user clicks Cancel or closes the popup box.
- Here are some examples of using popup boxes in JS:

```js
// alert box
window.alert("Hello, world!");

// confirm box
var result = window.confirm("Do you want to continue?");
if (result) {
  // user clicked OK
  window.alert("You clicked OK.");
} else {
  // user clicked Cancel
  window.alert("You clicked Cancel.");
}

// prompt box
var name = window.prompt("What is your name?", "Anonymous");
if (name) {
  // user entered a name and clicked OK
  window.alert("Hello, " + name + "!");
} else {
  // user clicked Cancel or closed the popup box
  window.alert("You did not enter a name.");
}
```