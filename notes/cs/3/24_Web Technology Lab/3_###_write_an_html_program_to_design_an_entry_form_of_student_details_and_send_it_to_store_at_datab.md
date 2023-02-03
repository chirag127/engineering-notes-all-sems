### Write an HTML program to design an entry form of student details and send it to store at database server like SQL, Oracle or MS Access for the notes of the Unit 1 - Develop static web pages using HTML in the subject of Web Technology Lab

HTML Program to Design an Entry Form for Student Details:

In Web Technology, HTML is used to create static web pages, including forms for collecting user data. The following is an example of an HTML program that can be used to design an entry form for student details and send it to a database server like SQL, Oracle, or MS Access:

```
<html>
<head>
  <title>Student Entry Form</title>
</head>
<body>
  <h1>Student Entry Form</h1>
  <form action="submit_student_details.php" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name"><br><br>
    <label for="roll_no">Roll No:</label>
    <input type="text" id="roll_no" name="roll_no"><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="phone">Phone:</label>
    <input type="text" id="phone" name="phone"><br><br>
    <input type="submit" value="Submit">
  </form>
</body>
</html>
```

In this example, the form is created using the `<form>` element, and the various fields for collecting student details are created using the `<input>` element. The `action` attribute of the `<form>` element specifies the URL of the script that will process the form data and store it in the database server. The `method` attribute specifies the HTTP method to be used to submit the form data, which is `post` in this example.

Each field in the form is labeled using the `<label>` element, and the various input types, such as text, email, and phone, are specified using the `type` attribute of the `<input>` element.

In conclusion, this HTML program can be used to design an entry form for student details and send it to a database server like SQL, Oracle, or MS Access. The form is created using the `<form>` element, and the various fields for collecting student details are created using the `<input>` element. The form data is submitted to the database server using the `post` method, and the URL of the script that will process the form data is specified using the `action` attribute of the `<form>` element.
