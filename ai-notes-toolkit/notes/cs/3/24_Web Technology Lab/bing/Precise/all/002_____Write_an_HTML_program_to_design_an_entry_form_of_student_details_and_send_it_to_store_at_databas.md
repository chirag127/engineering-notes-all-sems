# HTML Program to Design an Entry Form of Student Details

To design an entry form of student details and send it to store at a database server like SQL, Oracle or MS Access, you can use the following HTML code:

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
        <label for="address">Address:</label>
        <input type="text" id="address" name="address"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

This code creates a simple HTML form with fields for the student's name, email, phone, and address. The form data is sent to a server-side script (in this case, `submit.php`) when the user clicks the "Submit" button. The server-side script can then process the form data and store it in a database server like SQL, Oracle or MS Access.

It is important to note that the above code is only an example and may need to be modified to fit the specific requirements of the database server being used. Additionally, server-side scripting (such as PHP, ASP.NET, or JSP) is required to process the form data and interact with the database server.