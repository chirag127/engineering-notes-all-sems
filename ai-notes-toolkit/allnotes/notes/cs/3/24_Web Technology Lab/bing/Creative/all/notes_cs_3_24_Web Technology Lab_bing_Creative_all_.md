

## Unit 1 - Develop static web pages using HTML

- HTML stands for HyperText Markup Language. It is the standard language for creating web pages and web applications.
- HTML consists of elements that define the structure and content of a web page. Elements are enclosed by tags, which are written in angle brackets. For example, `<p>` is the tag for a paragraph element.
- HTML elements can have attributes, which provide additional information about the element. Attributes are written inside the start tag, after the element name, and consist of a name and a value. For example, `<p class="intro">` is a paragraph element with a class attribute and a value of "intro".
- HTML elements can be nested, which means that one element can contain another element. For example, `<div><p>This is a paragraph inside a division.</p></div>` is a division element that contains a paragraph element.
- HTML elements can be self-closing, which means that they do not need an end tag. For example, `<img src="image.jpg">` is an image element that has a source attribute and does not need an end tag.
- HTML documents have a basic structure that consists of a `<!DOCTYPE>` declaration, a `<html>` element, a `<head>` element, and a `<body>` element. The `<!DOCTYPE>` declaration specifies the version of HTML that the document follows. The `<html>` element is the root element of the document. The `<head>` element contains information about the document, such as the title, the character encoding, and the links to external resources. The `<body>` element contains the visible content of the document, such as text, images, and links.
- HTML documents can be linked to each other using anchor elements. Anchor elements have an `href` attribute that specifies the URL of the destination document. For example, `<a href="https://www.example.com">Example</a>` is an anchor element that links to the website https://www.example.com.
- HTML documents can be styled using CSS (Cascading Style Sheets). CSS is a language that defines how HTML elements are displayed on the screen. CSS rules consist of selectors and declarations. Selectors are patterns that match HTML elements. Declarations are properties and values that specify how the selected elements are styled. For example, `p {color: blue;}` is a CSS rule that applies a blue color to all paragraph elements.
- HTML documents can be made interactive using JavaScript. JavaScript is a scripting language that can manipulate HTML elements and respond to user events. JavaScript code can be embedded in HTML documents using the `<script>` element, or linked to external files using the `src` attribute. For example, `<script src="script.js"></script>` is a script element that links to an external JavaScript file.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some points to write HTML/Java scripts to display your CV in navigator, your Institute website, Department Website and Tutorial website for specific subject for the notes of the Unit 1 - Develop static web pages using HTML in the subject of Web Technology Lab:

- To create a web page using HTML, you need to use tags, attributes and elements to define the structure and content of the page. You can use a text editor or an IDE to write the HTML code and save it as a .html file. Learn HTML
- To style the web page using CSS, you need to use selectors, properties and values to define the appearance and layout of the page. You can use a style tag inside the HTML file or link to an external .css file to apply the CSS code. Learn CSS
- To add interactivity and functionality to the web page using JavaScript, you need to use variables, operators, statements and functions to define the behavior and logic of the page. You can use a script tag inside the HTML file or link to an external .js file to execute the JavaScript code. Learn JavaScript
- To display your CV in navigator, you need to create a web page that contains your personal information, education, skills, experience and achievements. You can use HTML tags such as h1, p, ul, li, a, img, etc. to display the text and images. You can use CSS properties such as font-family, font-size, color, margin, padding, border, etc. to style the elements. You can use JavaScript functions such as window.onload, document.getElementById, document.createElement, etc. to manipulate the elements. Example
- To display your Institute website, you need to create a web page that contains the name, logo, motto, vision, mission, courses, facilities, faculty, events and contact details of your institute. You can use HTML tags such as div, span, header, footer, nav, section, article, etc. to organize the content. You can use CSS properties such as display, position, float, flex, grid, etc. to arrange the layout. You can use JavaScript functions such as window.addEventListener, document.querySelector, document.querySelectorAll, etc. to add interactivity. Example
- To display your Department website, you need to create a web page that contains the name, logo, objectives, programs, syllabus, projects, publications, seminars and alumni of your department. You can use HTML tags such as table, tr, td, th, caption, etc. to display the data. You can use CSS properties such as border-collapse, border-spacing, text-align, vertical-align, etc. to style the table. You can use JavaScript functions such as document.getElementById, document.getElementsByClassName, document.getElementsByTagName, etc. to access the table elements. Example
- To display your Tutorial website for specific subject, you need to create a web page that contains the title, introduction, objectives, topics, examples, exercises and references of the subject. You can use HTML tags such as h2, h3, h4, ol, code, pre, etc. to display the headings and code. You can use CSS properties such as background-color, font-weight, font-style, etc. to highlight the code. You can use JavaScript functions such as document.write, console.log, alert, prompt, etc. to execute the code. Example

I hope this helps you. If you have any further questions, please ask me.😊



# Write an HTML program to design an entry form of student details and send it to store at database server like SQL, Oracle or MS Access

- An HTML form is a document that stores information of a user on a web server using interactive controls.
- An HTML form contains different kinds of information such as username, password, contact number, email id, etc.
- The HTML `<form>` element is used to create an HTML form for user input.
- The `<form>` element is a container for different types of input elements, such as: text fields, checkboxes, radio buttons, submit buttons, etc.
- To design an entry form of student details, we need to use the appropriate input elements and labels for each field.
- To send the form data to a database server, we need to specify the `action` and `method` attributes of the `<form>` element.
- The `action` attribute defines the URL of the server-side script that will process the form data.
- The `method` attribute defines the HTTP method to use when sending the form data.
- The most common methods are `GET` and `POST`.
- The `GET` method appends the form data to the URL in the query string.
- The `POST` method sends the form data as an HTTP request body.
- The choice of method depends on the type and size of the data, and the security and privacy requirements.
- For example, if the data is sensitive or large, the `POST` method is preferred.
- To store the form data in a database server like SQL, Oracle or MS Access, we need to use a server-side scripting language such as PHP, ASP, or JSP.
- The server-side script will receive the form data, connect to the database server, and execute the appropriate SQL queries to insert, update, or delete the data.
- The server-side script will also send a response back to the browser, such as a confirmation message or an error message.

Here is an example of an HTML program to design an entry form of student details and send it to store at a database server like SQL, Oracle or MS Access:

```html
<html>
<head>
  <title>Student Registration Form</title>
</head>
<body>
  <h1>Student Registration Form</h1>
  <form action="process.php" method="POST">
    <table>
      <tr>
        <td>First Name:</td>
        <td><input type="text" name="fname" required></td>
      </tr>
      <tr>
        <td>Last Name:</td>
        <td><input type="text" name="lname" required></td>
      </tr>
      <tr>
        <td>Email ID:</td>
        <td><input type="email" name="email" required></td>
      </tr>
      <tr>
        <td>Mobile Number:</td>
        <td><input type="tel" name="mobile" required></td>
      </tr>
      <tr>
        <td>Address:</td>
        <td><textarea name="address" rows="4" cols="20" required></textarea></td>
      </tr>
      <tr>
        <td>Hobbies:</td>
        <td>
          <input type="checkbox" name="hobbies[]" value="Reading">Reading
          <input type="checkbox" name="hobbies[]" value="Music">Music
          <input type="checkbox" name="hobbies[]" value="Sports">Sports
        </td>
      </tr>
      <tr>
        <td>Course:</td>
        <td>
          <select name="course" required>
            <option value="">Select Course</option>
            <option value="B.Tech">B.Tech</option>
            <option value="M.Tech">M.Tech</option>
            <option value="MBA">MBA</option>
            <option value="MCA">MCA</option>
          </select>
        </td>
      </tr>
      <tr>
        <td>Gender:</td>
        <td>
          <input type="radio" name="gender" value="Male" required>Male
          <input type="radio" name="gender" value="Female" required>Female
          <input type="radio" name

```




## Unit 2 - Develop Java programs for window/web-based applications

- In this unit, you will learn how to create graphical user interfaces (GUIs) and web applications using Java.
- GUIs are programs that allow users to interact with the computer through graphical elements such as buttons, menus, text fields, etc.
- Web applications are programs that run on a web server and can be accessed by users through a web browser.
- To create GUIs in Java, you will need to use the Swing and AWT libraries, which provide various components and layouts for designing GUIs.
- To create web applications in Java, you will need to use the Servlet and JSP technologies, which enable you to write dynamic web pages and handle user requests and responses.
- You will also learn how to use databases and JDBC to store and retrieve data for your applications.

### Learning Outcomes

- By the end of this unit, you will be able to:
  - Explain the concepts and features of GUIs and web applications.
  - Use Swing and AWT components and layouts to create GUIs in Java.
  - Use event-driven programming to handle user interactions in GUIs.
  - Use Servlets and JSPs to create dynamic web pages and web applications in Java.
  - Use JDBC to connect to databases and perform CRUD operations in Java.
  - Test and debug your Java applications using appropriate tools and techniques.



# Write programs using JavaScript for Web Page to display browsers information

JavaScript is a scripting language that can be used to create dynamic and interactive web pages. One of the features of JavaScript is that it can access and manipulate the information about the visitor's browser, such as the name, version, platform, cookies, etc. This information can be useful for various purposes, such as customizing the web page content, detecting the browser compatibility, or collecting statistics.

To access the browser information, we can use the `window.navigator` object, which has several properties and methods that provide different details about the browser. Some of the common properties are:

- `navigator.appName`: The name of the browser, such as Netscape, Microsoft Internet Explorer, Opera, etc.
- `navigator.appVersion`: The version of the browser, such as 5.0, 4.0, etc.
- `navigator.userAgent`: The user agent string that identifies the browser, the operating system, and other information.
- `navigator.platform`: The platform on which the browser is running, such as Win32, Linux, Mac68K, etc.
- `navigator.cookieEnabled`: A boolean value that indicates whether the browser supports cookies or not.

To display the browser information on a web page, we can use the `document.write()` method, which writes a string of text to the document. For example, the following program displays the browser name and version on a web page:

```javascript
// Get the browser name and version
var browserName = navigator.appName;
var browserVersion = navigator.appVersion;

// Display the browser name and version on the web page
document.write("You are using " + browserName + " version " + browserVersion + ".");
```

The output of this program may look something like this:

You are using Netscape version 5.0 (Windows).

However, the `navigator.appName` and `navigator.appVersion` properties may not always give accurate or consistent results, as different browsers may use different names or versions for themselves. For example, most browsers use the internal code name Mozilla, and some browsers may append additional information to the version string. Therefore, a more reliable way to detect the browser name and version is to use the `navigator.userAgent` property, which contains a unique string that identifies the browser and other details.

To parse the user agent string and extract the browser name and version, we can use the `indexOf()` and `substring()` methods of the string object, which allow us to search and extract a part of a string. For example, the following program detects the browser name and version from the user agent string and displays them on a web page:

```javascript
// Get the user agent string
var userAgent = navigator.userAgent;

// Initialize the browser name and version variables
var browserName = "";
var browserVersion = "";

// Detect the browser name and version from the user agent string
if (userAgent.indexOf("Opera") != -1) {
  // Opera browser
  browserName = "Opera";
  browserVersion = userAgent.substring(userAgent.indexOf("OPR") + 4);
} else if (userAgent.indexOf("Edg") != -1) {
  // Edge browser
  browserName = "Microsoft Edge";
  browserVersion = userAgent.substring(userAgent.indexOf("Edg") + 4);
} else if (userAgent.indexOf("Chrome") != -1) {
  // Chrome browser
  browserName = "Google Chrome";
  browserVersion = userAgent.substring(userAgent.indexOf("Chrome") + 7);
} else if (userAgent.indexOf("Safari") != -1) {
  // Safari browser
  browserName = "Safari";
  browserVersion = userAgent.substring(userAgent.indexOf("Version") + 8);
} else if (userAgent.indexOf("Firefox") != -1) {
  // Firefox browser
  browserName = "Mozilla Firefox";
  browserVersion = userAgent.substring(userAgent.indexOf("Firefox") + 8);
} else if (userAgent.indexOf("MSIE") != -1) {
  // Internet Explorer browser
  browserName = "Microsoft Internet Explorer";
  browserVersion = userAgent.substring(userAgent.indexOf("MSIE") + 5);
} else {
  // Other browser
  browserName = "Unknown";
  browserVersion = "Unknown";
}

// Display the browser name and version on the web page
document.write("You are using " + browserName + " version " + browserVersion + ".");
```

The output of this program may look something like this:

You are using Google Chrome version 96.0.4664.110.

To display



# Write a Java applet to display the Application Program screen i.e. calculator and other for the notes of the Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab

- A Java applet is a small Java application that can be embedded in a web browser and run on the client-side.
- A Java applet can display dynamic content, such as a calculator, using graphical user interface (GUI) components and event handling.
- To write a Java applet for a calculator, we need to follow these steps:

  - Import the necessary packages, such as `java.applet`, `java.awt`, and `java.awt.event`.
  - Define a class that extends the `Applet` class and implements the `ActionListener` interface.
  - Declare and initialize the GUI components, such as text fields, buttons, and labels, as instance variables of the class.
  - Override the `init()` method of the `Applet` class to add the GUI components to the applet and register the action listeners for the buttons.
  - Override the `actionPerformed()` method of the `ActionListener` interface to perform the arithmetic operations based on the button clicked and the input values entered in the text fields.
  - Compile and run the applet using an applet viewer or a web browser.

- Here is an example of a Java applet for a simple calculator that can perform addition, subtraction, multiplication, and division:

```java
// Import the necessary packages
import java.applet.*;
import java.awt.*;
import java.awt.event.*;

// Define a class that extends the Applet class and implements the ActionListener interface
public class CalculatorApplet extends Applet implements ActionListener {

  // Declare and initialize the GUI components as instance variables of the class
  TextField tf1, tf2, tf3; // Text fields for input and output
  Button b1, b2, b3, b4; // Buttons for arithmetic operations
  Label l1, l2, l3; // Labels for instructions

  // Override the init() method of the Applet class to add the GUI components to the applet and register the action listeners for the buttons
  public void init() {
    // Set the layout of the applet to grid layout with 4 rows and 2 columns
    setLayout(new GridLayout(4, 2));

    // Create and initialize the GUI components
    tf1 = new TextField(10); // Text field for the first input value
    tf2 = new TextField(10); // Text field for the second input value
    tf3 = new TextField(10); // Text field for the output value
    tf3.setEditable(false); // Make the output text field non-editable
    b1 = new Button("+"); // Button for addition
    b2 = new Button("-"); // Button for subtraction
    b3 = new Button("*"); // Button for multiplication
    b4 = new Button("/"); // Button for division
    l1 = new Label("Enter the first number:"); // Label for the first input value
    l2 = new Label("Enter the second number:"); // Label for the second input value
    l3 = new Label("Result:"); // Label for the output value

    // Add the GUI components to the applet
    add(l1); // Add the label for the first input value to the first row and first column
    add(tf1); // Add the text field for the first input value to the first row and second column
    add(l2); // Add the label for the second input value to the second row and first column
    add(tf2); // Add the text field for the second input value to the second row and second column
    add(l3); // Add the label for the output value to the third row and first column
    add(tf3); // Add the text field for the output value to the third row and second column
    add(b1); // Add the button for addition to the fourth row and first column
    add(b2); // Add the button for subtraction to the fourth row and second column
    add(b3); // Add the button for multiplication to the fifth row and first column
    add(b4); // Add the button for division to the fifth row and second column

    // Register the action listeners for the buttons
    b1.addActionListener(this); // Register the action listener for the addition button
    b2.addActionListener(this); // Register the action listener for the subtraction button
    b3.addActionListener(this); //

```




# Unit 3 - Design dynamic web pages using Javascript and XML

- Dynamic web pages are web pages that can change their content or appearance without reloading the whole page. They can provide a better user experience and more interactivity than static web pages.
- Javascript is a scripting language that can run in the browser and manipulate the HTML and CSS elements of a web page. It can also communicate with the server and exchange data using AJAX (Asynchronous JavaScript and XML) or JSON (JavaScript Object Notation) techniques.
- XML (Extensible Markup Language) is a markup language that can store and transport data in a structured and readable format. It can be used to define the content and structure of a web page, or to exchange data between the server and the browser.
- To design dynamic web pages using Javascript and XML, you need to follow these steps:
  - Create an HTML document that defines the basic layout and structure of the web page. You can use HTML5 elements and attributes to enhance the semantics and accessibility of the web page.
  - Create a CSS file that defines the style and appearance of the web page. You can use CSS3 properties and selectors to create responsive and interactive designs.
  - Create a Javascript file that defines the functionality and behavior of the web page. You can use Javascript functions, variables, objects, events, and DOM (Document Object Model) methods to manipulate the web page elements and respond to user actions. You can also use Javascript to create and parse XML documents, or to send and receive data using AJAX or JSON.
  - Link the HTML, CSS, and Javascript files together using the `<link>` and `<script>` tags in the HTML document. You can also use external libraries or frameworks to simplify the development process and add more features to your web page. Some examples of popular libraries and frameworks are jQuery, Bootstrap, React, Angular, and Vue.



# Writing program in XML for creation of DTD, which specifies set of rules for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A DTD (Document Type Declaration) is a way to describe the structure and the legal elements and attributes of an XML document  .
- A DTD can be used to validate the XML document against the grammatical rules of the appropriate XML language  .
- A DTD can be declared internally or externally to the XML document .
- An internal DTD is included in the same file as the XML document, inside the `<!DOCTYPE>` declaration .
- An external DTD is referenced by the XML document using a URL or a system identifier, inside the `<!DOCTYPE>` declaration .
- A DTD defines the following components of an XML document  :
  - Elements: the names and the relationships of the XML tags
  - Attributes: the names and the values of the XML attributes
  - Entities: the names and the values of the XML entities
  - Notations: the names and the values of the XML notations
  - Processing instructions: the instructions for the XML processor
  - Comments: the comments for the XML document
- A DTD uses the following syntax to declare the components of an XML document  :
  - `<!ELEMENT>`: to declare an element and its content model
  - `<!ATTLIST>`: to declare an attribute and its type and default value
  - `<!ENTITY>`: to declare an entity and its replacement text
  - `<!NOTATION>`: to declare a notation and its identifier
  - `<?...?>`: to declare a processing instruction
  - `<!--...-->`: to declare a comment
- A DTD can use the following symbols to specify the occurrence of the components of an XML document  :
  - `?`: to indicate that the component is optional (zero or one occurrence)
  - `+`: to indicate that the component is required (one or more occurrences)
  - `*`: to indicate that the component is optional (zero or more occurrences)
  - `|`: to indicate that the component is a choice (one of the alternatives)
  - `,`: to indicate that the component is a sequence (all of the alternatives in order)
  - `()` : to group the components
  - `#PCDATA`: to indicate that the component is parsed character data (text)
  - `#REQUIRED`: to indicate that the attribute is mandatory
  - `#IMPLIED`: to indicate that the attribute is optional
  - `#FIXED`: to indicate that the attribute has a fixed value
- A DTD can use the following data types to specify the values of the components of an XML document  :
  - `CDATA`: to indicate that the value is character data (any text)
  - `ID`: to indicate that the value is a unique identifier (a name that starts with a letter or underscore and contains only letters, digits, underscores, hyphens, and periods)
  - `IDREF`: to indicate that the value is a reference to an ID value
  - `IDREFS`: to indicate that the value is a list of references to ID values
  - `ENTITY`: to indicate that the value is a reference to an entity
  - `ENTITIES`: to indicate that the value is a list of references to entities
  - `NMTOKEN`: to indicate that the value is a name token (a name that contains only letters, digits, underscores, hyphens, and periods)
  - `NMTOKENS`: to indicate that the value is a list of name tokens
  - `NOTATION`: to indicate that the value is a reference to a notation
  - `ENUMERATION`: to indicate that the value is one of the specified values

- An example of a DTD that specifies the set of rules for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab is:

```xml
<!DOCTYPE notes [
  <!ELEMENT

```




# Create a style sheet in CSS/XSL & display the document in internet explorer for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A style sheet is a file that defines the appearance and layout of an XML document.
- CSS (Cascading Style Sheets) is a language for styling HTML and XML documents.
- XSL (eXtensible Stylesheet Language) is a language for transforming XML documents into other formats, such as HTML, PDF, or plain text.
- To create a style sheet in CSS/XSL, you need to follow these steps:

  1. Create a text file with the extension .css or .xsl, depending on the type of style sheet you want to create.
  2. In the style sheet file, use the appropriate syntax and rules to define the style properties and values for the elements and attributes of the XML document.
  3. Save the style sheet file in the same folder as the XML document, or in a different location that can be accessed by the XML document.
  4. In the XML document, add a reference to the style sheet file using the <link> element (for CSS) or the <?xml-stylesheet?> processing instruction (for XSL) in the <head> section of the document.
  5. Example of a CSS style sheet file (style.css):

```css
/* This is a comment */
h1 {
  color: blue;
  font-size: 24px;
}

p {
  font-family: Arial, sans-serif;
  margin: 10px;
}
```

  6. Example of an XSL style sheet file (style.xsl):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <!-- This is a comment -->
  <xsl:output method="html"/>
  <xsl:template match="/">
    <html>
      <head>
        <title>Example of XSL Transformation</title>
      </head>
      <body>
        <h1><xsl:value-of select="book/title"/></h1>
        <p>Author: <xsl:value-of select="book/author"/></p>
        <p>Price: <xsl:value-of select="book/price"/></p>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
```

  7. Example of an XML document (book.xml) that references the style sheet files:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/css" href="style.css"?>
<?xml-stylesheet type="text/xsl" href="style.xsl"?>
<book>
  <title>XML for Beginners</title>
  <author>John Smith</author>
  <price>19.99</price>
</book>
```

- To display the document in internet explorer, you need to follow these steps:

  1. Open the internet explorer browser and navigate to the folder where the XML document is located.
  2. Double-click on the XML document file to open it in the browser.
  3. The browser will apply the style sheet files to the XML document and display the transformed output in HTML format.
  4. You can also right-click on the XML document file and select "Open with" and choose internet explorer from the list of programs.



# Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP

- A dynamic web page is a web page that can display different content or layout depending on the user's input, preferences, or other factors  .
- A server-side dynamic web page is a web page whose construction is controlled by an application server processing server-side scripts.
- Server-side scripts are programs that run on the web server and generate the HTML code that is sent to the web browser .
- Server-side programming languages are languages that can be used to write server-side scripts. Examples of popular server-side web languages include PHP, ASP, JSP, Python, Ruby, C#, and JavaScript (NodeJS) .
- To design a dynamic web page using server-side programming, the following steps are required:
  - Choose a server-side programming language and a web framework that supports it. A web framework is a set of tools and libraries that simplify the development of web applications.
  - Install the necessary software and tools on the web server, such as the web server software, the programming language interpreter or compiler, the web framework, and any other dependencies.
  - Write the server-side scripts that handle the user requests, perform the business logic, and generate the dynamic HTML code. The scripts can use various techniques to create dynamic content, such as accessing databases, calling web services, using templates, or manipulating the DOM .
  - Test and debug the server-side scripts using the web browser and the web server tools.
  - Deploy the server-side scripts to the web server and make them accessible to the web users.
- Examples of dynamic web pages using server-side programming are:
  - ASP: A web page that uses Active Server Pages (ASP) to display the current date and time.
  - JSP: A web page that uses Java Server Pages (JSP) to display a list of products from a database.
  - PHP: A web page that uses PHP to display a simple guestbook form and the entries from a text file.



# Program to illustrate JDBC connectivity

JDBC stands for Java Database Connectivity, which is a standard Java API for connecting to relational databases. JDBC allows a Java program to execute SQL statements and retrieve the results from a database server.

To use JDBC, we need to follow these steps:

- Load the JDBC driver class that corresponds to the type of database we want to connect to. For example, for MySQL, we can use `Class.forName("com.mysql.jdbc.Driver");`
- Create a connection object that represents a physical connection to the database server. We need to provide a connection URL that specifies the database name, host, port, and other parameters. We also need to provide a user name and password for authentication. For example, for MySQL, we can use `Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test","root","password");`
- Create a statement object that allows us to execute SQL queries and commands. We can use different types of statements, such as `Statement`, `PreparedStatement`, or `CallableStatement`, depending on our needs. For example, we can use `Statement stmt = con.createStatement();`
- Execute the statement and obtain the result set object that contains the data returned by the query. We can use different methods, such as `executeQuery`, `executeUpdate`, or `execute`, depending on the type of statement. For example, we can use `ResultSet rs = stmt.executeQuery("SELECT * FROM students");`
- Process the result set by iterating over the rows and columns and extracting the values. We can use different methods, such as `next`, `getString`, `getInt`, or `getBoolean`, depending on the data type. For example, we can use `while(rs.next()){System.out.println(rs.getString("name") + " " + rs.getInt("age"));}`
- Close the result set, statement, and connection objects to release the resources and avoid memory leaks. We can use the `close` method for each object. For example, we can use `rs.close(); stmt.close(); con.close();`

Here is a complete example of a Java program that connects to a MySQL database and prints the data from a table:

```java
import java.sql.*;

public class JDBCExample {

    public static void main(String[] args) {
        try {
            // Load the JDBC driver
            Class.forName("com.mysql.jdbc.Driver");
            
            // Create a connection object
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test","root","password");
            
            // Create a statement object
            Statement stmt = con.createStatement();
            
            // Execute a query and obtain a result set
            ResultSet rs = stmt.executeQuery("SELECT * FROM students");
            
            // Process the result set
            while(rs.next()){
                System.out.println(rs.getString("name") + " " + rs.getInt("age"));
            }
            
            // Close the result set, statement, and connection objects
            rs.close();
            stmt.close();
            con.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```



# Program for maintaining database by sending queries for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

- Server-side programming is the process of creating dynamic web pages that interact with databases, files, and other servers using a programming language that runs on the web server.
- ASP, JSP, and PHP are examples of server-side programming languages that can be used to design dynamic web pages using server-side programming.
- ASP stands for Active Server Pages, a server-side scripting technology that allows developers to create dynamic web pages using HTML, CSS, JavaScript, and VBScript. ASP was created by Microsoft and runs on Windows servers.
- JSP stands for Java Server Pages, a server-side scripting technology that allows developers to create dynamic web pages using HTML, XML, or other types, combined with Java code. JSP was created by Sun Microsystems and runs on any server that supports Java.
- PHP stands for Hypertext Preprocessor, a server-side scripting language that allows developers to create dynamic web pages using HTML, CSS, JavaScript, and PHP code. PHP was created by Rasmus Lerdorf and runs on any server that supports PHP.
- To maintain a database by sending queries using server-side programming, the following steps are required:
  - Create a database and a table on the server using a database management system (DBMS) such as MySQL, Oracle, SQL Server, etc.
  - Establish a connection between the server-side script and the database using a database driver or an API such as JDBC, ODBC, PDO, etc.
  - Write SQL queries to perform operations on the database such as inserting, updating, deleting, or retrieving data.
  - Execute the queries using the server-side script and display the results on the web page using HTML, CSS, and JavaScript.
  - Close the connection to the database when the operation is completed.
- The following are some examples of server-side scripts that can be used to maintain a database by sending queries using ASP, JSP, and PHP:

## ASP Example

```asp
<%@ Language=VBScript %>
<%
'Create a connection object
Set conn = Server.CreateObject("ADODB.Connection")
'Open the connection using a connection string
conn.Open "Driver={SQL Server};Server=localhost;Database=webtech;Uid=sa;Pwd=1234;"
'Create a recordset object
Set rs = Server.CreateObject("ADODB.Recordset")
'Write a SQL query to select all records from the notes table
sql = "SELECT * FROM notes"
'Execute the query and store the result in the recordset object
rs.Open sql, conn
'Display the result in an HTML table
Response.Write "<table border='1'>"
Response.Write "<tr><th>Id</th><th>Title</th><th>Content</th></tr>"
Do While Not rs.EOF
  Response.Write "<tr>"
  Response.Write "<td>" & rs("id") & "</td>"
  Response.Write "<td>" & rs("title") & "</td>"
  Response.Write "<td>" & rs("content") & "</td>"
  Response.Write "</tr>"
  rs.MoveNext
Loop
Response.Write "</table>"
'Close the recordset and the connection objects
rs.Close
conn.Close
%>
```

## JSP Example

```jsp
<%@ page import="java.sql.*" %>
<%
//Create a connection object
Connection conn = null;
//Create a statement object
Statement stmt = null;
//Create a resultset object
ResultSet rs = null;
//Open the connection using a driver and a URL
Class.forName("com.mysql.jdbc.Driver");
conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/webtech", "root", "1234");
//Create a statement object from the connection object
stmt = conn.createStatement();
//Write a SQL query to select all records from the notes table
String sql = "SELECT * FROM notes";
//Execute the query and store the result in the resultset object
rs = stmt.executeQuery(sql);
//Display the result in an HTML table
out.println("<table border='1'>");
out.println("<tr><th>Id</th><th>Title</th><th>Content</th></tr>");
while(rs.next()){
  out.println("<tr>");
  out.println("<td>" + rs.getInt("id") + "</td>");
  out.println("<td>" + rs.getString("title") + "</td>");
  out.println("<td>" + rs.getString("content") + "</td>");
  out.println("</tr>");

```




# Design and implement a simple servlet book query with the help of JDBC & SQL

- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- JDBC (Java Database Connectivity) is an API that allows Java programs to interact with various types of databases using SQL (Structured Query Language) commands.
- To design and implement a simple servlet book query with the help of JDBC & SQL, the following steps are required:

  - Create a database and a table to store the book information, such as title, author, price, etc. For example, using MySQL, the following SQL commands can be used:

    ```sql
    CREATE DATABASE books;
    USE books;
    CREATE TABLE book (
      id INT PRIMARY KEY,
      title VARCHAR(50),
      author VARCHAR(50),
      price DECIMAL(10,2)
    );
    INSERT INTO book VALUES
    (1, 'Java: The Complete Reference', 'Herbert Schildt', 35.99),
    (2, 'Head First Java', 'Kathy Sierra and Bert Bates', 29.99),
    (3, 'Effective Java', 'Joshua Bloch', 39.99);
    ```

  - Download and install a web server that supports servlets, such as Apache Tomcat, and configure it to run on a specific port, such as 8080.
  - Download and add the JDBC driver for the database to the web server's classpath, such as mysql-connector.jar for MySQL.
  - Create a Java servlet class that extends HttpServlet and overrides the doGet or doPost method to handle the HTTP requests and responses. For example, the following servlet class can be used to query the book table and display the results in a HTML table:

    ```java
    import java.io.*;
    import java.sql.*;
    import javax.servlet.*;
    import javax.servlet.http.*;

    public class BookServlet extends HttpServlet {

      // JDBC driver name and database URL
      static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
      static final String DB_URL = "jdbc:mysql://localhost:3306/books";

      // Database credentials
      static final String USER = "root";
      static final String PASS = "password";

      // Method to handle GET requests
      public void doGet(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException {

        // Set response content type
        response.setContentType("text/html");

        // Get the printwriter object from response to write the required html in the response
        PrintWriter out = response.getWriter();

        // Write the HTML header
        out.println("<html><head><title>Book Query</title></head><body>");

        // Write the HTML form to get the user input
        out.println("<form method='post' action='BookServlet'>");
        out.println("<p>Enter the book title or author name to search:</p>");
        out.println("<input type='text' name='query' required>");
        out.println("<input type='submit' value='Search'>");
        out.println("</form>");

        // Write the HTML footer
        out.println("</body></html>");
      }

      // Method to handle POST requests
      public void doPost(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException {

        // Set response content type
        response.setContentType("text/html");

        // Get the printwriter object from response to write the required html in the response
        PrintWriter out = response.getWriter();

        // Write the HTML header
        out.println("<html><head><title>Book Query</title></head><body>");

        // Get the user input from the request
        String query = request.getParameter("query");

        // Declare JDBC objects
        Connection conn = null;
        PreparedStatement stmt = null;
        ResultSet rs = null;

        try {
          // Register JDBC driver
          Class.forName(JDBC_DRIVER);

          // Open a connection
          conn = DriverManager.getConnection(DB_URL, USER, PASS);

          // Prepare a SQL statement to search the book table by title or author
          String sql = "SELECT * FROM book WHERE title LIKE ? OR author LIKE ?";
          stmt = conn.prepareStatement(sql);
          stmt.setString(1, "%" + query + "%");
          stmt.setString(2, "%" + query + "%");

          // Execute the query and get the result set
          rs = stmt.executeQuery();

          // Write the HTML table to display the query results
          out.println("<table border='1'>");
          out.println("<tr><th>ID</th><th>Title</th><th>Author</th><th>Price</th></tr>");

          // Loop through the result

```




# Create MS Access Database, Create on ODBC link, Compile & execute JAVA JDVC Socket for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

## Create MS Access Database

- To create a MS Access database, you can follow these steps:
  - Open Access. If Access is already open, select File > New.
  - Select Blank database, or select a template.
  - Enter a name for the database, select a location, and then select Create.
  - If needed, select Enable content in the yellow message bar when the database opens.
- To create tables, queries, forms, reports, and other objects in the database, you can use the Navigation Pane and the ribbon tabs.
- To enter data into the tables, you can use the datasheet view or the form view.
- To save the database, you can use the Save or Save As commands in the File tab.

## Create on ODBC link

- To create an ODBC link to the MS Access database, you can follow these steps:
  - Open the ODBC Data Source Administrator from the Control Panel or the Start menu.
  - Select the System DSN tab and click Add.
  - Select the Microsoft Access Driver (*.mdb, *.accdb) and click Finish.
  - Enter a name and a description for the data source and click Select.
  - Browse to the location of the MS Access database file and click OK.
  - Click OK to create the data source.

## Compile & execute JAVA JDVC Socket

- To compile and execute a JAVA JDVC Socket program that connects to the MS Access database, you can follow these steps:
  - Write the JAVA JDVC Socket program in a text editor or an IDE. The program should import the java.sql package and use the DriverManager, Connection, Statement, and ResultSet classes to establish a connection, execute a query, and retrieve the results from the database. The program should also handle any exceptions that may occur during the process. The connection string should use the ODBC data source name that was created in the previous step.
  - Save the program as a .java file with the same name as the class name.
  - Open a command prompt and navigate to the directory where the .java file is saved.
  - Compile the program using the javac command. For example, javac MyProgram.java
  - Run the program using the java command. For example, java MyProgram
  - The program should display the output of the query or any error messages on the console.



# Unit 5 - Design server site applications using JDDC,ODBC and section tracking API

- JDBC stands for Java Database Connectivity, which is a standard Java API for connecting and executing queries with databases .
- ODBC stands for Open Database Connectivity, which is an older API for connecting and executing queries with databases, written in C language and platform-dependent  .
- JDBC-ODBC Bridge is an interface that converts JDBC API calls to ODBC API calls and vice versa, allowing Java applications to use ODBC drivers.
- Section tracking API is an API that allows web applications to track and manage user sessions, such as login, logout, preferences, shopping cart, etc.
- To design server site applications using JDDC,ODBC and section tracking API, the following steps are required:
  - Choose a suitable JDBC driver for the database that the application will use, such as MySQL, Oracle, SQL Server, etc. The driver must be compatible with the Java version and the database version.
  - Install and configure the JDBC driver on the server, following the instructions provided by the driver vendor. The driver may require some additional libraries or files to be placed in the classpath or the library path of the server.
  - If the application needs to use ODBC drivers, install and configure the JDBC-ODBC Bridge on the server, following the instructions provided by the bridge vendor. The bridge may require some additional settings or parameters to be specified in the connection string or the data source name (DSN).
  - Establish a connection to the database using the JDBC API, passing the appropriate connection string or DSN, username, password, and other parameters as needed. The connection string or DSN may vary depending on the driver or the bridge used.
  - Execute SQL queries or statements using the JDBC API, passing the connection object, the query or statement string, and other parameters as needed. The JDBC API provides various classes and methods for executing different types of queries or statements, such as Statement, PreparedStatement, CallableStatement, ResultSet, etc.
  - Process the results of the queries or statements using the JDBC API, accessing the data and metadata from the ResultSet object or the output parameters of the CallableStatement object. The JDBC API provides various methods for retrieving the data and metadata, such as getString, getInt, getBoolean, getMetaData, etc.
  - Close the connection to the database using the JDBC API, calling the close method on the connection object. The connection should be closed when it is no longer needed, to avoid resource leaks and performance issues.
  - Implement the section tracking API using the Java Servlet API, which provides various classes and methods for managing user sessions, such as HttpSession, HttpServletRequest, HttpServletResponse, Cookie, etc.
  - Create a session for each user using the getSession method of the HttpServletRequest object, passing a boolean parameter that indicates whether to create a new session or use an existing one. The getSession method returns an HttpSession object that represents the user session.
  - Store and retrieve session attributes using the setAttribute and getAttribute methods of the HttpSession object, passing the attribute name and value as parameters. The session attributes can be used to store and access user information, such as login status, preferences, shopping cart, etc.
  - Invalidate a session using the invalidate method of the HttpSession object, which removes the session and its attributes from the server. The session should be invalidated when the user logs out or the session expires.
  - Use cookies to store and retrieve session identifiers using the addCookie and getCookies methods of the HttpServletResponse and HttpServletRequest objects, respectively. The cookies can be used to associate a session with a user, by storing the session ID in the cookie and sending it to the server with each request. The cookies can be configured with various properties, such as name, value, domain, path, expiry, etc.



# Install TOMCAT web server and APACHE

- Apache Tomcat is an open source web server and servlet container that supports Java applications.
- Apache HTTP Server is a web server that can work with Tomcat to serve static and dynamic web content.
- To install and configure Tomcat and Apache, follow these steps:

## 1. Install Java
- Tomcat requires Java to run, so you need to install a Java Development Kit (JDK) on your system.
- You can download the latest JDK from https://www.oracle.com/java/technologies/downloads/.
- Follow the instructions to install the JDK and set the JAVA_HOME environment variable to point to the installation directory.

## 2. Create Tomcat System User
- Running Tomcat as the root user is not recommended for security reasons.
- You can create a dedicated system user and group for Tomcat with the following commands:

```bash
sudo groupadd tomcat
sudo useradd -s /bin/false -g tomcat -d /opt/tomcat tomcat
```

- This will create a tomcat user and group with no login shell and a home directory at /opt/tomcat.

## 3. Install and Configure Apache Tomcat
- You can download the latest Tomcat binary distribution from https://tomcat.apache.org/download-10.cgi.
- Choose the tar.gz file under the Core section and save it to your system.
- Extract the file to the /opt/tomcat directory with the following commands:

```bash
sudo mkdir /opt/tomcat
sudo tar xzvf apache-tomcat-10*tar.gz -C /opt/tomcat --strip-components=1
```

- Change the ownership and permissions of the Tomcat files and directories with the following commands:

```bash
sudo chown -R tomcat: /opt/tomcat
sudo chmod +x /opt/tomcat/bin/*.sh
```

- Create a systemd service file for Tomcat with the following command:

```bash
sudo nano /etc/systemd/system/tomcat.service
```

- Paste the following content into the file and save it:

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

- Reload the systemd daemon and start the Tomcat service with the following commands:

```bash
sudo systemctl daemon-reload
sudo systemctl start tomcat
```

- Enable the Tomcat service to start on boot with the following command:

```bash
sudo systemctl enable tomcat
```

- Verify that Tomcat is running by accessing http://your_server_ip:8080 in your web browser. You should see the Tomcat default page.

## 4. Install Apache HTTP Server
- You can install Apache HTTP Server from the default repositories with the following command:

```bash
sudo apt install apache2
```

- Start and enable the Apache service with the following commands:

```bash
sudo systemctl start apache2
sudo systemctl enable apache2
```

- Verify that Apache is running by accessing http://your_server_ip in your web browser. You should see the Apache default page.

## 5. Configure Tomcat to Work with Apache
- To enable Apache to communicate with Tomcat, you need to install and configure a connector module called mod_jk.
- You can install mod_jk from the default repositories with the following command:

```bash
sudo apt install libapache2-mod-jk
```

- Create a workers.properties file for mod_jk with the following command:

```bash
sudo nano /etc/libapache2-mod-jk/workers.properties
```

- Paste the following content into the file and save it:

```ini
# Define 1 real worker using ajp13
worker

```




# Access the above developed static web pages for books web site, using these servers by putting the web pages developed for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To access the static web pages for books web site, you need to have a web server that can host and serve the HTML files. You can use any web server software such as Apache, Nginx, IIS, etc. You also need to have a domain name and a web hosting service that can connect your web server to the internet.
- To put the web pages developed for the notes of the Unit 5, you need to have a database server that can store and retrieve the data for the server site applications. You can use any database software such as MySQL, PostgreSQL, Oracle, etc. You also need to have a JDBC driver that can communicate with the database server using Java. You also need to have a servlet container that can run the Java servlets that implement the section tracking API. You can use any servlet container software such as Tomcat, Jetty, GlassFish, etc.
- To design the server site applications using JDBC, ODBC and section tracking API, you need to follow these steps:

  - Create a database schema that can store the information about the books, users, sections, etc. You can use any database design tool such as MySQL Workbench, pgAdmin, Oracle SQL Developer, etc.
  - Create a JDBC connection that can establish a link between the Java servlets and the database server. You can use the DriverManager class or the DataSource class to create the connection. You also need to provide the database URL, username, password, and driver name as parameters.
  - Create a ODBC connection that can establish a link between the Java servlets and the database server. You can use the DriverManager class or the DataSource class to create the connection. You also need to provide the database URL, username, password, and driver name as parameters. You also need to configure the ODBC data source in the system settings or the registry.
  - Create a section tracking API that can manage the user sessions and store the user preferences. You can use the HttpSession class or the Cookie class to create and manipulate the sessions. You also need to use the HttpServletRequest and HttpServletResponse classes to handle the HTTP requests and responses.
  - Create the HTML pages that can display the books catalog, the user login, the user registration, and the user profile. You can use any HTML editor such as Notepad++, Sublime Text, Visual Studio Code, etc. You also need to use the <form> tag and the <input> tag to create the forms that can send the data to the servlets. You also need to use the <a> tag and the <img> tag to create the links and the images that can enhance the web pages.
  - Create the Java servlets that can process the data from the HTML forms and interact with the database server and the section tracking API. You can use any Java IDE such as Eclipse, NetBeans, IntelliJ IDEA, etc. You also need to use the @WebServlet annotation or the web.xml file to map the servlets to the URL patterns. You also need to use the doGet and doPost methods to handle the GET and POST requests. You also need to use the PrintWriter class or the RequestDispatcher class to send the output to the web pages or to other servlets.
  - Deploy the HTML pages, the Java servlets, the JDBC driver, and the ODBC driver to the web server and the servlet container. You can use any deployment tool such as FTP, SCP, Maven, Gradle, etc. You also need to make sure that the web server and the servlet container are running and configured properly. You also need to make sure that the web server and the database server are connected and accessible.
  - Test the web site by accessing the web pages from a web browser. You can use any web browser such as Chrome, Firefox, Edge, Safari, etc. You also need to check the functionality and the performance of the web site. You also need to check the security and the usability of the web site. You also need to check the compatibility and the responsiveness of the web site.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss.

Here is the content you requested:

# Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- In this unit, you will learn how to design server-side applications using Java Database Connectivity (JDBC), Open Database Connectivity (ODBC) and session tracking API.
- JDBC is an API that allows Java applications to interact with various types of databases using a standard interface.
- ODBC is an API that provides a common interface for accessing different types of data sources, such as relational databases, spreadsheets, text files, etc.
- Session tracking is a technique that enables a web server to maintain the state of a user across multiple requests, such as login information, shopping cart items, preferences, etc.
- Session tracking API is a set of classes and methods that allow Java servlets to create, manage and manipulate session objects.

## Learning objectives

By the end of this unit, you should be able to:

- Explain the concepts and benefits of JDBC and ODBC.
- Use JDBC drivers and ODBC drivers to connect to different types of databases and data sources.
- Perform basic CRUD (create, read, update and delete) operations on data using JDBC and ODBC.
- Use prepared statements, callable statements and batch updates to improve the performance and security of database operations.
- Handle exceptions and errors that may occur during database operations.
- Explain the concepts and benefits of session tracking.
- Use cookies, URL rewriting, hidden fields and HttpSession class to implement session tracking in Java servlets.
- Manage the lifecycle and attributes of session objects.
- Use listeners and filters to monitor and modify the behavior of session objects.

## Notes

The notes for this unit are password-protected. To access the notes, you need to enter the correct password for your user name. The passwords are as follows:

- user1: pwd1
- user2: pwd2
- user3: pwd3
- user4: pwd4

Please enter your user name and password below to access the notes.



# Write a servlet for doing the following for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- JDDC stands for Java Database Connectivity, which is a standard API for connecting to relational databases from Java applications.
- ODBC stands for Open Database Connectivity, which is a standard API for connecting to various types of databases from different programming languages.
- Section tracking API is a feature of servlets that allows storing and retrieving information about the state of a user session across multiple requests.

## Steps to write a servlet for doing the following:

- Import the necessary packages, such as javax.servlet, javax.servlet.http, java.sql, etc.
- Define a public class that extends HttpServlet and implements the doGet or doPost method, depending on the type of request you want to handle.
- In the doGet or doPost method, get the request parameters, such as the user name, password, etc.
- Create a connection to the database using either JDBC or ODBC, depending on the driver you have installed and the database you want to access.
- Execute SQL queries using the connection object and the statement or prepared statement object, depending on the type of query you want to execute.
- Process the results of the queries using the result set object and the metadata object, depending on the information you want to retrieve.
- Store or retrieve information about the user session using the session object and the getAttribute or setAttribute methods, depending on the operation you want to perform.
- Generate the response using the response object and the print writer object, depending on the type of output you want to produce.
- Close the connection, statement, result set, and print writer objects, using the close method, to release the resources.
- Handle any exceptions using the try-catch-finally blocks, depending on the type of error you want to handle.



# Create a Cookie and add these four user id’s and passwords to this Cookie for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A cookie is a small piece of data that is stored by the browser and sent to the server with every request. Cookies can be used to store user preferences, session information, authentication tokens, etc.
- To create a cookie in Java, we can use the `Cookie` class from the `javax.servlet.http` package. We can also use the `document.cookie` property in JavaScript .
- To add a cookie to the response, we can use the `addCookie(Cookie)` method of the `HttpServletResponse` interface. To read a cookie from the request, we can use the `getCookies()` method of the `HttpServletRequest` interface.
- To set the expiration date of a cookie, we can use the `setMaxAge(int)` method of the `Cookie` class. To delete a cookie, we can set its max age to zero.
- To store user id's and passwords in a cookie, we need to encode them using a suitable algorithm, such as Base64, to avoid exposing them in plain text. We also need to use a secure and http-only cookie to prevent unauthorized access or modification by malicious scripts.
- Here is an example of how to create a cookie and add four user id's and passwords to it in Java:

```java
// import the necessary packages
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.Base64;

// create a cookie object with a name and a value
Cookie cookie = new Cookie("users", "");

// encode the user id's and passwords using Base64
String user1 = Base64.getEncoder().encodeToString("user1:password1".getBytes());
String user2 = Base64.getEncoder().encodeToString("user2:password2".getBytes());
String user3 = Base64.getEncoder().encodeToString("user3:password3".getBytes());
String user4 = Base64.getEncoder().encodeToString("user4:password4".getBytes());

// concatenate the encoded user id's and passwords with a separator
String value = user1 + "|" + user2 + "|" + user3 + "|" + user4;

// set the value of the cookie
cookie.setValue(value);

// set the max age of the cookie to one day
cookie.setMaxAge(24 * 60 * 60);

// set the secure and http-only flags of the cookie
cookie.setSecure(true);
cookie.setHttpOnly(true);

// add the cookie to the response
response.addCookie(cookie);
```



# Read the user id and passwords entered in the Login form and authenticate with the values available in the cookies for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A login form is a web page that allows users to enter their user id and password to access a protected resource or service.
- A cookie is a small piece of data that is stored by the web browser on the user's device. Cookies can be used to store information such as user preferences, session identifiers, authentication tokens, etc.
- To authenticate the user id and password entered in the login form with the values available in the cookies, the following steps can be followed:

  - Create a login form using HTML and CSS. The form should have two input fields for user id and password, and a submit button. For example:

  ```html
  <form action="login" method="POST">
    <label for="user_id">User ID:</label>
    <input type="text" id="user_id" name="user_id" required>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required>
    <button type="submit">Login</button>
  </form>
  ```

  - Create a servlet that handles the login request. The servlet should use the `HttpServletRequest` and `HttpServletResponse` objects to access the request and response data. The servlet should also use the `Cookie` class to create, read, and manipulate cookies. For example:

  ```java
  import javax.servlet.*;
  import javax.servlet.http.*;
  import java.io.*;

  public class LoginServlet extends HttpServlet {

    // A method to check if the user id and password are valid
    // This method can be replaced by a database query or any other logic
    private boolean isValid(String user_id, String password) {
      // For simplicity, assume that the valid user id and password are "admin" and "1234"
      return user_id.equals("admin") && password.equals("1234");
    }

    // A method to create a cookie with the user id and password
    private Cookie createCookie(String user_id, String password) {
      // Create a cookie with the name "login" and the value as the user id and password separated by a colon
      Cookie cookie = new Cookie("login", user_id + ":" + password);
      // Set the cookie's max age to one hour (in seconds)
      cookie.setMaxAge(60 * 60);
      // Set the cookie's path to the root of the web application
      cookie.setPath("/");
      // Return the cookie
      return cookie;
    }

    // A method to read the cookie with the user id and password
    private Cookie readCookie(HttpServletRequest request) {
      // Get the array of cookies from the request
      Cookie[] cookies = request.getCookies();
      // If the cookies are not null, loop through them
      if (cookies != null) {
        for (Cookie cookie : cookies) {
          // If the cookie's name is "login", return the cookie
          if (cookie.getName().equals("login")) {
            return cookie;
          }
        }
      }
      // If no cookie is found, return null
      return null;
    }

    // A method to delete the cookie with the user id and password
    private void deleteCookie(HttpServletResponse response) {
      // Create a cookie with the name "login" and an empty value
      Cookie cookie = new Cookie("login", "");
      // Set the cookie's max age to zero (to expire it immediately)
      cookie.setMaxAge(0);
      // Set the cookie's path to the root of the web application
      cookie.setPath("/");
      // Add the cookie to the response
      response.addCookie(cookie);
    }

    // A method to handle the GET request
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
      // Set the content type of the response to text/html
      response.setContentType("text/html");
      // Get the print writer object to write the response
      PrintWriter out = response.getWriter();
      // Read the cookie with the user id and password
      Cookie cookie = readCookie(request);
      // If the cookie is not null, get the cookie value and split it by a colon
      if (cookie != null) {
        String value = cookie.getValue();
        String[] parts = value.split(":");
        // If the parts have length 2, get the user id and password from the parts
        if (parts.length == 2) {
          String user_id = parts[0];
          String password = parts[1

```




# Install a database (MySQL or Oracle) for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

## MySQL Installation on Microsoft Windows

- MySQL is a popular open-source relational database management system that can be used to store and manipulate data for web applications.
- To install MySQL on Windows, you need to download the MySQL Installer for Windows from https://dev.mysql.com/downloads/installer/ and execute it.
- The MySQL Installer will guide you through the steps of choosing a setup type, selecting the products to install, configuring the server, creating a root password, and applying the configuration.
- The setup type can be either Developer Default, Server Only, Client Only, or Custom. The Developer Default option will install the most common components for developing web applications, such as MySQL Server, MySQL Workbench, MySQL Shell, MySQL Router, MySQL Connector/ODBC, and MySQL Connector/J.
- The Server Only option will install only the MySQL Server and the required components, such as MySQL Installer and MySQL Notifier.
- The Client Only option will install only the client tools, such as MySQL Workbench, MySQL Shell, MySQL Router, and MySQL Connectors.
- The Custom option will allow you to choose the specific products and features that you want to install.
- After choosing the setup type, the MySQL Installer will download and install the selected products. You can monitor the progress and status of the installation on the screen.
- Next, the MySQL Installer will prompt you to configure the MySQL Server. You can choose the type of configuration, such as Development Machine, Server Machine, or Dedicated Machine, depending on the intended use of the server. You can also customize the configuration options, such as the port number, the network address, the authentication method, the character set, and the Windows service name.
- The MySQL Installer will also ask you to create a root password for the MySQL Server. The root user is the administrator of the MySQL Server and has full privileges to perform any operation on the database. You should choose a strong and secure password and remember it for future use.
- Finally, the MySQL Installer will apply the configuration and start the MySQL Server. You can verify that the MySQL Server is running by opening the MySQL Notifier in the system tray or by using the MySQL Command Line Client from the command prompt.
- You have successfully installed MySQL on Windows. You can now use the MySQL Workbench, MySQL Shell, or MySQL Connector/J to connect to the MySQL Server and create and manage databases and tables for your web applications.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to create a table with the following fields: name, password, email-id, phone number for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab. Here is the table I have created:

| name | password | email-id | phone number |
|------|----------|----------|--------------|
| Alice | 123456 | alice@gmail.com | 9876543210 |
| Bob | 654321 | bob@yahoo.com | 1234567890 |
| Charlie | 789456 | charlie@outlook.com | 4567891230 |

Some points to note about the table are:

- The table name can be anything you want, but it should be descriptive and unique.
- The fields should have appropriate data types and constraints, such as varchar, int, not null, primary key, etc.
- The table should be created using SQL commands, such as create table, insert into, etc.
- The table should be connected to a database server using JDBC, ODBC or session tracking API, depending on the programming language and framework you are using.
- The table should be used to store and retrieve user information for the server side applications you are designing, such as login, registration, profile, etc.



# Write a java program/servlet/JSP to connect to that database and extract data from the tables and display them

- To write a java program/servlet/JSP to connect to a database and extract data from the tables and display them, you need to follow these steps:

  - Import the required packages for JDBC (Java Database Connectivity), such as `java.sql.*` and `javax.sql.*`.
  - Load and register the JDBC driver for the database you want to connect to, such as `com.mysql.cj.jdbc.Driver` for MySQL.
  - Establish a connection to the database using the `DriverManager.getConnection()` method, passing the URL, username and password of the database as parameters.
  - Create a `Statement` or `PreparedStatement` object to execute SQL queries on the database.
  - Execute the query using the `executeQuery()` method, which returns a `ResultSet` object that contains the data from the tables.
  - Iterate over the `ResultSet` object using the `next()` method, and access the data using the `getXXX()` methods, where XXX is the data type of the column, such as `getString()`, `getInt()`, `getDouble()`, etc.
  - Display the data using `System.out.println()` or any other output method, such as `JOptionPane.showMessageDialog()` for GUI applications.
  - Close the `ResultSet`, `Statement` and `Connection` objects using the `close()` method to release the resources.

- Here is an example of a java program that connects to a MySQL database and displays the data from a table called `employees`:

```java
// Import the required packages
import java.sql.*;

public class DatabaseConnection {

  public static void main(String[] args) {
    // Declare the JDBC objects
    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;

    try {
      // Load and register the JDBC driver
      Class.forName("com.mysql.cj.jdbc.Driver");

      // Establish the connection to the database
      String url = "jdbc:mysql://localhost:3306/testdb";
      String user = "root";
      String password = "root";
      conn = DriverManager.getConnection(url, user, password);

      // Create a statement object to execute the query
      stmt = conn.createStatement();

      // Execute the query and get the result set
      String sql = "SELECT * FROM employees";
      rs = stmt.executeQuery(sql);

      // Display the data from the result set
      while (rs.next()) {
        // Retrieve the data by column name
        int id = rs.getInt("id");
        String name = rs.getString("name");
        String email = rs.getString("email");
        double salary = rs.getDouble("salary");

        // Print the data
        System.out.println("ID: " + id);
        System.out.println("Name: " + name);
        System.out.println("Email: " + email);
        System.out.println("Salary: " + salary);
        System.out.println();
      }
    } catch (Exception e) {
      // Handle any errors
      e.printStackTrace();
    } finally {
      // Close the JDBC objects
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
      } catch (SQLException se) {
        se.printStackTrace();
      }
    }
  }
}
```

- Here is an example of a servlet that connects to a MySQL database and displays the data from a table called `employees` in an HTML table:

```java
// Import the required packages
import java.io.*;
import java.sql.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class DatabaseConnectionServlet extends HttpServlet {

  public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    // Declare the JDBC objects
    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;

    // Set the content type and character encoding of the response
    response.setContentType("text/html");
    response.setCharacterEncoding("UTF-8");

    // Get the output stream to write the response
    PrintWriter out = response.getWriter();

    try {
      // Load and register the JDBC driver
      Class.forName("com.mysql.cj.jdbc.Driver");

      // Establish the connection to the database
      String url = "jdbc:mysql://localhost:3306/testdb";
      String user = "root";
      String password = "root";
      conn = DriverManager.getConnection(url, user, password);

      // Create a statement object to execute the query
      stmt =

```




# Insert the details of the users who register with the web site, whenever a new user clicks the submit button in the registration page for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- JDDC stands for Java Database Connectivity, which is an API that allows Java applications to interact with various types of databases .
- ODBC stands for Open Database Connectivity, which is an older API that allows applications written in different languages and platforms to access databases .
- Section tracking API is an interface that allows web applications to maintain state information across multiple requests from the same client.
- To insert the details of the users who register with the web site, the following steps are required:
  - Create a database table to store the user information, such as name, email, password, etc.
  - Create a registration form in HTML that collects the user input and sends it to a servlet or JSP page using the POST method.
  - Create a servlet or JSP page that receives the user input and validates it for errors and security issues.
  - Use the JDDC API to establish a connection with the database using a suitable driver, such as JDBC-ODBC bridge, JDBC driver, or API driver   .
  - Use the JDDC API to execute a SQL statement that inserts the user data into the database table.
  - Use the section tracking API to create a session object for the user and store the user information in the session attributes.
  - Send a response to the user that confirms the registration and displays the user information.



# Write a JSP which insert the details of the 3 or 4 users who register with the web site by using registration form for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- JSP stands for Java Server Pages, which is a technology that allows creating dynamic web pages using Java code.
- A registration form is a web page that allows users to enter their personal information and create an account on a website.
- To write a JSP that inserts the details of the users who register with the website, we need to follow these steps:

  - Create a database table to store the user details, such as name, email, password, etc. For example, we can use Oracle database and create a table named user432 with the following command:

    ```sql
    CREATE TABLE "USER432" (
      "NAME" VARCHAR2 (4000),
      "EMAIL" VARCHAR2 (4000),
      "PASS" VARCHAR2 (4000)
    )
    ```

  - Create a JSP page that displays the registration form with the input fields for the user details. For example, we can name the JSP page as index.jsp and write the following code:

    ```html
    <form action="process.jsp">
      <input type="text" name="uname" value="Name..." onclick="this.value=''"/><br/>
      <input type="text" name="uemail" value="Email ID..." onclick="this.value=''"/><br/>
      <input type="password" name="upass" value="Password..." onclick="this.value=''"/><br/>
      <input type="submit" value="register"/>
    </form>
    ```

  - Create another JSP page that processes the user input and inserts the user details into the database table. For example, we can name the JSP page as process.jsp and write the following code:

    ```java
    <%@ page import="java.sql.*" %>
    <%
      //Get the user input from the request object
      String name = request.getParameter("uname");
      String email = request.getParameter("uemail");
      String pass = request.getParameter("upass");

      //Create a connection to the database using JDBC and ODBC
      Class.forName("oracle.jdbc.driver.OracleDriver");
      Connection con = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","oracle");

      //Create a statement object to execute SQL queries
      Statement st = con.createStatement();

      //Insert the user details into the user432 table
      int i = st.executeUpdate("insert into user432 values('"+name+"','"+email+"','"+pass+"')");

      //Check if the insertion is successful
      if(i>0){
        //Display a success message
        out.println("You are successfully registered");
      }
      else{
        //Display an error message
        out.println("Registration failed");
      }

      //Close the connection and statement objects
      st.close();
      con.close();
    %>
    ```

  - Run the index.jsp page on a web server, such as Tomcat, and fill the registration form with the user details. For example, we can enter the following details for three users:

    | Name  | Email             | Password |
    | ----- | ----------------- | -------- |
    | Alice | alice@example.com | 1234     |
    | Bob   | bob@example.com   | 5678     |
    | Carol | carol@example.com | 9012     |

  - Click the register button and see the result of the process.jsp page. For example, we can see the following output:

    ```
    You are successfully registered
    ```

  - Check the database table and see the inserted user details. For example, we can see the following records in the user432 table:

    | NAME  | EMAIL             | PASS |
    | ----- | ----------------- | ---- |
    | Alice | alice@example.com | 1234 |
    | Bob   | bob@example.com   | 5678 |
    | Carol | carol@example.com | 9012 |

- This is how we can write a JSP that inserts the details of the users who register with the website by using registration form for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab.



# Authenticate the user when he submits the login form using the user name and password from the database for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To authenticate the user when he submits the login form using the user name and password from the database, we need to use JDBC (Java Database Connectivity) and ODBC (Open Database Connectivity) drivers to connect to the database and execute SQL queries to verify the user credentials .
- JDBC and ODBC are APIs (Application Programming Interfaces) that allow Java applications to interact with various types of databases, such as Oracle, MySQL, PostgreSQL, etc. JDBC and ODBC drivers are software components that implement the API methods and provide a bridge between the application and the database .
- To use JDBC and ODBC drivers, we need to configure them with the appropriate connection parameters, such as the database URL, the username, the password, the driver class name, etc. Depending on the database, we may also need to enable authentication methods, such as personal access tokens, IAM credentials, or single sign-on .
- Once we have configured the JDBC and ODBC drivers, we can use them to establish a connection to the database and create a statement object to execute SQL queries. For example, we can use the following code snippet to connect to an Oracle database using JDBC:

```java
// Load the Oracle JDBC driver
Class.forName("oracle.jdbc.driver.OracleDriver");

// Connect to the database
Connection conn = DriverManager.getConnection(
  "jdbc:oracle:thin:@localhost:1521:xe", "username", "password");

// Create a statement object
Statement stmt = conn.createStatement();
```

- To authenticate the user, we need to create a login form that accepts the user name and password as input fields. We can use HTML and CSS to design the form and use JavaScript to validate the input and send it to the server using AJAX (Asynchronous JavaScript and XML) or a form submission method. For example, we can use the following HTML code to create a simple login form:

```html
<form id="login-form" method="post" action="login.jsp">
  <div>
    <label for="username">User Name:</label>
    <input type="text" id="username" name="username" required>
  </div>
  <div>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required>
  </div>
  <div>
    <input type="submit" value="Login">
  </div>
</form>
```

- To process the login form, we need to create a server-side application that receives the user name and password from the form and uses the JDBC or ODBC driver to query the database and check if the user credentials are valid. We can use Java Servlets, JSP (Java Server Pages), or any other web framework to create the server-side application. For example, we can use the following JSP code to process the login form using JDBC:

```jsp
<%@ page import="java.sql.*" %>
<%
  // Get the user name and password from the form
  String username = request.getParameter("username");
  String password = request.getParameter("password");

  // Connect to the database
  Connection conn = DriverManager.getConnection(
    "jdbc:oracle:thin:@localhost:1521:xe", "username", "password");
  Statement stmt = conn.createStatement();

  // Query the database to check if the user credentials are valid
  String sql = "select username, password from users where username = '" + username + "'";
  ResultSet rs = stmt.executeQuery(sql);

  // If the user exists and the password matches, redirect to the welcome page
  if (rs.next() && password.equals(rs.getString("password"))) {
    response.sendRedirect("welcome.jsp");
  }
  // Otherwise, display an error message
  else {
    out.println("Invalid user name or password");
  }

  // Close the database connection
  rs.close();
  stmt.close();
  conn.close();
%>
```

- To track the user session, we need to use a session tracking API that allows us to store and retrieve information about the user across multiple requests. There are various ways to implement session tracking, such as cookies, URL rewriting, hidden fields, or HttpSession objects. For example, we can use the HttpSession object



# Design and implement a simple shopping cart example with session tracking API

- Session tracking is a technique to maintain the conversational state between a client and a server in a web application. It is needed when the client makes multiple requests to the server and the server needs to identify the client and its data. For example, in a shopping cart application, the client can add items to the cart using multiple requests, and the server needs to know which cart belongs to which client .
- Session tracking can be implemented using various methods, such as cookies, URL rewriting, hidden form fields, and HTTP session objects. Each method has its own advantages and disadvantages, such as security, performance, and compatibility.
- A session tracking API is an interface that provides methods and properties to create, access, and manage session data on the server. For example, the Java Servlet API provides the HttpSession interface that allows the servlet to store and retrieve session attributes, set the session timeout, invalidate the session, etc.
- A shopping cart API is an interface that provides methods and properties to create, update, and delete items in the cart, calculate the total price, apply discounts, etc. For example, the Shopify API provides the Cart resource that allows the client to add, remove, and update items in the cart, get the cart information, and check out the cart.
- A simple shopping cart example with session tracking API can be designed and implemented as follows:

  - The client sends a request to the server to create a new cart. The server creates a new cart object and assigns a unique identifier to it. The server also creates a new session object and stores the cart identifier as a session attribute. The server sends a response to the client with the cart information and a cookie that contains the session identifier.
  - The client sends a request to the server to add an item to the cart. The server reads the cookie from the request and retrieves the session object using the session identifier. The server then retrieves the cart object using the cart identifier from the session attribute. The server updates the cart object with the new item and sends a response to the client with the updated cart information.
  - The client repeats the previous step to add more items to the cart. The server updates the cart object and the session object accordingly.
  - The client sends a request to the server to check out the cart. The server reads the cookie from the request and retrieves the session object using the session identifier. The server then retrieves the cart object using the cart identifier from the session attribute. The server calculates the total price of the cart and sends a response to the client with the payment information.
  - The client sends a request to the server to confirm the payment. The server reads the cookie from the request and retrieves the session object using the session identifier. The server then retrieves the cart object using the cart identifier from the session attribute. The server processes the payment and sends a response to the client with the confirmation information. The server also invalidates the session object and the cart object.

- The following is a possible pseudocode implementation of the shopping cart example with session tracking API:

  - Server-side:

    ```java
    // Create a new cart and a new session
    public void createCart(HttpServletRequest request, HttpServletResponse response) {
      // Create a new cart object with a unique identifier
      Cart cart = new Cart(UUID.randomUUID().toString());
      // Create a new session object and store the cart identifier as a session attribute
      HttpSession session = request.getSession(true);
      session.setAttribute("cartId", cart.getId());
      // Set a cookie with the session identifier in the response
      Cookie cookie = new Cookie("sessionId", session.getId());
      response.addCookie(cookie);
      // Send the cart information in the response
      response.setContentType("application/json");
      response.getWriter().write(cart.toJson());
    }

    // Add an item to the cart
    public void addItem(HttpServletRequest request, HttpServletResponse response) {
      // Read the cookie from the request and get the session identifier
      Cookie[] cookies = request.getCookies();
      String sessionId = null;
      for (Cookie cookie : cookies) {
        if (cookie.getName().equals("sessionId")) {
          sessionId = cookie.getValue();
          break;
        }
      }
      // Retrieve the session object using the session identifier
      HttpSession session = request.getSession(false);
      if (session == null || !session.getId().equals(sessionId)) {
        // Invalid session, send an error response
        response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Invalid session");
        return;
      }
      // Retrieve the cart identifier from the session attribute

```


