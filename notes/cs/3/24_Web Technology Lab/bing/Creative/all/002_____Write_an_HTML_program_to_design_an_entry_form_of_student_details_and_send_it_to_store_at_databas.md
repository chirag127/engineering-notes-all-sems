# Write an HTML program to design an entry form of student details and send it to store at database server like SQL, Oracle or MS Access

- An HTML form is a document that stores information of a user on a web server using interactive controls.
- An HTML form contains different kinds of information such as username, password, contact number, email id, etc.
- The HTML `<form>` element is used to create an HTML form for user input.
- The `<form>` element is a container for different types of input elements, such as: text fields, checkboxes, radio buttons, submit buttons, etc.
- To design an entry form of student details, we need to use the appropriate input elements and labels for each field.
- To send the form data to a database server, we need to specify the `action` and `method` attributes of the `<form>` element.
- The `action` attribute defines the URL of the server-side script that will process the form data.
- The `method` attribute defines the HTTP method to use when sending the form data.
- The most common methods are `GET` and `POST`.
- The `GET` method appends the form data to the URL in the query string.
- The `POST` method sends the form data as an HTTP request body.
- The choice of method depends on the type and size of the data, and the security and privacy requirements.
- For example, if the data is sensitive or large, the `POST` method is preferred.
- To store the form data in a database server like SQL, Oracle or MS Access, we need to use a server-side scripting language such as PHP, ASP, or JSP.
- The server-side script will receive the form data, connect to the database server, and execute the appropriate SQL queries to insert, update, or delete the data.
- The server-side script will also send a response back to the browser, such as a confirmation message or an error message.

Here is an example of an HTML program to design an entry form of student details and send it to store at a database server like SQL, Oracle or MS Access:

```html
<html>
<head>
  <title>Student Registration Form</title>
</head>
<body>
  <h1>Student Registration Form</h1>
  <form action="process.php" method="POST">
    <table>
      <tr>
        <td>First Name:</td>
        <td><input type="text" name="fname" required></td>
      </tr>
      <tr>
        <td>Last Name:</td>
        <td><input type="text" name="lname" required></td>
      </tr>
      <tr>
        <td>Email ID:</td>
        <td><input type="email" name="email" required></td>
      </tr>
      <tr>
        <td>Mobile Number:</td>
        <td><input type="tel" name="mobile" required></td>
      </tr>
      <tr>
        <td>Address:</td>
        <td><textarea name="address" rows="4" cols="20" required></textarea></td>
      </tr>
      <tr>
        <td>Hobbies:</td>
        <td>
          <input type="checkbox" name="hobbies[]" value="Reading">Reading
          <input type="checkbox" name="hobbies[]" value="Music">Music
          <input type="checkbox" name="hobbies[]" value="Sports">Sports
        </td>
      </tr>
      <tr>
        <td>Course:</td>
        <td>
          <select name="course" required>
            <option value="">Select Course</option>
            <option value="B.Tech">B.Tech</option>
            <option value="M.Tech">M.Tech</option>
            <option value="MBA">MBA</option>
            <option value="MCA">MCA</option>
          </select>
        </td>
      </tr>
      <tr>
        <td>Gender:</td>
        <td>
          <input type="radio" name="gender" value="Male" required>Male
          <input type="radio" name="gender" value="Female" required>Female
          <input type="radio" name

```
