### Write an HTML program to design an entry form of student details and send it to store at database server like SQL, Oracle or MS Access for the notes of the Unit 1 - Develop static web pages using HTML in the subject of Web Technology Lab

Here is an example of an HTML program that can be used to design an entry form for student details and send it to a database server:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Student Details Form</title>
</head>
<body>
    <h1>Student Details Form</h1>
    <form action="submit.php" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="phone">Phone:</label>
        <input type="tel" id="phone" name="phone"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

This HTML code creates a form with three fields: `Name`, `Email`, and `Phone`. The form data is sent to a server-side script `submit.php` when the user clicks the `Submit` button. The `submit.php` script can then process the form data and store it in a database server such as SQL, Oracle, or MS Access.

It is important to note that the server-side script and database connection are not shown in this example. These would need to be implemented separately to complete the functionality of the form.