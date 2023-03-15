Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is a possible answer:

### Write an HTML program to design an entry form of student details and send it to store at database server like SQL, Oracle or MS Access for the notes of the Unit 1 - Develop static web pages using HTML in the subject of Web Technology Lab

- To design an entry form of student details, you need to use HTML elements such as `<form>`, `<input>`, `<label>`, `<select>`, `<option>`, `<button>`, etc. These elements allow you to create different kinds of input fields, such as text, password, email, number, radio, checkbox, dropdown, etc. You also need to use HTML attributes such as `name`, `value`, `type`, `id`, `class`, `required`, `placeholder`, etc. These attributes help you to specify the name, value, type, identifier, style, validation, and hint of each input field. You can also use CSS to style your form elements, such as changing the color, font, size, border, margin, padding, etc.   
- To send the form data to a database server, you need to use the `action` and `method` attributes of the `<form>` element. The `action` attribute specifies the URL of the server-side script that will handle the form data, such as `action="students.php"`. The `method` attribute specifies the HTTP method to use when sending the form data, such as `method="post"` or `method="get"`. The `post` method is preferred when sending sensitive or large data, while the `get` method is preferred when sending small or non-sensitive data. 
- To store the form data in a database server, you need to use a server-side scripting language, such as PHP, ASP.NET, Python, etc. These languages allow you to connect to a database server, such as SQL, Oracle, or MS Access, using various functions or libraries. You also need to create a database table that will store the student details, such as `CREATE TABLE students (id INT, name VARCHAR(50), email VARCHAR(50), course VARCHAR(50), gender VARCHAR(10), dob DATE)`. You then need to write a SQL query that will insert the form data into the database table, such as `INSERT INTO students (id, name, email, course, gender, dob) VALUES (?, ?, ?, ?, ?, ?)`. You also need to use prepared statements or parameterized queries to prevent SQL injection attacks. 

Here is an example of an HTML program that does the above tasks:

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        /* CSS code to style the form elements */
        form {
            width: 500px;
            margin: 0 auto;
            border: 1px solid black;
            padding: 20px;
        }

        label {
            display: block;
            margin-bottom: 10px;
        }

        input, select {
            width: 100%;
            height: 30px;
            font-size: 16px;
        }

        button {
            width: 100%;
            height: 40px;
            background-color: green;
            color: white;
            font-size: 20px;
        }
    </style>
</head>
<body>
    <form action="students.php" method="post">
        <label for="id">Student ID:</label>
        <input type="number" id="id" name="id" required>

        <label for="name">Student Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Student Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="course">Student Course:</label>
        <select id="course" name="course" required>
            <option value="">Select a course</option>
            <option value="Web Technology">Web Technology</option>
            <option value="Database Management">Database Management</option>
            <option value="Artificial Intelligence">Artificial Intelligence</option>
            <option value="Software Engineering">Software Engineering</option>
        </select>

        <label for="gender">Student Gender:</label>
        <input type="radio" id="male" name="gender" value="Male" required>