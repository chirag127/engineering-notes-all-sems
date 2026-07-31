### Designing an Entry Form of Student Details and Storing It in a Database Server

In the Unit 1 of Web Technology Lab, you will learn how to develop static web pages using HTML. As a part of the course, you will also learn how to create an entry form for student details and store it in a database server like SQL, Oracle, or MS Access.

Here are the steps to design an entry form of student details using HTML and store it in a database server:

1. Create a new HTML file and name it as "student_details.html".
2. Add the basic HTML structure to the file using the <!DOCTYPE html> declaration and <html>, <head>, and <body> tags.
3. In the <head> section, add a <title> tag and give it a suitable title like "Student Details Entry Form".
4. Inside the <body> section, add a <form> tag and specify the action and method attributes. The action attribute should point to the server-side script that will handle the form data, while the method attribute should be set to "post" to prevent the data from being visible in the URL.
5. Within the <form> tag, add <input> tags for each field of the student details form like name, email, phone number, etc. Use appropriate input types like text, email, number, etc. and also add labels for each input field.
6. Add a submit button at the end of the form using the <input type="submit"> tag.
7. Save the HTML file and upload it to the server.

To store the form data in a database server, you need to create a server-side script that will handle the form data and store it in the database. Here are the steps to create a server-side script:

1. Choose a server-side scripting language like PHP, ASP.NET, or Python.
2. Create a new file and name it as "store_student_details.php" (for PHP) or "store_student_details.asp" (for ASP.NET).
3. In the server-side script, establish a connection to the database server using appropriate credentials.
4. Define variables to store the form data submitted by the user using the $_POST superglobal variable (for PHP) or the Request.Form collection (for ASP.NET).
5. Write SQL queries to insert the form data into the database table. Use appropriate SQL commands like INSERT INTO, SELECT, etc.
6. Execute the SQL queries and close the database connection.
7. Save the server-side script and upload it to the server.

To test the entry form, open the "student_details.html" file in a web browser and fill in some sample data. Click on the submit button to submit the form data. The server-side script will handle the form data and store it in the database. You can check the database to ensure that the data has been stored successfully.

In conclusion, designing an entry form of student details and storing it in a database server is an important aspect of web development using HTML. By following the above steps, you can easily create an entry form and store the data in a database server.