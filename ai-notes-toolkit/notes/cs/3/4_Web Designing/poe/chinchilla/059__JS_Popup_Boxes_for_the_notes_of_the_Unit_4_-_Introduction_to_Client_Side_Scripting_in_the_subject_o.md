### JS Popup Boxes

JavaScript (JS) is a client-side scripting language that can be used to create dynamic web pages with interactive features. One such feature is the ability to display popup boxes, which are essentially dialog boxes that appear on top of the current page.

Popup boxes can be useful for displaying important messages, prompting users for input, or providing feedback on user actions. In this section, we will explore the different types of popup boxes that can be created using JavaScript.

#### Alert Box

The alert box is the simplest type of popup box and is used to display a message to the user. It contains a single button that the user can click to dismiss the box. To create an alert box, use the following code:

```javascript
alert("This is an alert box!");
```

#### Confirm Box

The confirm box is used to prompt the user for a yes or no answer. It contains two buttons, one for each option. To create a confirm box, use the following code:

```javascript
if (confirm("Do you want to proceed?")) {
   // User clicked "OK"
} else {
   // User clicked "Cancel"
}
```

#### Prompt Box

The prompt box is used to prompt the user for input. It contains a text field for the user to enter their response, as well as two buttons, one to submit the response and one to cancel. To create a prompt box, use the following code:

```javascript
var name = prompt("Please enter your name:");
if (name != null) {
   // User entered a name
} else {
   // User clicked "Cancel"
}
```

Popup boxes can be a useful way to add interactivity to your web pages. However, it is important to use them sparingly and only when necessary, as they can be intrusive and annoy users if overused.