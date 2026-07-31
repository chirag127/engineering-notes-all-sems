### JS Popup Boxes

- JS popup boxes are used to display messages or notifications to the user in a separate window.
- JS popup boxes can also be used to get input from the user, such as a name or a password.
- JS popup boxes prevent the user from accessing other aspects of the program until the popup is closed, so they should not be overused.
- JS has three kinds of popup boxes: alert box, confirm box, and prompt box.

#### Alert Box

- An alert box is used to display a warning or an information message to the user.
- An alert box has an OK button that the user has to click to proceed.
- An alert box is created using the `window.alert()` method, which takes a string argument as the message to be displayed.
- Example:

```javascript
window.alert("This is an alert box!");
```

#### Confirm Box

- A confirm box is used to ask the user to confirm or cancel an action.
- A confirm box has two buttons: OK and Cancel.
- A confirm box is created using the `window.confirm()` method, which takes a string argument as the message to be displayed.
- The `window.confirm()` method returns a boolean value: true if the user clicks OK, and false if the user clicks Cancel.
- Example:

```javascript
var result = window.confirm("Do you want to continue?");
if (result == true) {
  // user clicked OK
} else {
  // user clicked Cancel
}
```

#### Prompt Box

- A prompt box is used to get input from the user, such as a name or a password.
- A prompt box has two buttons: OK and Cancel, and a text field where the user can enter the input.
- A prompt box is created using the `window.prompt()` method, which takes two string arguments: the message to be displayed, and the default value for the text field.
- The `window.prompt()` method returns the input entered by the user, or null if the user clicks Cancel.
- Example:

```javascript
var name = window.prompt("What is your name?", "Anonymous");
if (name != null) {
  // user entered a name
} else {
  // user clicked Cancel
}
```

#### Modal Box

- A modal box is a popup box that is displayed on top of the current page, and requires the user to interact with it before returning to the page.
- A modal box can be used to create custom popup forms, such as login forms, contact forms, or feedback forms.
- A modal box is created using HTML, CSS, and JS, and can be styled and customized according to the needs.
- A modal box typically has a close button or an overlay that the user can click to close the modal box.
- Example:

```html
<!-- Trigger/Open The Modal -->
<button id="myBtn">Open Modal</button>

<!-- The Modal -->
<div id="myModal" class="modal">

  <!-- Modal content -->
  <div class="modal-content">
    <span class="close">&times;</span>
    <p>Some text in the Modal..</p>
  </div>

</div>
```

```css
/* The Modal (background) */
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

/* Modal Content/Box */
.modal-content {
  background-color: #fefefe;
  margin: 15% auto; /* 15% from the top and centered */
  padding: 20px;
  border: 1px solid #888;
  width: 80%; /* Could be more or less, depending on screen size */
}

/* The Close Button */
.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
```

```javascript
// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that

```
