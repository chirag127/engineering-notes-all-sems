### JS Popup Boxes

JavaScript has several built-in functions that allow the developer to create popup boxes on a webpage. These popup boxes are used to display information, ask for user input, or confirm an action. Here are the three types of popup boxes in JavaScript:

#### Alert Box

The alert box is used to display a message to the user. It has only one button, which is the OK button. To create an alert box, use the `alert()` function. For example:

```
alert("Hello, World!");
```

#### Prompt Box

The prompt box is used to ask the user to enter some input. It has two buttons - OK and Cancel. To create a prompt box, use the `prompt()` function. For example:

```
var name = prompt("Please enter your name:");
```

The `prompt()` function returns the value entered by the user, or null if the user clicked Cancel.

#### Confirm Box

The confirm box is used to ask the user to confirm an action. It has two buttons - OK and Cancel. To create a confirm box, use the `confirm()` function. For example:

```
var result = confirm("Are you sure you want to delete this item?");
```

The `confirm()` function returns true if the user clicked OK, and false if the user clicked Cancel.

#### Styling Popup Boxes

Popup boxes can be styled using CSS. The class names for the alert, prompt, and confirm boxes are `alert`, `prompt`, and `confirm`, respectively. For example, to change the background color of the alert box, use the following CSS:

```
.alert {
    background-color: yellow;
}
```

#### Conclusion

Popup boxes are a useful feature in JavaScript that allow developers to display information, ask for user input, or confirm an action. By using the built-in functions `alert()`, `prompt()`, and `confirm()`, developers can easily create popup boxes on a webpage. With CSS, the appearance of these popup boxes can be customized to fit the design of the webpage.