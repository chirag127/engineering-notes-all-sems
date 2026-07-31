

## Unit 1 - Develop static web pages using HTML

- HTML stands for HyperText Markup Language. It is the standard language for creating web pages and web applications.
- HTML consists of elements that define the structure and content of a web page. Elements are enclosed by tags, which are written in angle brackets (< and >).
- HTML elements can have attributes, which provide additional information about the element. Attributes are written inside the start tag, after the element name, and consist of a name and a value separated by an equal sign (=).
- HTML elements can be nested, which means that one element can contain another element inside it. The inner element is called the child element, and the outer element is called the parent element.
- HTML elements can be classified into two types: block-level elements and inline elements. Block-level elements create a new line and occupy the whole width of the page, while inline elements do not create a new line and only occupy the space needed for their content.
- Some examples of block-level elements are `<div>`, `<p>`, `<h1>` to `<h6>`, `<ul>`, `<ol>`, `<li>`, `<table>`, `<tr>`, `<td>`, `<th>`, `<form>`, and `<section>`.
- Some examples of inline elements are `<span>`, `<a>`, `<img>`, `<input>`, `<button>`, `<label>`, `<strong>`, `<em>`, and `<br>`.
- HTML also has some special elements that do not have a closing tag, such as `<img>`, `<input>`, `<br>`, and `<hr>`. These are called self-closing or void elements.
- HTML also has some elements that can contain only text and no other elements, such as `<title>`, `<script>`, `<style>`, and `<textarea>`. These are called text-only elements.
- HTML also has some elements that can contain only other elements and no text, such as `<head>`, `<body>`, `<ul>`, `<ol>`, `<table>`, and `<form>`. These are called element-only elements.
- HTML also has some elements that can contain both text and other elements, such as `<div>`, `<p>`, `<h1>` to `<h6>`, `<li>`, `<td>`, `<th>`, `<button>`, `<label>`, `<strong>`, and `<em>`. These are called mixed-content elements.
- HTML also has some elements that are not visible on the web page, but provide metadata or instructions for the browser or the server, such as `<html>`, `<head>`, `<title>`, `<meta>`, `<link>`, `<style>`, `<script>`, and `<base>`. These are called head elements.
- HTML also has some elements that are used to create interactive web pages, such as `<form>`, `<input>`, `<button>`, `<select>`, `<option>`, `<textarea>`, and `<label>`. These are called form elements.
- HTML also has some elements that are used to create multimedia content, such as `<img>`, `<audio>`, `<video>`, `<source>`, `<track>`, and `<canvas>`. These are called media elements.
- HTML also has some elements that are used to create semantic meaning and structure for the web page, such as `<section>`, `<article>`, `<nav>`, `<header>`, `<footer>`, `<aside>`, `<main>`, and `<figure>`. These are called semantic elements.



### Write HTML/Java scripts to display your CV in navigator, your Institute website, Department Website and Tutorial website for specific subject for the notes of the Unit 1 - Develop static web pages using HTML in the subject of Web Technology Lab

- To display your CV in navigator, you can use HTML to create the structure and content of your resume, such as your name, contact information, education, skills, work experience, etc. You can also use CSS to style your resume, such as changing the font, color, layout, etc. You can also use JavaScript to add some interactivity, such as switching between light and dark themes, exporting your resume as a PDF, etc. You can use OpenCV.js to read and show images from HTML canvas or img elements . You can also use JavaScript to display a CSV file that contains your resume data. Here is an example of HTML/JavaScript code to display your CV in navigator:

```html
<html>
<head>
  <title>My Resume</title>
  <style>
    /* Add your CSS style here */
  </style>
  <script src="opencv.js"></script> <!-- Load OpenCV.js library -->
  <script>
    // Add your JavaScript code here
    function readImage() {
      // Read an image from an img element with id="my-image"
      let src = cv.imread("my-image");
      // Display the image on a canvas element with id="my-canvas"
      cv.imshow("my-canvas", src);
      // Release the image memory
      src.delete();
    }
    function readCSV() {
      // Read a CSV file from a URL
      let url = "my-resume.csv";
      // Create a new XMLHttpRequest object
      let xhr = new XMLHttpRequest();
      // Open a GET request to the URL
      xhr.open("GET", url, true);
      // Set the response type to text
      xhr.responseType = "text";
      // Define a callback function to handle the response
      xhr.onload = function() {
        // Check if the status is OK
        if (xhr.status === 200) {
          // Get the response text
          let data = xhr.responseText;
          // Split the data by line breaks
          let lines = data.split("\n");
          // Loop through the lines
          for (let i = 0; i < lines.length; i++) {
            // Split the line by commas
            let values = lines[i].split(",");
            // Display the values in a table element with id="my-table"
            let table = document.getElementById("my-table");
            // Create a new table row element
            let row = document.createElement("tr");
            // Loop through the values
            for (let j = 0; j < values.length; j++) {
              // Create a new table cell element
              let cell = document.createElement("td");
              // Create a new text node with the value
              let text = document.createTextNode(values[j]);
              // Append the text node to the cell element
              cell.appendChild(text);
              // Append the cell element to the row element
              row.appendChild(cell);
            }
            // Append the row element to the table element
            table.appendChild(row);
          }
        }
      };
      // Send the request
      xhr.send();
    }
  </script>
</head>
<body onload="readImage(); readCSV();">
  <h1>My Resume</h1>
  <img id="my-image" src="my-photo.jpg" hidden> <!-- Hide the img element -->
  <canvas id="my-canvas" width="300" height="300"></canvas> <!-- Show the canvas element -->
  <table id="my-table" border="1">
    <tr>
      <th>Name</th>
      <th>Contact</th>
      <th>Education</th>
      <th>Skills</th>
      <th>Work Experience</th>
    </tr>
  </table>
</body>
</html>
```

- To display your Institute website, Department website and Tutorial website for specific subject for the notes of the Unit 1 - Develop static web pages using HTML in the subject of Web Technology Lab, you can use HTML to create the structure and content of each website, such as the title, header, navigation, main, footer, etc. You can also use CSS to style each website, such as changing the font, color, layout, etc. You can also use JavaScript to add some interactivity, such as switching between pages, loading content dynamically,



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a possible answer to your question:

### Write an HTML program to design an entry form of student details and send it to store at database server like SQL, Oracle or MS Access for the notes of the Unit 1 - Develop static web pages using HTML in the subject of Web Technology Lab

- To design an entry form of student details, you need to use HTML elements such as `<form>`, `<input>`, `<label>`, `<select>`, `<option>`, `<button>` etc. These elements allow you to create different types of input fields, labels, drop-down lists, buttons etc. that can collect the user's information.
- To send the form data to a database server, you need to specify the `action` and `method` attributes of the `<form>` element. The `action` attribute defines the URL of the server-side script that will process the form data, and the `method` attribute defines the HTTP method to use, such as `GET` or `POST`.
- To store the form data in a database server, you need to use a server-side scripting language such as PHP, ASP.NET, Python, etc. that can connect to the database server, execute SQL queries, and handle the form data. You also need to create a database table that can store the student details, with appropriate columns and data types.
- Here is an example of an HTML program that can design an entry form of student details and send it to store at a database server like SQL, Oracle or MS Access:

```html
<html>
<head>
  <title>Student Registration Form</title>
</head>
<body>
  <h1>Student Registration Form</h1>
  <form action="process.php" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required><br>
    <label for="phone">Phone:</label>
    <input type="tel" id="phone" name="phone" required><br>
    <label for="address">Address:</label>
    <input type="text" id="address" name="address" required><br>
    <label for="hobbies">Hobbies:</label>
    <select id="hobbies" name="hobbies" multiple>
      <option value="reading">Reading</option>
      <option value="writing">Writing</option>
      <option value="coding">Coding</option>
      <option value="sports">Sports</option>
      <option value="music">Music</option>
    </select><br>
    <label for="course">Course:</label>
    <input type="radio" id="btech" name="course" value="B.Tech" checked>
    <label for="btech">B.Tech</label>
    <input type="radio" id="mtech" name="course" value="M.Tech">
    <label for="mtech">M.Tech</label>
    <input type="radio" id="phd" name="course" value="Ph.D">
    <label for="phd">Ph.D</label><br>
    <label for="gender">Gender:</label>
    <input type="radio" id="male" name="gender" value="male" checked>
    <label for="male">Male</label>
    <input type="radio" id="female" name="gender" value="female">
    <label for="female">Female</label>
    <input type="radio" id="other" name="gender" value="other">
    <label for="other">Other</label><br>
    <label for="dob">Date of Birth:</label>
    <input type="date" id="dob" name="dob" required><br>
    <button type="submit" name="submit">Submit</button>
  </form>
</body>
</html>
```
- Here is an example of a PHP script that can process the form data and store it in a MySQL database server:

```php
<?php
// Connect to the database server
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "student_db";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection

```




## Unit 2 - Develop Java programs for window/web-based applications

- Java is a popular programming language that can be used to create dynamic and interactive web applications.
- Java web applications are composed of servlets, JavaServer Pages (JSPs), JavaBeans, and other components that run on a web server and communicate with a web browser.
- Java web applications follow a model-view-controller (MVC) architecture, where the servlets handle the requests from the browser, the JSPs generate the views or the HTML pages, and the JavaBeans encapsulate the business logic and data.
- To develop Java web applications, you need the following tools and technologies:
  - A Java Development Kit (JDK) that provides the compiler and the runtime environment for Java programs.
  - A web server that supports the Java Servlet API, such as Apache Tomcat, Jetty, or GlassFish.
  - An integrated development environment (IDE) that facilitates the coding, debugging, and testing of Java web applications, such as Eclipse, NetBeans, or IntelliJ IDEA.
  - A web browser that can render HTML, CSS, and JavaScript, and execute Java applets, such as Chrome, Firefox, or Edge.
- To create a Java web application, you need to perform the following steps:
  - Create a dynamic web project in your IDE and configure the web server settings.
  - Write the servlets and JSPs that implement the functionality of your web application and place them in the appropriate folders in the web project.
  - Write the JavaBeans that store the data and logic of your web application and place them in the source folder of the web project.
  - Write the web.xml file that defines the configuration and mapping of the servlets and JSPs in your web application and place it in the WEB-INF folder of the web project.
  - Build and deploy your web project to the web server and test it using the web browser.
- Java web applications can also use various frameworks and libraries that provide additional features and functionalities, such as Spring, Hibernate, Struts, JSF, etc.
- Java web applications can also be launched using Java Web Start, which is a technology that allows users to download and run Java applications from a web browser with a single click.
- Java Web Start uses a special file called JNLP (Java Network Launching Protocol) that describes the properties and resources of the Java application and how to launch it.
- To use Java Web Start, you need to create a JNLP file for your Java application and place it on a web server, and then provide a link to the JNLP file on your web page.
- When the user clicks on the link, the JNLP file is downloaded and executed by the Java Web Start software, which then downloads and launches the Java application.



# Write programs using JavaScript for Web Page to display browsers information

JavaScript is a scripting language that can be used to create dynamic and interactive web pages. One of the features of JavaScript is that it can access the information about the visitor's browser, such as the name, version, platform, and user agent. This information can be useful for various purposes, such as customizing the web page content, detecting browser compatibility, or performing analytics.

There are different ways to write programs using JavaScript for web page to display browsers information. Here are some of the common methods:

- **Using the window.navigator object**: The window.navigator object is a built-in object that contains the information about the visitor's browser. Some of the properties of this object are:

  - `navigator.appName`: The name of the browser, such as Netscape or Microsoft Internet Explorer.
  - `navigator.appVersion`: The version of the browser, such as 5.0 or 11.0.
  - `navigator.platform`: The operating system of the browser, such as Win32 or Linux.
  - `navigator.userAgent`: The user agent string of the browser, which contains more detailed information about the browser and its features.

  To use the window.navigator object, we can write a simple HTML page with a script tag that displays the browser information in an alert box or on the web page itself. For example:

  ```html
  <html>
  <head>
    <title>Browser Information</title>
  </head>
  <body>
    <script>
      // Display the browser information in an alert box
      alert(
        "Browser Name: " +
          navigator.appName +
          "\n" +
          "Browser Version: " +
          navigator.appVersion +
          "\n" +
          "Browser Platform: " +
          navigator.platform +
          "\n" +
          "Browser User Agent: " +
          navigator.userAgent
      );

      // Display the browser information on the web page
      document.write(
        "<h1>Browser Information</h1>" +
          "<p>Browser Name: " +
          navigator.appName +
          "</p>" +
          "<p>Browser Version: " +
          navigator.appVersion +
          "</p>" +
          "<p>Browser Platform: " +
          navigator.platform +
          "</p>" +
          "<p>Browser User Agent: " +
          navigator.userAgent +
          "</p>"
      );
    </script>
  </body>
  </html>
  ```

  However, using the window.navigator object has some limitations and drawbacks. For instance:

  - Different browsers can use the same name, such as Netscape or Mozilla, which can cause confusion or false detection.
  - The navigator data can be changed by the browser owner or the user, which can make it unreliable or inaccurate.
  - Some browsers misidentify themselves to bypass site tests or to mimic other browsers, which can lead to incorrect results.

- **Using a detection library**: A detection library is a third-party JavaScript library that can help to detect the browser and its features more accurately and reliably. One of the popular detection libraries is Bowser, which can parse the user agent string and provide a simple and consistent API to access the browser information. To use Bowser, we need to include the library in our HTML page and then use its methods and properties to get the browser information. For example:

  ```html
  <html>
  <head>
    <title>Browser Information</title>
    <!-- Include the Bowser library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bowser/2.11.0/bowser.min.js"></script>
  </head>
  <body>
    <script>
      // Get the browser information using Bowser
      var browser = bowser.getParser(window.navigator.userAgent);

      // Display the browser information in an alert box
      alert(
        "Browser Name: " +
          browser.getBrowserName() +
          "\n" +
          "Browser Version: " +
          browser.getBrowserVersion() +
          "\n" +
          "Browser Platform: " +
          browser.getOSName() +
          "\n" +
          "Browser User Agent: " +
          browser.getUA()
      );

      // Display the browser information on the web page
      document.write(
        "<h1>Browser Information</h1>" +
          "<p>Browser Name: " +
          browser.getBrowserName() +
          "</p>" +
          "<p>Browser Version: " +
          browser.getBrowserVersion() +
          "</p>" +
          "<p

```




# Write a Java applet to display the Application Program screen i.e. calculator and other for the notes of the Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab

- A Java applet is a small Java application that can be embedded with web browsers to display dynamic content and can run on the client-side directly .
- A Java applet program for a calculator can use a grid layout to arrange buttons for the digits and for the addition, subtraction, multiplication, and division operations.
- A Java applet program for a calculator can also use a text field to display the first and second numbers and the result.
- A Java applet program for a calculator can add an action listener to each button to perform the corresponding arithmetic operation.
- A Java applet program for a calculator can use the `java.applet.Applet` class and the `java.awt` package to create the user interface and handle the events   .
- A Java applet program for a calculator can be compiled and run using the `appletviewer` tool or a web browser that supports Java .

- Here is an example of a Java applet program for a calculator:

```java
// Import the necessary packages
import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;

// Define the applet class
public class Calculator extends Applet implements ActionListener {
  // Declare the components
  TextField tf1, tf2, tf3;
  Button b1, b2, b3, b4;
  Label l1, l2, l3, l4;

  // Initialize the components
  public void init() {
    // Create the components
    tf1 = new TextField();
    tf2 = new TextField();
    tf3 = new TextField();
    b1 = new Button("+");
    b2 = new Button("-");
    b3 = new Button("*");
    b4 = new Button("/");
    l1 = new Label("First Number");
    l2 = new Label("Second Number");
    l3 = new Label("Result");
    l4 = new Label("Calculator");

    // Set the layout
    setLayout(new GridLayout(5, 2));

    // Add the components to the applet
    add(l4);
    add(new Label()); // Empty label for spacing
    add(l1);
    add(tf1);
    add(l2);
    add(tf2);
    add(l3);
    add(tf3);
    add(b1);
    add(b2);
    add(b3);
    add(b4);

    // Add action listeners to the buttons
    b1.addActionListener(this);
    b2.addActionListener(this);
    b3.addActionListener(this);
    b4.addActionListener(this);

    // Set the result text field as non-editable
    tf3.setEditable(false);
  }

  // Handle the button clicks
  public void actionPerformed(ActionEvent e) {
    // Get the numbers from the text fields
    int num1 = Integer.parseInt(tf1.getText());
    int num2 = Integer.parseInt(tf2.getText());

    // Get the source of the event
    Object source = e.getSource();

    // Perform the corresponding operation
    if (source == b1) {
      // Addition
      tf3.setText(String.valueOf(num1 + num2));
    } else if (source == b2) {
      // Subtraction
      tf3.setText(String.valueOf(num1 - num2));
    } else if (source == b3) {
      // Multiplication
      tf3.setText(String.valueOf(num1 * num2));
    } else if (source == b4) {
      // Division
      tf3.setText(String.valueOf(num1 / num2));
    }
  }
}
```



```
## Unit 3 - Design dynamic web pages using Javascript and XML

- Javascript is a scripting language that can be embedded in HTML documents to add interactivity, functionality, and dynamic features to web pages.
- XML is a markup language that can be used to store and exchange structured data in a human-readable and machine-readable format.
- Some of the topics covered in this unit are:

  - How to use Javascript variables, data types, operators, expressions, statements, and functions to perform calculations and manipulate data.
  - How to use Javascript events, event handlers, and event listeners to respond to user actions and changes in the web page.
  - How to use Javascript objects, methods, and properties to access and manipulate elements of the Document Object Model (DOM), which is a representation of the web page structure and content.
  - How to use Javascript arrays, loops, and conditional statements to store and process multiple values and perform repetitive tasks.
  - How to use Javascript built-in objects, such as Math, Date, String, and Number, to perform common operations and conversions.
  - How to use Javascript to validate user input, handle errors, and debug code using tools such as console, alert, and try-catch-finally blocks.
  - How to use Javascript to create and manipulate cookies, which are small pieces of data stored on the user's browser, to remember user preferences and settings.
  - How to use Javascript to communicate with web servers using methods such as XMLHttpRequest, Fetch, and JSONP, to send and receive data asynchronously without reloading the web page.
  - How to use XML to create and parse well-formed and valid documents that follow a predefined structure and syntax.
  - How to use XML namespaces, attributes, and elements to define and organize data in XML documents.
  - How to use XML schemas and Document Type Definitions (DTDs) to specify the rules and constraints for the structure and content of XML documents.
  - How to use XML technologies, such as XPath, XSLT, and XQuery, to query, transform, and manipulate XML data.
  - How to use XML with Javascript to create and display dynamic web pages that can adapt to different data sources and formats.
```



### Writing program in XML for creation of DTD, which specifies set of rules for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A DTD (Document Type Declaration) is a way to describe the structure, elements and attributes of an XML document  .
- A DTD can be used to validate the XML document against the grammatical rules of the XML language .
- A DTD can be declared internally or externally to the XML document .
- An internal DTD is written inside the XML document, within the `<!DOCTYPE>` declaration .
- An external DTD is written in a separate file, and referenced by the XML document using the `SYSTEM` or `PUBLIC` keyword .
- A DTD defines the elements and attributes of an XML document using the following syntax  :

  - `<!ELEMENT element-name category>`: defines an element and its category, such as empty, any, mixed, or children.
  - `<!ATTLIST element-name attribute-name attribute-type attribute-value>`: defines an attribute and its type and value for an element.
  - `<!ENTITY entity-name value>`: defines an entity and its value, which can be a text, a character, or an external file.

- A DTD can also use parameter entities, which are entities that can be used within the DTD itself .
- A DTD can also use conditional sections, which are sections of the DTD that are included or ignored based on some conditions .

- An example of a DTD that specifies the rules for the notes of Unit 3 is:

```xml
<!-- This is an external DTD file named notes.dtd -->
<!ELEMENT notes (unit)+>
<!ELEMENT unit (title, content)>
<!ATTLIST unit number CDATA #REQUIRED>
<!ELEMENT title (#PCDATA)>
<!ELEMENT content (paragraph | list | code)*>
<!ELEMENT paragraph (#PCDATA)>
<!ELEMENT list (item)+>
<!ATTLIST list type (ordered | unordered) #REQUIRED>
<!ELEMENT item (#PCDATA)>
<!ELEMENT code (#CDATA)>
<!ENTITY js "Javascript">
<!ENTITY xml "XML">
<!ENTITY % common "<!ENTITY js 'Javascript'><!ENTITY xml 'XML'>">
%common;
```

- An example of an XML document that uses the above DTD is:

```xml
<?xml version="1.0"?>
<!DOCTYPE notes SYSTEM "notes.dtd">
<notes>
  <unit number="3">
    <title>Design dynamic web pages using &js; and &xml;</title>
    <content>
      <paragraph>This unit covers the following topics:</paragraph>
      <list type="ordered">
        <item>Introduction to &js;</item>
        <item>Variables, data types, operators, and expressions in &js;</item>
        <item>Control structures, functions, and objects in &js;</item>
        <item>DOM manipulation and event handling in &js;</item>
        <item>Introduction to &xml;</item>
        <item>DTD and Schema for &xml; validation</item>
        <item>XPath and XSLT for &xml; transformation</item>
        <item>AJAX for asynchronous communication between &js; and &xml;</item>
      </list>
      <paragraph>The following is an example of a simple &js; program:</paragraph>
      <code><![CDATA[
        // This is a comment
        document.write("Hello, world!"); // This writes a message to the web page
      ]]></code>
    </content>
  </unit>
</notes>
```



# Create a style sheet in CSS/XSL & display the document in internet explorer for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A style sheet is a set of rules that defines how to format and present an XML document.
- CSS (Cascading Style Sheets) is a language for defining style rules for HTML and XML documents.
- XSL (Extensible Stylesheet Language) is a language for transforming and formatting XML documents.
- XSL consists of three parts: XSLT, XPath, and XSL-FO.
- XSLT (XSL Transformations) is a language for transforming XML documents into other formats, such as HTML, XML, or plain text.
- XPath (XML Path Language) is a language for selecting nodes and values from an XML document.
- XSL-FO (XSL Formatting Objects) is a language for defining the layout and presentation of XML documents.
- To create a style sheet in CSS/XSL, you need to follow these steps:

  1. Create an XML document that contains the data and structure of your web page.
  2. Create a CSS file that defines the style rules for your web page, such as fonts, colors, margins, etc.
  3. Create an XSL file that defines the transformation rules for your web page, such as how to select and display the data from the XML document, how to apply the CSS style rules, etc.
  4. Link the XML document to the XSL file using the `<?xml-stylesheet?>` processing instruction, which specifies the type, href, and media attributes of the XSL file.
  5. Link the XSL file to the CSS file using the `<xsl:import>` or `<xsl:include>` element, which specifies the href attribute of the CSS file.
  6. Save the XML, XSL, and CSS files in the same folder or directory.
  7. Open the XML file in Internet Explorer, which will apply the XSL transformation and display the web page according to the CSS style rules.

- Here is an example of an XML document that contains some notes for Unit 3:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="notes.xsl"?>
<notes>
  <unit>
    <title>Design dynamic web pages using Javascript and XML</title>
    <topics>
      <topic>
        <name>Javascript</name>
        <description>Javascript is a scripting language that can be embedded in HTML documents to add interactivity and functionality to web pages.</description>
      </topic>
      <topic>
        <name>XML</name>
        <description>XML is a markup language that can be used to store and exchange structured data.</description>
      </topic>
      <topic>
        <name>AJAX</name>
        <description>AJAX is a technique that uses Javascript and XML to communicate with a server and update a web page without reloading it.</description>
      </topic>
    </topics>
  </unit>
</notes>
```

- Here is an example of a CSS file that defines some style rules for the web page:

```css
body {
  font-family: Arial, sans-serif;
  background-color: lightblue;
}

h1 {
  color: white;
  background-color: navy;
  text-align: center;
}

h2 {
  color: navy;
  margin-left: 20px;
}

p {
  margin-left: 40px;
}
```

- Here is an example of an XSL file that defines the transformation rules for the web page:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <!-- Import the CSS file -->
  <xsl:import href="notes.css"/>
  <!-- Output method is HTML -->
  <xsl:output method="html"/>
  <!-- Template for the root element -->
  <xsl:template match="/">
    <!-- Create the HTML document -->
    <html>
      <head>
        <title>Notes for Unit 3</title>
      </head>
      <body>
        <!-- Apply the template for the unit element -->
        <xsl:apply-templates select="notes/unit"/>
      </body>
    </html>
  </xsl:template>
  <!-- Template for the unit element -->

```




## Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP

- A dynamic web page is a web page that can display different content or layout depending on the user's input, preferences, or other factors  .
- A server-side dynamic web page is a web page whose construction is controlled by an application server processing server-side scripts.
- Server-side scripts are programs that run on the web server and generate HTML or other output that is sent to the web browser .
- Examples of popular server-side web languages include PHP, Python, Ruby, C#, and JavaScript (NodeJS).
- In this unit, we will learn how to design dynamic web pages using three server-side web languages: ASP, JSP, and PHP.
- ASP stands for Active Server Pages, and it is a Microsoft technology that allows us to create dynamic web pages using VBScript or JScript.
- JSP stands for Java Server Pages, and it is a Java technology that allows us to create dynamic web pages using Java code or custom tags.
- PHP stands for Hypertext Preprocessor, and it is an open-source language that allows us to create dynamic web pages using PHP code embedded in HTML.
- The advantages of using server-side dynamic web pages are:
  - They can provide personalized and interactive content to the users based on their input, preferences, or other factors .
  - They can reduce the network traffic and the load on the web browser by performing complex tasks on the web server .
  - They can access and manipulate data stored in databases or other sources on the web server .
- The disadvantages of using server-side dynamic web pages are:
  - They require more processing power and memory on the web server, which can affect the performance and scalability of the web application .
  - They can expose the server-side code and logic to the web browser, which can pose security risks or allow unauthorized access to the web server .
  - They can be incompatible with some web browsers or devices, which can affect the usability and accessibility of the web application .

: Dynamic web page - Wikipedia
: Dynamic Website | How Dynamic Website works? | Uses of Website - EDUCBA
: Dynamic Web Pages In Java | Java Tutorial For Beginners | Edureka
: Server-side website programming - Learn web development | MDN - Mozilla
: Introduction to the server side - Learn web development | MDN - Mozilla
: Dynamic Websites - GeeksforGeeks
: ASP Introduction - W3Schools
: JSP Introduction - W3Schools
: PHP Introduction - W3Schools



### Program to illustrate JDBC connectivity for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

JDBC stands for Java Database Connectivity, which is an API that allows Java programs to interact with various types of databases. JDBC provides a standard interface for connecting to different databases, executing queries, and retrieving results.

To illustrate JDBC connectivity, we will use a simple example of a web page that displays the details of students from a database. The web page will be written in JSP, which is a server-side technology that allows embedding Java code in HTML. The database will be MySQL, which is a popular open-source relational database management system.

The steps involved in creating the web page are:

1. Create a database and a table in MySQL. For this example, we will create a database named `webtech` and a table named `students` with the following schema:

| Column | Type | Description |
|--------|------|-------------|
| id | int | The primary key of the table |
| name | varchar(50) | The name of the student |
| course | varchar(20) | The course enrolled by the student |
| marks | int | The marks obtained by the student |

We can use the following SQL commands to create the database and the table:

```sql
CREATE DATABASE webtech;
USE webtech;
CREATE TABLE students (
  id int PRIMARY KEY,
  name varchar(50),
  course varchar(20),
  marks int
);
```

2. Insert some sample data into the table. We can use the following SQL commands to insert some sample data:

```sql
INSERT INTO students VALUES (1, 'Alice', 'B.Tech', 85);
INSERT INTO students VALUES (2, 'Bob', 'M.Tech', 90);
INSERT INTO students VALUES (3, 'Charlie', 'B.Sc', 75);
INSERT INTO students VALUES (4, 'David', 'M.Sc', 80);
```

3. Create a JSP page that connects to the database and displays the data from the table. We will name the JSP page as `students.jsp` and save it in the web server's directory. The JSP page will have the following code:

```jsp
<%@ page import="java.sql.*" %> <!-- Import the JDBC classes -->
<html>
<head>
  <title>Students Details</title>
</head>
<body>
  <h1>Students Details</h1>
  <table border="1">
    <tr>
      <th>ID</th>
      <th>Name</th>
      <th>Course</th>
      <th>Marks</th>
    </tr>
    <% // Start of Java code
      // Load the JDBC driver for MySQL
      Class.forName("com.mysql.jdbc.Driver");
      // Establish a connection to the database
      Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/webtech", "root", "root");
      // Create a statement object to execute queries
      Statement stmt = con.createStatement();
      // Execute a query to select all records from the students table
      ResultSet rs = stmt.executeQuery("SELECT * FROM students");
      // Loop through the result set and display the data in the table
      while (rs.next()) {
        // Get the data from the current row
        int id = rs.getInt("id");
        String name = rs.getString("name");
        String course = rs.getString("course");
        int marks = rs.getInt("marks");
        // Print the data in a table row
        out.println("<tr>");
        out.println("<td>" + id + "</td>");
        out.println("<td>" + name + "</td>");
        out.println("<td>" + course + "</td>");
        out.println("<td>" + marks + "</td>");
        out.println("</tr>");
      }
      // Close the result set, statement, and connection objects
      rs.close();
      stmt.close();
      con.close();
    %> // End of Java code
  </table>
</body>
</html>
```

4. Run the JSP page on the web browser. The web browser will send a request to the web server, which will execute the JSP page and send the HTML output to the browser. The browser will display the web page as shown below:

| ID | Name | Course | Marks |
|----|------|--------|-------|
| 1 | Alice | B.Tech | 85 |
| 2 | Bob | M.Tech | 90 |
| 3 | Charlie | B.Sc | 75 |
| 4 | David | M.Sc | 80 |

This is how we can illustrate JDBC connectivity for the notes of the



### Program for maintaining database by sending queries for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

- A dynamic web page is a web page that can change its content or layout depending on the user's input, preferences, or environment.
- A dynamic web page can use server-side scripting to generate mutable content. Server-side scripting is the technique of using a programming language that runs on the web server to create web pages.
- Some of the common server-side languages are PHP, Perl, ASP, ASP.NET, JSP, and ColdFusion. These languages can use the Common Gateway Interface (CGI) to communicate with the web server and the database.
- A database is a collection of structured data that can be accessed, manipulated, and updated by the server-side language. A database can store information such as user profiles, product details, orders, etc.
- A query is a request for data or information from a database. A query can be written in a specific language such as SQL (Structured Query Language) or NoSQL (Not only SQL) depending on the type of database.
- To maintain a database by sending queries, the server-side language needs to perform the following steps:
  - Establish a connection with the database using the appropriate driver or library.
  - Create a query string that specifies the data or information to be retrieved, inserted, updated, or deleted from the database.
  - Execute the query string using the appropriate method or function of the driver or library.
  - Fetch the results of the query execution and store them in a variable or an array.
  - Close the connection with the database.
- The following are some examples of how to maintain a database by sending queries using different server-side languages:

  - PHP: PHP is a widely used open source scripting language that can be embedded in HTML. PHP can use various extensions or libraries to connect with different types of databases such as MySQL, PostgreSQL, SQLite, etc.
    - Example: The following code snippet shows how to connect to a MySQL database, create a query string to select all the records from a table named `notes`, execute the query, and display the results in a HTML table.

    ```php
    <?php
    // Create a connection with the database
    $conn = mysqli_connect("localhost", "username", "password", "database_name");

    // Check if the connection is successful
    if (!$conn) {
      die("Connection failed: " . mysqli_connect_error());
    }

    // Create a query string to select all the records from the notes table
    $sql = "SELECT * FROM notes";

    // Execute the query and store the result in a variable
    $result = mysqli_query($conn, $sql);

    // Check if the query returned any records
    if (mysqli_num_rows($result) > 0) {
      // Create a HTML table to display the results
      echo "<table border='1'>";
      echo "<tr><th>ID</th><th>Title</th><th>Content</th></tr>";

      // Loop through the result array and fetch each record
      while($row = mysqli_fetch_assoc($result)) {
        // Display each record in a table row
        echo "<tr><td>" . $row["id"] . "</td><td>" . $row["title"] . "</td><td>" . $row["content"] . "</td></tr>";
      }

      // Close the HTML table
      echo "</table>";
    } else {
      // Display a message if no records are found
      echo "No notes found";
    }

    // Close the connection with the database
    mysqli_close($conn);
    ?>
    ```

  - ASP: ASP (Active Server Pages) is a server-side scripting technology developed by Microsoft that can run on Windows servers. ASP can use various components or objects to connect with different types of databases such as Access, SQL Server, Oracle, etc.
    - Example: The following code snippet shows how to connect to an Access database, create a query string to select all the records from a table named `notes`, execute the query, and display the results in a HTML table.

    ```asp
    <% 
    ' Create a connection object
    Set conn = Server.CreateObject("ADODB.Connection")

    ' Specify the connection string to the database
    conn.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4

```




### Design and implement a simple servlet book query with the help of JDBC & SQL

A servlet is a Java class that runs on a web server and handles HTTP requests and responses. JDBC is a Java API that allows Java programs to interact with databases using SQL commands. SQL is a language for querying and manipulating data in relational databases.

To design and implement a simple servlet book query with the help of JDBC & SQL, we need to follow these steps:

- Create a database and a table to store the book information, such as title, author, price, etc. For example, we can use MySQL as the database and create a table called books with the following SQL statement:

```sql
CREATE TABLE books (
  id INT PRIMARY KEY,
  title VARCHAR(50),
  author VARCHAR(50),
  price DECIMAL(10,2)
);
```

- Insert some sample data into the books table using SQL statements, such as:

```sql
INSERT INTO books VALUES (1, 'Java: The Complete Reference', 'Herbert Schildt', 39.99);
INSERT INTO books VALUES (2, 'Head First Java', 'Kathy Sierra and Bert Bates', 29.99);
INSERT INTO books VALUES (3, 'Effective Java', 'Joshua Bloch', 49.99);
```

- Download and install a web server that supports servlets, such as Apache Tomcat, and configure it to run on a specific port, such as 8080.
- Download and copy the JDBC driver for the database, such as mysql-connector.jar, to the web server's lib folder, such as apache-tomcat/lib.
- Create a Java servlet class that extends HttpServlet and overrides the doGet method to handle the HTTP GET requests. In the doGet method, we need to:

  - Get the HTTP request parameters, such as the book id, from the request object.
  - Load the JDBC driver class and establish a connection to the database using the DriverManager class and the connection URL, username, and password.
  - Create a SQL SELECT query to fetch the book information from the books table based on the book id parameter.
  - Execute the query using a PreparedStatement object and store the result in a ResultSet object.
  - Set the content type of the HTTP response to text/html using the response object.
  - Get the PrintWriter object from the response object to write the HTML output to the browser.
  - Write the HTML code to display the book information in a table format, such as:

```html
<html>
<head>
  <title>Book Query</title>
</head>
<body>
  <h1>Book Query</h1>
  <table border="1">
    <tr>
      <th>ID</th>
      <th>Title</th>
      <th>Author</th>
      <th>Price</th>
    </tr>
    <tr>
      <td>1</td>
      <td>Java: The Complete Reference</td>
      <td>Herbert Schildt</td>
      <td>39.99</td>
    </tr>
  </table>
</body>
</html>
```

  - Close the ResultSet, PreparedStatement, and Connection objects to release the resources.

- Compile the servlet class and copy the class file to the web server's webapps folder, such as apache-tomcat/webapps/ROOT/WEB-INF/classes.
- Create a web.xml file in the web server's webapps folder, such as apache-tomcat/webapps/ROOT/WEB-INF, to map the servlet class to a URL pattern, such as /bookquery. For example, the web.xml file can look like this:

```xml
<web-app>
  <servlet>
    <servlet-name>BookQueryServlet</servlet-name>
    <servlet-class>BookQueryServlet</servlet-class>
  </servlet>
  <servlet-mapping>
    <servlet-name>BookQueryServlet</servlet-name>
    <url-pattern>/bookquery</url-pattern>
  </servlet-mapping>
</web-app>
```




### Create MS Access Database

- To create a database in MS Access, you can follow these steps:
  - Open Access. If Access is already open, select File > New.
  - Select Blank database, or select a template.
  - Enter a name for the database, select a location, and then select Create.
  - If needed, select Enable content in the yellow message bar when the database opens.
- To create a table in the database, you can follow these steps:
  - On the Create tab, in the Tables group, click Table.
  - Access adds a new, blank table to your database.
  - Note: You do not need to follow this step if you open a new, blank database, but you will need to follow it whenever you need to add a table to the database.
  - Start typing in the first cell of the Click to Add column. As you type, Access assigns a data type to the field based on the values that you enter or you can assign the data type and format for the field.
  - Press TAB or ENTER to move to the next field. Repeat this step until you have entered all the fields that you want in your table.
  - To save the table, press CTRL+S, or click Save on the Quick Access Toolbar. Enter a name for the table and click OK.



## Unit 5 - Design server site applications using JDDC,ODBC and section tracking API

- JDDC stands for Java Database Connectivity, which is a standard Java API for connecting to relational databases from Java applications. It provides a uniform interface for executing SQL statements, retrieving results, and handling errors. JDDC supports various types of drivers, such as Type 1 (JDBC-ODBC bridge), Type 2 (native API), Type 3 (network protocol), and Type 4 (pure Java).
- ODBC stands for Open Database Connectivity, which is a standard API for accessing different types of data sources, such as relational databases, spreadsheets, text files, etc. ODBC is independent of any specific DBMS or operating system, and it allows applications to use the same code to access different data sources. ODBC drivers are software components that implement the ODBC API and communicate with the underlying data source.
- Section tracking API is a term that refers to the methods and techniques for maintaining the state of a user session across multiple requests in a web application. Section tracking is necessary because HTTP is a stateless protocol, which means that each request is independent and does not carry any information about previous requests. Section tracking API can use various mechanisms, such as cookies, URL rewriting, hidden form fields, or server-side objects, to store and retrieve session data. Section tracking API can enable features such as authentication, personalization, shopping carts, etc. in web applications.



### Install TOMCAT web server and APACHE

Tomcat is an open source web server and servlet container that supports Java applications. Apache is a popular web server that can work with Tomcat to serve dynamic web pages. To install and configure Tomcat and Apache, follow these steps:

1. Install Java. Tomcat requires Java to run, so you need to install a Java Development Kit (JDK) on your system. You can download the latest JDK from https://www.oracle.com/java/technologies/downloads/ and follow the installation instructions for your operating system.
2. Create a Tomcat system user. It is not recommended to run Tomcat as the root user, as it poses a security risk. You can create a dedicated user and group for Tomcat with the following commands:

```bash
sudo groupadd tomcat
sudo useradd -s /bin/false -g tomcat -d /opt/tomcat tomcat
```

3. Install and configure Tomcat. You can download the latest version of Tomcat from https://tomcat.apache.org/download-10.cgi and extract the files to a suitable location, such as /opt/tomcat. You can also change the ownership and permissions of the Tomcat files to the tomcat user and group with the following commands:

```bash
sudo chown -R tomcat:tomcat /opt/tomcat
sudo chmod +x /opt/tomcat/bin/*.sh
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

You can also modify the environment variables according to your Java and Tomcat settings. After creating the file, you need to reload the systemd daemon and enable the Tomcat service with the following commands:

```bash
sudo systemctl daemon-reload
sudo systemctl enable tomcat
```

You can then start, stop, or check the status of the Tomcat service with the following commands:

```bash
sudo systemctl start tomcat
sudo systemctl stop tomcat
sudo systemctl status tomcat
```

5. Install Apache HTTP Server. You can install Apache from the official repositories of your operating system using the package manager. For example, on Ubuntu, you can use the following command:

```bash
sudo apt install apache2
```

You can also configure Apache according to your needs, such as changing the document root, enabling SSL, or adding virtual hosts. For more details, see https://httpd.apache.org/docs/2.4/.
6. Configure Tomcat to work with Apache. To connect Tomcat and Apache, you need to use a connector module called mod_jk. You can download the latest version of mod_jk from https://tomcat.apache.org/download-connectors.cgi and compile it from source. Alternatively, you can install it from the official repositories of your operating system using the package manager. For example, on Ubuntu, you can use the following command:

```bash
sudo apt install libapache2-mod-jk
```

You also need to configure mod_jk to communicate with Tomcat. You can create a file named /etc/apache2/workers.properties with the following content:

```ini
worker.list=worker1
worker.worker1.type=ajp13
worker

```




### Access the above developed static web pages for books web site, using these servers by putting the web pages developed for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To access the static web pages for books web site, you need to have a web server that can host and serve the HTML files. You can use any web server software such as Apache, Nginx, IIS, etc. You also need to configure the web server to point to the directory where the HTML files are stored.
- To put the web pages developed for the notes of the Unit 5, you need to have a database server that can store and retrieve the data for the server site applications. You can use any database server software such as MySQL, PostgreSQL, Oracle, etc. You also need to install and configure the JDBC and ODBC drivers that can connect the web server and the database server. You also need to implement the session tracking API that can maintain the state of the user across multiple requests.
- To design the server site applications using JDBC, ODBC and session tracking API, you need to have a programming language that can run on the web server and interact with the database server. You can use any programming language such as Java, PHP, Python, etc. You also need to use the JDBC and ODBC APIs to execute SQL queries and manipulate the data in the database. You also need to use the session tracking API to create, store, and retrieve the session objects that can store the user information and preferences.
- The following are the steps to access the static web pages for books web site and put the web pages developed for the notes of the Unit 5:

  - Install and configure the web server software on your machine. Make sure the web server is running and listening on a port (usually 80 or 443).
  - Install and configure the database server software on your machine or another machine. Make sure the database server is running and listening on a port (usually 3306 or 5432).
  - Install and configure the JDBC and ODBC drivers on your machine. Make sure the drivers are compatible with the web server and the database server software.
  - Create a database and a table for the server site applications. Populate the table with some sample data.
  - Create a directory for the static web pages for books web site. Copy the HTML files from the source to the directory. Make sure the web server can access the directory and the HTML files.
  - Create a directory for the web pages developed for the notes of the Unit 5. Write the code for the server site applications using JDBC, ODBC and session tracking API. Make sure the code can access the database and the session objects.
  - Access the static web pages for books web site by typing the URL of the web server and the directory name in the browser. For example, http://localhost/books/
  - Access the web pages developed for the notes of the Unit 5 by typing the URL of the web server and the directory name in the browser. For example, http://localhost/notes/



### Assume four users user1, user2, user3 and user4 having the passwords pwd1, pwd2, pwd3 and pwd4 respectively for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- The notes of the Unit 5 are stored in a database on a web server that can be accessed by the users through a web browser.
- The web server uses Java Database Connectivity (JDBC) to connect to the database and execute SQL queries to retrieve or update the notes.
- The web server also uses Open Database Connectivity (ODBC) to provide a standard interface for different database systems and drivers.
- The web server uses session tracking API to maintain the state of each user and authenticate them with their passwords.
- The session tracking API can use cookies, URL rewriting, hidden form fields or HTTP sessions to store the session information of each user.
- The web server can use servlets, JavaServer Pages (JSP) or JavaServer Faces (JSF) to generate dynamic web pages that display the notes of the Unit 5 to the users.
- The web server can also use filters, listeners and custom tags to enhance the functionality and performance of the web application.
- The web server can use Model-View-Controller (MVC) design pattern to separate the business logic, presentation logic and data access logic of the web application.
- The web server can use JavaBeans, Enterprise JavaBeans (EJB) or Java Persistence API (JPA) to create reusable components that encapsulate the data and behavior of the notes of the Unit 5.
- The web server can use Java Naming and Directory Interface (JNDI) to locate and access the database and other resources on the network.



# Servlet for JDDC,ODBC and section tracking API

- A servlet is a Java program that runs on a web server or application server and handles requests from web clients.
- JDBC (Java Database Connectivity) is an API that allows Java programs to connect and interact with various types of databases using a common interface.
- ODBC (Open Database Connectivity) is an older API that allows programs written in different languages and platforms to connect and interact with various types of databases using a common interface.
- JDBC-ODBC Bridge is a type of JDBC driver that uses ODBC as an intermediate layer to communicate with the database. It is platform-dependent and not recommended for production use.
- Section tracking API is a feature of servlets that allows them to maintain state information across multiple requests from the same client. It can be implemented using cookies, URL rewriting, hidden form fields, or HttpSession objects.

## Steps to write a servlet for JDDC,ODBC and section tracking API

1. Import the required packages, such as javax.servlet.*, javax.servlet.http.*, and java.sql.*.
2. Define a public class that extends HttpServlet and implements the doGet() or doPost() method, depending on the type of request.
3. Load the JDBC-ODBC Bridge driver using Class.forName("sun.jdbc.odbc.JdbcOdbcDriver").
4. Establish a connection to the database using DriverManager.getConnection("jdbc:odbc:dsn", "username", "password"), where dsn is the name of the data source configured in the ODBC administrator.
5. Create a Statement or PreparedStatement object using the connection object and execute a SQL query using executeQuery() or executeUpdate() methods.
6. Process the ResultSet object returned by executeQuery() or the int value returned by executeUpdate() to obtain the desired results.
7. Use the response object to write the output to the web client, such as response.setContentType("text/html"), response.getWriter().println("some html code"), etc.
8. Use the request object to get the parameters or attributes from the web client, such as request.getParameter("name"), request.getAttribute("name"), etc.
9. Use the section tracking API to store or retrieve state information across multiple requests, such as request.getSession().setAttribute("name", "value"), request.getSession().getAttribute("name"), etc.
10. Close the ResultSet, Statement, and Connection objects using the close() method.



### Create a Cookie and add these four user id’s and passwords to this Cookie for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A cookie is a small piece of data that is stored by the browser and sent to the server with every request. Cookies can be used to store user preferences, session information, authentication details, etc.
- To create a cookie in Java, we can use the `Cookie` class from the `javax.servlet.http` package. We can create an object of this class and pass a name and a value as parameters to the constructor. For example:

```java
Cookie cookie = new Cookie("username", "Alice");
```

- To add a cookie to the response, we can use the `addCookie()` method of the `HttpServletResponse` interface. This method takes a `Cookie` object as an argument and adds it to the response header. For example:

```java
response.addCookie(cookie);
```

- To read a cookie from the request, we can use the `getCookies()` method of the `HttpServletRequest` interface. This method returns an array of `Cookie` objects that are associated with the request. We can loop through this array and find the cookie we want by using the `getName()` and `getValue()` methods of the `Cookie` class. For example:

```java
Cookie[] cookies = request.getCookies();
if (cookies != null) {
  for (Cookie c : cookies) {
    if (c.getName().equals("username")) {
      String username = c.getValue();
      // do something with username
    }
  }
}
```

- To add the four user ids and passwords to a cookie, we can use a delimiter to separate the values and store them as a single string. For example, we can use a comma to separate the user ids and a colon to separate the passwords. Then we can create a cookie with this string and add it to the response. For example:

```java
String users = "user1:pass1,user2:pass2,user3:pass3,user4:pass4";
Cookie cookie = new Cookie("users", users);
response.addCookie(cookie);
```

- To retrieve the user ids and passwords from the cookie, we can use the `getCookies()` method as before and find the cookie with the name "users". Then we can use the `split()` method of the `String` class to split the string by the delimiter and get an array of user id and password pairs. For example:

```java
Cookie[] cookies = request.getCookies();
if (cookies != null) {
  for (Cookie c : cookies) {
    if (c.getName().equals("users")) {
      String users = c.getValue();
      String[] pairs = users.split(",");
      for (String pair : pairs) {
        String[] userPass = pair.split(":");
        String userId = userPass[0];
        String password = userPass[1];
        // do something with userId and password
      }
    }
  }
}
```

- Note: Storing user ids and passwords in a cookie is not a secure practice and should be avoided. Cookies can be easily intercepted, modified, or stolen by malicious parties. A better way to handle user authentication is to use a secure protocol such as HTTPS, a database to store user credentials, and a session management mechanism to track user sessions.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write the content on the topic of ### Read the user id and passwords entered in the Login form and authenticate with the values available in the cookies for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab. Here is the content I have written in markdown format:

```markdown
### Read the user id and passwords entered in the Login form and authenticate with the values available in the cookies

- A login form is a web page that allows users to enter their user id and password to access a protected resource or service.
- A cookie is a small piece of data that is stored by the web browser on the user's device. It can be used to store information such as user preferences, session identifiers, authentication tokens, etc.
- To authenticate the user id and password entered in the login form, the server can compare them with the values stored in the cookies. This can be done using Java Database Connectivity (JDBC), Open Database Connectivity (ODBC), or session tracking API.
- JDBC is a Java API that allows Java applications to connect to and interact with various types of databases. It provides methods to execute SQL queries, update data, retrieve results, etc.
- ODBC is a standard API that allows applications to access data from different database management systems. It uses drivers to communicate with the specific database.
- Session tracking API is a Java API that allows web applications to maintain the state of a user across multiple requests. It uses objects such as HttpSession, HttpServletRequest, HttpServletResponse, etc. to store and retrieve information about the user.

- The steps to read the user id and password entered in the login form and authenticate with the values available in the cookies are:

  - Create a login form using HTML and submit it to a servlet using the POST method.
  - In the servlet, use the HttpServletRequest object to get the user id and password parameters from the request.
  - Use the HttpServletResponse object to create a cookie object with the user id and password values and add it to the response.
  - Use the JDBC, ODBC, or session tracking API to connect to the database and verify the user id and password with the stored values.
  - If the authentication is successful, redirect the user to the protected resource or service. If the authentication fails, display an error message and ask the user to try again.
```



### Install a database (Mysql or Oracle) for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

This section will explain how to install MySQL database on Windows using the MySQL Installer, which is the recommended way to install and configure MySQL on Microsoft Windows .

- Download MySQL Installer from https://dev.mysql.com/downloads/installer/ and execute it.
- On the welcome screen, choose the first option: Install MySQL Products.
- On the license agreement screen, read the terms and conditions and select the checkbox to accept them. Then click Next.
- On the choosing a setup type screen, select the type of installation that suits your needs. For example, you can choose Developer Default, which includes the MySQL server, MySQL Workbench, MySQL Shell, MySQL Router, MySQL for Visual Studio, and Connector/NET. Then click Next.
- On the checking requirements screen, the installer will check if your system meets the requirements for the selected setup type. If there are any missing requirements, the installer will download and install them for you. Then click Next.
- On the installation screen, the installer will show you the list of products that will be installed. Click Execute to start the installation process.
- On the product configuration screen, the installer will guide you through the configuration steps for each product. For example, for the MySQL server, you will need to choose the type and networking options, set the root password, create user accounts, and configure advanced options. Then click Next.
- On the installation complete screen, the installer will show you the status of the installation and configuration. Click Finish to complete the process.
- On the dashboard screen, you can see the list of installed products and their status. You can also launch the MySQL Shell or the MySQL Workbench to connect to the MySQL server and start working with it.

To verify the MySQL installation, you can open the MySQL Command Line Client from cmd and enter the root password. You should see a prompt like this:

```
mysql>
```

You can then run some basic commands to check the server version, the databases, and the tables. For example:

```
mysql> SELECT VERSION();
+-----------+
| VERSION() |
+-----------+
| 8.0.23    |
+-----------+
1 row in set (0.00 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)

mysql> USE mysql;
Database changed
mysql> SHOW TABLES;
+---------------------------+
| Tables_in_mysql           |
+---------------------------+
| columns_priv              |
| component                 |
| db                        |
| default_roles             |
| engine_cost               |
| func                      |
| general_log               |
| global_grants             |
| gtid_executed             |
| help_category             |
| help_keyword              |
| help_relation             |
| help_topic                |
| innodb_index_stats        |
| innodb_table_stats        |
| password_history          |
| plugin                    |
| procs_priv                |
| proxies_priv              |
| role_edges                |
| server_cost               |
| servers                   |
| slave_master_info         |
| slave_relay_log_info      |
| slave_worker_info         |
| slow_log                  |
| tables_priv               |
| time_zone                 |
| time_zone_leap_second     |
| time_zone_name            |
| time_zone_transition      |
| time_zone_transition_type |
| user                      |
+---------------------------+
34 rows in set (0.00 sec)
```

You have successfully installed and verified the MySQL database on Windows. You can now use it to design server site applications using JDDC, ODBC and section tracking API in the subject of Web Technology Lab.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is the content you requested:

### Create a table which should contain at least the following fields: name, password, email-id, phone number for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A table is a collection of data organized in rows and columns in a database.
- To create a table, you need to specify the name of the table, the names and data types of the columns, and any constraints or rules that apply to the data.
- The syntax for creating a table in SQL is:

```sql
CREATE TABLE table_name (
  column1 data_type constraints,
  column2 data_type constraints,
  ...
);
```

- For example, to create a table called `users` with the fields `name`, `password`, `email_id`, and `phone_number`, you can use the following SQL statement:

```sql
CREATE TABLE users (
  name VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL,
  email_id VARCHAR(50) UNIQUE,
  phone_number VARCHAR(15)
);
```

- The data type `VARCHAR(n)` means a variable-length character string with a maximum length of `n` characters.
- The constraint `NOT NULL` means that the column cannot have a null or missing value.
- The constraint `UNIQUE` means that the column cannot have duplicate values.
- The column `phone_number` does not have any constraints, so it can have any value or be null.

- To insert data into the table, you can use the `INSERT INTO` statement:

```sql
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
```

- For example, to insert a row into the `users` table, you can use the following SQL statement:

```sql
INSERT INTO users (name, password, email_id, phone_number) VALUES ('Alice', '1234', 'alice@example.com', '1234567890');
```

- To retrieve data from the table, you can use the `SELECT` statement:

```sql
SELECT column1, column2, ... FROM table_name WHERE condition;
```

- For example, to select all the rows from the `users` table, you can use the following SQL statement:

```sql
SELECT * FROM users;
```

- To select only the rows where the `name` is 'Bob', you can use the following SQL statement:

```sql
SELECT * FROM users WHERE name = 'Bob';
```

- To update data in the table, you can use the `UPDATE` statement:

```sql
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
```

- For example, to change the `password` of the user with the `email_id` 'alice@example.com' to 'abcd', you can use the following SQL statement:

```sql
UPDATE users SET password = 'abcd' WHERE email_id = 'alice@example.com';
```

- To delete data from the table, you can use the `DELETE` statement:

```sql
DELETE FROM table_name WHERE condition;
```

- For example, to delete the row with the `phone_number` '1234567890', you can use the following SQL statement:

```sql
DELETE FROM users WHERE phone_number = '1234567890';
```

- To delete the entire table, you can use the `DROP TABLE` statement:

```sql
DROP TABLE table_name;
```

- For example, to delete the `users` table, you can use the following SQL statement:

```sql
DROP TABLE users;
```

- JDDC, ODBC, and session tracking API are technologies that enable server-side applications to interact with databases and web clients.
- JDDC stands for Java Database Connectivity, which is a Java API that allows Java applications to connect to various types of databases using a common interface.
- ODBC stands for Open Database Connectivity, which is a standard API that allows applications to connect to various types of databases using a common interface.
- Session tracking API is a Java API that allows web applications to maintain state information across multiple requests from the same client using cookies, URL rewriting, or hidden fields.
- To use JDDC, ODBC, or session tracking API in a web application, you need to import the relevant packages, create and configure the objects, and use the methods and properties of the objects to perform the desired operations.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a possible answer to your question:

### Write a java program/servlet/JSP to connect to that database and extract data from the tables and display them for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To connect to a database using Java, you need to use the JDBC (Java Database Connectivity) API, which provides a set of classes and interfaces to interact with various databases like Oracle, SQL, PostgreSQL, MongoDB, etc.   
- To use JDBC, you need to follow these steps:
  - Load and register the JDBC driver for your database. This can be done by using the `Class.forName()` method with the driver class name as the argument. For example, to load the MySQL driver, you can use `Class.forName("com.mysql.cj.jdbc.Driver");`
  - Establish a connection to the database using the `DriverManager.getConnection()` method, which takes the database URL, username and password as the arguments. For example, to connect to a MySQL database named `webtech`, you can use `Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/webtech", "root", "password");`
  - Create a statement object using the `Connection.createStatement()` method, which allows you to execute SQL queries on the database. For example, to create a statement object, you can use `Statement stmt = conn.createStatement();`
  - Execute the query using the `Statement.executeQuery()` method, which returns a `ResultSet` object that contains the data retrieved from the database. For example, to execute a query that selects all the records from a table named `students`, you can use `ResultSet rs = stmt.executeQuery("select * from students");`
  - Process the result set using the `ResultSet.next()` method, which moves the cursor to the next row of the result set, and the `ResultSet.getXXX()` methods, which retrieve the values of the columns in the current row. For example, to print the name and age of each student in the result set, you can use a loop like this:

  ```java
  while(rs.next()){
    String name = rs.getString("name");
    int age = rs.getInt("age");
    System.out.println(name + " " + age);
  }
  ```
  - Close the resources using the `ResultSet.close()`, `Statement.close()` and `Connection.close()` methods, which release the resources and prevent memory leaks. For example, to close the resources, you can use:

  ```java
  rs.close();
  stmt.close();
  conn.close();
  ```

- To display the data from the database in a JTable, you need to use the Swing API, which provides a set of graphical components for creating GUI applications in Java. 
- To use Swing, you need to follow these steps:
  - Create a JFrame object, which is a top-level container that holds other components. For example, to create a JFrame object with the title "Database Data", you can use `JFrame frame = new JFrame("Database Data");`
  - Create a JTable object, which is a component that displays data in a tabular format. For example, to create a JTable object with two columns named "Name" and "Age", you can use `JTable table = new JTable();`
  - Create a DefaultTableModel object, which is a model that stores the data for the JTable. For example, to create a DefaultTableModel object with two columns named "Name" and "Age", you can use `DefaultTableModel model = new DefaultTableModel(new String[]{"Name", "Age"}, 0);`
  - Set the model for the JTable using the `JTable.setModel()` method. For example, to set the model for the table, you can use `table.setModel(model);`
  - Add the data from the result set to the model using the `DefaultTableModel.addRow()` method, which takes an array of objects as the argument. For example, to add the name and age of each student in the result set to the model, you can use a loop like this:

  ```java
  while(rs.next()){
    String name = rs.getString("name");
    int age = rs.getInt("age");
    model.addRow(new Object[]{name, age});
  }
  ```
  - Add the JTable to the JFrame using the `JFrame.add()` method. For example,



### Insert the details of the users who register with the web site, whenever a new user clicks the submit button in the registration page for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To insert the details of the users who register with the web site, we need to use a server-side application that can connect to a database and execute SQL queries.
- One of the possible technologies to use is Java Database Connectivity (JDBC), which is an API that allows Java programs to access various types of databases.
- JDBC consists of two components: a JDBC driver and a JDBC API. The JDBC driver is a software module that implements the JDBC interface and communicates with a specific database. The JDBC API is a set of classes and interfaces that define how a Java program can interact with the JDBC driver and the database.
- To use JDBC, we need to follow these steps:

  1. Load the JDBC driver class using the `Class.forName()` method. This registers the driver with the JDBC driver manager, which is responsible for selecting the appropriate driver for each connection request.
  2. Establish a connection to the database using the `DriverManager.getConnection()` method. This returns a `Connection` object that represents a physical connection to the database. We need to provide the URL, username and password of the database as parameters.
  3. Create a `Statement` object using the `Connection.createStatement()` method. This object can be used to execute SQL queries and update statements on the database.
  4. Execute the SQL query or update statement using the `Statement.executeQuery()` or `Statement.executeUpdate()` method. This returns a `ResultSet` object for queries, which contains the data returned by the database, or an integer for updates, which indicates the number of rows affected by the statement.
  5. Process the `ResultSet` object by using methods such as `next()`, `getString()`, `getInt()` etc. to retrieve the values of each column in each row. We can also use the `ResultSetMetaData` object to get information about the structure of the result set, such as the number and name of columns.
  6. Close the `ResultSet`, `Statement` and `Connection` objects using the `close()` method. This releases the resources associated with them and prevents memory leaks.

- To insert the details of the users who register with the web site, we need to create a registration page that contains a form with input fields for the user's name, email, password and other information. We also need to add a submit button that sends the form data to the server-side application using the `POST` method.
- The server-side application then needs to retrieve the form data from the request object, validate the input, and construct an SQL insert statement that inserts the user's details into a table in the database. For example, the SQL statement could look like this:

  ```sql
  INSERT INTO users (name, email, password, ...) VALUES (?, ?, ?, ...);
  ```

- The question marks are placeholders for the actual values, which are passed as parameters to the `PreparedStatement` object, which is a subclass of `Statement` that allows us to execute SQL statements with parameters. This prevents SQL injection attacks, which are a type of security vulnerability that allows malicious users to execute arbitrary SQL commands by manipulating the input data.
- The server-side application then executes the SQL insert statement using the `PreparedStatement.executeUpdate()` method, which returns the number of rows inserted into the table. If the insertion is successful, the application can send a response to the user, such as a confirmation message or a redirection to another page. If the insertion fails, the application can send an error message or ask the user to try again.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a possible answer to your question:

### Write a JSP which insert the details of the 3 or 4 users who register with the web site by using registration form for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To write a JSP that inserts the details of the users who register with the web site, we need to follow these steps:

  - Create a registration form in HTML or JSP that takes the input from the users, such as name, email, password, etc. For example, we can use the following code:

    ```html
    <form action="process.jsp">
      <input type="text" name="uname" value="Name..." onclick="this.value=''"/><br/>
      <input type="text" name="uemail" value="Email ID..." onclick="this.value=''"/><br/>
      <input type="password" name="upass" value="Password..." onclick="this.value=''"/><br/>
      <input type="submit" value="register"/>
    </form>
    ```

  - Create a JSP page that processes the form data and inserts it into the database using JDBC, ODBC or any other database connectivity API. For example, we can use the following code:

    ```jsp
    <%@ page import="java.sql.*" %>
    <%
      //Get the form data
      String name = request.getParameter("uname");
      String email = request.getParameter("uemail");
      String pass = request.getParameter("upass");

      //Create a connection to the database
      Class.forName("oracle.jdbc.driver.OracleDriver");
      Connection con = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","oracle");

      //Create a statement and execute a query to insert the data
      Statement stmt = con.createStatement();
      int i = stmt.executeUpdate("insert into user432 values('"+name+"','"+email+"','"+pass+"')");
      if(i>0){
        out.println("You are successfully registered");
      }
      else{
        out.println("Registration failed");
      }

      //Close the connection and the statement
      stmt.close();
      con.close();
    %>
    ```

  - Optionally, we can use session tracking API to store the user information in the session object and retrieve it later. For example, we can use the following code:

    ```jsp
    <%@ page import="javax.servlet.http.HttpSession" %>
    <%
      //Get the form data
      String name = request.getParameter("uname");
      String email = request.getParameter("uemail");
      String pass = request.getParameter("upass");

      //Create a session object and store the user information
      HttpSession session = request.getSession();
      session.setAttribute("name", name);
      session.setAttribute("email", email);
      session.setAttribute("pass", pass);

      //Redirect to another JSP page that displays the user information
      response.sendRedirect("display.jsp");
    %>
    ```

    ```jsp
    <%@ page import="javax.servlet.http.HttpSession" %>
    <%
      //Get the session object and retrieve the user information
      HttpSession session = request.getSession();
      String name = (String) session.getAttribute("name");
      String email = (String) session.getAttribute("email");
      String pass = (String) session.getAttribute("pass");

      //Display the user information
      out.println("Welcome, " + name + "<br/>");
      out.println("Your email is: " + email + "<br/>");
      out.println("Your password is: " + pass + "<br/>");
    %>
    ```

- These are the basic steps to write a JSP that inserts the details of the users who register with the web site. You can modify the code according to your requirements and preferences. I hope this answer helps you.😊



### Authenticate the user when he submits the login form using the user name and password from the database for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To authenticate the user when he submits the login form using the user name and password from the database, we need to use JDBC (Java Database Connectivity) and ODBC (Open Database Connectivity) drivers to establish a connection between the web application and the database server.
- JDBC and ODBC drivers are software components that enable the web application to communicate with the database server using a standard interface and protocol. JDBC drivers are specific to Java-based web applications, while ODBC drivers are generic and can be used by any web application that supports ODBC.
- To use JDBC and ODBC drivers, we need to configure the connection parameters, such as the database URL, the user name, the password, and the driver class name. These parameters can be specified in the web application code, in a configuration file, or in a data source object.
- To authenticate the user, we need to use a session tracking API, such as HttpSession in Java, to store the user credentials and other information in the web server memory or in a cookie. A session is a unique identifier that is assigned to each user when he visits the web application. A session can be used to maintain the state and security of the user across multiple requests and pages.
- The session tracking API provides methods to create, retrieve, update, and invalidate sessions. We can use these methods to check if the user has a valid session, to store the user credentials in the session, to retrieve the user credentials from the session, and to terminate the session when the user logs out or when the session expires.
- The following steps describe the basic process of authenticating the user when he submits the login form using the user name and password from the database:

  1. The user enters his user name and password in the login form and submits it to the web server.
  2. The web server receives the login request and invokes the web application code that handles the authentication logic.
  3. The web application code uses the JDBC or ODBC driver to establish a connection with the database server using the configured connection parameters.
  4. The web application code executes a SQL query to select the user record from the database table that matches the user name and password entered by the user.
  5. The web application code checks the result of the SQL query. If the user record is found, the user is authenticated. If the user record is not found, the user is not authenticated and an error message is displayed.
  6. If the user is authenticated, the web application code uses the session tracking API to create a new session or retrieve an existing session for the user. The web application code stores the user credentials and other information in the session object or in a cookie.
  7. The web application code redirects the user to the home page or another page of the web application, depending on the business logic. The web application code can use the session tracking API to access the user credentials and other information from the session object or the cookie in subsequent requests and pages.
  8. If the user wants to log out, the web application code uses the session tracking API to invalidate the session object or delete the cookie. The web application code redirects the user to the login page or another page of the web application.



### Design and implement a simple shopping cart example with session tracking API

- Session tracking is a technique to maintain the state of a client across multiple requests to a server. It is useful for applications that need to remember the actions or preferences of a client, such as an online shopping cart.
- Session tracking can be implemented using various methods, such as cookies, URL rewriting, hidden form fields, or the HttpSession interface in servlets.
- The HttpSession interface provides a way to create, store, and retrieve information about a client's session on the server. It also allows the server to invalidate a session if it expires or the client logs out.
- A simple shopping cart example with session tracking API can be designed and implemented as follows:

1. Create a servlet that handles the requests for adding, removing, or viewing items in the cart. The servlet should use the HttpSession interface to get or create a session object for each client. The session object can store a list of items that the client has added to the cart.
2. Create a JSP page that displays the items in the cart and allows the client to modify the quantity or remove an item. The JSP page should use the session object to access the list of items and display them in a table. The JSP page should also provide a link to check out or continue shopping.
3. Create another servlet that handles the requests for checking out or continuing shopping. The servlet should use the session object to get the list of items and calculate the total amount. The servlet should also invalidate the session object if the client checks out or logs out.
4. Create another JSP page that displays the confirmation or error message after the client checks out or continues shopping. The JSP page should use the request object to get the message and display it to the client.

- The following code snippets show an example of the servlet and JSP pages for the shopping cart application:

```java
//CartServlet.java
import java.io.*;
import java.util.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class CartServlet extends HttpServlet {

  //A method to handle GET requests
  public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {
    
    //Get or create a session object for the client
    HttpSession session = request.getSession(true);
    
    //Get the action parameter from the request
    String action = request.getParameter("action");
    
    //Get the list of items from the session object or create a new one
    List<Item> items = (List<Item>) session.getAttribute("items");
    if (items == null) {
      items = new ArrayList<Item>();
      session.setAttribute("items", items);
    }
    
    //Perform the action based on the parameter value
    if (action != null) {
      if (action.equals("add")) {
        //Get the item id and quantity from the request
        String id = request.getParameter("id");
        int quantity = Integer.parseInt(request.getParameter("quantity"));
        
        //Create a new item object and add it to the list
        Item item = new Item(id, quantity);
        items.add(item);
      } else if (action.equals("remove")) {
        //Get the item id from the request
        String id = request.getParameter("id");
        
        //Find and remove the item from the list
        for (Item item : items) {
          if (item.getId().equals(id)) {
            items.remove(item);
            break;
          }
        }
      } else if (action.equals("view")) {
        //Do nothing, just display the cart
      }
    }
    
    //Forward the request to the cart.jsp page
    RequestDispatcher dispatcher = request.getRequestDispatcher("cart.jsp");
    dispatcher.forward(request, response);
  }
  
  //A method to handle POST requests
  public void doPost(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {
    
    //Call the doGet method
    doGet(request, response);
  }
}
```

```html
<!-- cart.jsp -->
<%@ page import="java.util.*" %>
<%@ page import="com.demo.Item" %>
<html>
<head>
  <title>Shopping Cart</title>
</head>
<body>
  <h1>Shopping Cart</h1>
  <% 
    //Get the session object
    HttpSession session = request.getSession(false);
    
    //Get the list of items from the session object
    List<Item> items = (List<Item>) session.getAttribute("items");
    
    //Check if the list is empty or not
    if (items == null || items.isEmpty()) {
  %>
  <p>Your cart is empty.</p>

```


