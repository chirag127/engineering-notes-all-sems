### Forms in Web Page Designing

- Forms are used to collect user input on web pages. They can be used for various purposes, such as registration, login, feedback, surveys, etc.
- Forms consist of one or more input elements, such as text fields, checkboxes, radio buttons, dropdown lists, etc. Each input element has a name and a value that are sent to the server when the form is submitted.
- Forms also have a submit button, which triggers the form submission. The submit button can be an input element of type "submit" or a button element.
- Forms have two attributes: action and method. The action attribute specifies the URL of the server-side script that handles the form data. The method attribute specifies how the form data is sent to the server. The two common methods are GET and POST.
- GET method appends the form data to the URL as a query string. It is suitable for simple and short data, such as search queries. It has a limit on the length of the URL, which varies depending on the browser and the server. GET method is not secure, as the form data is visible in the URL and can be cached by the browser or the server.
- POST method sends the form data as a separate entity in the HTTP request body. It is suitable for large and complex data, such as file uploads. It has no limit on the size of the data, but it may take longer to process. POST method is more secure, as the form data is not visible in the URL and cannot be cached by the browser or the server.
- An example of a simple form using GET method is:

```html
<form action="search.php" method="get">
  <label for="query">Search:</label>
  <input type="text" id="query" name="query">
  <input type="submit" value="Search">
</form>
```

- An example of a simple form using POST method is:

```html
<form action="login.php" method="post">
  <label for="username">Username:</label>
  <input type="text" id="username" name="username">
  <label for="password">Password:</label>
  <input type="password" id="password" name="password">
  <input type="submit" value="Login">
</form>
```

- A mnemonic to remember the difference between GET and POST methods is: GET is for Getting data, POST is for Posting data.