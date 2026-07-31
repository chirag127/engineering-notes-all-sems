

## Unit 1 - Develop static web pages using HTML

- HTML stands for HyperText Markup Language. It is the standard language for creating web pages and web applications.
- HTML consists of elements that define the structure and content of a web page. Elements are enclosed by tags, which are written in angle brackets (< and >).
- HTML elements can have attributes, which provide additional information or functionality to the elements. Attributes are written inside the start tag, after the element name, and consist of a name and a value, separated by an equal sign (=).
- HTML elements can be nested, which means that one element can contain another element inside it. The inner element is called the child element, and the outer element is called the parent element.
- HTML elements can be classified into two types: block-level elements and inline elements. Block-level elements create a new line and occupy the whole width of the page, while inline elements do not create a new line and only occupy the space needed for their content.
- Some common block-level elements are: `<div>`, `<p>`, `<h1>` to `<h6>`, `<ul>`, `<ol>`, `<li>`, `<table>`, `<tr>`, `<td>`, `<th>`, `<form>`, `<header>`, `<footer>`, `<section>`, `<article>`, `<nav>`, `<aside>`, etc.
- Some common inline elements are: `<span>`, `<a>`, `<img>`, `<input>`, `<button>`, `<label>`, `<strong>`, `<em>`, `<br>`, `<code>`, `<sub>`, `<sup>`, `<small>`, `<b>`, `<i>`, `<u>`, etc.
- HTML also has some special elements that do not have a closing tag, such as `<br>`, `<img>`, `<input>`, `<hr>`, `<meta>`, `<link>`, etc. These are called self-closing or void elements.
- HTML documents have a basic structure that consists of the following elements: `<!DOCTYPE html>`, `<html>`, `<head>`, `<title>`, `<body>`.
- The `<!DOCTYPE html>` declaration tells the browser that the document is an HTML5 document. It must be the first line of the document.
- The `<html>` element is the root element of the document. It contains all the other elements of the document. It can have a `lang` attribute that specifies the language of the document.
- The `<head>` element contains information about the document, such as the title, the character encoding, the style sheets, the scripts, the metadata, etc. It is not visible on the web page, but it is important for the browser and the search engines.
- The `<title>` element defines the title of the document, which is displayed on the browser tab or window. It must be inside the `<head>` element and it must have a text content.
- The `<body>` element contains the visible content of the document, such as text, images, links, forms, tables, etc. It is the main part of the web page that the user interacts with.
- HTML documents can be styled using CSS (Cascading Style Sheets), which is a language that defines how HTML elements should look and behave on the web page. CSS can be written inside the `<style>` element, inside the `<head>` element, or in a separate file that is linked to the HTML document using the `<link>` element.
- HTML documents can also have dynamic functionality using JavaScript, which is a scripting language that can manipulate the HTML elements and respond to user events. JavaScript can be written inside the `<script>` element, inside the `<head>` or the `<body>` element, or in a separate file that is linked to the HTML document using the `<script>` element.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a possible answer to your question:

### Write HTML/Java scripts to display your CV in navigator, your Institute website, Department Website and Tutorial website for specific subject for the notes of the Unit 1 - Develop static web pages using HTML in the subject of Web Technology Lab

- To display your CV in navigator, you need to create an HTML file that contains the structure and content of your resume, such as your name, contact details, education, skills, achievements, etc. You can use HTML tags such as `<h1>`, `<p>`, `<ul>`, `<li>`, `<a>`, etc. to format your text and create links. You can also use CSS to style your CV, such as changing the font, color, background, etc. You can use a `<style>` tag inside the `<head>` section of your HTML file to write your CSS code, or you can link to an external CSS file using a `<link>` tag. Here is an example of a simple HTML file that displays a CV:

```html
<html>
<head>
  <style>
    /* CSS code to style your CV */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }

    h1 {
      color: blue;
    }

    h2 {
      color: green;
    }

    ul {
      list-style-type: none;
    }

    li {
      margin: 10px;
    }

    a {
      text-decoration: none;
      color: black;
    }

    a:hover {
      color: red;
    }
  </style>
</head>
<body>
  <h1>John Smith</h1>
  <p>Email: <a href="mailto:john.smith@example.com">john.smith@example.com</a></p>
  <p>Phone: <a href="tel:+1234567890">+1234567890</a></p>
  <h2>Education</h2>
  <ul>
    <li>Bachelor of Science in Computer Science, ABC University, 2020 - 2024</li>
    <li>High School Diploma, XYZ School, 2018 - 2020</li>
  </ul>
  <h2>Skills</h2>
  <ul>
    <li>HTML, CSS, JavaScript</li>
    <li>Java, Python, C++</li>
    <li>MySQL, MongoDB, Firebase</li>
    <li>Git, GitHub, VS Code</li>
  </ul>
  <h2>Achievements</h2>
  <ul>
    <li>Won the first prize in the ABC Hackathon, 2021</li>
    <li>Published a research paper on Machine Learning in the Journal of Computer Science, 2020</li>
    <li>Completed the Google IT Support Professional Certificate, 2019</li>
  </ul>
</body>
</html>
```

- To display your Institute website, Department Website and Tutorial website for specific subject, you need to create separate HTML files for each of them, and link them together using `<a>` tags. You can use the same CSS code to style them, or you can create different CSS files for each of them. You can also use JavaScript to add interactivity and functionality to your websites, such as validating forms, creating animations, fetching data from APIs, etc. You can use a `<script>` tag inside the `<head>` or `<body>` section of your HTML file to write your JavaScript code, or you can link to an external JavaScript file using a `<script>` tag with a `src` attribute. Here is an example of a simple HTML file that displays a Home page having three links: About Us, Our Services and Contact Us:

```html
<html>
<head>
  <style>
    /* CSS code to style your website */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }

    h1 {
      color: blue;
    }

    ul {
      list-style-type: none;
    }

    li {
      margin: 10px;
    }

    a {
      text-decoration: none;
      color: black;
    }

    a:hover {
      color: red;
    }
  </style>
</head>
<body>
  <h1>Welcome to ABC Institute</h1>
  <p>We are a leading institute of higher education in the field of computer science

```




Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a possible answer to your question:

### Write an HTML program to design an entry form of student details and send it to store at database server like SQL, Oracle or MS Access for the notes of the Unit 1 - Develop static web pages using HTML in the subject of Web Technology Lab

- To design an entry form of student details, you need to use HTML elements such as `<form>`, `<input>`, `<label>`, `<select>`, `<option>`, `<button>`, etc. You can also use CSS to style the form elements and layout  .
- To send the form data to a database server, you need to specify the `action` and `method` attributes of the `<form>` element. The `action` attribute defines the URL where the form data will be sent, and the `method` attribute defines the HTTP request method to use, such as `GET` or `POST`.
- To store the form data in a database server, you need to write a server-side script that can handle the form data and execute SQL queries to insert, update, delete, or retrieve data from the database. You can use any programming language that can communicate with the database server, such as PHP, ASP.NET, Python, etc .
- Here is an example of an HTML program that creates a simple entry form of student details and sends it to a PHP script that stores the data in a MySQL database:

```html
<html>
<head>
    <style>
        /* CSS code to style the form elements and layout */
        form {
            width: 400px;
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
            box-sizing: border-box;
        }

        button {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <form action="save_student.php" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone:</label>
        <input type="tel" id="phone" name="phone" required>

        <label for="course">Course:</label>
        <select id="course" name="course" required>
            <option value="">Select a course</option>
            <option value="Web Technology">Web Technology</option>
            <option value="Database Management">Database Management</option>
            <option value="Software Engineering">Software Engineering</option>
        </select>

        <label for="gender">Gender:</label>
        <input type="radio" id="male" name="gender" value="Male" required>
        <label for="male">Male</label>
        <input type="radio" id="female" name="gender" value="Female" required>
        <label for="female">Female</label>

        <label for="dob">Date of Birth:</label>
        <input type="date" id="dob" name="dob" required>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

- Here is an example of a PHP script that receives the form data and stores it in a MySQL database:

```php
<?php
// Connect to the database server
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "student_db";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Get the form data
$name = $_POST["name"];
$email = $_POST["email"];
$phone = $_POST["phone"];
$course = $_POST["course"];
$gender = $_POST["gender"];
$dob = $_POST["dob"];

// Prepare and execute the SQL query to insert the data
$sql = "INSERT INTO student (name, email, phone, course, gender, dob) VALUES (?, ?, ?, ?, ?, ?)";
$stmt = $conn

```




## Unit 2 - Develop Java programs for window/web-based applications

- In this unit, you will learn how to create graphical user interfaces (GUIs) and web applications using Java.
- GUIs are programs that allow users to interact with the application through graphical elements such as buttons, menus, text fields, etc.
- Web applications are programs that run on a web server and can be accessed by users through a web browser.
- To create GUIs in Java, you will need to use the Swing and AWT libraries, which provide various components and layouts for designing GUIs.
- To create web applications in Java, you will need to use the Servlet and JSP technologies, which enable you to write dynamic web pages that can process user requests and generate responses.
- You will also learn how to use databases and JDBC to store and retrieve data for your applications, and how to use threads and sockets to enable concurrency and communication between applications.

Some of the topics covered in this unit are:

- Swing and AWT components and layouts
- Event handling and listeners
- Model-View-Controller (MVC) pattern
- Servlets and JSPs
- HTTP protocol and request-response cycle
- JDBC and SQL
- Threads and sockets
- Client-server and peer-to-peer architectures



# Write programs using JavaScript for Web Page to display browsers information

JavaScript is a scripting or programming language that allows you to implement complex features on web pages. To display browser information, such as the name, version, platform, and user agent, we can use the `window.navigator` object. This object contains properties that help to identify a web browser. Here are some examples of JavaScript programs to display browser information on a web page:

## Example 1: Display browser name and version

```javascript
// Get the browser name and version from the navigator object
var browserName = navigator.appName;
var browserVersion = navigator.appVersion;

// Display the browser name and version on the web page
document.write("Browser name: " + browserName + "<br>");
document.write("Browser version: " + browserVersion + "<br>");
```

## Example 2: Display browser platform and user agent

```javascript
// Get the browser platform and user agent from the navigator object
var browserPlatform = navigator.platform;
var browserUserAgent = navigator.userAgent;

// Display the browser platform and user agent on the web page
document.write("Browser platform: " + browserPlatform + "<br>");
document.write("Browser user agent: " + browserUserAgent + "<br>");
```

## Example 3: Display browser cookies and online status

```javascript
// Get the browser cookies and online status from the navigator object
var browserCookies = navigator.cookieEnabled;
var browserOnline = navigator.onLine;

// Display the browser cookies and online status on the web page
document.write("Browser cookies: " + browserCookies + "<br>");
document.write("Browser online: " + browserOnline + "<br>");
```

These are some of the basic programs to display browser information using JavaScript. You can also use other properties and methods of the `window.navigator` object to get more information about the browser, such as the language, the geolocation, the device memory, etc. You can find more information and examples on the following websites:

: https://phptpoint.com/how-to-get-browser-details-through-javascript/
: http://www.alanwood.net/demos/browserinfo.html
: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript
: https://www.w3schools.com/js/js_window_navigator.asp
: https://www.w3schools.com/js/js_ex_browser.asp
: https://stackoverflow.com/questions/11219582/how-to-detect-my-browser-version-and-operating-system-using-javascript



# Write a Java applet to display the Application Program screen i.e. calculator and other for the notes of the Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab

- A Java applet is a small Java application that can be embedded with web browsers to display dynamic content and can run on the client-side directly  .
- A Java applet can be used to create a calculator program that can perform basic arithmetic operations such as addition, subtraction, multiplication and division.
- A Java applet can use the `java.awt` and `java.applet` packages to create the graphical user interface (GUI) and the logic of the calculator program.
- A Java applet can use the `Applet` class to define the applet, the `init()` method to initialize the applet, the `paint()` method to draw the applet, and the `actionPerformed()` method to handle the user events  .
- A Java applet can use the `TextField` class to create the input and output fields, the `Button` class to create the buttons, the `GridLayout` class to arrange the components in a grid, and the `ActionListener` interface to register the event listeners  .
- A Java applet can use the `Double.parseDouble()` method to convert the input strings to double values, the `String.valueOf()` method to convert the double values to output strings, and the `switch` statement to perform the arithmetic operations based on the selected operator  .
- A Java applet can use the `repaint()` method to update the applet display after each operation  .

- A possible example of a Java applet program for a calculator is as follows:

```java
// import the necessary packages
import java.awt.*;
import java.applet.*;
import java.awt.event.*;

// define the applet class
public class Calculator extends Applet implements ActionListener {
  // declare the components
  TextField input1, input2, output;
  Button add, subtract, multiply, divide, clear;
  double num1, num2, result;
  char op;

  // initialize the applet
  public void init() {
    // create the components
    input1 = new TextField(10);
    input2 = new TextField(10);
    output = new TextField(10);
    add = new Button("+");
    subtract = new Button("-");
    multiply = new Button("*");
    divide = new Button("/");
    clear = new Button("C");

    // add the components to the applet
    add(input1);
    add(input2);
    add(output);
    add(add);
    add(subtract);
    add(multiply);
    add(divide);
    add(clear);

    // set the layout of the applet
    setLayout(new GridLayout(4, 2));

    // register the event listeners
    add.addActionListener(this);
    subtract.addActionListener(this);
    multiply.addActionListener(this);
    divide.addActionListener(this);
    clear.addActionListener(this);
  }

  // draw the applet
  public void paint(Graphics g) {
    // set the font and color of the applet
    g.setFont(new Font("Arial", Font.BOLD, 20));
    g.setColor(Color.blue);

    // draw the title of the applet
    g.drawString("Calculator Applet", 50, 20);
  }

  // handle the user events
  public void actionPerformed(ActionEvent e) {
    // get the source of the event
    Object source = e.getSource();

    // if the source is the clear button, clear the input and output fields
    if (source == clear) {
      input1.setText("");
      input2.setText("");
      output.setText("");
    }
    // else, get the input values and the selected operator
    else {
      num1 = Double.parseDouble(input1.getText());
      num2 = Double.parseDouble(input2.getText());

      if (source == add) {
        op = '+';
      } else if (source == subtract) {
        op = '-';
      } else if (source == multiply) {
        op = '*';
      } else if (source == divide) {
        op = '/';
      }

      // perform the arithmetic operation based on the operator
      switch (op) {
        case '+':
          result = num1 + num2;
          break;
        case '-':

```




## Unit 3 - Design dynamic web pages using Javascript and XML

- Javascript is a scripting language that can be embedded in HTML documents to add interactivity, functionality, and dynamic features to web pages.
- XML is a markup language that can be used to store, exchange, and manipulate structured data in a platform-independent and human-readable way.
- Some of the topics covered in this unit are:

  - How to use Javascript variables, data types, operators, expressions, statements, and functions to perform basic computations and control the flow of the program.
  - How to use Javascript objects, arrays, and built-in methods to store and manipulate complex data structures.
  - How to use Javascript events and event handlers to respond to user actions and modify the Document Object Model (DOM) of the web page.
  - How to use Javascript to validate user input, handle errors and exceptions, and debug the code using tools such as the browser console and debugger.
  - How to use Javascript to create and manipulate XML documents using the XML DOM and the XMLHTTPRequest object.
  - How to use Javascript to parse and process XML data using methods such as DOM traversal, XPath, and XSLT.
  - How to use Javascript to communicate with web servers and exchange data using techniques such as AJAX, JSON, and RESTful APIs.
  - How to use Javascript frameworks and libraries such as jQuery, Bootstrap, and AngularJS to simplify and enhance the development of dynamic web pages.



### Writing program in XML for creation of DTD, which specifies set of rules for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A DTD (Document Type Declaration) is a way to describe the structure, elements and attributes of an XML document  .
- A DTD can be used to validate the XML document against the grammatical rules of the XML language .
- A DTD can be declared internally or externally to the XML document .
- An internal DTD is declared inside the XML document, within the `<!DOCTYPE>` tag.
- An external DTD is declared in a separate file, with the extension `.dtd`, and referenced by the XML document using the `SYSTEM` or `PUBLIC` keyword .
- A DTD defines the elements and attributes of an XML document using declarations .
- An element declaration specifies the name and content model of an element .
- An attribute declaration specifies the name, type and default value of an attribute .
- A DTD can also define entities, notations and comments .

Here is an example of an XML document with an internal DTD that specifies the rules for the notes of Unit 3:

```xml
<?xml version="1.0"?>
<!DOCTYPE notes [
  <!ELEMENT notes (unit+)>
  <!ELEMENT unit (title, content)>
  <!ELEMENT title (#PCDATA)>
  <!ELEMENT content (section+)>
  <!ELEMENT section (heading, paragraph+)>
  <!ELEMENT heading (#PCDATA)>
  <!ELEMENT paragraph (#PCDATA)>
  <!ATTLIST unit number CDATA #REQUIRED>
  <!ATTLIST section number CDATA #REQUIRED>
]>
<notes>
  <unit number="3">
    <title>Design dynamic web pages using Javascript and XML</title>
    <content>
      <section number="1">
        <heading>Introduction to Javascript</heading>
        <paragraph>Javascript is a scripting language that runs on the web browser.</paragraph>
        <paragraph>It can be used to create dynamic and interactive web pages.</paragraph>
      </section>
      <section number="2">
        <heading>Introduction to XML</heading>
        <paragraph>XML is a markup language that defines a set of rules for encoding data.</paragraph>
        <paragraph>It can be used to store and exchange data between different applications.</paragraph>
      </section>
    </content>
  </unit>
</notes>
```



### Create a style sheet in CSS/ XSL & display the document in internet explorer for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A style sheet is a file that defines the appearance and layout of an XML document.
- CSS (Cascading Style Sheets) is a language for styling HTML and XML documents.
- XSL (eXtensible Stylesheet Language) is a language for transforming XML documents into other formats, such as HTML, PDF, or plain text.
- To create a style sheet in CSS, you need to use the `<style>` element inside the `<head>` element of your HTML or XML document, or use the `<link>` element to reference an external CSS file.
- To create a style sheet in XSL, you need to use the `<xsl:stylesheet>` or `<xsl:transform>` element as the root element of your XSL file, and use the `<xsl:template>` element to define the rules for transforming the XML document.
- To display the document in internet explorer, you need to save the XML and XSL files with the .xml and .xsl extensions, respectively, and use the `<?xml-stylesheet?>` processing instruction in the XML file to link to the XSL file.
- Alternatively, you can use a server-side script, such as PHP or ASP, to transform the XML document using the XSL file and send the output to the browser as HTML.

Example:

XML file (notes.xml):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="notes.xsl"?>
<notes>
  <note>
    <title>Introduction to Javascript</title>
    <content>Javascript is a scripting language that runs in the browser and can manipulate the HTML document.</content>
  </note>
  <note>
    <title>Introduction to XML</title>
    <content>XML is a markup language that defines a set of rules for encoding data in a human-readable and machine-readable format.</content>
  </note>
</notes>
```

XSL file (notes.xsl):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" doctype-system="about:legacy-compat"/>
  <xsl:template match="/">
    <html>
      <head>
        <style>
          h1 {
            color: blue;
          }
          p {
            font-family: Arial;
          }
        </style>
      </head>
      <body>
        <h1>Notes for Unit 3 - Design dynamic web pages using Javascript and XML</h1>
        <xsl:apply-templates select="notes/note"/>
      </body>
    </html>
  </xsl:template>
  <xsl:template match="note">
    <h2><xsl:value-of select="title"/></h2>
    <p><xsl:value-of select="content"/></p>
  </xsl:template>
</xsl:stylesheet>
```

Output (in internet explorer):

Output



## Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP

- A dynamic web page is a web page whose content and layout can change depending on the user's input, preferences, or other factors .
- A server-side dynamic web page is a web page whose construction is controlled by an application server processing server-side scripts.
- Server-side scripts are programs that run on the web server and generate the HTML code that is sent to the web browser .
- Server-side scripts can be written in any number of programming languages, such as PHP, ASP, JSP, Python, Ruby, C#, or JavaScript (NodeJS) .
- Server-side scripts can access the server operating system, databases, and other resources, and can perform complex tasks such as authentication, validation, data processing, and dynamic content generation .
- Server-side programming requires a web server, a web application framework, and a database system to store and retrieve data.
- Some examples of popular web application frameworks are Django (Python), Express (JavaScript), Laravel (PHP), ASP.NET (C#), and Spring (Java).
- Some examples of popular database systems are MySQL, MongoDB, PostgreSQL, SQLite, and Oracle.
- To design a dynamic web page using server-side programming, one needs to follow these steps:
  - Define the purpose and functionality of the web page, and identify the user requirements and expectations.
  - Choose a suitable server-side programming language and web application framework, and install the necessary software and tools.
  - Create the database schema and tables, and populate them with some sample data.
  - Write the server-side scripts that handle the HTTP requests and responses, and connect to the database to perform CRUD (create, read, update, delete) operations .
  - Write the HTML, CSS, and JavaScript code that define the structure, style, and behavior of the web page .
  - Test and debug the web page using a web browser and a web server, and check for errors, bugs, and security issues.
  - Deploy the web page to a production server, and monitor its performance and user feedback.



### Program to illustrate JDBC connectivity

JDBC stands for Java Database Connectivity, which is a standard Java API for connecting to relational databases. JDBC allows a Java program to execute SQL statements and retrieve the results from a database server.

To use JDBC, a Java program needs to do the following steps:

1. Load the JDBC driver class that corresponds to the type of database server. For example, to connect to a MySQL database, the driver class is `com.mysql.jdbc.Driver`. The driver class can be loaded by using the `Class.forName()` method, which registers the driver with the `DriverManager` class.
2. Obtain a connection object from the `DriverManager` class by passing the connection URL, the user name and the password. The connection URL specifies the protocol, the host name, the port number, the database name and other parameters for connecting to the database server. For example, the connection URL for a MySQL database is `jdbc:mysql://localhost:3306/test`, where `localhost` is the host name, `3306` is the port number and `test` is the database name.
3. Create a statement object from the connection object by using the `createStatement()` method. A statement object allows the Java program to execute SQL statements on the database server.
4. Execute the SQL statement by using the `executeQuery()` method for queries that return a result set, or the `executeUpdate()` method for queries that modify the database. The result set object contains the data returned by the query, and can be accessed by using the `next()` and the `getXXX()` methods, where `XXX` is the data type of the column. The execute update method returns an integer value indicating the number of rows affected by the query.
5. Close the statement object and the connection object by using the `close()` method. This releases the resources used by the JDBC objects and closes the connection to the database server.

The following code snippet shows an example of a Java program that connects to a MySQL database and executes a simple query:

```java
// Load the JDBC driver
Class.forName("com.mysql.jdbc.Driver");

// Obtain a connection
Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "password");

// Create a statement
Statement stmt = con.createStatement();

// Execute a query
ResultSet rs = stmt.executeQuery("SELECT * FROM students");

// Process the result set
while (rs.next()) {
  // Get the data from each column
  int id = rs.getInt("id");
  String name = rs.getString("name");
  int age = rs.getInt("age");
  // Print the data
  System.out.println(id + " " + name + " " + age);
}

// Close the statement and the connection
stmt.close();
con.close();
```



### Program for maintaining database by sending queries for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

- Server-side programming is the process of creating web pages that are dynamically generated by the web server based on the user's request, input, or session data.
- Server-side programming languages are used to interact with databases, files, other servers, web applications, and user input.
- Some examples of server-side programming languages are ASP, JSP, and PHP  .
- ASP stands for Active Server Pages, a server-side scripting language developed by Microsoft that uses VBScript or JScript as the scripting language.
- JSP stands for Java Server Pages, a server-side scripting language developed by Sun Microsystems that uses Java as the scripting language and has access to Java APIs and databases .
- PHP stands for Hypertext Preprocessor, a server-side scripting language that can be embedded in HTML and can connect to various databases .
- To maintain a database by sending queries using server-side programming, the following steps are required:
  - Create a database and a table with the required fields and data using a database management system (DBMS) such as MySQL, Oracle, or SQL Server.
  - Establish a connection between the server-side script and the database using the appropriate functions or methods of the chosen language.
  - Write SQL queries to perform operations on the database such as insert, update, delete, or select data.
  - Execute the queries using the server-side script and display the results on the web page using HTML tags or other methods.
  - Close the connection to the database when the operation is completed.
- The following is an example of a program for maintaining a database by sending queries using PHP and MySQL:

```php
<?php
// Create a connection to the database
$conn = mysqli_connect("localhost", "root", "", "webtech");

// Check if the connection is successful
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

// Write a SQL query to select all data from the notes table
$sql = "SELECT * FROM notes";

// Execute the query and store the result
$result = mysqli_query($conn, $sql);

// Check if the result is not empty
if (mysqli_num_rows($result) > 0) {
  // Display the result in a HTML table
  echo "<table border='1'>";
  echo "<tr><th>ID</th><th>Topic</th><th>Content</th></tr>";
  // Loop through each row of the result
  while($row = mysqli_fetch_assoc($result)) {
    // Display each field of the row
    echo "<tr><td>" . $row["id"] . "</td><td>" . $row["topic"] . "</td><td>" . $row["content"] . "</td></tr>";
  }
  echo "</table>";
} else {
  // Display a message if the result is empty
  echo "No notes found";
}

// Close the connection to the database
mysqli_close($conn);
?>
```



### Design and implement a simple servlet book query with the help of JDBC & SQL

A servlet is a Java class that runs on a web server and handles HTTP requests and responses. JDBC is a Java API that allows Java programs to interact with databases using SQL commands. SQL is a language for querying and manipulating data in relational databases.

To design and implement a simple servlet book query with the help of JDBC & SQL, we need to follow these steps:

1. Create a database and a table for storing book information, such as title, author, price, etc. For example, we can use MySQL as the database and create a table called books with the following SQL statement:

```sql
CREATE TABLE books (
  id INT PRIMARY KEY,
  title VARCHAR(50),
  author VARCHAR(50),
  price DECIMAL(10,2)
);
```

2. Insert some sample data into the books table using SQL statements, such as:

```sql
INSERT INTO books VALUES (1, 'Java: The Complete Reference', 'Herbert Schildt', 35.99);
INSERT INTO books VALUES (2, 'Head First Java', 'Kathy Sierra and Bert Bates', 29.99);
INSERT INTO books VALUES (3, 'Effective Java', 'Joshua Bloch', 39.99);
```

3. Download and install a web server that supports servlets, such as Apache Tomcat, and configure it to run on a specific port, such as 8080. Also, download and copy the JDBC driver for MySQL, such as mysql-connector.jar, to the lib folder of Tomcat.

4. Create a Java project in an IDE, such as Eclipse, and add the servlet-api.jar and mysql-connector.jar to the build path. Also, create a web.xml file in the WEB-INF folder of the project and define the servlet name, class, and URL mapping. For example, we can create a servlet called BookServlet that handles requests to /books URL:

```xml
<web-app>
  <servlet>
    <servlet-name>BookServlet</servlet-name>
    <servlet-class>com.example.BookServlet</servlet-class>
  </servlet>
  <servlet-mapping>
    <servlet-name>BookServlet</servlet-name>
    <url-pattern>/books</url-pattern>
  </servlet-mapping>
</web-app>
```

5. Create a Java class that extends HttpServlet and overrides the doGet method to handle GET requests to /books URL. In the doGet method, we need to:

  - Get the request parameter for the book title, if any, and store it in a variable, such as title.
  - Load the JDBC driver and establish a connection to the MySQL database using the DriverManager class and the connection URL, username, and password. For example:

  ```java
  Class.forName("com.mysql.jdbc.Driver");
  Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/bookdb", "root", "password");
  ```

  - Create a SQL SELECT query to fetch the book information from the books table based on the title parameter, if any, or fetch all the books otherwise. For example:

  ```java
  String sql = "SELECT * FROM books";
  if (title != null && !title.isEmpty()) {
    sql += " WHERE title LIKE ?";
  }
  ```

  - Create a PreparedStatement object from the connection and set the title parameter, if any, using the setString method. For example:

  ```java
  PreparedStatement ps = con.prepareStatement(sql);
  if (title != null && !title.isEmpty()) {
    ps.setString(1, "%" + title + "%");
  }
  ```

  - Execute the query and get the ResultSet object that contains the book information. For example:

  ```java
  ResultSet rs = ps.executeQuery();
  ```

  - Get the response object and set the content type to text/html. For example:

  ```java
  HttpServletResponse response = (HttpServletResponse) resp;
  response.setContentType("text/html");
  ```

  - Get the PrintWriter object from the response and write the HTML code to display the book information in a table. For example:

  ```java
  PrintWriter out = response.getWriter();
  out.println("<html><head><title>Book Query</title></head><body>");
  out.println("<h1>Book Query</h1>");
  out.println("<form method='get' action='/books'>");
  out.println("Enter book title: <input type='text' name='title'>");
  out.println("<input type='submit'

```




Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on how to create MS Access database, create an ODBC link, compile and execute JAVA JDVC socket for the notes of the unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab.

### Create MS Access Database
- Microsoft Access is a database management software that lets you create intuitive applications using various templates and tools.
- To create a database in Access, you can follow these steps:
  - Open Access. If Access is already open, select File > New.
  - Select Blank database, or select a template.
  - Enter a name for the database, select a location, and then select Create.
  - If needed, select Enable content in the yellow message bar when the database opens.
  - To create a table, select Create > Table Design, and then add the fields, data types, and properties for the table.
  - To save the table, select File > Save, and then enter a name for the table.
  - To add data to the table, select Home > View > Datasheet View, and then enter the values in the cells.
  - To create a relationship between tables, select Database Tools > Relationships, and then drag the primary key field from one table to the foreign key field in another table.
  - To create a query, select Create > Query Design, and then add the tables and fields you want to query. You can also specify criteria and sorting options in the query grid.
  - To run the query, select Run on the Design tab, or double-click the query in the Navigation Pane.
  - To create a form, select Create > Form, and then select the table or query you want to base the form on. You can also use the Form Wizard or the Blank Form tool to create a custom form.
  - To create a report, select Create > Report, and then select the table or query you want to base the report on. You can also use the Report Wizard or the Blank Report tool to create a custom report.

### Create an ODBC Link
- ODBC (Open Database Connectivity) is a standard that allows you to connect to different types of databases using a common interface.
- To create an ODBC link, you can follow these steps:
  - Open the ODBC Data Source Administrator from the Control Panel or the Start menu.
  - Select the User DSN or System DSN tab, depending on whether you want to create a user-level or system-level data source.
  - Select Add to launch the Create New Data Source wizard.
  - Select the driver for the database you want to connect to, such as Microsoft Access Driver (*.mdb, *.accdb), and then select Finish.
  - Enter a name and a description for the data source, and then select Select to browse for the database file you want to link to.
  - Select OK to complete the data source creation.

### Compile and Execute JAVA JDVC Socket
- JDBC (Java Database Connectivity) is an API that allows you to access and manipulate data in databases using Java.
- To compile and execute a Java JDBC socket, you can follow these steps:
  - Write a Java program that imports the java.sql package and uses the DriverManager, Connection, Statement, ResultSet, and SQLException classes to connect to the database, execute queries, and handle errors.
  - Save the program as a .java file, such as Example.java.
  - Compile the program using the javac command, such as javac Example.java. This will generate a .class file, such as Example.class.
  - Run the program using the java command, such as java Example. This will execute the JDBC socket and display the results.



## Unit 5 - Design server site applications using JDDC,ODBC and section tracking API

- JDBC (Java Database Connectivity) is an API that allows Java applications to interact with various types of databases using a standard interface.
- ODBC (Open Database Connectivity) is an older API that enables applications written in different languages and platforms to access databases using a common driver.
- JDBC-ODBC Bridge is a type of driver that acts as an interface between JDBC and ODBC, converting the JDBC calls to ODBC calls and vice versa.
- Section tracking API is an API that enables web applications to maintain state information across multiple requests from the same client, such as user preferences, shopping cart items, etc.
- To design server site applications using these APIs, one needs to follow these steps:

  - Choose a suitable database and install the corresponding JDBC or ODBC driver on the server.
  - Establish a connection to the database using the DriverManager class or the DataSource interface in JDBC, or the SQLConnect function in ODBC.
  - Create and execute SQL statements using the Statement, PreparedStatement, or CallableStatement classes in JDBC, or the SQLExecDirect or SQLPrepare functions in ODBC.
  - Process the results using the ResultSet class in JDBC, or the SQLFetch or SQLGetData functions in ODBC.
  - Close the connection and release the resources using the close method in JDBC, or the SQLDisconnect function in ODBC.
  - Implement section tracking using the HttpSession interface or the Cookie class in Java, or the Session or Application objects in ASP.NET.



### Install TOMCAT web server and APACHE

Tomcat is an open source web server and servlet container that supports Java applications. Apache is another web server that can work with Tomcat to handle static content and load balancing. To install and configure Tomcat and Apache, follow these steps:

1. Install Java. Tomcat requires Java to run, so you need to install a Java Development Kit (JDK) on your system. You can download the latest JDK from https://www.oracle.com/java/technologies/downloads/ and follow the installation instructions for your operating system. Make sure to set the JAVA_HOME environment variable to point to the JDK installation directory.
2. Create a Tomcat system user. It is not recommended to run Tomcat as the root user, as it poses a security risk. You can create a dedicated user and group for Tomcat with the following commands:

```bash
sudo groupadd tomcat
sudo useradd -s /bin/false -g tomcat -d /opt/tomcat tomcat
```

3. Install and configure Tomcat. You can download the latest version of Tomcat from https://tomcat.apache.org/download-10.cgi and choose the binary distribution for your platform. For example, to download and extract Tomcat 10 on Linux, you can use the following commands:

```bash
cd /tmp
curl -O https://downloads.apache.org/tomcat/tomcat-10/v10.0.14/bin/apache-tomcat-10.0.14.tar.gz
sudo mkdir -p /opt/tomcat
sudo tar xzvf apache-tomcat-10.0.14.tar.gz -C /opt/tomcat --strip-components=1
```

Then, you need to change the ownership and permissions of the Tomcat directory to the tomcat user and group:

```bash
sudo chown -R tomcat:tomcat /opt/tomcat
sudo chmod -R u+rwx,g+rx,o-rwx /opt/tomcat
```

You can also edit the Tomcat configuration file (/opt/tomcat/conf/server.xml) to change the default port number, enable HTTPS, or add virtual hosts. For more details, see https://tomcat.apache.org/tomcat-10.0-doc/config/index.html.
4. Create a Tomcat systemd service. To start and stop Tomcat as a service, you need to create a systemd unit file for Tomcat. You can create a file named /etc/systemd/system/tomcat.service with the following content:

```ini
[Unit]
Description=Apache Tomcat Web Application Container
After=network.target

[Service]
Type=forking

Environment=JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
Environment=CATALINA_PID=/opt/tomcat/temp/tomcat.pid
Environment=CATALINA_HOME=/opt/tomcat
Environment=CATALINA_BASE=/opt/tomcat
Environment='CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC'
Environment='JAVA_OPTS=-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom'

ExecStart=/opt/tomcat/bin/startup.sh
ExecStop=/opt/tomcat/bin/shutdown.sh

User=tomcat
Group=tomcat
UMask=0007
RestartSec=10
Restart=always

[Install]
WantedBy=multi-user.target
```

Make sure to adjust the JAVA_HOME environment variable to match your JDK installation directory. Then, reload the systemd daemon and enable the Tomcat service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable tomcat
```

You can now start, stop, and check the status of Tomcat with the following commands:

```bash
sudo systemctl start tomcat
sudo systemctl stop tomcat
sudo systemctl status tomcat
```

5. Install Apache HTTP Server. You can install Apache on your system using the package manager of your operating system. For example, on Ubuntu, you can use the following command:

```bash
sudo apt install apache2
```

You can also configure Apache to suit your needs, such as changing the document root, enabling SSL, or adding virtual hosts. For more details, see https://httpd.apache.org/docs/2.4/.
6. Configure Tomcat to work with Apache. To connect Tomcat and Apache, you need to use a connector module called mod_jk. You can install mod_jk on your system using the package manager of your operating system.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is the content you requested:

### Access the above developed static web pages for books web site, using these servers by putting the web pages developed for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To access the static web pages for books web site, you need to have a web server that can host and serve the HTML files. You can use any web server software, such as Apache, Nginx, IIS, etc.  
- You also need to have a database server that can store and retrieve the data for the books, such as MySQL, PostgreSQL, Oracle, etc. You need to create a database schema and populate it with some sample data.  
- You need to have a JDBC driver that can connect to the database server from your web server. JDBC stands for Java Database Connectivity, and it is an API that allows Java applications to access data from various sources. ODBC stands for Open Database Connectivity, and it is a standard that allows applications to access data from various sources using a common interface. 
- You need to have a servlet container that can run Java servlets on your web server. Servlets are Java classes that handle requests and responses from clients. You can use any servlet container software, such as Tomcat, Jetty, GlassFish, etc. 
- You need to have a session tracking API that can maintain the state of the users across multiple requests. Session tracking is a technique that allows web applications to identify and store information about the users, such as their preferences, shopping cart, login status, etc. There are various ways to implement session tracking, such as cookies, URL rewriting, hidden fields, etc. 
- You need to develop the server-side applications using JDBC, ODBC and session tracking API. These applications will interact with the database server and the static web pages to provide dynamic functionality, such as authentication, authorization, searching, browsing, ordering, etc. You need to follow the design principles and best practices for developing server-side applications. 
- You need to put the web pages and the server-side applications in the appropriate directories on your web server. You need to configure the web server, the database server, the JDBC driver, the servlet container, and the session tracking API properly. You need to test and debug your web applications using various tools and techniques. 

: Design The Following Static Web Pages of an Online Book Store, https://www.programmingwithbasics.com/2016/04/design-following-static-web-pages.html
: Develop Static Pages (Using Only HTML) of An Online Book Store, https://www.scribd.com/doc/60394208/wt
: Web Technology Lab Manual, https://www.scribd.com/document/387574481/Web-Technology-Lab-Manual



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use for your study material.

### Unit 5 - Design server site applications using JDDC,ODBC and section tracking API

- JDDC stands for Java Database Connectivity, which is an API that allows Java programs to access various types of databases.
- ODBC stands for Open Database Connectivity, which is a standard interface that enables applications to connect to different data sources, such as relational databases, spreadsheets, or text files.
- Session tracking is a technique that allows a web server to maintain the state of a user across multiple requests, such as login information, shopping cart items, or preferences.
- Some of the session tracking APIs in Java are:
  - Cookies: small pieces of data that are stored by the browser and sent to the server with each request. Cookies can store user-specific information, such as username, password, or preferences.
  - URL rewriting: a method of appending session information to the URL of each request. URL rewriting can be used when cookies are disabled or not supported by the browser.
  - Hidden fields: hidden input elements in HTML forms that can store session information. Hidden fields can be used to pass session information from one page to another.
  - HttpSession: an object that represents a session between a user and a web server. HttpSession can store session information as attributes, which can be accessed by the server-side code.

- To design server-side applications using JDDC, ODBC, and session tracking API, the following steps are required:
  - Import the required packages, such as java.sql, javax.servlet, javax.servlet.http, etc.
  - Load the appropriate JDBC driver, such as com.mysql.jdbc.Driver, oracle.jdbc.driver.OracleDriver, etc.
  - Establish a connection to the database using DriverManager.getConnection(url, username, password), where url is the connection string, username is the database user, and password is the database password.
  - Create a Statement or PreparedStatement object to execute SQL queries or commands.
  - Use ResultSet or ResultSetMetaData objects to retrieve the results of the queries or commands.
  - Use Cookie, URL, HiddenField, or HttpSession objects to store or retrieve session information, such as user1, pwd1, user2, pwd2, etc.
  - Close the connection, statement, and result set objects when done.



A servlet is a Java class that runs on a web server and handles HTTP requests and responses. A servlet can use the JDBC API to connect to a database and perform SQL operations. JDBC is a standard Java API that allows Java applications to interact with various types of databases. ODBC is a similar API that supports multiple programming languages and platforms, but requires a bridge driver to work with Java. Section tracking API is a way to maintain state information across multiple requests from the same client, such as using cookies, URL rewriting, or hidden form fields.

To write a servlet for doing the following for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab, you can follow these steps:

- Import the necessary Java packages, such as javax.servlet, javax.servlet.http, java.sql, and java.io.
- Define a public class that extends HttpServlet and implements the doGet or doPost method, depending on the type of request you want to handle.
- In the doGet or doPost method, get the request parameters, such as the database name, username, password, query, or section information, using the request object's methods, such as getParameter or getParameterValues.
- Create a Connection object using the DriverManager class's getConnection method, passing the appropriate JDBC or ODBC URL, username, and password as arguments. For example, to connect to an Oracle database using JDBC, you can use the URL "jdbc:oracle:thin:@hostname:port:SID".
- Create a Statement or PreparedStatement object using the Connection object's createStatement or prepareStatement method, passing the SQL query as an argument.
- Execute the query using the Statement or PreparedStatement object's executeQuery or executeUpdate method, depending on the type of query. This will return a ResultSet object for queries that return data, or an int value for queries that modify data.
- Process the ResultSet object using its methods, such as next, getString, getInt, or getBlob, to retrieve the data from each row and column. You can also use the ResultSetMetaData object to get the metadata of the result set, such as the number and type of columns.
- Write the output to the response object using its methods, such as setContentType, getWriter, or getOutputStream, to specify the content type, character encoding, and output stream of the response. You can also use HTML tags, CSS styles, or JavaScript code to format the output.
- Close the ResultSet, Statement, Connection, and output stream objects using their close methods, to release the resources and avoid memory leaks.
- Optionally, use the section tracking API to store or retrieve section information using the request or response object's methods, such as getCookies, setCookie, encodeURL, or getParameter. You can also use the HttpSession object to store or retrieve section attributes using its methods, such as getId, getAttribute, setAttribute, or invalidate.

Here is an example of a servlet that connects to an Oracle database using JDBC, executes a query, and displays the result in a table, using cookies to store the username and password:

```java
import javax.servlet.*;
import javax.servlet.http.*;
import java.sql.*;
import java.io.*;

public class DatabaseServlet extends HttpServlet {

  public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    // Get the request parameters
    String dbname = request.getParameter("dbname");
    String query = request.getParameter("query");

    // Get the username and password from cookies, or from request parameters if cookies are not available
    String username = null;
    String password = null;
    Cookie[] cookies = request.getCookies();
    if (cookies != null) {
      for (Cookie cookie : cookies) {
        if (cookie.getName().equals("username")) {
          username = cookie.getValue();
        }
        if (cookie.getName().equals("password")) {
          password = cookie.getValue();
        }
      }
    }
    if (username == null || password == null) {
      username = request.getParameter("username");
      password = request.getParameter("password");
    }

    // Set the content type and character encoding of the response
    response.setContentType("text/html");
    response.setCharacterEncoding("UTF-8");

    // Get the output stream of the response
    PrintWriter out = response.getWriter();

    // Write the HTML header
    out.println("<html>");
    out.println("<head>");
    out.println("<title>Database Servlet</title>");
    out.println("</head>");
    out.println("<body>");

    // Declare the database objects
    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;

    try {
      // Load the

```




### Create a Cookie and add these four user id’s and passwords to this Cookie for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A cookie is a small piece of data that is stored by the browser and sent to the server with every request. Cookies can be used to store user preferences, session information, authentication tokens, etc.
- To create a cookie in Java, we can use the `Cookie` class from the `javax.servlet.http` package. We can also use the `document.cookie` property in JavaScript .
- To create a cookie, we need to specify a name and a value for the cookie. Optionally, we can also set some attributes, such as the expiration date, the domain, the path, the secure flag, etc.
- To add a cookie to the response, we can use the `addCookie(Cookie)` method of the `HttpServletResponse` interface  . This will send the cookie to the browser along with the response headers.
- To read a cookie from the request, we can use the `getCookies()` method of the `HttpServletRequest` interface . This will return an array of `Cookie` objects that represent the cookies sent by the browser.
- To update or delete a cookie, we can modify its value or attributes and send it back to the browser using the `addCookie(Cookie)` method. To delete a cookie, we can set its expiration date to a past time.
- To add the user id's and passwords to a cookie, we can use the following steps:

  - Create a `Cookie` object for each user id and password pair, using the user id as the name and the password as the value. For example:

    ```java
    Cookie user1 = new Cookie("user1", "pass1");
    Cookie user2 = new Cookie("user2", "pass2");
    Cookie user3 = new Cookie("user3", "pass3");
    Cookie user4 = new Cookie("user4", "pass4");
    ```

  - Set the expiration date for each cookie to a future time, using the `setMaxAge(int)` method. For example, to set the cookie to expire in one hour:

    ```java
    user1.setMaxAge(60 * 60); // 60 seconds * 60 minutes
    user2.setMaxAge(60 * 60);
    user3.setMaxAge(60 * 60);
    user4.setMaxAge(60 * 60);
    ```

  - Optionally, set other attributes for the cookies, such as the domain, the path, the secure flag, etc. using the corresponding methods of the `Cookie` class. For example, to set the domain to `example.com` and the path to `/webtech`:

    ```java
    user1.setDomain("example.com");
    user1.setPath("/webtech");
    user2.setDomain("example.com");
    user2.setPath("/webtech");
    user3.setDomain("example.com");
    user3.setPath("/webtech");
    user4.setDomain("example.com");
    user4.setPath("/webtech");
    ```

  - Add the cookies to the response, using the `addCookie(Cookie)` method of the `HttpServletResponse` interface. For example:

    ```java
    response.addCookie(user1);
    response.addCookie(user2);
    response.addCookie(user3);
    response.addCookie(user4);
    ```

- To read the user id's and passwords from the cookie, we can use the following steps:

  - Get the array of `Cookie` objects from the request, using the `getCookies()` method of the `HttpServletRequest` interface. For example:

    ```java
    Cookie[] cookies = request.getCookies();
    ```

  - Loop through the array and check the name of each cookie. If the name matches the user id, get the value of the cookie, which is the password. For example:

    ```java
    for (Cookie cookie : cookies) {
      String name = cookie.getName();
      String value = cookie.getValue();
      if (name.equals("user1")) {
        // value is the password for user1
      } else if (name.equals("user2")) {
        // value is the password for user2
      } else if (name.equals("user3")) {
        // value is the password for

```




Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some information that might be useful for you:

### Read the user id and passwords entered in the Login form and authenticate with the values available in the cookies for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To read the user id and password from the login form in Java, you can use the `request.getParameter()` method to get the values entered by the user in the HTML input fields.
- To authenticate the user id and password with the values available in the cookies, you can use the `request.getCookies()` method to get an array of cookies sent by the browser.
- You can then loop through the array and compare the cookie name and value with the user id and password entered by the user. If they match, you can grant access to the user. Otherwise, you can redirect them to the login page or display an error message.
- For example, the following code snippet shows how to read the user id and password from the login form and authenticate them with the cookies:

```java
// Get the user id and password from the login form
String userId = request.getParameter("userId");
String password = request.getParameter("password");

// Get the cookies from the request
Cookie[] cookies = request.getCookies();

// Initialize a flag to indicate if the user is authenticated
boolean authenticated = false;

// Loop through the cookies and check if they match the user id and password
if (cookies != null) {
  for (Cookie cookie : cookies) {
    if (cookie.getName().equals(userId) && cookie.getValue().equals(password)) {
      // The user is authenticated
      authenticated = true;
      break;
    }
  }
}

// If the user is authenticated, proceed to the next page
if (authenticated) {
  // Do something
}
// If the user is not authenticated, redirect them to the login page or display an error message
else {
  // Do something else
}
```

- To design server-side applications using JDBC, ODBC and session tracking API, you can refer to the following topics:
  - JDBC (Java Database Connectivity) is an API that allows Java programs to connect to various types of databases and execute SQL queries and commands.
  - ODBC (Open Database Connectivity) is a standard that allows applications to access data from different database management systems using a common interface.
  - Session tracking API is a set of methods and classes that enable web applications to maintain the state of a user across multiple requests and pages.
  - Some of the session tracking techniques are cookies, URL rewriting, hidden form fields and HttpSession objects.



### Install a database (Mysql or Oracle) for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

This section will explain how to install MySQL database on Windows using the MySQL Installer method   . This is the recommended way to install MySQL on Microsoft Windows as it simplifies the installation and configuration process.

- Download MySQL Installer from https://dev.mysql.com/downloads/installer/ and execute it .
- A welcome screen provides several options. Choose the first option: Install MySQL Products.
- On the Choosing a Setup Type page, select the setup type for your installation. You can choose from Developer Default, Server Only, Client Only, or Full.
- On the Check Requirements page, MySQL Installer checks to see if any software prerequisites are missing. If any are found, they are listed on this page. You can choose to have MySQL Installer download and install the missing software, or you can install them manually.
- On the Installation page, MySQL Installer downloads and installs the MySQL products that you have selected.
- On the Product Configuration page, MySQL Installer configures the MySQL products that you have installed. You can choose to configure each product individually, or use the default configuration for all products.
- On the Type and Networking page, you can choose the configuration type and the network options for your MySQL server. You can choose from Development Machine, Server Machine, or Dedicated Machine. You can also choose the port number, the protocol, and the firewall rules for your MySQL server.
- On the Accounts and Roles page, you can set the password for the root user and create other user accounts for your MySQL server. You can also assign roles and privileges to the users.
- On the Windows Service page, you can choose the Windows service name, the start type, and the account for your MySQL server. You can also choose to run the MySQL server as a Windows service or not.
- On the Apply Server Configuration page, MySQL Installer applies the configuration settings that you have chosen to your MySQL server. You can also choose to start the MySQL server after the configuration is done.
- On the Installation Complete page, MySQL Installer shows the status of the installation and configuration process. You can also choose to view the log file or launch the MySQL Workbench.

You have successfully installed and configured MySQL database on Windows using the MySQL Installer method. You can now use the MySQL Command Line Client or the MySQL Workbench to connect to your MySQL server and perform database operations  .

: MySQL Installation on Microsoft Windows - W3Schools
: Getting Started with MySQL - MySQL
: Install MySQL on Windows Using MySQL Installer - MySQL Tutorial
: Installing MySQL on Microsoft Windows - MySQL



Hello, I am Sydney, your AI assistant. I can help you with your query.

To create a table with the fields you specified, you can use the following steps:

- Choose a database management system (DBMS) that supports JDBC, ODBC and session tracking API. For example, MySQL, Oracle, PostgreSQL, etc.
- Connect to the DBMS using the appropriate driver and connection string. For example, `jdbc:mysql://localhost:3306/webtechlab` for MySQL.
- Create a database or schema to store the table. For example, `CREATE DATABASE webtechlab;`
- Use the `CREATE TABLE` statement to define the table name and the columns with their data types, constraints and indexes. For example,

```
CREATE TABLE users (
  name VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL,
  email_id VARCHAR(50) UNIQUE,
  phone_number VARCHAR(15) UNIQUE,
  PRIMARY KEY (name)
);
```

- Optionally, you can insert some sample data into the table using the `INSERT INTO` statement. For example,

```
INSERT INTO users (name, password, email_id, phone_number) VALUES
('Alice', '1234', 'alice@example.com', '1111111111'),
('Bob', '5678', 'bob@example.com', '2222222222'),
('Charlie', '9012', 'charlie@example.com', '3333333333');
```

- You can query the table using the `SELECT` statement to retrieve the data. For example,

```
SELECT * FROM users;
```

This will return the following result:

| name | password | email_id | phone_number |
| --- | --- | --- | --- |
| Alice | 1234 | alice@example.com | 1111111111 |
| Bob | 5678 | bob@example.com | 2222222222 |
| Charlie | 9012 | charlie@example.com | 3333333333 |

- You can also use the JDBC, ODBC and session tracking API to access the table from your server-side applications. For example, you can use the `java.sql` package in Java to create a connection, statement and result set objects to execute SQL queries and process the results. You can use the `javax.servlet.http.HttpSession` interface to create and manage sessions for each user. You can use the `sun.jdbc.odbc.JdbcOdbcDriver` class to connect to the DBMS using ODBC.




Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a possible answer to your question:

### Write a java program/servlet/JSP to connect to that database and extract data from the tables and display them for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To connect to a database using Java, you need to use JDBC (Java Database Connectivity), which is a standard API that allows you to interact with various databases like Oracle, SQL, PostgreSQL, MongoDB, etc.   
- To use JDBC, you need to have a JDBC driver for your specific database, which is a JAR file that must be in the classpath while compiling and running the Java code. You can download the JDBC driver from the official website of your database vendor.  
- To connect to a database, you need to use the Connection class, which represents a physical connection to the database. You can obtain a Connection object by calling the DriverManager.getConnection() method, which takes the URL, username, and password of the database as parameters.    
- To execute queries on the database, you need to use the Statement or PreparedStatement classes, which represent SQL statements that can be sent to the database. You can create a Statement or PreparedStatement object by calling the Connection.createStatement() or Connection.prepareStatement() methods, respectively.   
- To retrieve the results of the queries, you need to use the ResultSet class, which represents a table of data generated by executing a query. You can obtain a ResultSet object by calling the Statement.executeQuery() or PreparedStatement.executeQuery() methods, which take the SQL query as a parameter.   
- To display the data from the ResultSet, you can use the ResultSetMetaData class, which provides information about the columns of the ResultSet, such as the name, type, and size. You can obtain a ResultSetMetaData object by calling the ResultSet.getMetaData() method. You can then use a loop to iterate over the rows of the ResultSet, and use the ResultSet.getString(), ResultSet.getInt(), ResultSet.getDouble(), etc. methods to get the values of each column. You can also use the DBTablePrinter class, which is a utility class that can print the contents of a ResultSet in a formatted table. 
- To write a servlet or JSP that can connect to a database and display the data, you need to import the necessary classes from the java.sql package, and use the same steps as above to create a Connection, Statement, ResultSet, and ResultSetMetaData objects. You can then use the PrintWriter class to write the HTML code that will display the data in a web page. You can also use the JSTL (JavaServer Pages Standard Tag Library) or EL (Expression Language) to simplify the code and avoid using scriptlets.   

Here is an example of a Java program that can connect to a MySQL database and display the data from a table called employees:

```java
// Import the necessary classes
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.Statement;

public class DatabaseConnection {

    public static void main(String[] args) {
        // Declare the variables
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        ResultSetMetaData rsmd = null;

        try {
            // Load the JDBC driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Connect to the database
            String url = "jdbc:mysql://localhost:3306/test";
            String user = "root";
            String password = "root";
            conn = DriverManager.getConnection(url, user, password);

            // Create a statement
            stmt = conn.createStatement();

            // Execute a query
            String sql = "SELECT * FROM employees";
            rs = stmt.executeQuery(sql);

            // Get the metadata
            rsmd = rs.getMetaData();

            // Print the column names
            int columnCount = rsmd.getColumnCount();
            for (int i = 1; i <= columnCount; i++) {
                System.out.print(rsmd.getColumnName(i) + "\t");
            }
            System.out.println();

            // Print the data
            while (

```




### Insert the details of the users who register with the web site, whenever a new user clicks the submit button in the registration page

- To insert the details of the users who register with the web site, we need to use Java Database Connectivity (JDBC) and Open Database Connectivity (ODBC) to connect to a database and execute SQL statements.
- JDBC is an API that allows Java programs to access various types of databases using a common interface.
- ODBC is a standard that enables applications to access data from different database management systems using a common interface.
- To use JDBC and ODBC, we need to follow these steps:

  1. Load the JDBC driver class using the `Class.forName()` method. The driver class is specific to the database system and the ODBC driver that we are using. For example, to use the Microsoft Access ODBC driver, we can load the driver class as follows:

  ```java
  Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
  ```

  2. Establish a connection to the database using the `DriverManager.getConnection()` method. The method takes three parameters: the connection URL, the username, and the password. The connection URL specifies the ODBC data source name (DSN) that we have configured for the database. For example, to connect to a database named `users` with the username `admin` and the password `admin`, we can use the following connection URL:

  ```java
  String url = "jdbc:odbc:users";
  String user = "admin";
  String password = "admin";
  Connection con = DriverManager.getConnection(url, user, password);
  ```

  3. Create a statement object using the `Connection.createStatement()` method. The statement object allows us to execute SQL queries and updates on the database. For example, to create a statement object, we can use the following code:

  ```java
  Statement stmt = con.createStatement();
  ```

  4. Execute the SQL statement using the `Statement.executeUpdate()` method. The method takes a string parameter that contains the SQL statement to be executed. The method returns an integer value that indicates the number of rows affected by the statement. For example, to insert a new user with the name `Alice` and the email `alice@example.com` into a table named `users`, we can use the following SQL statement:

  ```java
  String sql = "INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')";
  int rows = stmt.executeUpdate(sql);
  ```

  5. Close the statement and the connection objects using the `Statement.close()` and `Connection.close()` methods. These methods release the resources associated with the objects and prevent memory leaks. For example, to close the statement and the connection objects, we can use the following code:

  ```java
  stmt.close();
  con.close();
  ```

- To insert the details of the users who register with the web site, whenever a new user clicks the submit button in the registration page, we need to write the JDBC and ODBC code in a servlet class that handles the registration request from the web browser.
- A servlet is a Java class that extends the `HttpServlet` class and overrides the `doPost()` method to process the HTTP POST request from the web browser.
- The `doPost()` method takes two parameters: a `HttpServletRequest` object and a `HttpServletResponse` object. The `HttpServletRequest` object contains the information about the request, such as the parameters, the headers, and the cookies. The `HttpServletResponse` object contains the information about the response, such as the status code, the headers, and the output stream.
- To get the parameters from the request, we can use the `HttpServletRequest.getParameter()` method. The method takes a string parameter that specifies the name of the parameter and returns the value of the parameter as a string. For example, to get the name and the email parameters from the request, we can use the following code:

  ```java
  String name = request.getParameter("name");
  String email = request.getParameter("email");
  ```

- To insert the details of the users who register with the web site, whenever a new user clicks the submit button in the registration page, we need to write the JDBC and ODBC code inside the `doPost()` method of the servlet class, using the parameters from the request as the values for the SQL statement. For example, to insert the name and the email parameters into the users table, we can use the following code:

  ```java
  String sql = "INSERT INTO users (name, email) VALUES ('" + name + "', '" + email + "')";
  int rows = stmt.executeUpdate(sql);
  ```

- To



### Write a JSP which insert the details of the 3 or 4 users who register with the web site by using registration form for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- JSP stands for Java Server Pages, which is a technology that allows creating dynamic web pages using Java code and HTML tags.
- JSP can connect to a database using JDBC (Java Database Connectivity) or ODBC (Open Database Connectivity) drivers, which are APIs that enable communication between Java applications and various data sources.
- JSP can also use session tracking API, which is a mechanism that allows maintaining state information across multiple requests from the same client.
- To create a registration form in JSP, we need to have a table in the database that can store the user details, such as name, email, password, etc.
- We also need to have two JSP files: one for displaying the form and another for processing the form data and inserting it into the database.
- The following steps can be followed to write a JSP that can insert the details of the users who register with the web site:

1. Create a table in the database that can store the user details. For example, we can use the Oracle database and create a table named user432 with the following command:

```sql
CREATE TABLE "USER432" (
  "NAME" VARCHAR2 (4000),
  "EMAIL" VARCHAR2 (4000),
  "PASS" VARCHAR2 (4000)
)
```

2. Create a JSP file named index.jsp that can display the registration form. The form should have input fields for name, email, and password, and a submit button that can send the form data to another JSP file named process.jsp. The form can look like this:

```html
<form action="process.jsp">
  <input type="text" name="uname" value="Name..." onclick="this.value=''"/><br/>
  <input type="text" name="uemail" value="Email ID..." onclick="this.value=''"/><br/>
  <input type="password" name="upass" value="Password..." onclick="this.value=''"/><br/>
  <input type="submit" value="register"/>
</form>
```

3. Create a JSP file named process.jsp that can process the form data and insert it into the database. The file should have the following steps:

  - Import the necessary packages for JDBC or ODBC and session tracking API.
  - Get the form data from the request object using the getParameter() method.
  - Establish a connection to the database using the DriverManager class and the getConnection() method. Provide the appropriate driver name, URL, username, and password for the database.
  - Create a statement object using the createStatement() method of the connection object.
  - Execute an SQL insert query using the executeUpdate() method of the statement object. Provide the table name and the form data as the values to be inserted.
  - Close the statement and connection objects using the close() method.
  - Create a session object using the getSession() method of the request object. Set the form data as session attributes using the setAttribute() method of the session object.
  - Display a message to the user that the registration is successful and show the session attributes using the getAttribute() method of the session object.

The process.jsp file can look like this:

```jsp
<%@ page import="java.sql.*,javax.servlet.http.*" %>
<%
  //Get the form data from the request object
  String name=request.getParameter("uname");
  String email=request.getParameter("uemail");
  String pass=request.getParameter("upass");
  
  //Establish a connection to the database
  Class.forName("oracle.jdbc.driver.OracleDriver");
  Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","oracle");
  
  //Create a statement object
  Statement st=con.createStatement();
  
  //Execute an SQL insert query
  int i=st.executeUpdate("insert into user432 values('"+name+"','"+email+"','"+pass+"')");
  
  //Close the statement and connection objects
  st.close();
  con.close();
  
  //Create a session object
  HttpSession session=request.getSession();
  
  //Set the form data as session attributes
  session.setAttribute("name",name);
  session.setAttribute("email",email);
  session.setAttribute("pass",pass);
  
  //Display a message to the user and show the session attributes
  out.println("

```




### Authenticate the user when he submits the login form using the user name and password from the database for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To authenticate the user when he submits the login form using the user name and password from the database, we need to use JDBC (Java Database Connectivity) and ODBC (Open Database Connectivity) drivers to establish a connection between the web application and the database server.
- JDBC and ODBC drivers are software components that enable the web application to communicate with the database server using a standard interface and protocol. JDBC drivers are specific to Java-based web applications, while ODBC drivers are generic and can be used by any web application that supports ODBC.
- To use JDBC and ODBC drivers, we need to configure the connection parameters, such as the database URL, the user name, the password, and the driver class name. These parameters can be specified in the web application code, in a configuration file, or in a data source object.
- To authenticate the user, we need to use a SQL query to check if the user name and password entered by the user match the records in the database table. If the query returns a result, the user is authenticated and a session is created for the user. If the query returns no result, the user is not authenticated and an error message is displayed.
- A session is a mechanism to store and track information about the user across multiple requests and responses. A session can be implemented using cookies, URL rewriting, hidden fields, or session tracking API. Session tracking API is a set of methods and classes provided by the Java Servlet API to create and manage sessions.
- The following are the steps to authenticate the user using JDBC, ODBC, and session tracking API:

  1. Import the required packages, such as java.sql, javax.servlet, and javax.servlet.http.
  2. Load the JDBC or ODBC driver class using the Class.forName() method.
  3. Establish a connection to the database using the DriverManager.getConnection() method, passing the database URL, the user name, and the password as arguments.
  4. Create a statement object using the connection.createStatement() method.
  5. Execute a SQL query to select the user name and password from the database table using the statement.executeQuery() method, passing the query as an argument.
  6. Get the result set object from the query execution using the statement.getResultSet() method.
  7. Check if the result set has any row using the resultset.next() method. If it returns true, the user is authenticated. If it returns false, the user is not authenticated.
  8. If the user is authenticated, create a session object using the request.getSession() method, passing true as an argument to indicate that a new session is created if none exists.
  9. Set the user name as an attribute of the session object using the session.setAttribute() method, passing the user name and the resultset.getString() method as arguments.
  10. Redirect the user to a welcome page using the response.sendRedirect() method, passing the URL of the welcome page as an argument.
  11. If the user is not authenticated, display an error message using the response.getWriter() method and the out.println() method, passing the error message as an argument.
  12. Close the result set, the statement, and the connection objects using the resultset.close(), statement.close(), and connection.close() methods, respectively.

- The following is an example of a Java servlet code that implements the above steps:

```java
// Import the required packages
import java.io.*;
import java.sql.*;
import javax.servlet.*;
import javax.servlet.http.*;

// Define the servlet class
public class LoginServlet extends HttpServlet {

  // Define the database connection parameters
  private static final String DB_URL = "jdbc:odbc:mydb"; // ODBC data source name
  private static final String DB_USER = "admin"; // Database user name
  private static final String DB_PASS = "admin123"; // Database password
  private static final String DB_DRIVER = "sun.jdbc.odbc.JdbcOdbcDriver"; // ODBC driver class name

  // Override the doPost() method to handle the login form submission
  public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    // Get the user name and password from the request parameters
    String userName = request.getParameter("userName");
    String password = request.getParameter("password");

    // Declare the JDBC or ODBC objects
    Connection connection

```




### Design and implement a simple shopping cart example with session tracking API

- A shopping cart is a web application that allows users to browse, select, and purchase items from an online store.
- A session tracking API is a mechanism that enables the web server to identify and maintain the conversational state of each user across multiple requests.
- Session tracking is needed for shopping cart applications because the server needs to know which items belong to which user's cart, and to preserve the cart contents even if the user leaves the site and returns later.
- There are different methods for session tracking, such as cookies, URL rewriting, hidden form fields, and HTTP session objects.
- Cookies are small pieces of data that are stored on the user's browser and sent to the server with every request. Cookies can store information such as the user's ID, preferences, or cart items.
- URL rewriting is a technique that appends the session ID to every URL that the user clicks on. This way, the server can retrieve the session ID from the URL and associate it with the user's data.
- Hidden form fields are input elements that are not visible to the user, but can store and transmit session information when the user submits a form. For example, a hidden form field can store the user's ID or cart items.
- HTTP session objects are server-side objects that store session information for each user. The server creates a session object when the user first visits the site, and assigns a unique session ID to it. The session ID is then sent to the user's browser as a cookie or a URL parameter, and the server uses it to retrieve the session object with the user's data.

- A simple shopping cart example with session tracking API can be designed and implemented as follows:

  - Create a web page that displays the available products and their prices, and allows the user to add or remove items from their cart.
  - Create a servlet that handles the user's requests and performs the following tasks:
    - Check if the user has a valid session ID. If not, create a new session object and send the session ID to the user's browser as a cookie or a URL parameter.
    - Retrieve the session object from the server using the session ID, and get the user's cart data from the session object.
    - Process the user's request, such as adding or removing items from the cart, and update the session object accordingly.
    - Display the updated cart contents and the total amount to the user.
  - Create a web page that allows the user to confirm their order and enter their payment and delivery details.
  - Create a servlet that handles the order confirmation and performs the following tasks:
    - Retrieve the session object from the server using the session ID, and get the user's cart data and personal information from the session object.
    - Validate the user's input and process the payment and delivery.
    - Display a confirmation message and a receipt to the user.
    - Invalidate the session object and delete the session ID from the user's browser.

