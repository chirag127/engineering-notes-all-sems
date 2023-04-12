Hello, I am Sydney, your AI assistant. I can help you with your notes on forms for the Unit 3 - Scripting in the subject of Web Technology. Here is the content in markdown format:

### Forms
- Forms are HTML elements that allow users to enter data and submit it to a web server.
- Forms consist of one or more input elements, such as text fields, checkboxes, radio buttons, drop-down lists, etc.
- Forms also have a submit button, which sends the data to the server when clicked.
- Forms use the `<form>` tag to define the start and end of the form element.
- Forms have two attributes: `action` and `method`.
  - The `action` attribute specifies the URL of the server-side script that will process the form data.
  - The `method` attribute specifies the HTTP method to use when sending the form data. The two common methods are `GET` and `POST`.
    - The `GET` method appends the form data to the URL as a query string, and is visible in the browser's address bar. The `GET` method is suitable for simple and short data, and for data that does not need to be secure.
    - The `POST` method sends the form data as part of the HTTP request body, and is not visible in the browser's address bar. The `POST` method is suitable for large and complex data, and for data that needs to be secure.
- An example of a simple form using the `GET` method is:

```html
<form action="https://example.com/script.php" method="GET">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name">
  <label for="email">Email:</label>
  <input type="email" id="email" name="email">
  <input type="submit" value="Submit">
</form>
```

- An example of a simple form using the `POST` method is:

```html
<form action="https://example.com/script.php" method="POST">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name">
  <label for="email">Email:</label>
  <input type="email" id="email" name="email">
  <input type="submit" value="Submit">
</form>
```

- The input elements have different attributes, such as `type`, `id`, `name`, `value`, `placeholder`, `required`, etc.
  - The `type` attribute specifies the type of input element, such as `text`, `email`, `password`, `number`, `checkbox`, `radio`, `submit`, etc.
  - The `id` attribute assigns a unique identifier to the input element, which can be used for styling or scripting purposes.
  - The `name` attribute assigns a name to the input element, which is used as the key when sending the form data to the server.
  - The `value` attribute specifies the initial or default value of the input element.
  - The `placeholder` attribute specifies a hint or example of what the user should enter in the input element.
  - The `required` attribute specifies that the input element must be filled in before submitting the form.
- An example of a form with different types of input elements is:

```html
<form action="https://example.com/script.php" method="POST">
  <label for="username">Username:</label>
  <input type="text" id="username" name="username" placeholder="Enter your username" required>
  <label for="password">Password:</label>
  <input type="password" id="password" name="password" placeholder="Enter your password" required>
  <label for="age">Age:</label>
  <input type="number" id="age" name="age" min="18" max="100" value="25">
  <label for="gender">Gender:</label>
  <input type="radio" id="male" name="gender" value="male" checked>
  <label for="male">Male</label>
  <input type="radio" id="female" name="gender" value="female">
  <label for="female">Female</label>
  <label for="hobbies">Hobbies:</label>
  <input type="checkbox" id="reading" name="hobbies" value="reading" checked>
  <label for="reading">Reading</label>
  <input type="checkbox" id="music" name="hobbies" value="music">
  <label for="music">Music</label>
  <input type

```
