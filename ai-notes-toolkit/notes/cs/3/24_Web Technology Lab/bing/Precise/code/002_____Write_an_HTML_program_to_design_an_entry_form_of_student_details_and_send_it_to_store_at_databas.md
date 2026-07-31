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

This HTML code creates a simple form with fields for the student's name, email, and phone number. When the form is submitted, the data is sent to a server-side script (in this case, `submit.php`) using the `POST` method. The server-side script can then process the data and store it in a database server such as SQL, Oracle, or MS Access.

Some key points to note:
- The `form` element is used to create the form and specifies the location of the server-side script that will process the form data (`action` attribute) and the method used to send the data (`method` attribute).
- The `label` element is used to provide a text description for each form control.
- The `input` element is used to create various form controls, such as text fields, email fields, and telephone fields. The `type` attribute specifies the type of form control to create, and the `name` attribute specifies the name of the form control (used when sending the data to the server).
- The `submit` input type creates a submit button that, when clicked, submits the form data to the server.

I hope this helps you understand how to write an HTML program to design an entry form for student details and send it to a database server. Let me know if you have any further questions.