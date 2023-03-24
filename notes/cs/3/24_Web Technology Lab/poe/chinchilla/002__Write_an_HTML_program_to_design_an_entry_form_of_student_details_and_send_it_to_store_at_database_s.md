### HTML Program for Designing an Entry Form for Student Details and Storing it in a Database Server

In web development, a common task is to collect user data and store it in a database for later use. This can be achieved through the use of forms and database management systems like SQL, Oracle, or MS Access. In this Unit 1 of the Web Technology Lab, we will learn how to create a static web page using HTML and design an entry form to collect student details and store it in a database server. Let's get started!

#### Step 1: Creating the HTML Form

1. Open a text editor and create a new HTML file.
2. Use the `<form>` tag to create a form element.
3. Inside the form element, create input fields using the `<input>` tag.
4. Use the `name` attribute to label each input field.
5. Use the `type` attribute to specify the input field type (e.g., text, email, password, etc.).
6. Use the `placeholder` attribute to provide a hint to the user about what information to enter in each field.
7. Use the `<label>` tag to create labels for each input field.

Example:

```html
<form>
  <label for="fullname">Full Name:</label>
  <input type="text" id="fullname" name="fullname" placeholder="Enter your full name"><br><br>

  <label for="email">Email:</label>
  <input type="email" id="email" name="email" placeholder="Enter your email"><br><br>

  <label for="password">Password:</label>
  <input type="password" id="password" name="password" placeholder="Enter your password"><br><br>

  <label for="dob">Date of Birth:</label>
  <input type="date" id="dob" name="dob"><br><br>

  <label for="gender">Gender:</label>
  <input type="radio" id="male" name="gender" value="male">
  <label for="male">Male</label>
  <input type="radio" id="female" name="gender" value="female">
  <label for="female">Female</label><br><br>

  <input type="submit" value="Submit">
</form>
```

#### Step 2: Connecting to a Database Server

1. Choose a database management system like SQL, Oracle, or MS Access.
2. Create a new database and a table to store the student details.
3. Use a server-side scripting language like PHP to connect to the database server and insert the form data into the table.

Example:

```php
<?php
// Connect to the database server
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

$conn = mysqli_connect($servername, $username, $password, $dbname);

// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

// Insert form data into the table
$sql = "INSERT INTO students (fullname, email, password, dob, gender)
VALUES ('".$_POST["fullname"]."', '".$_POST["email"]."', '".$_POST["password"]."', '".$_POST["dob"]."', '".$_POST["gender"]."')";

if (mysqli_query($conn, $sql)) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

mysqli_close($conn);
?>
```

#### Step 3: Testing the HTML Form

1. Save the HTML file and the PHP file with the database connection code in the same directory on your local machine.
2. Open the HTML file in a web browser and fill out the form with some sample student details.
3. Click the Submit button to send the form data to the PHP file.
4. Check the database table to make sure the form data was successfully inserted.

Congratulations! You have successfully designed an HTML entry form to collect student details and stored it in a database server using SQL, Oracle, or MS Access. Keep practicing and exploring new ways to create dynamic web pages with HTML and other web development technologies.