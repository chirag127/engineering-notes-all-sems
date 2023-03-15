# JS Popup Boxes

- JS popup boxes are used to display information or get user input in a web page.
- There are three types of popup boxes in JS: alert, confirm, and prompt.
- Alert boxes are used to show a message and an OK button to the user. They are created with the `alert()` function, which takes a string argument as the message to display. For example:

```js
alert("Hello, world!");
```

- Confirm boxes are used to show a message and an OK and a Cancel button to the user. They are created with the `confirm()` function, which takes a string argument as the message to display. The function returns a boolean value, true if the user clicks OK and false if the user clicks Cancel. For example:

```js
var result = confirm("Are you sure?");
if (result) {
  // do something if OK
} else {
  // do something else if Cancel
}
```

- Prompt boxes are used to show a message and a text input field and an OK and a Cancel button to the user. They are created with the `prompt()` function, which takes two string arguments: the message to display and the default value for the input field. The function returns the value entered by the user, or null if the user clicks Cancel. For example:

```js
var name = prompt("What is your name?", "Anonymous");
if (name) {
  // do something with name
} else {
  // do something else if Cancel
}
```

- Popup boxes are modal, meaning they block the execution of the code until the user responds to them. They are also synchronous, meaning they return a value immediately after the user responds to them.
- Popup boxes are not recommended for modern web design, as they are intrusive and can be annoying for the user. They can also be disabled by the user in some browsers. It is better to use HTML elements or CSS styles to create custom dialogs or modals.