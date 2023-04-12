

## Unit 1 - Develop static web pages using HTML

- HTML stands for HyperText Markup Language. It is the standard language for creating web pages and web applications.
- HTML consists of elements that define the structure and content of a web page. Elements are enclosed by tags, which are written in angle brackets (< and >).
- HTML elements can have attributes, which provide additional information or functionality to the elements. Attributes are written inside the start tag, after the element name, and consist of a name and a value separated by an equal sign (=).
- HTML elements can be nested, which means that one element can contain another element inside it. The inner element is called the child element, and the outer element is called the parent element. The child element inherits some properties from the parent element, such as alignment, font, and color.
- HTML elements can be classified into two types: block-level elements and inline elements. Block-level elements create a new line on the web page and occupy the entire width of the parent element. Inline elements do not create a new line and only occupy the space needed by their content. Examples of block-level elements are `<div>`, `<p>`, `<h1>`, and `<ul>`. Examples of inline elements are `<span>`, `<a>`, `<img>`, and `<em>`.
- HTML documents have a basic structure that consists of a `<html>` element, a `<head>` element, and a `<body>` element. The `<html>` element is the root element that contains all other elements. The `<head>` element contains information about the document, such as the title, the character encoding, and the links to external resources. The `<body>` element contains the visible content of the document, such as text, images, and links.
- HTML documents can be linked to each other using the `<a>` element, which creates a hyperlink. The `<a>` element has an attribute called `href`, which specifies the URL of the destination document. The content of the `<a>` element is the text or image that the user can click on to follow the link.
- HTML documents can display images using the `<img>` element, which is an empty element that does not have a closing tag. The `<img>` element has an attribute called `src`, which specifies the URL of the image file. The `<img>` element can also have attributes such as `alt`, `width`, `height`, and `title`, which provide alternative text, size, and tooltip for the image.
- HTML documents can create lists using the `<ul>` element, which creates an unordered list, and the `<ol>` element, which creates an ordered list. Both elements contain one or more `<li>` elements, which create list items. The `<ul>` element displays the list items with bullets, while the `<ol>` element displays them with numbers or letters.
- HTML documents can create tables using the `<table>` element, which contains one or more `<tr>` elements, which create table rows. Each `<tr>` element contains one or more `<td>` elements, which create table cells. The `<table>` element can also have a `<caption>` element, which creates a title for the table, and a `<thead>` element, a `<tbody>` element, and a `<tfoot>` element, which create the header, body, and footer sections of the table. The `<td>` element can have attributes such as `colspan` and `rowspan`, which specify how many columns or rows the cell spans.



### Write HTML/Java scripts to display your CV in navigator, your Institute website, Department Website and Tutorial website for specific subject for the notes of the Unit 1 - Develop static web pages using HTML in the subject of Web Technology Lab

- To display your CV in navigator, you can use HTML to create the structure and content of your resume, such as your name, contact details, education, skills, work experience, etc. You can use CSS to style your resume, such as fonts, colors, layout, etc. You can use JavaScript to add interactivity and functionality to your resume, such as light/dark theme, export PDF, etc. You can use OpenCV.js to read and show images from HTML canvas or img element . You can use a responsive design to make your resume adaptable to different screen sizes and devices.
- To display your Institute website, you can use HTML to create the structure and content of your website, such as your logo, navigation bar, footer, etc. You can use CSS to style your website, such as backgrounds, borders, animations, etc. You can use JavaScript to add interactivity and functionality to your website, such as drop-down menus, sliders, pop-ups, etc. You can use a responsive design to make your website adaptable to different screen sizes and devices.
- To display your Department website, you can use HTML to create the structure and content of your website, such as your department name, mission, vision, faculty, courses, etc. You can use CSS to style your website, such as grids, columns, cards, etc. You can use JavaScript to add interactivity and functionality to your website, such as tabs, accordions, filters, etc. You can use a responsive design to make your website adaptable to different screen sizes and devices.
- To display your Tutorial website for specific subject for the notes of the Unit 1 - Develop static web pages using HTML, you can use HTML to create the structure and content of your website, such as your subject name, unit name, topics, examples, exercises, etc. You can use CSS to style your website, such as headings, lists, tables, etc. You can use JavaScript to add interactivity and functionality to your website, such as quizzes, feedback, progress, etc. You can use a responsive design to make your website adaptable to different screen sizes and devices. You can use JavaScript to display CSV files in HTML, such as using the FileReader API, the Papa Parse library, or the D3.js library.



### Write an HTML program to design an entry form of student details and send it to store at database server like SQL, Oracle or MS Access for the notes of the Unit 1 - Develop static web pages using HTML in the subject of Web Technology Lab

- To design an entry form of student details using HTML, you need to use the `<form>` element, which allows you to create various input fields, such as text boxes, radio buttons, checkboxes, dropdown lists, etc. 
- To send the form data to a database server, you need to specify the `action` attribute of the `<form>` element, which defines the URL of the server-side script that will process the form data. You also need to specify the `method` attribute, which defines how the form data will be transmitted. The most common methods are `GET` and `POST`. 
- To store the form data in a database server like SQL, Oracle or MS Access, you need to use a server-side scripting language, such as PHP, ASP.NET, Java, etc., that can connect to the database and execute SQL queries to insert, update, delete, or retrieve data. 

- Here is an example of an HTML program that creates a simple entry form of student details and sends it to a PHP script that stores the data in a MySQL database. You can modify the code according to your requirements and preferences.

```html
<html>
<head>
  <title>Student Entry Form</title>
</head>
<body>
  <h1>Student Entry Form</h1>
  <form action="student.php" method="POST">
    <p>First Name: <input type="text" name="fname" required></p>
    <p>Last Name: <input type="text" name="lname" required></p>
    <p>Email: <input type="email" name="email" required></p>
    <p>Phone: <input type="tel" name="phone" required></p>
    <p>Address: <input type="text" name="address" required></p>
    <p>Gender: <input type="radio" name="gender" value="Male" checked> Male <input type="radio" name="gender" value="Female"> Female</p>
    <p>Course: <select name="course" required>
      <option value="Web Technology">Web Technology</option>
      <option value="Database Management">Database Management</option>
      <option value="Software Engineering">Software Engineering</option>
      <option value="Artificial Intelligence">Artificial Intelligence</option>
    </select></p>
    <p>Date of Birth: <input type="date" name="dob" required></p>
    <p>Hobbies: <input type="checkbox" name="hobbies[]" value="Reading"> Reading <input type="checkbox" name="hobbies[]" value="Music"> Music <input type="checkbox" name="hobbies[]" value="Sports"> Sports</p>
    <p><input type="submit" value="Submit"> <input type="reset" value="Reset"></p>
  </form>
</body>
</html>
```

- Here is an example of a PHP script that receives the form data and stores it in a MySQL database. You need to create a database and a table with the appropriate columns and data types before running this script. You also need to change the database connection parameters according to your configuration.

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
$fname = $_POST["fname"];
$lname = $_POST["lname"];
$email = $_POST["email"];
$phone = $_POST["phone"];
$address = $_POST["address"];
$gender = $_POST["gender"];
$course = $_POST["course"];
$dob = $_POST["dob"];
$hobbies = $_POST["hobbies"];

// Convert the hobbies array to a comma-separated string
$hobbies = implode(",", $hobbies);

// Prepare and execute the SQL query to insert the data
$sql = "INSERT INTO student (fname, lname, email, phone, address, gender, course, dob, hobbies) VALUES ('$fname', '$lname', '$

```




## Unit 2 - Develop Java programs for window/web-based applications

- Java is a popular programming language that can be used to create dynamic and interactive web applications.
- A web application is a software that runs on a web server and communicates with a web browser through the internet.
- A window application is a software that runs on a desktop or laptop computer and interacts with the user through a graphical user interface (GUI).
- Java provides various technologies and frameworks to support the development of both window and web applications, such as:
  - Servlets: A servlet is a Java class that extends the functionality of a web server by processing requests and generating responses. Servlets can handle various types of requests, such as HTTP, FTP, or SOAP.
  - JavaServer Pages (JSP): A JSP is a text file that contains HTML, XML, or other markup languages, as well as Java code snippets that are executed on the server side. JSPs can dynamically generate web pages based on the user input or data from a database.
  - Java Web Start: A Java Web Start is a technology that allows users to launch Java applications from a web browser with a single click, without installing them on the local machine. Java Web Start uses a special file format called JNLP (Java Network Launching Protocol) to describe how to download, install, and run a Java application.
  - Struts: Struts is a framework that follows the Model-View-Controller (MVC) design pattern for developing web applications. Struts provides a set of components and tools that help developers to separate the business logic, presentation logic, and data access logic of a web application.
  - Broadleaf: Broadleaf is an open-source e-commerce platform that is built on top of Java technologies, such as Spring, Hibernate, and Thymeleaf. Broadleaf provides a flexible and customizable solution for creating online stores, catalogs, and shopping carts.



### Write programs using JavaScript for Web Page to display browsers information

- JavaScript is a scripting language that can be used to create dynamic and interactive web pages.
- JavaScript can access the browser's information through the `window.navigator` object, which contains properties and methods related to the browser and the user agent.
- The `window.navigator` object can provide information such as the browser name, version, platform, language, online status, and more.
- However, the `window.navigator` object is not reliable for browser detection, as different browsers may use the same name, change the user agent data, or misidentify themselves to bypass site tests.
- Therefore, it is recommended to use other methods for browser detection, such as:
  - Extracting information from the user agent string and checking if it contains the browser's name. For example, to check for Chrome browsers:

  ```javascript
  if (navigator.userAgent.indexOf("Chrome") != -1) {
    // code for Chrome browser
  }
  ```

  - Using a detection library such as Bowser, which can parse the user agent string and return a detailed object with browser name, version, engine, platform, and more.
  - Detecting the CSS vendor prefix, which is a prefix added to some CSS properties to indicate the browser or engine that supports them. For example, to check for WebKit browsers:

  ```javascript
  if ("WebkitAppearance" in document.documentElement.style) {
    // code for WebKit browsers
  }
  ```

  - Browser duck typing, which is a technique of checking for unique features that each browser has. For example, to check for Internet Explorer browsers:

  ```javascript
  if ("ActiveXObject" in window) {
    // code for IE browsers
  }
  ```

- Here is an example of a simple web page that displays some browser information using the `window.navigator` object:

  ```html
  <html>
    <head>
      <title>Browser Information</title>
      <script>
        // function to display browser information
        function displayBrowserInfo() {
          // get the browser information elements
          var browserName = document.getElementById("browserName");
          var browserVersion = document.getElementById("browserVersion");
          var browserPlatform = document.getElementById("browserPlatform");
          var browserLanguage = document.getElementById("browserLanguage");
          var browserOnline = document.getElementById("browserOnline");

          // set the browser information elements
          browserName.textContent = navigator.appName;
          browserVersion.textContent = navigator.appVersion;
          browserPlatform.textContent = navigator.platform;
          browserLanguage.textContent = navigator.language;
          browserOnline.textContent = navigator.onLine ? "Yes" : "No";
        }
      </script>
    </head>
    <body onload="displayBrowserInfo()">
      <h1>Browser Information</h1>
      <p>
        Browser Name: <span id="browserName"></span>
      </p>
      <p>
        Browser Version: <span id="browserVersion"></span>
      </p>
      <p>
        Browser Platform: <span id="browserPlatform"></span>
      </p>
      <p>
        Browser Language: <span id="browserLanguage"></span>
      </p>
      <p>
        Browser Online: <span id="browserOnline"></span>
      </p>
    </body>
  </html>
  ```



### Write a Java applet to display the Application Program screen i.e. calculator and other for the notes of the Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab

- A Java applet is a small Java application that can be embedded with web browsers to display dynamic content and can run on the client-side directly .
- A Java applet can be used to create a calculator program that can perform basic arithmetic operations such as addition, subtraction, multiplication and division  .
- To create a Java applet for a calculator program, the following steps are required:

  - Import the necessary packages such as `java.applet`, `java.awt` and `java.awt.event`  .
  - Define a class that extends the `Applet` class and implements the `ActionListener` interface  .
  - Declare the components such as text fields, buttons and labels as instance variables of the class  .
  - Initialize the components in the `init()` method of the applet and add them to the applet layout  .
  - Register the action listeners for the buttons in the `init()` method  .
  - Define the `actionPerformed()` method to handle the button clicks and perform the arithmetic operations  .
  - Override the `paint()` method to display the applet title and other information  .
  - Compile and run the applet using an applet viewer or a web browser  .

- A sample code for a Java applet calculator program is given below:

```java
// Import the necessary packages
import java.applet.*;
import java.awt.*;
import java.awt.event.*;

// Define a class that extends the Applet class and implements the ActionListener interface
public class CalculatorApplet extends Applet implements ActionListener {

  // Declare the components as instance variables
  TextField tf1, tf2, tf3; // Text fields for input and output
  Button b1, b2, b3, b4; // Buttons for arithmetic operations
  Label l1, l2, l3; // Labels for instructions

  // Initialize the components in the init() method
  public void init() {
    // Set the applet layout to grid layout with 4 rows and 2 columns
    setLayout(new GridLayout(4, 2));

    // Create the components
    tf1 = new TextField(10); // Text field for the first operand
    tf2 = new TextField(10); // Text field for the second operand
    tf3 = new TextField(10); // Text field for the result
    tf3.setEditable(false); // Make the result text field read-only
    b1 = new Button("+"); // Button for addition
    b2 = new Button("-"); // Button for subtraction
    b3 = new Button("*"); // Button for multiplication
    b4 = new Button("/"); // Button for division
    l1 = new Label("Enter the first number:"); // Label for the first operand
    l2 = new Label("Enter the second number:"); // Label for the second operand
    l3 = new Label("Result:"); // Label for the result

    // Add the components to the applet layout
    add(l1); // Add the first label to the first row and first column
    add(tf1); // Add the first text field to the first row and second column
    add(l2); // Add the second label to the second row and first column
    add(tf2); // Add the second text field to the second row and second column
    add(l3); // Add the third label to the third row and first column
    add(tf3); // Add the third text field to the third row and second column
    add(b1); // Add the first button to the fourth row and first column
    add(b2); // Add the second button to the fourth row and second column
    add(b3); // Add the third button to the fifth row and first column
    add(b4); // Add the fourth

```




## Unit 3 - Design dynamic web pages using Javascript and XML

- Dynamic web pages are web pages that can change their content or appearance without reloading the whole page. They can provide a better user experience and more interactivity than static web pages.
- Javascript is a scripting language that can run in the browser and manipulate the HTML elements and CSS styles of a web page. It can also communicate with the server and exchange data using AJAX (Asynchronous JavaScript and XML) or JSON (JavaScript Object Notation).
- XML (Extensible Markup Language) is a markup language that can store and transport data in a structured and readable format. It can be used to define the content and structure of a web page, or to exchange data between the client and the server.
- To design dynamic web pages using Javascript and XML, you need to:
  - Learn the basics of HTML, CSS and Javascript syntax and features. You can use online tutorials and references such as [W3Schools](https://www.w3schools.com/).
  - Learn how to use the Document Object Model (DOM) to access and modify the HTML elements and CSS styles of a web page using Javascript. You can use the [DOM API](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) or libraries such as [jQuery](https://jquery.com/).
  - Learn how to use AJAX to send and receive data from the server using Javascript and XML. You can use the [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) object or libraries such as [axios](https://axios-http.com/).
  - Learn how to use XML to define the content and structure of a web page, or to exchange data with the server. You can use the [XML API](https://developer.mozilla.org/en-US/docs/Web/API/XML) or libraries such as [xml2js](https://www.npmjs.com/package/xml2js).
  - Learn how to use JSON as an alternative to XML for data exchange. You can use the [JSON API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON) or libraries such as [json2xml](https://www.npmjs.com/package/json2xml).
  - Learn how to use frameworks and tools that can simplify the development of dynamic web pages using Javascript and XML, such as [React](https://reactjs.org/), [Angular](https://angular.io/), [Vue](https://vuejs.org/), [Bootstrap](https://getbootstrap.com/), [Webpack](https://webpack.js.org/), etc.



### Writing program in XML for creation of DTD, which specifies set of rules for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A DTD (Document Type Declaration) is a way to describe the structure, elements and attributes of an XML document. It defines the rules and constraints for the XML language.   
- A DTD can be declared internally or externally to the XML document. An internal DTD is included in the same file as the XML document, while an external DTD is referenced by a URL or a file path.  
- A DTD can be used to validate the XML document against the grammatical rules of the appropriate XML language. It can also help independent groups of people to agree on a standard DTD for interchanging data.  
- To create a DTD for the notes of the Unit 3, we need to follow these steps:
  - Identify the root element of the XML document. For example, we can use `<notes>` as the root element.
  - Declare the DTD in the XML document using the `<!DOCTYPE>` declaration. For example, we can use `<!DOCTYPE notes SYSTEM "notes.dtd">` to reference an external DTD file named notes.dtd.
  - Define the elements and attributes of the XML document in the DTD file. For example, we can use `<!ELEMENT notes (note+)>` to define the notes element as having one or more note elements as its children. We can also use `<!ELEMENT note (title, content)>` to define the note element as having two child elements: title and content. We can also use `<!ATTLIST note id ID #REQUIRED>` to define the note element as having an id attribute of type ID and required value.
  - Optionally, we can also define the data types, default values, entities, notations and comments in the DTD file. For example, we can use `<!ENTITY author "John Doe">` to define an entity named author with the value "John Doe". We can also use `<!-- This is a comment -->` to add a comment in the DTD file.
  - Save the DTD file and the XML file in the same folder or location. For example, we can save them as notes.dtd and notes.xml respectively.
  - Test the XML document and the DTD file using an XML validator or parser. For example, we can use https://www.w3schools.com/xml/xml_validator.asp to validate the XML document and the DTD file online.

- Here is an example of the XML document and the DTD file for the notes of the Unit 3:

notes.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE notes SYSTEM "notes.dtd">
<notes>
  <note id="n1">
    <title>Introduction to Javascript</title>
    <content>Javascript is a scripting language that can run in web browsers and other environments. It can manipulate HTML elements, handle events, perform calculations, and communicate with web servers.</content>
  </note>
  <note id="n2">
    <title>Introduction to XML</title>
    <content>XML is a markup language that can store and exchange structured data. It can be validated by DTDs or schemas, and transformed by XSLT or XQuery.</content>
  </note>
  <note id="n3">
    <title>Using Javascript and XML together</title>
    <content>Javascript can access and manipulate XML data using the DOM (Document Object Model) or the AJAX (Asynchronous Javascript and XML) technique. It can also use XML parsers and serializers to read and write XML data.</content>
  </note>
</notes>
```

notes.dtd
```xml
<!ELEMENT notes (note+)>
<!ELEMENT note (title, content)>
<!ATTLIST note id ID #REQUIRED>
<!ELEMENT title (#PCDATA)>
<!ELEMENT content (#PCDATA)>
<!ENTITY author "John Doe">
<!-- This DTD defines the rules for the notes of the Unit 3 -->
```



### Create a style sheet in CSS/XSL & display the document in internet explorer for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A style sheet is a file that defines the appearance and layout of a web page or an XML document.
- CSS (Cascading Style Sheets) is a language that describes how HTML elements are displayed on the screen, in print, or in other media.
- XSL (Extensible Stylesheet Language) is a language that describes how XML elements are transformed and formatted for different purposes, such as HTML, PDF, or plain text.
- To create a style sheet in CSS/XSL, you need to follow these steps:

  1. Create a text file with the extension .css or .xsl, depending on the type of style sheet you want to create.
  2. In the first line of the file, declare the document to be a style sheet by using the <xsl:stylesheet> or <xsl:transform> element for XSL, or the @charset or @import rule for CSS.
  3. Define the rules or templates that specify how the elements in the source document are styled or transformed. You can use selectors, properties, values, attributes, expressions, functions, and other syntax elements depending on the language you are using.
  4. Save the file in a location that is accessible by the web browser or the XML processor.

- To display the document in internet explorer, you need to follow these steps:

  1. Create an HTML or XML file that contains the content of the web page or the XML document you want to display.
  2. In the <head> section of the file, link the style sheet to the document by using the <link> element for HTML, or the <?xml-stylesheet?> processing instruction for XML. You need to specify the type, href, and title attributes of the link, and the media attribute if you want to apply the style sheet to a specific media type.
  3. Save the file in a location that is accessible by the web browser or the XML processor.
  4. Open the file in internet explorer and view the result of applying the style sheet to the document. You can also use the developer tools to inspect the source code and the style information of the document.



## Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP

- A dynamic web page is a web page that can display different content or layout depending on the user's input, preferences, or other factors  .
- A server-side dynamic web page is a web page whose construction is controlled by an application server processing server-side scripts.
- Server-side scripts are programs that run on the web server and generate HTML or other output that is sent to the web browser .
- Examples of popular server-side web languages include PHP, Python, Ruby, C#, and JavaScript (NodeJS).
- Server-side programming allows the web developer to create dynamic websites that can deliver customized information in response to HTTP requests, interact with databases, handle user authentication and authorization, and perform other complex tasks.
- To design a dynamic web page using server-side programming, the web developer needs to:
  - Choose a server-side web language and a web framework that supports it. A web framework is a set of tools and libraries that simplify common web development tasks and provide a consistent structure for the web application. Examples of web frameworks are Django (Python), Laravel (PHP), Rails (Ruby), ASP.NET (C#), and Express (JavaScript).
  - Set up a web server that can run the server-side scripts and serve the web pages. A web server is a software that listens for HTTP requests and sends back HTTP responses. Examples of web servers are Apache, Nginx, IIS, and Node.js .
  - Write the server-side scripts that define the logic and functionality of the web application. The server-side scripts can use various techniques to generate dynamic web pages, such as templating, scripting, or compiling. Templating is a method of inserting data into predefined HTML templates. Scripting is a method of embedding code snippets into HTML files. Compiling is a method of transforming source code into executable files.
  - Connect the web application to a database or other data sources if needed. A database is a structured collection of data that can be queried and manipulated by the web application. Examples of databases are MySQL, PostgreSQL, MongoDB, and SQLite .
  - Test and debug the web application using various tools and methods, such as logging, breakpoints, unit testing, and integration testing.
  - Deploy the web application to a production environment, which is a web server that is accessible to the public or the intended users. The web developer needs to consider various factors, such as security, performance, scalability, and reliability, when deploying the web application.



### Program to illustrate JDBC connectivity for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

- JDBC stands for Java Database Connectivity, which is an API that allows Java programs to interact with various types of databases.
- JDBC provides a standard interface for connecting to different databases, executing SQL statements, and retrieving the results.
- JDBC consists of two components: a JDBC driver and a JDBC API.
- A JDBC driver is a software module that implements the JDBC interface for a specific database. It acts as a bridge between the Java program and the database.
- A JDBC API is a set of classes and interfaces that define the methods and constants for accessing the database. It is part of the Java standard library (java.sql and javax.sql packages).
- To use JDBC, a Java program needs to perform the following steps:
  - Load the JDBC driver class using the Class.forName() method.
  - Establish a connection to the database using the DriverManager.getConnection() method.
  - Create a statement object using the Connection.createStatement() method.
  - Execute a SQL query using the Statement.executeQuery() or Statement.executeUpdate() method.
  - Process the result set using the ResultSet.next() and ResultSet.getXXX() methods.
  - Close the resources using the ResultSet.close(), Statement.close(), and Connection.close() methods.

- The following is an example of a Java program that illustrates JDBC connectivity with MySQL database:

```java
//import the required packages
import java.sql.*;

public class JDBCExample {

  public static void main(String[] args) {
    //declare the JDBC objects
    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;

    try {
      //load the JDBC driver class
      Class.forName("com.mysql.cj.jdbc.Driver");

      //establish a connection to the database
      conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/webtech", "root", "password");

      //create a statement object
      stmt = conn.createStatement();

      //execute a SQL query
      rs = stmt.executeQuery("SELECT * FROM students");

      //process the result set
      while (rs.next()) {
        //retrieve the data from each row
        int id = rs.getInt("id");
        String name = rs.getString("name");
        String course = rs.getString("course");
        double marks = rs.getDouble("marks");

        //display the data
        System.out.println("ID: " + id);
        System.out.println("Name: " + name);
        System.out.println("Course: " + course);
        System.out.println("Marks: " + marks);
        System.out.println();
      }
    } catch (Exception e) {
      //handle the exceptions
      e.printStackTrace();
    } finally {
      //close the resources
      try {
        if (rs != null) {
          rs.close();
        }
        if (stmt != null) {
          stmt.close();
        }
        if (conn != null) {
          conn.close();
        }
      } catch (SQLException e) {
        e.printStackTrace();
      }
    }
  }
}
```



### Program for maintaining database by sending queries for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

- In this program, we will use PHP as the server-side programming language to create and query a MySQL database.
- The steps to create and query a database using PHP are:

  1. Establish a connection to MySQL server from your PHP script using either MySQLi or PDO extension. You need to provide the server name, username, password, and optionally the database name as parameters. For example:

  ```php
  // Using MySQLi Object-oriented
  $servername = "localhost";
  $username = "username";
  $password = "password";
  $dbname = "myDB";

  // Create connection
  $conn = new mysqli($servername, $username, $password, $dbname);

  // Check connection
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  ```

  ```php
  // Using PDO
  $servername = "localhost";
  $username = "username";
  $password = "password";
  $dbname = "myDB";

  try {
    // Create connection
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  } catch(PDOException $e) {
    die("Connection failed: " . $e->getMessage());
  }
  ```

  2. Write a SQL query to create a database and store it in a string variable. The CREATE DATABASE statement is used to create a new database in MySQL. For example:

  ```php
  // SQL query to create a database named demo
  $sql = "CREATE DATABASE demo";
  ```

  3. Execute the query using either the mysqli_query() or the PDO::exec() method. If the query is successful, it will return TRUE, otherwise it will return FALSE or an error message. For example:

  ```php
  // Using MySQLi Object-oriented
  if ($conn->query($sql) === TRUE) {
    echo "Database created successfully";
  } else {
    echo "Error creating database: " . $conn->error;
  }
  ```

  ```php
  // Using PDO
  try {
    // Execute the query
    $conn->exec($sql);
    echo "Database created successfully";
  } catch(PDOException $e) {
    echo "Error creating database: " . $e->getMessage();
  }
  ```

  4. Write a SQL query to create a table and store it in a string variable. The CREATE TABLE statement is used to create a new table in a database. You need to specify the table name, the column names, the data types, and optionally the constraints for each column. For example:

  ```php
  // SQL query to create a table named students with four columns: id, name, email, and score
  $sql = "CREATE TABLE students (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(50),
    score INT(3)
  )";
  ```

  5. Execute the query using either the mysqli_query() or the PDO::exec() method. If the query is successful, it will return TRUE, otherwise it will return FALSE or an error message. For example:

  ```php
  // Using MySQLi Object-oriented
  if ($conn->query($sql) === TRUE) {
    echo "Table created successfully";
  } else {
    echo "Error creating table: " . $conn->error;
  }
  ```

  ```php
  // Using PDO
  try {
    // Execute the query
    $conn->exec($sql);
    echo "Table created successfully";
  } catch(PDOException $e) {
    echo "Error creating table: " . $e->getMessage();
  }
  ```

  6. Write a SQL query to insert data into the table and store it in a string variable. The INSERT INTO statement is used to insert new records into a table. You need to specify the table name, the column names, and the values for each column. For example:

  ```php
  // SQL query to insert a record into the students table
  $sql = "INSERT INTO students (

```




### Design and implement a simple servlet book query with the help of JDBC & SQL

- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- JDBC (Java Database Connectivity) is an API that allows Java programs to interact with various types of databases using SQL (Structured Query Language) commands.
- To design and implement a simple servlet book query with the help of JDBC & SQL, the following steps are required:

  1. Set up the JDBC environment and the database. Download the mysql-connector.jar file from the internet and move it to the apache-tomcat server folder. Create a database named `books` and a table named `book` with the following schema:

  | Column | Type | Description |
  | ------ | ---- | ----------- |
  | id | int | The primary key of the book |
  | title | varchar(50) | The title of the book |
  | author | varchar(50) | The author of the book |
  | price | double | The price of the book |

  2. Create a servlet class that extends the `HttpServlet` class and overrides the `doGet` method. The `doGet` method should perform the following tasks:

    - Get the book id from the request parameter using the `request.getParameter` method.
    - Load the JDBC driver using the `Class.forName` method with the driver class name as the argument.
    - Establish a connection to the database using the `DriverManager.getConnection` method with the database URL, username and password as the arguments.
    - Prepare a SQL select query to fetch the book details from the `book` table using the `Connection.prepareStatement` method with the query string as the argument. The query string should use a placeholder (`?`) for the book id and set it using the `PreparedStatement.setInt` method with the index and the book id as the arguments.
    - Execute the query using the `PreparedStatement.executeQuery` method and store the result in a `ResultSet` object.
    - Check if the result set is not empty using the `ResultSet.next` method and get the book details using the `ResultSet.getString` and `ResultSet.getDouble` methods with the column names as the arguments.
    - Set the content type of the response to `text/html` using the `response.setContentType` method.
    - Get the output stream of the response using the `response.getWriter` method and store it in a `PrintWriter` object.
    - Write the HTML code to display the book details in a table using the `PrintWriter.println` method. If the result set is empty, write a message to indicate that the book is not found.
    - Close the result set, the prepared statement and the connection using the `close` method.

  3. Compile the servlet class and place the class file in the `WEB-INF/classes` folder of the web application.
  4. Create a web.xml file in the `WEB-INF` folder of the web application and define the servlet and the servlet mapping using the `<servlet>` and `<servlet-mapping>` tags. The servlet name, the servlet class and the URL pattern should be specified as the child elements of the respective tags.



### Create MS Access Database

- To create a database in MS Access, you can follow these steps:
  - Open Access. If Access is already open, select File > New .
  - Select Blank database, or select a template  .
  - Enter a name for the database, select a location, and then select Create  .
  - If needed, select Enable content in the yellow message bar when the database opens .
  - To create tables, queries, forms, reports, and other database objects, use the Navigation Pane and the ribbon tabs .
  - To save your database, click Save on the Quick Access Toolbar, or press Ctrl+S.



## Unit 5 - Design server site applications using JDDC,ODBC and section tracking API

- JDBC stands for Java Database Connectivity, which is a standard Java API for connecting and executing queries with databases .
- ODBC stands for Open Database Connectivity, which is a standard C API for connecting and executing queries with databases  .
- JDBC-ODBC Bridge is a type of driver that acts as an interface between Java applications and databases that support ODBC.
- Section tracking API is a way of tracking the state of a user session across multiple requests and responses in a web application.
- To design server site applications using JDDC,ODBC and section tracking API, one needs to:
  - Choose a suitable JDBC driver for the database to be used, such as JDBC-ODBC Bridge, JDBC-Net, Native-API, or Native-Protocol .
  - Load the JDBC driver using the Class.forName() method and register it with the DriverManager class .
  - Establish a connection with the database using the DriverManager.getConnection() method and passing the URL, username, and password of the database .
  - Create a Statement, PreparedStatement, or CallableStatement object using the Connection.createStatement(), Connection.prepareStatement(), or Connection.prepareCall() methods respectively .
  - Execute the SQL queries using the Statement.execute(), Statement.executeQuery(), or Statement.executeUpdate() methods and obtain the ResultSet object for retrieving the data .
  - Process the ResultSet object using the methods such as ResultSet.next(), ResultSet.getString(), ResultSet.getInt(), etc. and close the ResultSet, Statement, and Connection objects when done .
  - Use the section tracking API to store and retrieve the user session information, such as user ID, preferences, shopping cart, etc. using the methods such as HttpSession.setAttribute(), HttpSession.getAttribute(), HttpSession.invalidate(), etc. and configure the web.xml file to enable session tracking.
  - Handle any exceptions that may occur during the database operations or the session tracking using the try-catch-finally blocks and the SQLException, ClassNotFoundException, or IOException classes  .



### Install TOMCAT web server and APACHE for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- TOMCAT is an open source web server and servlet container that supports Java Servlet and JavaServer Pages (JSP) technologies.
- APACHE is an open source web server that can handle requests from various protocols, such as HTTP, HTTPS, FTP, and SMTP.
- To install TOMCAT and APACHE on a Windows system, follow these steps:

  1. Download the latest version of TOMCAT from https://tomcat.apache.org/download-10.cgi and extract the zip file to a desired location, such as C:\tomcat.
  2. Download the latest version of APACHE from https://httpd.apache.org/download.cgi and run the installer. Follow the instructions and choose the default options, such as the installation directory (C:\Apache24) and the server name (localhost).
  3. To configure APACHE to work with TOMCAT, open the file C:\Apache24\conf\httpd.conf in a text editor and add the following lines at the end of the file:

```
# Load the proxy modules
LoadModule proxy_module modules/mod_proxy.so
LoadModule proxy_http_module modules/mod_proxy_http.so
LoadModule proxy_ajp_module modules/mod_proxy_ajp.so

# Proxy requests to TOMCAT
ProxyPass /tomcat http://localhost:8080/
ProxyPassReverse /tomcat http://localhost:8080/
```

  4. To test the installation, start both TOMCAT and APACHE by running the files C:\tomcat\bin\startup.bat and C:\Apache24\bin\httpd.exe respectively. Then open a web browser and go to http://localhost/tomcat. You should see the TOMCAT welcome page.
  5. To stop both TOMCAT and APACHE, run the files C:\tomcat\bin\shutdown.bat and C:\Apache24\bin\httpd.exe -k stop respectively.



### Access the above developed static web pages for books web site, using these servers by putting the web pages developed for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A static web page is a page that is built using HTML code and features the same presentation and content, regardless of user identity or other factors.
- An online book store is a website that sells books and other related products to customers through the internet.
- To access the above developed static web pages for books web site, using these servers, you need to follow these steps:

  - Create a folder named `books` in your web server's root directory (e.g. `C:\inetpub\wwwroot\books` for IIS or `/var/www/html/books` for Apache).
  - Copy the static web pages that you have developed for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab into the `books` folder. These pages should include:

    - A home page that contains three frames: a header, a navigation bar and a main content area.
    - A login page that allows the user to enter their username and password and submit them to the server for authentication.
    - A catalogue page that displays the details of all the books available on the website in a table, such as title, author, price, genre, etc.
    - A registration page that allows the user to create an account by entering their personal information and choosing a username and password.
  - Test your web pages by opening a web browser and typing the URL of your web server followed by `/books` (e.g. `http://localhost/books` or `http://192.168.0.1/books`).
  - You should be able to see the home page of your online book store and navigate to the other pages using the links in the navigation bar.
  - You should also be able to log in and register as a user and see the changes in the main content area accordingly.



### Assume four users user1, user2, user3 and user4 having the passwords pwd1, pwd2, pwd3 and pwd4 respectively for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- The topic is about how to design server-side applications using Java Database Connectivity (JDBC), Open Database Connectivity (ODBC) and session tracking API in the subject of Web Technology Lab.
- JDBC is an API that allows Java applications to interact with various types of databases, such as relational, hierarchical, object-oriented, etc.
- ODBC is a standard interface that allows applications to access data from different database management systems, such as Oracle, MySQL, SQL Server, etc.
- Session tracking is a technique that allows a web server to maintain the state of a user across multiple requests, such as login information, shopping cart items, preferences, etc.
- Session tracking can be implemented using various methods, such as cookies, URL rewriting, hidden form fields, or servlet API.
- The notes of the Unit 5 cover the following topics:

  - How to use JDBC to connect to a database, execute SQL queries, and process the results.
  - How to use ODBC to access data from different types of databases using a common interface.
  - How to use session tracking API to create, retrieve, and invalidate sessions, and store and retrieve session attributes.
  - How to use cookies, URL rewriting, hidden form fields, and servlet API to implement session tracking in web applications.
  - How to design server-side applications that use JDBC, ODBC, and session tracking API to perform various tasks, such as authentication, authorization, data manipulation, etc.

- The four users user1, user2, user3 and user4 have the passwords pwd1, pwd2, pwd3 and pwd4 respectively for the notes of the Unit 5.
- The passwords are used to access the notes of the Unit 5 from a web server that hosts the notes as PDF files.
- The web server uses a servlet to authenticate the users and grant them access to the notes based on their passwords.
- The servlet uses JDBC to connect to a database that stores the user information, such as username, password, and notes URL.
- The servlet also uses session tracking API to create a session for each user and store their username and notes URL as session attributes.
- The servlet then redirects the user to the notes URL stored in the session attribute.
- The user can view the notes of the Unit 5 as long as the session is valid.
- The session expires after a certain period of inactivity or when the user logs out.



### A servlet for notes of Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in Web Technology Lab

- A servlet is a Java program that runs on a web server or application server and handles requests from clients and generates responses  .
- A servlet can use the Java Database Connectivity (JDBC) API to access databases and perform CRUD (Create, Read, Update, Delete) operations .
- A servlet can use the Open Database Connectivity (ODBC) API to connect to various data sources that support the ODBC standard, such as Microsoft Access, Excel, SQL Server, Oracle, etc.
- A servlet can use the session tracking API to maintain the state of a client across multiple requests, such as storing user preferences, shopping cart items, authentication information, etc .
- A servlet can use the following classes and interfaces from the javax.servlet and javax.servlet.http packages to implement the above functionalities :
  - Servlet: The interface that defines the lifecycle methods of a servlet, such as init, service, and destroy.
  - GenericServlet: The abstract class that implements the Servlet interface and provides a generic, protocol-independent servlet.
  - HttpServlet: The abstract class that extends GenericServlet and provides a framework for handling HTTP requests and responses.
  - ServletRequest: The interface that represents an object containing the request information from the client, such as parameters, headers, attributes, etc.
  - ServletResponse: The interface that represents an object containing the response information to the client, such as status code, headers, content type, etc.
  - HttpServletRequest: The interface that extends ServletRequest and provides additional methods for handling HTTP requests, such as getMethod, getCookies, getSession, etc.
  - HttpServletResponse: The interface that extends ServletResponse and provides additional methods for handling HTTP responses, such as setStatus, addCookie, sendRedirect, etc.
  - ServletConfig: The interface that represents an object containing the initialization parameters and context of a servlet.
  - ServletContext: The interface that represents an object containing the information about the web application and its environment, such as attributes, resources, log, etc.
  - HttpSession: The interface that represents an object containing the session information of a client, such as id, creation time, attributes, etc.
  - Cookie: The class that represents a small piece of information that is sent by the server to the client and stored by the browser.
  - JDBC: The API that provides a set of classes and interfaces for connecting to databases, executing SQL statements, retrieving results, etc.
  - ODBC: The API that provides a set of functions for connecting to data sources, executing SQL statements, retrieving results, etc.



### Create a Cookie and add these four user id’s and passwords to this Cookie for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A cookie is a small piece of data that is stored by the browser and sent to the server with every request. Cookies can be used to store user preferences, session information, authentication tokens, etc.
- To create a cookie in Java, we can use the `Cookie` class from the `javax.servlet.http` package. We can pass the name and value of the cookie to the constructor, and optionally set other attributes such as domain, path, expiry date, secure flag, etc.
- To add a cookie to the response, we can use the `addCookie` method of the `HttpServletResponse` interface. This method will send a `Set-Cookie` header to the browser with the cookie information.
- To read a cookie from the request, we can use the `getCookies` method of the `HttpServletRequest` interface. This method will return an array of `Cookie` objects that represent the cookies sent by the browser. We can loop through the array and find the cookie by its name.
- To update or delete a cookie, we can create a new cookie with the same name and domain, and set the new value or expiry date. Then we can add the cookie to the response as before.

Here is an example of how to create a cookie and add four user ids and passwords to it:

```java
// Create a cookie with the name "users" and a value that is a comma-separated list of user ids and passwords
Cookie cookie = new Cookie("users", "user1:pass1,user2:pass2,user3:pass3,user4:pass4");

// Set the cookie domain to the current host name
cookie.setDomain(request.getServerName());

// Set the cookie path to the root
cookie.setPath("/");

// Set the cookie expiry date to one month from now
Calendar calendar = Calendar.getInstance();
calendar.add(Calendar.MONTH, 1);
Date expiryDate = calendar.getTime();
cookie.setMaxAge((int) (expiryDate.getTime() - System.currentTimeMillis()) / 1000);

// Add the cookie to the response
response.addCookie(cookie);
```



### Read the user id and passwords entered in the Login form and authenticate with the values available in the cookies for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A login form is a web page that allows users to enter their user id and password to access a protected resource or service.
- A cookie is a small piece of data that is stored by the web browser on the user's device. Cookies can be used to store user preferences, session information, authentication tokens, and other data.
- JDDC (Java Database Driver Connectivity) is a Java API that allows Java applications to connect to various types of databases and execute SQL queries and commands.
- ODBC (Open Database Connectivity) is a standard API that allows applications to access data from different database management systems using a common interface.
- Session tracking is a technique that allows web servers to maintain the state of a user's interaction with a web application across multiple requests. Session tracking can be implemented using cookies, URL rewriting, hidden form fields, or a server-side API.
- To read the user id and password entered in the login form and authenticate with the values available in the cookies, the following steps can be followed:

  - Create a login form using HTML and CSS. The form should have two input fields for user id and password, and a submit button. For example:

  ```html
  <form action="login" method="post">
    <label for="user_id">User ID:</label>
    <input type="text" id="user_id" name="user_id" required>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required>
    <button type="submit">Login</button>
  </form>
  ```

  - Create a servlet that handles the login request. The servlet should read the user id and password from the request parameters, and compare them with the values stored in the cookies. If the values match, the servlet should redirect the user to the protected resource or service. If the values do not match, the servlet should display an error message. For example:

  ```java
  import javax.servlet.*;
  import javax.servlet.http.*;
  import java.io.*;

  public class LoginServlet extends HttpServlet {
    public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
      // Get the user id and password from the request parameters
      String user_id = request.getParameter("user_id");
      String password = request.getParameter("password");

      // Get the cookies from the request
      Cookie[] cookies = request.getCookies();

      // Initialize a flag to indicate whether the user is authenticated or not
      boolean authenticated = false;

      // Loop through the cookies and check if there is a cookie with the name "user_id" and "password"
      // and if the values match with the user input
      if (cookies != null) {
        for (Cookie cookie : cookies) {
          if (cookie.getName().equals("user_id") && cookie.getValue().equals(user_id)) {
            authenticated = true;
          }
          if (cookie.getName().equals("password") && cookie.getValue().equals(password)) {
            authenticated = true;
          }
        }
      }

      // If the user is authenticated, redirect to the protected resource or service
      if (authenticated) {
        response.sendRedirect("protected");
      }
      // If the user is not authenticated, display an error message
      else {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<p>Invalid user id or password. Please try again.</p>");
        out.println("<a href='login.html'>Back to login page</a>");
        out.close();
      }
    }
  }
  ```

  - Configure the servlet mapping in the web.xml file. The servlet mapping tells the web server which servlet to invoke for a given URL pattern. For example:

  ```xml
  <web-app>
    <servlet>
      <servlet-name>LoginServlet</servlet-name>
      <servlet-class>LoginServlet</servlet-class>
    </servlet>
    <servlet-mapping>
      <servlet-name>LoginServlet</servlet-name>
      <url-pattern>/login</url-pattern>
    </servlet-mapping>
  </web-app>
  ```

  - Deploy the web application to the web server and test the login functionality. The web server should be able to connect to the database using JDDC or ODBC and execute SQL queries and commands. The web server should also be able to use session tracking API to maintain the state of the user's interaction with the web application.



### Install a database (Mysql or Oracle) for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- In this topic, we will learn how to install MySQL database on Windows using the MySQL Installer method .
- MySQL is a popular open-source relational database management system that can store and manipulate data for web applications.
- MySQL can be used with various programming languages, such as Java, PHP, Python, etc., to create dynamic web pages and applications.
- To install MySQL, we need to follow these steps:

  1. Download MySQL Installer for Windows from https://dev.mysql.com/downloads/installer/ and execute it.
  2. Choose the first option: Install MySQL Products, and click Next.
  3. Accept the license agreement and click Next.
  4. Choose the setup type that suits your needs. For example, you can choose Developer Default, which includes MySQL Server, MySQL Workbench, MySQL Shell, MySQL Router, MySQL Connector/ODBC, and MySQL Connector/J.
  5. Click Next and review the products that will be installed. You can also change the installation path or add or remove products if needed.
  6. Click Execute to start the installation process. Wait for the installation to complete and click Next.
  7. Click Next to configure MySQL Server. You can choose the configuration type, such as Development Computer, Server Computer, or Dedicated Computer, depending on your usage scenario.
  8. Enter the root password and optionally create a new user account for MySQL. Click Next.
  9. Choose the default schema options and click Next.
  10. Choose the default Windows service options and click Next.
  11. Click Execute to apply the configuration. Wait for the configuration to complete and click Finish.
  12. Click Next to configure other products, such as MySQL Workbench, MySQL Shell, MySQL Router, etc. Follow the instructions on the screen and click Finish when done.
  13. Click Next to check for product updates. If there are any updates available, you can download and install them. Click Next when done.
  14. Click Finish to complete the installation and configuration of MySQL.

- To verify MySQL installation, you can open the MySQL Command Line Client from cmd and enter the root password. You should see a prompt like this:

  ```
  mysql>
  ```

- You can also use MySQL Workbench or MySQL Shell to connect to the MySQL Server and perform various tasks, such as creating databases, tables, queries, etc.
- To use MySQL with Java, you need to have the MySQL Connector/J installed, which is a JDBC driver that allows Java applications to communicate with MySQL databases. You can download it from https://dev.mysql.com/downloads/connector/j/ and add it to your classpath or project dependencies.
- To use MySQL with ODBC, you need to have the MySQL Connector/ODBC installed, which is an ODBC driver that allows ODBC-enabled applications to access MySQL databases. You can download it from https://dev.mysql.com/downloads/connector/odbc/ and configure it using the ODBC Data Source Administrator tool in Windows.
- To use session tracking API, you need to have a web server, such as Apache Tomcat, installed and configured to run Java servlets and JSP pages. You can download it from https://tomcat.apache.org/download-10.cgi and follow the installation instructions. You also need to have the Java Development Kit (JDK) installed and set the JAVA_HOME and CATALINA_HOME environment variables.
- Session tracking API is a mechanism that allows web applications to maintain state information across multiple requests from the same client. It can be implemented using various techniques, such as cookies, URL rewriting, hidden form fields, or HttpSession objects.
- Cookies are small pieces of data that are stored on the client's browser and sent to the server with each request. They can be used to store session identifiers or other information that can be retrieved by the server. Cookies can be created, read, and deleted using the javax.servlet.http.Cookie class and the javax.servlet.http.HttpServletRequest and javax.servlet.http.HttpServletResponse interfaces.
- URL rewriting is a technique that appends the session identifier to the URL of each request. It can be used when cookies are disabled or not supported by the client's browser. URL rewriting can be done using the javax.servlet.http.HttpServletResponse.encodeURL() and javax.servlet.http.HttpServletResponse.encodeRedirectURL() methods.
- Hidden form fields are input elements that are not visible to the user but can store



### Create a table which should contain at least the following fields: name, password, email-id, phone number for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To create a table in a relational database, we need to use the SQL (Structured Query Language) command `CREATE TABLE`.
- The syntax of the `CREATE TABLE` command is as follows:

```sql
CREATE TABLE table_name (
  column1 data_type constraints,
  column2 data_type constraints,
  ...
  columnN data_type constraints
);
```

- The `table_name` is the name of the table we want to create. The `column` names are the names of the fields we want to store in the table. The `data_type` specifies the type of data that can be stored in each column, such as `VARCHAR`, `INT`, `DATE`, etc. The `constraints` are optional and can be used to define rules for the data in each column, such as `NOT NULL`, `PRIMARY KEY`, `UNIQUE`, etc.
- For the given topic, we can create a table named `users` with the following fields: `name`, `password`, `email_id`, and `phone_number`. The data types and constraints for each field can vary depending on the requirements, but one possible example is:

```sql
CREATE TABLE users (
  name VARCHAR(50) NOT NULL,
  password VARCHAR(20) NOT NULL,
  email_id VARCHAR(50) PRIMARY KEY,
  phone_number VARCHAR(15) UNIQUE
);
```

- This table will store the name, password, email-id, and phone number of each user. The name and password fields cannot be empty, the email-id field is the primary key that uniquely identifies each user, and the phone number field is unique and cannot be duplicated.



### Write a java program/servlet/JSP to connect to that database and extract data from the tables and display them for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To write a java program/servlet/JSP to connect to a database and extract data from the tables and display them, you need to follow these steps:

  - Import the required packages for JDBC (Java Database Connectivity), such as `java.sql.*` and `javax.servlet.*` .
  - Load and register the JDBC driver for the database you want to connect to, such as MySQL, Oracle, etc. You can use the `Class.forName()` method to load the driver class and the `DriverManager.registerDriver()` method to register it  .
  - Establish a connection to the database using the `DriverManager.getConnection()` method, which takes the URL, username and password of the database as parameters. You can store the connection object in a `Connection` variable  .
  - Create a statement object using the `Connection.createStatement()` method, which allows you to execute SQL queries on the database. You can store the statement object in a `Statement` variable  .
  - Execute the SQL query using the `Statement.executeQuery()` method, which returns a `ResultSet` object that contains the data retrieved from the database. You can store the result set object in a `ResultSet` variable  .
  - Iterate over the result set using the `ResultSet.next()` method, which moves the cursor to the next row of data. You can access the data in each column using the `ResultSet.getXXX()` methods, where XXX is the data type of the column, such as `getString()`, `getInt()`, etc. You can display the data using the `System.out.println()` method or the `out.println()` method if you are using a servlet or JSP  .
  - Close the result set, statement and connection objects using the `ResultSet.close()`, `Statement.close()` and `Connection.close()` methods, respectively. This releases the resources and avoids memory leaks  .

- Here is an example of a java program that connects to a MySQL database and displays the data from a table called `employees`:

  ```java
  // Import the required packages
  import java.sql.*;

  public class DatabaseConnection {

    public static void main(String[] args) {

      // Declare the connection, statement and result set variables
      Connection conn = null;
      Statement stmt = null;
      ResultSet rs = null;

      try {
        // Load and register the MySQL driver
        Class.forName("com.mysql.cj.jdbc.Driver");
        DriverManager.registerDriver(new com.mysql.cj.jdbc.Driver());

        // Establish a connection to the database
        String url = "jdbc:mysql://localhost:3306/mydb";
        String user = "root";
        String password = "root";
        conn = DriverManager.getConnection(url, user, password);

        // Create a statement object
        stmt = conn.createStatement();

        // Execute a SQL query
        String sql = "SELECT * FROM employees";
        rs = stmt.executeQuery(sql);

        // Iterate over the result set and display the data
        while (rs.next()) {
          // Get the data from each column
          int id = rs.getInt("id");
          String name = rs.getString("name");
          String department = rs.getString("department");
          double salary = rs.getDouble("salary");

          // Display the data
          System.out.println("ID: " + id);
          System.out.println("Name: " + name);
          System.out.println("Department: " + department);
          System.out.println("Salary: " + salary);
          System.out.println();
        }
      } catch (Exception e) {
        // Handle any exceptions
        e.printStackTrace();
      } finally {
        // Close the result set, statement and connection objects
        try {
          if (rs != null) {
            rs.close();
          }
          if (stmt != null) {
            stmt.close();
          }
          if (conn != null) {
            conn.close();
          }
        } catch (SQLException e) {
          e.printStackTrace();
        }
      }
    }
  }
  ```
[assistant



### Insert the details of the users who register with the web site, whenever a new user clicks the submit button in the registration page for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To insert the details of the users who register with the web site, we need to use a server-side scripting language such as PHP, ASP.NET, or JSP that can interact with a database management system such as MySQL, SQL Server, or Oracle.
- The registration page should have a form that collects the user's information such as name, email, password, and any other relevant data. The form should have a submit button that sends the data to the server using the POST method.
- The server-side script should validate the user's input and check if the email is already registered in the database. If not, it should insert the user's details into a table that stores the user's information. The table should have a primary key that uniquely identifies each user, such as a user ID or an email address.
- The server-side script should also create a session for the user using the session tracking API. A session is a way of maintaining the state of the user across multiple requests. The session can store the user's ID, name, and any other data that is needed for the web site. The session can be implemented using cookies, URL rewriting, or hidden fields.
- The server-side script should then redirect the user to a welcome page that displays the user's name and a message that confirms the registration. The welcome page should also have a link to the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab. The user should be able to access the notes only if they are logged in with their session.



### Write a JSP which insert the details of the 3 or 4 users who register with the web site by using registration form for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- JSP stands for Java Server Pages, which is a technology that allows creating dynamic web pages using Java code.
- A registration form is a web page that collects user information and stores it in a database or a cache.
- To create a registration form in JSP, you need to have a table in the database that can store the user details. You also need to have a JSP file that contains the HTML code for the form and the Java code for the database connection and insertion.
- Here are the steps to create a registration form in JSP:

  1. Create a table in the database that can store the user details. For example, you can use the following SQL statement to create a table named user432 in the Oracle database:

  ```sql
  CREATE TABLE "USER432" (
    "NAME" VARCHAR2 (4000),
    "EMAIL" VARCHAR2 (4000),
    "PASS" VARCHAR2 (4000)
  )
  ```

  2. Create a JSP file that contains the HTML code for the registration form and the Java code for the database connection and insertion. For example, you can name the file as index.jsp and write the following code:

  ```jsp
  <%@ page import="java.sql.*" %>
  <html>
  <head>
  <title>Registration Form</title>
  </head>
  <body>
  <h1>Registration Form</h1>
  <form action="process.jsp">
  <input type="text" name="uname" value="Name..." onclick="this.value=''"/><br/>
  <input type="text" name="uemail" value="Email ID..." onclick="this.value=''"/><br/>
  <input type="password" name="upass" value="Password..." onclick="this.value=''"/><br/>
  <input type="submit" value="register"/>
  </form>
  </body>
  </html>
  ```

  3. Create another JSP file that contains the Java code for processing the user input and inserting it into the database. For example, you can name the file as process.jsp and write the following code:

  ```jsp
  <%@ page import="java.sql.*" %>
  <%
  String name=request.getParameter("uname");
  String email=request.getParameter("uemail");
  String pass=request.getParameter("upass");
  try{
    Class.forName("oracle.jdbc.driver.OracleDriver");
    Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","oracle");
    PreparedStatement ps=con.prepareStatement("insert into user432 values(?,?,?)");
    ps.setString(1,name);
    ps.setString(2,email);
    ps.setString(3,pass);
    int i=ps.executeUpdate();
    if(i>0){
      out.println("You are successfully registered");
    }
    else{
      out.println("Registration failed");
    }
  }
  catch(Exception e){
    e.printStackTrace();
  }
  %>
  ```

  4. Save the JSP files in the webapps folder of the Tomcat server and run the server.
  5. Open the browser and enter the URL of the index.jsp file. For example, http://localhost:8080/index.jsp
  6. Fill the registration form with the user details and click on the register button. The process.jsp file will execute and insert the user details into the database. It will also display a message indicating the success or failure of the registration.
  7. Repeat the steps 6 for 3 or 4 users who register with the web site. You can check the database table to verify the insertion of the user details.



### Authenticate the user when he submits the login form using the user name and password from the database for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To authenticate the user when he submits the login form using the user name and password from the database, we need to use JDBC and ODBC drivers that can connect to the database server and execute SQL queries.
- JDBC stands for Java Database Connectivity, which is a standard API for Java applications to interact with various types of databases. ODBC stands for Open Database Connectivity, which is a standard API for applications written in different languages to interact with various types of databases.
- Both JDBC and ODBC drivers support different authentication methods, such as personal access tokens, username and password, Kerberos integrated authentication, or IAM credentials. The authentication method depends on the type of database server and the security configuration.
- The following steps describe the general process of authenticating the user using JDBC and ODBC drivers:

  1. Create a login form that asks the user to enter the user name and password. The form should have a submit button that sends the user input to a servlet or a JSP page that handles the authentication logic.
  2. In the servlet or JSP page, load the appropriate JDBC or ODBC driver class using the Class.forName() method. For example, to load the JDBC driver for SQL Server, use Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver").
  3. Create a connection object using the DriverManager.getConnection() method. The method takes a connection URL as a parameter, which specifies the database server name, port number, database name, and authentication method. For example, to use SQL Server authentication, the connection URL can be jdbc:sqlserver://server:port;databaseName=db;user=user;password=pass. To use Kerberos authentication, the connection URL can be jdbc:sqlserver://server:port;databaseName=db;authenticationScheme=JavaKerberos.
  4. Create a statement object using the connection.createStatement() method. The statement object can execute SQL queries using the executeQuery() or executeUpdate() methods.
  5. Execute a SQL query that selects the user name and password from the login table where the user name matches the user input. For example, the query can be SELECT username, password FROM login WHERE username = ?.
  6. Use a prepared statement object to set the parameter value for the user name using the setString() method. For example, preparedStatement.setString(1, username).
  7. Execute the query using the executeQuery() method, which returns a result set object that contains the query results.
  8. Check if the result set object has any rows using the next() method. If it has, then compare the password from the result set with the user input using the getString() method. For example, if (resultSet.next() && resultSet.getString("password").equals(password)).
  9. If the password matches, then the user is authenticated and can be redirected to the welcome page or the main page of the application. If the password does not match, then the user is not authenticated and can be shown an error message or asked to try again.
  10. Close the result set, statement, and connection objects using the close() method to release the resources.



### Design and implement a simple shopping cart example with session tracking API

- Session tracking is a technique to maintain the state of a client across multiple requests to a server. It is useful for applications that need to remember the actions or preferences of a client, such as an online shopping cart.
- Session tracking can be implemented using various methods, such as cookies, URL rewriting, hidden form fields, or the HttpSession interface in servlets.
- The HttpSession interface provides a way to create and manage sessions on the server side. It allows the servlet to store and retrieve attributes associated with a client's session. It also provides methods to check the status, duration, and validity of a session.
- A simple shopping cart example with session tracking API can be designed and implemented as follows:

  - Create a servlet that handles the requests for adding, removing, and viewing items in the cart. The servlet should use the HttpSession interface to get or create a session for each client, and store the cart items as an attribute in the session object.
  - Create a JSP page that displays the cart items and allows the client to modify the cart. The JSP page should use the session implicit object to access the session attributes, and use the request implicit object to send parameters to the servlet.
  - Create a web.xml file that maps the servlet to a URL pattern, and specifies the session timeout value.
  - Deploy and run the application on a web server, and test it using a web browser.

- The following is a possible code snippet for the servlet:

```java
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/cart")
public class CartServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// Get or create a session for the client
		HttpSession session = request.getSession();
		
		// Get the action parameter from the request
		String action = request.getParameter("action");
		
		// Get the cart attribute from the session, or create a new one if not present
		List<String> cart = (List<String>) session.getAttribute("cart");
		if (cart == null) {
			cart = new ArrayList<String>();
			session.setAttribute("cart", cart);
		}
		
		// Perform the action based on the parameter value
		if (action != null) {
			if (action.equals("add")) {
				// Get the item parameter from the request
				String item = request.getParameter("item");
				if (item != null && !item.isEmpty()) {
					// Add the item to the cart
					cart.add(item);
				}
			} else if (action.equals("remove")) {
				// Get the item parameter from the request
				String item = request.getParameter("item");
				if (item != null && !item.isEmpty()) {
					// Remove the item from the cart
					cart.remove(item);
				}
			} else if (action.equals("clear")) {
				// Clear the cart
				cart.clear();
			}
		}
		
		// Set the content type and character encoding of the response
		response.setContentType("text/html");
		response.setCharacterEncoding("UTF-8");
		
		// Get the print writer of the response
		PrintWriter out = response.getWriter();
		
		// Write the HTML code for the response
		out.println("<html>");
		out.println("<head>");
		out.println("<title>Shopping Cart</title>");
		out.println("</head>");
		out.println("<body>");
		out.println("<h1>Shopping Cart</h1>");
		out.println("<p>Your cart contains " + cart.size() + " items.</p>");
		out.println("<ul>");
		for (String item : cart) {
			out.println("<li>" + item + "</li>");
		}
		out.println("</ul>");
		out.println("<p><a href='cart?action=clear'>Clear Cart</a></p>");
		out.println("<p><a href='index.jsp'>Continue Shopping</a></p>");
		out.println("</body>");
		out.println("</html>");
	}
}
```

- The following is a possible code snippet for the JSP page:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title

```


