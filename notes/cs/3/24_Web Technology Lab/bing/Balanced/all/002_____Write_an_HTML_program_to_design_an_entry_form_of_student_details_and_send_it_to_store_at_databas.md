# HTML program to design an entry form of student details and send it to store at database server

- HTML stands for HyperText Markup Language, which is used to create web pages and display information on the web browser.
- HTML forms are used to collect user input and send it to a web server for processing or storing.
- HTML forms consist of one or more input elements, such as text fields, checkboxes, radio buttons, etc., that allow the user to enter or select data.
- HTML forms also have a submit button, which triggers the action of sending the form data to the web server.
- HTML forms use the `<form>` tag to define the form and its attributes, such as `action`, `method`, `enctype`, etc.
- The `action` attribute specifies the URL of the web server that will handle the form data.
- The `method` attribute specifies the HTTP method to use when sending the form data, such as `GET` or `POST`.
- The `enctype` attribute specifies the encoding type of the form data, such as `application/x-www-form-urlencoded` or `multipart/form-data`.
- The `<input>` tag is used to create different types of input elements, such as `text`, `password`, `email`, `number`, `checkbox`, `radio`, etc.
- The `<input>` tag has various attributes, such as `type`, `name`, `value`, `placeholder`, `required`, etc., that define the input element and its properties.
- The `type` attribute specifies the type of the input element, such as `text`, `password`, `email`, etc.
- The `name` attribute specifies the name of the input element, which is used to identify the form data on the web server.
- The `value` attribute specifies the default or initial value of the input element, which can be changed by the user.
- The `placeholder` attribute specifies a hint or a sample value for the input element, which is displayed when the input element is empty.
- The `required` attribute specifies that the input element must be filled in before submitting the form.
- The `<label>` tag is used to create a label for the input element, which helps the user to understand the purpose of the input element.
- The `<label>` tag has an attribute called `for`, which links the label to the input element by using the `id` attribute of the input element.
- The `<select>` tag is used to create a drop-down list of options for the user to choose from.
- The `<select>` tag has an attribute called `name`, which specifies the name of the input element on the web server.
- The `<option>` tag is used to create an option within the `<select>` tag, which has a `value` attribute that specifies the value of the option.
- The `<textarea>` tag is used to create a multi-line text input element, which allows the user to enter a large amount of text.
- The `<textarea>` tag has attributes such as `name`, `rows`, and `cols`, which specify the name, number of rows, and number of columns of the input element, respectively.
- The `<button>` tag is used to create a button element, which can perform various actions, such as submitting the form, resetting the form, or executing a script.
- The `<button>` tag has an attribute called `type`, which specifies the type of the button, such as `submit`, `reset`, or `button`.
- The `<button>` tag also has an attribute called `name`, which specifies the name of the button on the web server.
- The `<button>` tag can contain text or an image as its content, which is displayed on the button.

## Example of an HTML program to design an entry form of student details and send it to store at database server

```html
<html>
<head>
  <title>Student Entry Form</title>
</head>
<body>
  <h1>Student Entry Form</h1>
  <form action="https://example.com/student.php" method="POST" enctype="multipart/form-data">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" placeholder="Enter your name" required><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" placeholder="Enter your email" required><br>
    <label for="phone">Phone:</label>
    <input type="tel" id="phone" name="phone" placeholder="Enter your phone