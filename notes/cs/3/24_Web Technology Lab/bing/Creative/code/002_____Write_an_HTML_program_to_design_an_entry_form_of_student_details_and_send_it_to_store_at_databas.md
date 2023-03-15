# HTML program to design an entry form of student details and send it to store at database server

- HTML stands for HyperText Markup Language, which is used to create web pages and display information on the web browser.
- HTML forms are used to collect user input and send it to a web server for processing.
- HTML forms consist of one or more input elements, such as text boxes, checkboxes, radio buttons, dropdown lists, etc., that allow the user to enter or select data.
- HTML forms also have a submit button, which triggers the action attribute of the form element, which specifies where and how the form data should be sent to the web server.
- To store the form data in a database server, such as SQL, Oracle or MS Access, the web server needs to have a script or program that can connect to the database and execute SQL queries to insert, update, delete or retrieve data.
- The script or program can be written in any server-side language, such as PHP, ASP.NET, Java, etc., and it should be specified in the action attribute of the form element.
- The method attribute of the form element determines how the form data is encoded and transmitted to the web server. The most common methods are GET and POST.
- The GET method appends the form data to the URL of the action attribute, and it is visible in the browser's address bar. The GET method is suitable for sending small and non-sensitive data, such as search queries.
- The POST method sends the form data in the body of the HTTP request, and it is not visible in the browser's address bar. The POST method is suitable for sending large and sensitive data, such as passwords, personal details, etc.

## Example of HTML program to design an entry form of student details and send it to store at database server

```html
<!-- This is the HTML form that collects the student details -->
<form action="student.php" method="POST">
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
        <input type="radio" name="gender" value="Other" required>Other
      </td>
    </tr>
    <tr>
      <td>Date of Birth:</td>
      <td><input type="date" name="dob" required></td>
    </tr>
    <tr>
      <td></td>
      <td><input type="submit" name="submit" value="Register"></td>
    </tr>
  </table>
</form>
```

```php
<?php
// This is