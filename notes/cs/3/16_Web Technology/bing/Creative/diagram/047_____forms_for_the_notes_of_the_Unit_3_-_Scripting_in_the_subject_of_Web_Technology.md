# Forms

Forms are a part of an HTML document containing HTML form elements such as input, select, checkboxes, radio, buttons, etc. Users typically complete a form by entering texts, selecting options, and modifying form elements before submitting the form for processing.

Forms are a very powerful tool for interacting with users — most commonly they are used for collecting data from users, or allowing them to control a user interface.

Some examples of web forms are:

- Registration forms
- Login forms
- Contact forms
- Order forms
- Feedback forms
- Survey forms
- Quiz forms

## How to create a web form

To create a web form, we need to use the `<form>` element, which defines the form itself, and various input elements, which define the different types of user input. The `<form>` element has two important attributes: `action` and `method`.

- The `action` attribute specifies the URL of the server-side script that will process the form data.
- The `method` attribute specifies the HTTP method to use when sending the form data. The most common methods are `GET` and `POST`.

For example, the following HTML code creates a simple web form that asks for the user's name and email address, and sends the data to a server-side script called `process.php` using the `POST` method.

```html
<form action="process.php" method="POST">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" required>
  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required>
  <button type="submit">Submit</button>
</form>
```

## How to style a web form

To style a web form, we can use CSS properties and selectors to apply different styles to the form elements. For example, we can use the `:focus` pseudo-class to change the appearance of an input element when it is focused by the user.

```css
input {
  border: 1px solid black;
  padding: 10px;
}

input:focus {
  border: 2px solid blue;
  outline: none;
}
```

We can also use CSS grid or flexbox to layout the form elements in a responsive and flexible way. For example, we can use CSS grid to create a two-column layout for the form labels and inputs.

```css
form {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 10px;
}

label {
  text-align: right;
}

button {
  grid-column: span 2;
  justify-self: center;
}
```

## How to validate a web form

To validate a web form, we can use HTML attributes, JavaScript, or server-side scripts to check if the user input is valid and meets the requirements. For example, we can use the `required` attribute to make an input element mandatory, or the `pattern` attribute to specify a regular expression that the input value must match.

```html
<form action="process.php" method="POST">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" required>
  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required>
  <label for="phone">Phone:</label>
  <input type="tel" id="phone" name="phone" pattern="[0-9]{10}">
  <button type="submit">Submit</button>
</form>
```

We can also use JavaScript to add event listeners to the form elements and perform custom validation logic. For example, we can use the `addEventListener` method to attach a `submit` event handler to the form, and use the `preventDefault` method to stop the form from submitting if the validation fails.

```javascript
// Get the form element
var form = document.getElementById("form");

// Add a submit event listener to the form
form.addEventListener("submit", function(event) {
  // Get the input elements
  var name = document.getElementById("name");
  var email = document.getElementById("email");
  var phone = document.getElementById("phone");

  // Check if the name input is empty
  if (name.value === "") {
    // Display an error message
    alert("Please enter your name");
    // Stop the form from submitting
    event.preventDefault();
  }

  // Check if the email input is valid

```
