### JS Popup Boxes

- JS popup boxes are used to display messages or get user input in a web page.
- There are three types of popup boxes in JS: alert, confirm, and prompt.
- Alert boxes are used to show a message and an OK button. They are created with the `alert()` function, which takes a string argument as the message to display. For example:

```js
alert("Hello, world!");
```

- Confirm boxes are used to show a message and an OK and a Cancel button. They are created with the `confirm()` function, which takes a string argument as the message to display. The function returns a boolean value, true if the user clicks OK and false if the user clicks Cancel. For example:

```js
var result = confirm("Are you sure you want to delete this file?");
if (result) {
  // delete the file
} else {
  // cancel the operation
}
```

- Prompt boxes are used to show a message and a text input field and an OK and a Cancel button. They are created with the `prompt()` function, which takes two string arguments: the message to display and the default value for the input field. The function returns the value entered by the user, or null if the user clicks Cancel. For example:

```js
var name = prompt("What is your name?", "Anonymous");
if (name) {
  // greet the user
  alert("Hello, " + name + "!");
} else {
  // do nothing
}
```

- JS popup boxes are modal, meaning they block the execution of the code until the user responds to them. They are also synchronous, meaning they wait for the user's input before returning a value.
- JS popup boxes are not customizable in terms of appearance or behavior. They depend on the browser and the operating system settings. Therefore, they are not recommended for modern web design. Instead, it is better to use HTML, CSS, and JS to create custom dialogs or modals that are more user-friendly and responsive.