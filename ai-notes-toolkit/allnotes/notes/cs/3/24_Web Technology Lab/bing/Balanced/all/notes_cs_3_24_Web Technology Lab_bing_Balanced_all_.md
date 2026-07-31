

## Unit 1 - Develop static web pages using HTML

- HTML stands for HyperText Markup Language. It is the standard language for creating web pages and web applications.
- HTML consists of elements that define the structure and content of a web page. Elements are enclosed by tags, which are written in angle brackets (< and >).
- HTML elements can have attributes, which provide additional information or functionality to the elements. Attributes are written inside the start tag, after the element name, and consist of a name and a value separated by an equal sign (=).
- HTML elements can be nested, which means that one element can contain another element inside it. The inner element is called the child element, and the outer element is called the parent element. The child element inherits some properties from the parent element, such as alignment, font, and color.
- HTML elements can be classified into two types: block-level elements and inline elements. Block-level elements create a new line on the web page and occupy the entire width of the parent element. Inline elements do not create a new line and only occupy the space needed by their content. Examples of block-level elements are `<div>`, `<p>`, `<h1>`-`<h6>`, `<ul>`, `<ol>`, `<li>`, `<table>`, `<tr>`, `<td>`, `<th>`, `<form>`, and `<button>`. Examples of inline elements are `<span>`, `<a>`, `<img>`, `<input>`, `<label>`, `<select>`, `<option>`, `<textarea>`, `<strong>`, `<em>`, `<br>`, and `<hr>`.
- HTML documents have a basic structure that consists of the following elements: `<!DOCTYPE html>`, `<html>`, `<head>`, `<title>`, `<body>`, and `<meta>`. The `<!DOCTYPE html>` declaration specifies the HTML version and should be the first line of the document. The `<html>` element is the root element that contains all other elements. The `<head>` element contains information about the document, such as the title, the character encoding, the style sheets, and the scripts. The `<title>` element defines the title of the document, which is displayed on the browser tab or window. The `<body>` element contains the visible content of the document, such as text, images, links, forms, and tables. The `<meta>` element provides metadata about the document, such as the author, the keywords, the description, and the viewport.
- HTML supports various types of content, such as text, images, links, lists, tables, forms, multimedia, and graphics. Text can be formatted using different elements, such as headings, paragraphs, line breaks, horizontal rules, bold, italic, underline, strike-through, subscript, superscript, and quotation marks. Images can be inserted using the `<img>` element, which has attributes such as `src`, `alt`, `width`, `height`, and `title`. Links can be created using the `<a>` element, which has attributes such as `href`, `target`, `rel`, and `title`. Lists can be created using the `<ul>` element for unordered lists, the `<ol>` element for ordered lists, and the `<li>` element for list items. Tables can be created using the `<table>` element, which contains the `<tr>` element for table rows, the `<td>` element for table data cells, and the `<th>` element for table header cells. Forms can be created using the `<form>` element, which contains various input elements, such as `<input>`, `<label>`, `<select>`, `<option>`, `<textarea>`, and `<button>`. Multimedia can be embedded using the `<audio>` element for audio files, the `<video>` element for video files, and the `<source>` element for specifying multiple sources. Graphics can be drawn using the `<canvas>` element, which provides a drawing context for JavaScript.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some points to write HTML/Java scripts to display your CV in navigator, your Institute website, Department Website and Tutorial website for specific subject for the notes of the Unit 1 - Develop static web pages using HTML in the subject of Web Technology Lab:

- To create a web page using HTML, you need to use tags, attributes and elements to define the structure and content of the page. You can use a text editor or an IDE to write the HTML code and save it as a .html file. Learn HTML
- To style the web page using CSS, you need to use selectors, properties and values to define the appearance and layout of the page. You can use a style tag, a style attribute or a separate .css file to link the CSS code to the HTML code. Learn CSS
- To add interactivity and functionality to the web page using JavaScript, you need to use variables, operators, statements and functions to define the behavior and logic of the page. You can use a script tag, a script attribute or a separate .js file to link the JavaScript code to the HTML code. Learn JavaScript
- To display your CV in navigator, you need to create a web page that contains your personal information, education, skills, experience and achievements. You can use HTML tags such as h1, p, ul, li, a, img, etc. to display the text and images. You can use CSS properties such as font-family, font-size, color, margin, padding, etc. to style the text and images. You can use JavaScript functions such as window.print(), window.open(), etc. to add features such as printing and downloading your CV. See an example
- To display your Institute website, you need to create a web page that contains the name, logo, motto, vision, mission, courses, facilities, faculty, etc. of your Institute. You can use HTML tags such as div, span, header, footer, nav, section, article, etc. to organize the content into sections. You can use CSS properties such as display, position, float, flex, grid, etc. to arrange the sections into a layout. You can use JavaScript functions such as document.getElementById(), document.querySelector(), etc. to access and manipulate the elements in the web page. See an example
- To display your Department website, you need to create a web page that contains the name, logo, objectives, programs, syllabus, projects, events, etc. of your Department. You can use HTML tags such as table, tr, td, th, caption, etc. to display the data in a tabular format. You can use CSS properties such as border, background, width, height, etc. to style the table and its cells. You can use JavaScript functions such as document.createElement(), document.appendChild(), etc. to create and insert new elements in the web page. See an example
- To display your Tutorial website for specific subject, you need to create a web page that contains the title, introduction, objectives, topics, examples, exercises, quizzes, etc. of the subject. You can use HTML tags such as h2, h3, h4, ol, dl, dt, dd, pre, code, etc. to display the headings, lists, definitions, code snippets, etc. You can use CSS properties such as text-align, text-decoration, font-weight, font-style, etc. to emphasize the important points and keywords. You can use JavaScript functions such as Math.random(), Math.floor(), etc. to generate random numbers and questions for the quizzes. See an example

I hope this helps you with your assignment. If you have any further questions, please let me know.😊



# HTML program to design an entry form of student details and send it to store at database server

- HTML stands for HyperText Markup Language, which is used to create web pages and display information on the web browser.
- HTML forms are used to collect user input and send it to a web server for processing or storing.
- HTML forms consist of one or more input elements, such as text fields, checkboxes, radio buttons, etc., that allow the user to enter or select data.
- HTML forms also have a submit button, which triggers the action of sending the form data to the web server.
- HTML forms use the `<form>` tag to define the form and its attributes, such as `action`, `method`, `enctype`, etc.
- The `action` attribute specifies the URL of the web server that will handle the form data.
- The `method` attribute specifies the HTTP method to use when sending the form data, such as `GET` or `POST`.
- The `enctype` attribute specifies the encoding type of the form data, such as `application/x-www-form-urlencoded` or `multipart/form-data`.
- The `<input>` tag is used to create different types of input elements, such as `text`, `password`, `email`, `number`, `checkbox`, `radio`, etc.
- The `<input>` tag has various attributes, such as `type`, `name`, `value`, `placeholder`, `required`, etc., that define the input element and its properties.
- The `type` attribute specifies the type of the input element, such as `text`, `password`, `email`, etc.
- The `name` attribute specifies the name of the input element, which is used to identify the form data on the web server.
- The `value` attribute specifies the default or initial value of the input element, which can be changed by the user.
- The `placeholder` attribute specifies a hint or a sample value for the input element, which is displayed when the input element is empty.
- The `required` attribute specifies that the input element must be filled in before submitting the form.
- The `<label>` tag is used to create a label for the input element, which helps the user to understand the purpose of the input element.
- The `<label>` tag has an attribute called `for`, which links the label to the input element by using the `id` attribute of the input element.
- The `<select>` tag is used to create a drop-down list of options for the user to choose from.
- The `<select>` tag has an attribute called `name`, which specifies the name of the input element on the web server.
- The `<option>` tag is used to create an option within the `<select>` tag, which has a `value` attribute that specifies the value of the option.
- The `<textarea>` tag is used to create a multi-line text input element, which allows the user to enter a large amount of text.
- The `<textarea>` tag has attributes such as `name`, `rows`, and `cols`, which specify the name, number of rows, and number of columns of the input element, respectively.
- The `<button>` tag is used to create a button element, which can perform various actions, such as submitting the form, resetting the form, or executing a script.
- The `<button>` tag has an attribute called `type`, which specifies the type of the button, such as `submit`, `reset`, or `button`.
- The `<button>` tag also has an attribute called `name`, which specifies the name of the button on the web server.
- The `<button>` tag can contain text or an image as its content, which is displayed on the button.

## Example of an HTML program to design an entry form of student details and send it to store at database server

```html
<html>
<head>
  <title>Student Entry Form</title>
</head>
<body>
  <h1>Student Entry Form</h1>
  <form action="https://example.com/student.php" method="POST" enctype="multipart/form-data">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" placeholder="Enter your name" required><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" placeholder="Enter your email" required><br>
    <label for="phone">Phone:</label>
    <input type="tel" id="phone" name="phone" placeholder="Enter your phone

```




# Unit 2 - Develop Java programs for window/web-based applications

- Java is a popular programming language that can be used to create dynamic and interactive web applications.
- Java web applications run on a web server, such as Apache Tomcat, and communicate with the web browser using technologies such as Servlets, JavaServer Pages (JSPs), and Java Web Start.
- Servlets are Java classes that handle requests and responses from the web browser. They can process data, perform business logic, and generate dynamic content.
- JSPs are HTML pages that contain Java code snippets that are executed on the server. They can use JavaBeans, custom tags, and expression language to simplify web development.
- Java Web Start is a technology that allows users to launch Java applications from the web browser with a single click. It downloads and caches the application files and ensures that they are always up to date.
- To develop Java web applications, we need the following tools and components:
  - A Java Development Kit (JDK) that provides the Java compiler and runtime environment.
  - An Integrated Development Environment (IDE) that supports Java web development, such as Eclipse or NetBeans.
  - A web server that supports Servlet and JSP technology, such as Apache Tomcat or GlassFish.
  - A web browser that supports Java Web Start, such as Chrome or Firefox.
- The steps to create a simple Java web application are as follows:
  - Create a dynamic web project in the IDE and configure the web server settings.
  - Create a Servlet class that extends the HttpServlet class and overrides the doGet or doPost methods.
  - Create a JSP page that contains HTML and Java code and uses the request and response objects to communicate with the Servlet.
  - Create a web.xml file that defines the mapping between the Servlet and the JSP page.
  - Deploy the web application to the web server and test it in the web browser.
  - Optionally, create a Java Web Start application that launches the web application from the browser.



# Write programs using JavaScript for Web Page to display browsers information

JavaScript is a scripting language that can be used to create dynamic and interactive web pages. JavaScript can access the browser's information through the `window.navigator` object, which contains properties and methods that provide information about the browser and the operating system.

Some of the common properties of the `window.navigator` object are:

- `navigator.appName`: The name of the browser application, such as "Netscape" or "Microsoft Internet Explorer".
- `navigator.appVersion`: The version of the browser application, such as "5.0" or "4.0".
- `navigator.userAgent`: The user agent string that identifies the browser and the operating system, such as "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36".
- `navigator.platform`: The platform on which the browser is running, such as "Win32" or "Linux x86_64".
- `navigator.language`: The preferred language of the user, such as "en-US" or "fr-FR".
- `navigator.cookieEnabled`: A boolean value that indicates whether cookies are enabled in the browser or not.

To display the browser's information on a web page, we can use the `document.write()` method, which writes HTML expressions or JavaScript code to a document. For example, the following program displays the browser's name, version, user agent, platform, language, and cookie status on a web page:

```javascript
// Get the browser's information from the window.navigator object
var name = navigator.appName;
var version = navigator.appVersion;
var userAgent = navigator.userAgent;
var platform = navigator.platform;
var language = navigator.language;
var cookieEnabled = navigator.cookieEnabled;

// Write the browser's information to the document
document.write("<h1>Browser Information</h1>");
document.write("<p>Name: " + name + "</p>");
document.write("<p>Version: " + version + "</p>");
document.write("<p>User Agent: " + userAgent + "</p>");
document.write("<p>Platform: " + platform + "</p>");
document.write("<p>Language: " + language + "</p>");
document.write("<p>Cookies Enabled: " + cookieEnabled + "</p>");
```

The output of the program may look something like this:

Browser Information

Note that the information from the `window.navigator` object can be misleading or inaccurate, as different browsers may use the same name, change the data, or misidentify themselves to bypass site tests. Therefore, it is not recommended to use the `window.navigator` object to detect browser versions or features. Instead, it is better to use a detection library such as Bowser, or check for the support of specific features using feature detection techniques.



# Java Applet Program For Calculator

- An applet is a small Java application that can be embedded with web browsers to display dynamic content and can run on the client-side directly .
- Applets are not stand-alone programs, they can be viewed using direct JVM .
- Applets do not contain any main() method .
- To create a Java applet program for calculator, we need to follow these steps:

  - Import the necessary packages, such as java.applet, java.awt, and java.awt.event.
  - Extend the Applet class and implement the ActionListener interface.
  - Declare the components, such as text fields, buttons, and labels, as instance variables.
  - Initialize the components in the init() method, which is invoked by the browser when the applet is loaded.
  - Add the components to the applet using the add() method.
  - Register the applet as the listener for the buttons using the addActionListener() method.
  - Override the actionPerformed() method, which is invoked by the browser when a button is clicked.
  - Perform the arithmetic operations based on the button clicked and the values entered in the text fields.
  - Display the result in the third text field using the setText() method.

- Here is an example of a Java applet program for calculator:

```java
//Import the necessary packages
import java.applet.*;
import java.awt.*;
import java.awt.event.*;

//Extend the Applet class and implement the ActionListener interface
public class Calculator extends Applet implements ActionListener {

  //Declare the components as instance variables
  TextField t1, t2, t3;
  Button b1, b2, b3, b4;
  Label l1, l2, l3, l4;

  //Initialize the components in the init() method
  public void init() {
    //Create the components
    t1 = new TextField(10);
    t2 = new TextField(10);
    t3 = new TextField(10);
    b1 = new Button("+");
    b2 = new Button("-");
    b3 = new Button("*");
    b4 = new Button("/");
    l1 = new Label("Enter First Number");
    l2 = new Label("Enter Second Number");
    l3 = new Label("Result");
    l4 = new Label("Calculator");

    //Set the layout of the applet
    setLayout(null);

    //Set the bounds of the components
    l4.setBounds(100, 20, 100, 20);
    l1.setBounds(20, 60, 100, 20);
    t1.setBounds(150, 60, 100, 20);
    l2.setBounds(20, 100, 100, 20);
    t2.setBounds(150, 100, 100, 20);
    b1.setBounds(20, 140, 50, 20);
    b2.setBounds(80, 140, 50, 20);
    b3.setBounds(140, 140, 50, 20);
    b4.setBounds(200, 140, 50, 20);
    l3.setBounds(20, 180, 100, 20);
    t3.setBounds(150, 180, 100, 20);

    //Add the components to the applet
    add(l4);
    add(l1);
    add(t1);
    add(l2);
    add(t2);
    add(b1);
    add(b2);
    add(b3);
    add(b4);
    add(l3);
    add(t3);

    //Register the applet as the listener for the buttons
    b1.addActionListener(this);
    b2.addActionListener(this);
    b3.addActionListener(this);
    b4.addActionListener(this);
  }

  //Override the actionPerformed() method
  public void actionPerformed(ActionEvent e) {
    //Get the values from the text fields
    int n1 = Integer.parseInt(t1.getText());
    int n2 = Integer.parseInt(t2.getText());

    //Perform the arithmetic operations based on the button clicked
    if (e.getSource() == b1) {
      //Addition
      t3.setText(String.valueOf(n1 + n2));
    }
    if (e.getSource() == b2) {
      //Subtraction
      t3.setText(String.valueOf(n1 - n2));
    }
    if (e.getSource() == b3) {
      //Multiplication
      t3

```




## Unit 3 - Design dynamic web pages using Javascript and XML

- Javascript is a scripting language that can be embedded in HTML documents to add interactivity, functionality, and dynamic features to web pages.
- XML stands for eXtensible Markup Language, which is a standard format for storing and exchanging structured data using tags and attributes.
- Some of the topics covered in this unit are:

  - How to use Javascript variables, data types, operators, expressions, statements, and functions to perform calculations and manipulate data.
  - How to use Javascript events, event handlers, and event listeners to respond to user actions and modify the web page content or appearance.
  - How to use Javascript objects, methods, and properties to access and manipulate the Document Object Model (DOM), which is a tree-like representation of the web page elements and attributes.
  - How to use Javascript arrays, loops, and conditional statements to store and process multiple values and perform repetitive or conditional tasks.
  - How to use Javascript built-in objects, such as Math, Date, String, and Number, to perform common operations and conversions on numbers, strings, and dates.
  - How to use Javascript regular expressions to validate user input and perform pattern matching and replacement on strings.
  - How to use Javascript to create and manipulate cookies, which are small pieces of data stored on the user's browser, to remember user preferences and settings.
  - How to use Javascript to communicate with the web server using XMLHttpRequest (XHR) object, which allows sending and receiving data asynchronously without reloading the web page.
  - How to use XML to create and parse well-formed and valid documents that follow a predefined structure and syntax.
  - How to use XML namespaces to avoid name conflicts and identify the source of the XML elements and attributes.
  - How to use XML schemas to define the structure, content, and data types of the XML documents and validate them against the schema rules.
  - How to use XML transformations (XSLT) to transform XML documents into other formats, such as HTML, using XSL style sheets and XPath expressions.
  - How to use XML parsers, such as DOM and SAX, to access and manipulate the XML documents in Javascript.



# Writing program in XML for creation of DTD, which specifies set of rules for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A DTD (Document Type Declaration) is a way to describe the structure and the legal elements and attributes of an XML document  .
- A DTD can be used to validate the XML document against the grammatical rules of the appropriate XML language  .
- A DTD can be declared internally or externally to the XML document .
- An internal DTD is included in the same file as the XML document, while an external DTD is referenced by a URL .
- An internal DTD declaration has the following syntax:

```xml
<!DOCTYPE root-element [
  <!-- Element declarations -->
  <!-- Attribute declarations -->
  <!-- Entity declarations -->
  <!-- Notation declarations -->
]>
```

- An external DTD declaration has the following syntax:

```xml
<!DOCTYPE root-element SYSTEM "URL">
```

- To create a DTD for the notes of the Unit 3, we need to define the elements and attributes that are allowed in the XML document.
- For example, we can define the following elements and attributes:

```xml
<!-- The root element of the document -->
<!ELEMENT notes (unit)+>

<!-- The unit element has a number attribute and contains one or more topics -->
<!ELEMENT unit (topic)+>
<!ATTLIST unit number CDATA #REQUIRED>

<!-- The topic element has a name attribute and contains one or more subtopics -->
<!ELEMENT topic (subtopic)+>
<!ATTLIST topic name CDATA #REQUIRED>

<!-- The subtopic element has a name attribute and contains text -->
<!ELEMENT subtopic (#PCDATA)>
<!ATTLIST subtopic name CDATA #REQUIRED>
```

- The above DTD defines the rules for the notes of the Unit 3, such as:
  - The root element must be `notes` and it must contain one or more `unit` elements.
  - The `unit` element must have a `number` attribute and it must contain one or more `topic` elements.
  - The `topic` element must have a `name` attribute and it must contain one or more `subtopic` elements.
  - The `subtopic` element must have a `name` attribute and it must contain text.
- An example of an XML document that follows the above DTD is:

```xml
<?xml version="1.0"?>
<!DOCTYPE notes [
  <!-- The DTD declarations go here -->
]>
<notes>
  <unit number="3">
    <topic name="Javascript">
      <subtopic name="Introduction">Javascript is a scripting language for the web.</subtopic>
      <subtopic name="Syntax">Javascript has a C-like syntax with curly braces and semicolons.</subtopic>
      <subtopic name="Variables">Javascript has var, let and const keywords for declaring variables.</subtopic>
    </topic>
    <topic name="XML">
      <subtopic name="Introduction">XML is a markup language for storing and exchanging data.</subtopic>
      <subtopic name="Syntax">XML has a tree-like structure with tags and attributes.</subtopic>
      <subtopic name="DTD">XML can be validated by a DTD that defines the rules for the XML document.</subtopic>
    </topic>
  </unit>
</notes>
```



# Create a style sheet in CSS/ XSL & display the document in internet explorer for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A style sheet is a file that defines the appearance and layout of an XML document.
- CSS (Cascading Style Sheets) is a language that can be used to style XML documents by applying rules to elements based on their names, attributes, or positions.
- XSL (Extensible Stylesheet Language) is a language that can be used to transform XML documents into other formats, such as HTML, by applying templates to elements based on their names, attributes, or patterns.
- To create a style sheet in CSS/ XSL, you need to follow these steps:

  - Create a text file with the extension .css or .xsl, depending on the type of style sheet you want to create.
  - In the first line of the file, declare the document to be a style sheet by using the <xsl:stylesheet> or <xsl:transform> element, and specify the version and namespace of XSL. For example:

    ```xml
    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    ```

  - In the style sheet, define the rules or templates that you want to apply to the XML document. For CSS, you can use selectors and properties to style elements. For example:

    ```css
    h1 {
      color: blue;
      font-size: 24px;
    }
    ```

    For XSL, you can use <xsl:template> elements to match elements and output the desired content. For example:

    ```xml
    <xsl:template match="title">
      <h1><xsl:value-of select="."/></h1>
    </xsl:template>
    ```

  - Save the file and link it to the XML document by using the <?xml-stylesheet?> processing instruction. For example:

    ```xml
    <?xml version="1.0"?>
    <?xml-stylesheet type="text/css" href="style.css"?>
    <book>
      <title>Web Technology Lab</title>
      <author>Sydney</author>
    </book>
    ```

- To display the document in internet explorer, you need to follow these steps:

  - Open the XML document in internet explorer by using the File > Open menu or by dragging and dropping the file into the browser window.
  - The browser will apply the style sheet to the document and render it accordingly. You can view the source code of the document by using the View > Source menu or by right-clicking on the document and selecting View Source.
  - You can also use the F12 Developer Tools to inspect the elements and styles of the document by using the Tools > F12 Developer Tools menu or by pressing F12 on the keyboard.



## Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP

- A dynamic web page is a web page that can display different content or layout depending on the user's input, preferences, or other factors  .
- A server-side dynamic web page is a web page whose construction is controlled by an application server processing server-side scripts.
- Server-side scripts are programs that run on the web server and generate HTML or other output that is sent to the web browser .
- Examples of popular server-side web languages include PHP, Python, Ruby, C#, and JavaScript (NodeJS).
- In this unit, we will learn how to design dynamic web pages using three server-side web languages: ASP, JSP, and PHP.
- ASP stands for Active Server Pages, and it is a Microsoft technology that allows you to create dynamic web pages using VBScript or JScript.
- JSP stands for Java Server Pages, and it is a Java technology that allows you to create dynamic web pages using Java code or special tags.
- PHP stands for Hypertext Preprocessor, and it is an open-source language that allows you to create dynamic web pages using PHP code embedded in HTML.
- The advantages of using server-side dynamic web pages are:
  - They can provide personalized and interactive content to the users based on their input, preferences, or other factors .
  - They can reduce the network traffic and load on the web browser by performing complex tasks on the web server .
  - They can access and manipulate data stored on the web server, such as databases, files, or sessions .
- The disadvantages of using server-side dynamic web pages are:
  - They require more processing power and memory on the web server, which can affect the performance and scalability of the web application .
  - They can expose the source code and logic of the web application to the web server, which can pose security risks if the web server is compromised .
  - They can be more difficult to debug and test than client-side dynamic web pages, as the errors and output are not visible on the web browser .

: Dynamic web page - Wikipedia
: Dynamic Website | How Dynamic Website works? | Uses of Website - EDUCBA
: Dynamic Web Pages In Java | Java Tutorial For Beginners | Edureka
: Server-side website programming - Learn web development | MDN - Mozilla
: Introduction to the server side - Learn web development | MDN - Mozilla
: Dynamic Websites - GeeksforGeeks
: ASP Introduction - W3Schools
: JSP Introduction - W3Schools
: PHP Introduction - W3Schools



### Program to illustrate JDBC connectivity

JDBC stands for Java Database Connectivity, which is an API that allows Java programs to interact with various types of databases. JDBC provides a standard set of interfaces and classes that define how to connect to a database, execute queries and updates, and retrieve the results.

To illustrate JDBC connectivity, we will use a simple example of a Java program that connects to a MySQL database and performs some basic operations. The steps involved are:

- Import the required packages, such as `java.sql.*` and `com.mysql.cj.jdbc.*`.
- Register the JDBC driver for MySQL using the `Class.forName()` method.
- Establish a connection to the database using the `DriverManager.getConnection()` method, which takes the URL, username, and password of the database as parameters.
- Create a `Statement` object using the `Connection.createStatement()` method, which allows us to execute SQL queries and updates.
- Execute a query using the `Statement.executeQuery()` method, which returns a `ResultSet` object that contains the data returned by the query.
- Iterate over the `ResultSet` using the `next()` method, and access the values of each column using the `getXXX()` methods, where XXX is the data type of the column.
- Close the `ResultSet`, `Statement`, and `Connection` objects using the `close()` method, to release the resources and avoid memory leaks.

The following code snippet shows the Java program that illustrates JDBC connectivity:

```java
// Import the required packages
import java.sql.*;
import com.mysql.cj.jdbc.*;

public class JDBCExample {

    public static void main(String[] args) {
        // Declare the variables for the database connection
        String url = "jdbc:mysql://localhost:3306/webtech"; // The URL of the database
        String user = "root"; // The username of the database
        String password = "root"; // The password of the database
        Connection conn = null; // The connection object
        Statement stmt = null; // The statement object
        ResultSet rs = null; // The result set object

        try {
            // Register the JDBC driver for MySQL
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Establish a connection to the database
            conn = DriverManager.getConnection(url, user, password);

            // Create a statement object
            stmt = conn.createStatement();

            // Execute a query
            String sql = "SELECT * FROM student"; // The SQL query to execute
            rs = stmt.executeQuery(sql); // The result set object that contains the data returned by the query

            // Iterate over the result set
            while (rs.next()) {
                // Access the values of each column using the getXXX() methods
                int id = rs.getInt("id"); // The id column
                String name = rs.getString("name"); // The name column
                int age = rs.getInt("age"); // The age column
                String course = rs.getString("course"); // The course column

                // Print the values of each row
                System.out.println("ID: " + id + ", Name: " + name + ", Age: " + age + ", Course: " + course);
            }
        } catch (Exception e) {
            // Handle any exceptions
            e.printStackTrace();
        } finally {
            // Close the result set, statement, and connection objects
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
                // Handle any SQL exceptions
                se.printStackTrace();
            }
        }
    }
}
```

The output of the program will depend on the data stored in the `student` table of the `webtech` database. For example, if the table contains the following data:

| id | name  | age | course |
|----|-------|-----|--------|
| 1  | Alice | 20  | Java   |
| 2  | Bob   | 21  | PHP    |
| 3  | Carol | 19  | ASP    |

The output of the program will be:

```
ID: 1, Name: Alice, Age: 20, Course: Java
ID: 2, Name: Bob, Age: 21, Course: PHP
ID: 3, Name: Carol, Age: 19, Course: ASP
```



# Program for maintaining database by sending queries for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

- Server-side programming is the process of creating dynamic web pages that interact with databases, files, and other servers using a programming language that runs on the web server.
- ASP, JSP, and PHP are examples of popular server-side programming languages that can be used to design dynamic web pages using server site programming.
- ASP stands for Active Server Pages, a server-side scripting technology that allows developers to create dynamic web pages using HTML, CSS, JavaScript, and VBScript. ASP was created by Microsoft and is mainly used on Windows servers.
- JSP stands for Java Server Pages, a server-side scripting technology that allows developers to create dynamic web pages using HTML, XML, or other types. JSP was created by Sun Microsystems and is based on the Java programming language. JSP is an abstraction of Servlets, which are Java classes that handle HTTP requests and responses.
- PHP stands for Hypertext Preprocessor, a server-side scripting language that allows developers to create dynamic web pages using HTML, CSS, JavaScript, and PHP code. PHP was created by Rasmus Lerdorf and is widely used on various platforms and servers.
- To maintain a database by sending queries using server-side programming, the following steps are required:
  - Establish a connection to the database server using the appropriate driver or library for the chosen server-side language. For example, in ASP, the connection can be made using the ADODB.Connection object; in JSP, the connection can be made using the java.sql.DriverManager class; in PHP, the connection can be made using the mysqli or PDO extension.
  - Create a SQL query to perform the desired operation on the database, such as selecting, inserting, updating, or deleting data. For example, the query can be a string variable or a parameterized statement that prevents SQL injection attacks.
  - Execute the query using the appropriate method or function for the chosen server-side language. For example, in ASP, the query can be executed using the ADODB.Command object or the ADODB.Recordset object; in JSP, the query can be executed using the java.sql.Statement or java.sql.PreparedStatement interface; in PHP, the query can be executed using the mysqli_query or PDO::query function.
  - Fetch the results of the query and display them on the web page using the appropriate syntax and tags for the chosen server-side language. For example, in ASP, the results can be displayed using the Response.Write method or the <%= %> tag; in JSP, the results can be displayed using the out.println method or the <%= %> tag; in PHP, the results can be displayed using the echo or print function or the <?= ?> tag.
  - Close the connection to the database server using the appropriate method or function for the chosen server-side language. For example, in ASP, the connection can be closed using the ADODB.Connection.Close method; in JSP, the connection can be closed using the java.sql.Connection.close method; in PHP, the connection can be closed using the mysqli_close or PDO::close function.



# Design and implement a simple servlet book query with the help of JDBC & SQL

- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- JDBC is a Java API that allows Java programs to interact with databases using SQL commands.
- SQL is a language for querying, manipulating, and analyzing data stored in relational databases.
- To design and implement a simple servlet book query with the help of JDBC & SQL, the following steps are required:

  1. Set up the database and the table that contains the book information, such as title, author, price, etc. You can use any relational database management system (RDBMS) that supports JDBC, such as MySQL, Oracle, PostgreSQL, etc. For example, you can create a database named `books` and a table named `book` with the following SQL commands:

  ```sql
  CREATE DATABASE books;
  USE books;
  CREATE TABLE book (
    id INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL
  );
  ```

  2. Insert some sample data into the table using SQL `INSERT` statements. For example, you can insert three books with the following SQL commands:

  ```sql
  INSERT INTO book VALUES (1, 'Java: The Complete Reference', 'Herbert Schildt', 35.99);
  INSERT INTO book VALUES (2, 'Effective Java', 'Joshua Bloch', 29.99);
  INSERT INTO book VALUES (3, 'Head First Java', 'Kathy Sierra and Bert Bates', 39.99);
  ```

  3. Download the JDBC driver for your RDBMS and add it to the classpath of your web application. The JDBC driver is a Java library that enables the communication between the Java program and the database. You can find the JDBC driver for your RDBMS from the official website or a third-party source. For example, if you are using MySQL, you can download the MySQL Connector/J from https://dev.mysql.com/downloads/connector/j/. You can then copy the JAR file to the `WEB-INF/lib` folder of your web application.

  4. Create a Java servlet class that extends the `HttpServlet` class and overrides the `doGet` or `doPost` method. The servlet class should handle the HTTP request from the client, connect to the database using JDBC, execute the SQL query to retrieve the book information, and send the HTTP response to the client. For example, you can create a servlet class named `BookServlet` with the following code:

  ```java
  import java.io.IOException;
  import java.io.PrintWriter;
  import java.sql.Connection;
  import java.sql.DriverManager;
  import java.sql.ResultSet;
  import java.sql.Statement;
  import javax.servlet.ServletException;
  import javax.servlet.annotation.WebServlet;
  import javax.servlet.http.HttpServlet;
  import javax.servlet.http.HttpServletRequest;
  import javax.servlet.http.HttpServletResponse;

  @WebServlet("/BookServlet")
  public class BookServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    // Database URL, username and password
    private static final String DB_URL = "jdbc:mysql://localhost:3306/books";
    private static final String DB_USER = "root";
    private static final String DB_PASS = "root";

    // SQL query to select all books
    private static final String SQL_QUERY = "SELECT * FROM book";

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
      // Set the content type and character encoding of the response
      response.setContentType("text/html");
      response.setCharacterEncoding("UTF-8");

      // Get the output stream of the response
      PrintWriter out = response.getWriter();

      // Try to connect to the database and execute the query
      try {
        // Load the JDBC driver
        Class.forName("com.mysql.cj.jdbc.Driver");

        // Get a connection to the database
        Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);

        // Create a statement object to execute the query
        Statement stmt = conn.createStatement();

        // Execute the query and get a result set object
        ResultSet rs = stmt.executeQuery(SQL_QUERY);

        // Print the HTML header
        out.println("<html>");
        out.println("<head>");
        out.println("<title>Book Query</title>");
        out.println("</head>");
        out.println("<body>");
        out.println("<h1>Book Query</h1>");

        // Check if the result set is not empty

```




# Create MS Access Database, Create on ODBC link, Compile & execute JAVA JDVC Socket

## Create MS Access Database

- To create a database in Microsoft Access, follow these steps  :
  - Open Access. If Access is already open, select File > New.
  - Select Blank database, or select a template that suits your needs.
  - Enter a name for the database, select a location, and then select Create.
  - If needed, select Enable content in the yellow message bar when the database opens.
  - To create tables, queries, forms, reports, and other objects, use the tabs on the ribbon or the navigation pane.

## Create on ODBC link

- To create an ODBC link to connect your MS Access database to other applications, follow these steps :
  - Open the ODBC Data Source Administrator tool on your computer. You can find it in the Control Panel > Administrative Tools > Data Sources (ODBC).
  - Select the User DSN tab, and then click Add.
  - Select the Microsoft Access Driver (*.mdb, *.accdb) from the list of drivers, and then click Finish.
  - Enter a name and a description for the data source, and then click Select.
  - Browse to the location of your MS Access database file, and then click OK.
  - Click OK to save the data source.

## Compile & execute JAVA JDVC Socket

- To compile and execute a Java program that uses JDBC to connect to your MS Access database, follow these steps :
  - Write your Java code that imports the java.sql package and uses the DriverManager class to get a connection to your database. For example:

```java
import java.sql.*;
public class JDBCExample {
  public static void main(String[] args) {
    try {
      // Load the driver
      Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
      // Get the connection
      Connection con = DriverManager.getConnection("jdbc:odbc:YourDataSourceName");
      // Create a statement
      Statement stmt = con.createStatement();
      // Execute a query
      ResultSet rs = stmt.executeQuery("SELECT * FROM YourTableName");
      // Print the results
      while (rs.next()) {
        System.out.println(rs.getString(1) + " " + rs.getString(2));
      }
      // Close the resources
      rs.close();
      stmt.close();
      con.close();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
```

  - Save your Java file with a .java extension, such as JDBCExample.java.
  - Open a command prompt and navigate to the folder where your Java file is located.
  - Compile your Java file using the javac command, such as javac JDBCExample.java. This will create a .class file with the same name as your Java file.
  - Execute your Java file using the java command, such as java JDBCExample. This will run your program and display the output on the console.

: Create a database in Access - Access  (https://support.microsoft.com/en-us/office/create-a-database-in-access-f200d95b-e429-4acc-98c1-b883d4e9fc0a)
: Basic tasks for an Access desktop database - Microsoft Support (https://support.microsoft.com/en-us/office/basic-tasks-for-an-access-desktop-database-5ddb8595-497c-4366-8327-ae79d2abdc9c)
: How to Create a Database in Microsoft Access: A Step-by-Step Guide - MUO (https://www.makeuseof.com/how-to-create-database-microsoft-access/)
: How to Connect to MS Access Database in Java Using JDBC (https://www.thoughtco.com/connect-to-ms-access-database-in-java-2033993)
: How to connect to a Microsoft Access database - Apache OpenOffice Wiki (https://wiki.openoffice.org/wiki/Documentation/How_Tos/Connecting_to_Microsoft_Access)
: JDBC - ODBC Bridge Driver Example - Tutorialspoint (https://www.tutorialspoint.com/jdbc/jdbc-odbc-bridge-driver-example.htm)
: Java JDBC MS Access Database Connection Steps - Java Guides (https://www.javaguides.net/2019/08/java-jdbc-ms-access-database-connection-steps.html)



# Unit 5 - Design server site applications using JDDC,ODBC and section tracking API

- JDBC (Java Database Connectivity) is an API that allows Java applications to interact with various types of databases using a standard interface.
- ODBC (Open Database Connectivity) is an older API that enables applications written in different languages and platforms to access databases using a common driver.
- JDBC-ODBC Bridge is a type of driver that acts as an interface between JDBC and ODBC, converting the JDBC calls to ODBC calls and vice versa.
- Section tracking API is an API that enables web applications to maintain state information across multiple requests from the same client, such as user preferences, shopping cart items, etc.

## Learning objectives

- Understand the concepts and benefits of JDBC and ODBC
- Compare and contrast JDBC and ODBC in terms of architecture, performance, security, and portability
- Identify the different types of JDBC drivers and their advantages and disadvantages
- Explain how to use JDBC to connect to a database, execute queries, and handle results
- Understand the concepts and benefits of section tracking API
- Compare and contrast different methods of section tracking, such as cookies, URL rewriting, hidden fields, and session objects
- Explain how to use section tracking API to create and manage sessions, store and retrieve session attributes, and handle session events
- Apply the best practices and design principles for developing server-side applications using JDBC, ODBC, and section tracking API



# Install TOMCAT web server and APACHE

- Apache Tomcat is an open source web server and servlet container that supports Java applications.
- Apache HTTP Server is a web server that can work with Tomcat to serve static and dynamic web content.
- To install and configure Tomcat and Apache, follow these steps:

## 1. Install Java
- Tomcat requires Java to run, so you need to install a Java Development Kit (JDK) on your system.
- You can download the latest JDK from https://www.oracle.com/java/technologies/javase-downloads.html and follow the installation instructions for your operating system.
- You also need to set the JAVA_HOME environment variable to point to the JDK installation directory.

## 2. Create Tomcat System User
- Running Tomcat as the root user is not recommended for security reasons, so you should create a dedicated system user for Tomcat.
- On Linux, you can use the following commands to create a tomcat user and group:

```bash
sudo groupadd tomcat
sudo useradd -s /bin/false -g tomcat -d /opt/tomcat tomcat
```

- On Windows, you can use the User Accounts tool in the Control Panel to create a tomcat user and assign it a password.

## 3. Install and Configure Apache Tomcat
- You can download the latest Tomcat binary distribution from https://tomcat.apache.org/download-10.cgi and choose the appropriate package for your operating system.
- On Linux, you can extract the downloaded file to /opt/tomcat and change the ownership and permissions of the files to the tomcat user and group:

```bash
sudo tar xvf apache-tomcat-10.0.13.tar.gz -C /opt/tomcat
sudo chown -R tomcat:tomcat /opt/tomcat
sudo chmod +x /opt/tomcat/bin/*.sh
```

- On Windows, you can run the downloaded installer and follow the wizard to install Tomcat to a desired location, such as C:\Tomcat.
- You also need to configure Tomcat to work with Apache by editing the server.xml file in the conf directory of the Tomcat installation.
- You need to add a Connector element inside the Service element with the following attributes:

```xml
<Connector port="8009" protocol="AJP/1.3" redirectPort="8443" />
```

- This will enable the AJP protocol on port 8009, which is used by Apache to communicate with Tomcat.
- You also need to add an Engine element inside the Host element with the following attribute:

```xml
<Engine name="Catalina" defaultHost="localhost" jvmRoute="tomcat1">
```

- This will assign a unique name to the Tomcat instance, which is used by Apache to load balance requests among multiple Tomcat servers.

## 4. Create a Tomcat Systemd Service
- On Linux, you can create a systemd service file to manage the Tomcat service.
- You can create a file named tomcat.service in the /etc/systemd/system directory with the following content:

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

- You need to adjust the JAVA_HOME and CATALINA_HOME variables according to your Java and Tomcat installation paths.
- You also need to reload the systemd daemon and enable the Tomcat service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable tomcat
```

- You can then start, stop, and check the status of the Tomcat service using the following commands:

```bash
sudo systemctl start tomcat
sudo systemctl stop tomcat
sudo systemctl status tom

```




# Access the above developed static web pages for books web site, using these servers by putting the web pages developed for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To access the static web pages for books web site, you need to have a web server that can host and serve the HTML files. You can use any web server software, such as Apache, Nginx, IIS, etc. You also need to configure the web server to point to the directory where the HTML files are stored.
- To develop the web pages for the notes of the Unit 5, you need to use Java Database Connectivity (JDBC) and Open Database Connectivity (ODBC) to connect to a database and perform queries and updates. You also need to use session tracking API to maintain the state of the user across multiple requests. You can use Java Servlets or JavaServer Pages (JSP) to create dynamic web pages that interact with the database and the session.
- To put the web pages developed for the notes of the Unit 5 on the web server, you need to copy the HTML, JSP, and Servlet files to the appropriate directories on the web server. You also need to copy the JDBC and ODBC drivers and configure them to connect to the database. You also need to enable the session tracking API on the web server and set the session timeout and cookie parameters.
- To access the web pages developed for the notes of the Unit 5, you need to use a web browser and enter the URL of the web server and the web page. For example, if the web server is running on localhost and the port is 8080, and the web page is named index.jsp, you can enter http://localhost:8080/index.jsp in the web browser. You can then view the web page and interact with the database and the session.



# Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

## Introduction

- Server-side applications are programs that run on a web server and interact with clients through web browsers or other web protocols.
- Server-side applications can perform various tasks, such as processing user input, accessing databases, generating dynamic web pages, sending emails, etc.
- Server-side applications can be written in different programming languages, such as Java, PHP, Python, etc.
- Server-side applications can use various technologies and frameworks to simplify and enhance their development, such as JDDC, ODBC, and session tracking API.

## JDDC

- JDDC stands for Java Database Driver Connectivity, which is a technology that allows Java applications to connect to various types of databases using a standard interface.
- JDDC consists of four components: drivers, driver manager, connection, and statement.
- Drivers are software modules that implement the JDDC interface for a specific database. For example, there are drivers for MySQL, Oracle, PostgreSQL, etc.
- Driver manager is a class that manages the loading and registration of drivers. It also provides methods to obtain a connection to a database using a driver.
- Connection is an interface that represents a session with a database. It provides methods to create and execute statements, manage transactions, etc.
- Statement is an interface that represents a SQL command to be executed on a database. It provides methods to execute queries, update data, retrieve results, etc.

## ODBC

- ODBC stands for Open Database Connectivity, which is a standard that allows applications to access data from various types of databases using a common interface.
- ODBC consists of three components: drivers, driver manager, and data source.
- Drivers are software modules that implement the ODBC interface for a specific database. For example, there are drivers for MySQL, Oracle, PostgreSQL, etc.
- Driver manager is a software component that manages the loading and registration of drivers. It also provides functions to obtain a connection to a database using a driver.
- Data source is a logical name that identifies a database and its connection parameters. It can be defined in a configuration file or in the system registry.

## Session tracking API

- Session tracking API is a technology that allows server-side applications to maintain state information across multiple requests from the same client.
- Session tracking API consists of two components: session and session context.
- Session is an interface that represents a unique identifier and a collection of attributes associated with a client. It provides methods to get and set attributes, invalidate the session, etc.
- Session context is an interface that manages the creation and retrieval of sessions. It provides methods to get a session by its identifier, create a new session, etc.

## Notes for users

- The notes for this unit are password-protected and can be accessed by the following users and passwords:

| User | Password |
|------|----------|
| user1 | pwd1 |
| user2 | pwd2 |
| user3 | pwd3 |
| user4 | pwd4 |

- To access the notes, the users need to enter their username and password in a web form and submit it to a server-side application that validates their credentials and displays the notes if they are correct.
- The server-side application can use JDDC or ODBC to connect to a database that stores the user information and the notes.
- The server-side application can also use session tracking API to remember the user's login status and prevent unauthorized access to the notes.



# Servlet for JDDC,ODBC and section tracking API

- A servlet is a Java program that runs on a web server or application server and handles requests from web clients.
- JDBC (Java Database Connectivity) is an API that allows Java programs to connect and interact with various types of databases using a common interface.
- ODBC (Open Database Connectivity) is an older API that allows programs written in different languages and platforms to connect and interact with various types of databases using a common interface.
- A JDBC-ODBC bridge is a type of JDBC driver that allows Java programs to use ODBC drivers to connect to databases that do not have native JDBC drivers.
- Section tracking API is an API that allows servlets to maintain state information about a web client across multiple requests using cookies, URL rewriting, hidden fields, or sessions.

## Steps to write a servlet for JDDC,ODBC and section tracking API

1. Import the required packages, such as `javax.servlet.*`, `javax.servlet.http.*`, and `java.sql.*`.
2. Define a servlet class that extends `HttpServlet` and implements the `doGet` or `doPost` methods to handle the client requests.
3. Load the JDBC-ODBC bridge driver using `Class.forName("sun.jdbc.odbc.JdbcOdbcDriver")`.
4. Establish a connection to the database using `DriverManager.getConnection("jdbc:odbc:dsn", "username", "password")`, where `dsn` is the data source name of the ODBC driver.
5. Create a `Statement` or `PreparedStatement` object to execute SQL queries on the database.
6. Use the `executeQuery` or `executeUpdate` methods to retrieve or modify data from the database, and process the results using `ResultSet` or `ResultSetMetaData` objects.
7. Use the `HttpServletResponse` object to send the response back to the client, such as setting the content type, writing HTML output, or sending redirects or errors.
8. Use the `HttpServletRequest` object to access the request parameters, headers, or cookies from the client.
9. Use the `HttpSession` object to create, retrieve, or invalidate sessions for the client, and store or retrieve attributes in the session scope.
10. Close the database connection, statement, and result set objects using the `close` methods.



# Create a Cookie and add these four user id’s and passwords to this Cookie for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A cookie is a small piece of data that is stored by the browser and sent to the server with every request. Cookies can be used to store user preferences, authentication information, session tracking, etc.
- To create a cookie in Java, we can use the `Cookie` class from the `javax.servlet.http` package. The constructor of this class takes two parameters: the name and the value of the cookie. For example:

```java
Cookie cookie = new Cookie("username", "Alice");
```

- To add a cookie to the response, we can use the `addCookie` method of the `HttpServletResponse` interface. This method takes a `Cookie` object as an argument and adds it to the `Set-Cookie` header of the response. For example:

```java
response.addCookie(cookie);
```

- To read a cookie from the request, we can use the `getCookies` method of the `HttpServletRequest` interface. This method returns an array of `Cookie` objects that represent all the cookies sent by the browser. We can loop through this array and find the cookie we want by its name. For example:

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

- To add four user ids and passwords to a cookie, we can either create four separate cookies, one for each pair of user id and password, or we can create one cookie that contains all four pairs of user id and password, separated by some delimiter. For example, using the first approach:

```java
Cookie cookie1 = new Cookie("user1", "password1");
Cookie cookie2 = new Cookie("user2", "password2");
Cookie cookie3 = new Cookie("user3", "password3");
Cookie cookie4 = new Cookie("user4", "password4");
response.addCookie(cookie1);
response.addCookie(cookie2);
response.addCookie(cookie3);
response.addCookie(cookie4);
```

Using the second approach:

```java
Cookie cookie = new Cookie("users", "user1:password1;user2:password2;user3:password3;user4:password4");
response.addCookie(cookie);
```

- Note that storing passwords in plain text in cookies is not a secure practice and should be avoided. A better way to handle authentication is to use a session id or a token that is stored in a cookie and verified by the server.



# Read the user id and passwords entered in the Login form and authenticate with the values available in the cookies for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To read the user id and password from the login form in Java, you can use the `request.getParameter()` method to get the values entered by the user in the HTML input fields. For example, if your login form has `<input type="text" name="userid">` and `<input type="password" name="password">`, you can get the user id and password as follows:

```java
String userid = request.getParameter("userid");
String password = request.getParameter("password");
```

- To authenticate the user id and password with the values available in the cookies, you can use the `request.getCookies()` method to get an array of `Cookie` objects that represent the cookies sent by the browser. You can then iterate over the array and compare the cookie names and values with the user id and password. For example, if your cookies have the names "userid" and "password", you can do something like this:

```java
Cookie[] cookies = request.getCookies();
boolean authenticated = false;
if (cookies != null) {
  for (Cookie cookie : cookies) {
    if (cookie.getName().equals("userid") && cookie.getValue().equals(userid)) {
      authenticated = true;
    }
    if (cookie.getName().equals("password") && cookie.getValue().equals(password)) {
      authenticated = true;
    }
  }
}
if (authenticated) {
  // proceed to the next page
} else {
  // redirect to the login page with an error message
}
```

- To design server-side applications using JDBC, ODBC and session tracking API, you can follow these steps:

  - JDBC (Java Database Connectivity) is an API that allows Java programs to interact with various types of databases. You can use JDBC to establish a connection to a database, execute SQL queries and statements, and process the results. To use JDBC, you need to have a JDBC driver that matches your database type and version. You can then use the `DriverManager` class to get a `Connection` object that represents the database connection. For example, to connect to a MySQL database, you can do something like this:

  ```java
  // load the MySQL JDBC driver
  Class.forName("com.mysql.jdbc.Driver");
  // get the database connection using the driver, the URL, the user name and the password
  Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "root", "password");
  ```

  - ODBC (Open Database Connectivity) is a standard that allows applications to access data from various types of databases. You can use ODBC to connect to a database that has an ODBC driver installed on your system. You can then use the `DriverManager` class to get a `Connection` object that represents the database connection. For example, to connect to a Microsoft Access database, you can do something like this:

  ```java
  // load the ODBC driver
  Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
  // get the database connection using the driver and the data source name (DSN)
  Connection con = DriverManager.getConnection("jdbc:odbc:mydsn");
  ```

  - Session tracking API is a set of classes and interfaces that allow you to maintain the state of a user across multiple requests. You can use session tracking API to store and retrieve information about a user, such as their preferences, shopping cart items, etc. You can use the `HttpSession` interface to represent a session object that is associated with a user. You can get the session object from the `request` object using the `getSession()` method. You can then use the `setAttribute()` and `getAttribute()` methods to store and retrieve data in the session object. For example, to store the user name in the session object, you can do something like this:

  ```java
  // get the session object, creating a new one if it does not exist
  HttpSession session = request.getSession(true);
  // store the user name in the session object
  session.setAttribute("username", userid);
  ```

  - To retrieve the user name from the session object, you can do something like this:

  ```java
  // get the session object, returning null if it does not exist
  HttpSession session = request.getSession(false);
  if (session != null) {
    // get the user name from

```




# Install a database (MySQL or Oracle) for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

## MySQL Installation on Microsoft Windows

- MySQL is a popular open-source relational database management system that can be used to store and manipulate data for web applications.
- To install MySQL on Windows, you need to download the MySQL Installer from the official website  and run it on your computer.
- The MySQL Installer will guide you through the steps of choosing the products, features, and configuration options for your MySQL installation.
- You can choose between different setup types, such as Developer Default, Server Only, Client Only, or Custom, depending on your needs and preferences.
- The MySQL Installer will also install the required dependencies, such as the Visual C++ Redistributable, the .NET Framework, and the Connector/ODBC driver, which are needed to connect to the MySQL server from other applications.
- After the installation is complete, you can verify that the MySQL server is running by opening the MySQL Command Line Client from the Start menu or the command prompt and entering your root password.
- You can also use the MySQL Workbench, a graphical user interface tool, to manage your MySQL server and databases.
- For more details and instructions on how to install MySQL on Windows, you can refer to the official documentation  or the online tutorials .

## Oracle Installation on Microsoft Windows

- Oracle is another popular relational database management system that can be used to store and manipulate data for web applications.
- To install Oracle on Windows, you need to download the Oracle Database software from the official website and run it on your computer.
- The Oracle Database software will guide you through the steps of choosing the edition, the installation type, the installation location, and the configuration options for your Oracle installation.
- You can choose between different editions, such as Enterprise, Standard, or Express, depending on your needs and preferences.
- You can also choose between different installation types, such as Typical, Advanced, or Instant Client, depending on the features and components you want to install.
- The Oracle Database software will also install the required dependencies, such as the Oracle Universal Installer, the Oracle Net Configuration Assistant, and the Oracle Database Configuration Assistant, which are needed to create and configure your Oracle database and network services.
- After the installation is complete, you can verify that the Oracle database is running by opening the SQL*Plus tool from the Start menu or the command prompt and entering your username and password.
- You can also use the Oracle SQL Developer, a graphical user interface tool, to manage your Oracle database and schemas.
- For more details and instructions on how to install Oracle on Windows, you can refer to the official documentation or the online tutorials.



# Unit 5 - Design server site applications using JDDC,ODBC and section tracking API

## Introduction

- JDDC stands for Java Database Connectivity, which is an API that allows Java applications to interact with various types of databases.
- ODBC stands for Open Database Connectivity, which is an API that allows applications written in different languages and platforms to access databases using a common interface.
- Section tracking API is an API that allows web applications to maintain state information across multiple requests from the same client.

## Creating a table with name, password, email-id, and phone number fields

- To create a table with the required fields, we need to use the SQL statement `CREATE TABLE` with the appropriate data types and constraints for each field.
- For example, we can use the following SQL statement to create a table named `users` with the four fields:

```sql
CREATE TABLE users (
  name VARCHAR(50) NOT NULL,
  password VARCHAR(20) NOT NULL,
  email_id VARCHAR(50) UNIQUE NOT NULL,
  phone_number VARCHAR(15) UNIQUE NOT NULL
);
```

- The data type `VARCHAR(n)` means a variable-length character string with a maximum length of `n` characters.
- The constraint `NOT NULL` means that the field cannot be empty or missing.
- The constraint `UNIQUE` means that the field cannot have duplicate values in the table.

## Using JDDC, ODBC, and section tracking API to design server site applications

- To use JDDC, ODBC, and section tracking API to design server site applications, we need to follow these steps:

  - Load the appropriate driver for the database we want to connect to. For example, if we want to use MySQL database, we can load the driver using the following Java code:

  ```java
  Class.forName("com.mysql.jdbc.Driver");
  ```

  - Establish a connection to the database using the driver. For example, we can use the following Java code to connect to a MySQL database named `webtech` with the username `root` and the password `password`:

  ```java
  Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/webtech", "root", "password");
  ```

  - Create a statement object to execute SQL queries. For example, we can use the following Java code to create a statement object:

  ```java
  Statement stmt = con.createStatement();
  ```

  - Execute the SQL queries using the statement object and process the results. For example, we can use the following Java code to insert a new user into the `users` table and retrieve all the users from the table:

  ```java
  // Insert a new user
  String sql = "INSERT INTO users VALUES ('Alice', '1234', 'alice@gmail.com', '111-222-3333')";
  int rows = stmt.executeUpdate(sql); // returns the number of rows affected by the query
  System.out.println("Inserted " + rows + " row(s)");

  // Retrieve all the users
  sql = "SELECT * FROM users";
  ResultSet rs = stmt.executeQuery(sql); // returns a result set object that contains the query results
  while (rs.next()) { // loop through the result set
    // get the values of each field using the column name or index
    String name = rs.getString("name");
    String password = rs.getString(2);
    String email_id = rs.getString("email_id");
    String phone_number = rs.getString(4);
    // print the values
    System.out.println(name + " " + password + " " + email_id + " " + phone_number);
  }
  ```

  - Close the connection, statement, and result set objects when done. For example, we can use the following Java code to close the objects:

  ```java
  rs.close();
  stmt.close();
  con.close();
  ```

- To use ODBC, we need to use a JDBC-ODBC bridge driver that converts the JDBC API calls to ODBC API calls and vice versa. For example, we can use the following Java code to load the bridge driver:

```java
Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
```

- Then, we can use the same JDBC API methods as before, but with a different connection URL that specifies the ODBC data source name (DSN) that we have configured for the database. For example, we can use the following Java code to connect to a MySQL database using ODBC:

```java
Connection con = DriverManager.getConnection("jdbc:odbc:

```




# Write a java program/servlet/JSP to connect to that database and extract data from the tables and display them for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To write a java program/servlet/JSP to connect to a database and extract data from the tables and display them, you need to follow these steps:

  - Import the required packages for JDBC (Java Database Connectivity), such as `java.sql.*` and `javax.sql.*` .
  - Load and register the JDBC driver for the database you want to connect to, such as MySQL, Oracle, PostgreSQL, etc. You can use the `Class.forName()` method to load the driver class and the `DriverManager.registerDriver()` method to register it  .
  - Establish a connection to the database using the `DriverManager.getConnection()` method, which takes the URL, username and password of the database as parameters. You can store the connection object in a `Connection` variable  .
  - Create a statement object using the `Connection.createStatement()` method, which allows you to execute SQL queries on the database. You can store the statement object in a `Statement` variable  .
  - Execute the SQL query using the `Statement.executeQuery()` method, which returns a `ResultSet` object that contains the data retrieved from the database. You can store the result set object in a `ResultSet` variable  .
  - Iterate over the result set using the `ResultSet.next()` method, which moves the cursor to the next row of data. You can access the data in each column using the `ResultSet.getXXX()` methods, where XXX is the data type of the column, such as `getString()`, `getInt()`, `getDouble()`, etc. You can display the data using the `System.out.println()` method or any other output method   .
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
      String url = "jdbc:mysql://localhost:3306/mydb"; // Change the URL, database name, username and password as per your configuration
      String username = "root";
      String password = "root";
      conn = DriverManager.getConnection(url, username, password);

      // Create a statement object
      stmt = conn.createStatement();

      // Execute a SQL query
      String sql = "SELECT * FROM employees"; // Change the query as per your table name and columns
      rs = stmt.executeQuery(sql);

      // Iterate over the result set and display the data
      while (rs.next()) {
        // Retrieve the data from each column using the column name or index
        int id = rs.getInt("id"); // or rs.getInt(1);
        String name = rs.getString("name"); // or rs.getString(2);
        String department = rs.getString("department"); // or rs.getString(3);
        double salary = rs.getDouble("salary"); // or rs.getDouble(4);

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
        if (rs != null)

```




# Insert the details of the users who register with the web site, whenever a new user clicks the submit button in the registration page

- To insert the details of the users who register with the web site, we need to use Java Database Connectivity (JDBC) and Open Database Connectivity (ODBC) to connect to a database and execute SQL queries.
- JDBC is an API that allows Java programs to interact with various types of databases, such as MySQL, Oracle, SQL Server, etc.
- ODBC is a standard that enables applications to access data from different database management systems, such as Access, Excel, etc.
- To use JDBC and ODBC, we need to follow these steps:

  - Import the required packages, such as `java.sql.*` and `javax.servlet.*`.
  - Load and register the appropriate JDBC driver, such as `com.mysql.jdbc.Driver` for MySQL database.
  - Establish a connection to the database using the `DriverManager.getConnection()` method, which takes the database URL, username and password as parameters.
  - Create a `Statement` object using the `Connection.createStatement()` method, which allows us to execute SQL queries.
  - Execute the SQL query using the `Statement.executeUpdate()` method, which takes the SQL query as a parameter and returns the number of rows affected by the query. The SQL query should be an `INSERT` statement that inserts the user details into the database table.
  - Close the `Statement` and `Connection` objects using the `close()` method, which releases the resources and prevents memory leaks.

- To get the user details from the registration page, we need to use session tracking API, which allows us to maintain the state of the user across multiple requests.
- Session tracking API provides various ways to track the user session, such as cookies, URL rewriting, hidden form fields, and HttpSession objects.
- Cookies are small pieces of information that are stored on the client's browser and sent to the server with each request. Cookies can be created, read, and deleted using the `Cookie` class and the `HttpServletResponse.addCookie()` and `HttpServletRequest.getCookies()` methods.
- URL rewriting is a technique that appends the session ID to the URL of each request. URL rewriting can be done using the `HttpServletResponse.encodeURL()` method, which takes the original URL as a parameter and returns the modified URL with the session ID.
- Hidden form fields are input elements that are not visible to the user but can store and send data to the server. Hidden form fields can be created using the `<input type="hidden" name="name" value="value">` tag, where `name` and `value` are the attributes of the hidden field.
- HttpSession objects are server-side objects that store the user information and are associated with a unique session ID. HttpSession objects can be created, accessed, and invalidated using the `HttpServletRequest.getSession()`, `HttpSession.getAttribute()`, `HttpSession.setAttribute()`, and `HttpSession.invalidate()` methods.

- To insert the user details into the database using session tracking API, we need to follow these steps:

  - Get the user details from the registration page using the `HttpServletRequest.getParameter()` method, which takes the name of the input field as a parameter and returns the value entered by the user.
  - Create or access a HttpSession object using the `HttpServletRequest.getSession()` method, which takes a boolean parameter that indicates whether to create a new session or use an existing one.
  - Store the user details into the HttpSession object using the `HttpSession.setAttribute()` method, which takes the name and value of the attribute as parameters.
  - Redirect the user to another servlet that handles the database insertion using the `HttpServletResponse.sendRedirect()` method, which takes the URL of the servlet as a parameter. The URL should be encoded using the `HttpServletResponse.encodeURL()` method if URL rewriting is used for session tracking.
  - In the servlet that handles the database insertion, get the HttpSession object using the `HttpServletRequest.getSession()` method, which takes a boolean parameter that indicates whether to create a new session or use an existing one.
  - Get the user details from the HttpSession object using the `HttpSession.getAttribute()` method, which takes the name of the attribute as a parameter and returns the value stored in the session.
  - Follow the steps mentioned above to use JDBC and ODBC to insert the user details into the database.
  - Invalidate the HttpSession object using the `HttpSession.invalidate()` method, which removes the session and its attributes from the server.



# Write a JSP which insert the details of the 3 or 4 users who register with the web site by using registration form for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- JSP stands for Java Server Pages, which is a technology that allows creating dynamic web pages using Java code.
- A registration form is a web page that allows users to enter their personal information and create an account on a website.
- To write a JSP registration form, we need to follow these steps:

  - Create a HTML form that contains the input fields for the user details, such as name, email, password, etc. The form should have an action attribute that specifies the JSP file that will process the form data. For example:

    ```html
    <form action="register.jsp">
      <input type="text" name="name" placeholder="Name" required><br>
      <input type="email" name="email" placeholder="Email" required><br>
      <input type="password" name="password" placeholder="Password" required><br>
      <input type="submit" value="Register">
    </form>
    ```

  - Create a JSP file that will receive the form data and insert it into a database using JDBC and ODBC. JDBC stands for Java Database Connectivity, which is an API that allows connecting and executing queries to various databases. ODBC stands for Open Database Connectivity, which is a standard that enables accessing different types of data sources. To use JDBC and ODBC, we need to import the required packages, load the driver class, establish a connection, create a statement, execute the query, and close the resources. For example:

    ```jsp
    <%@ page import="java.sql.*" %>
    <%@ page import="javax.sql.*" %>
    <%
      // Get the form data
      String name = request.getParameter("name");
      String email = request.getParameter("email");
      String password = request.getParameter("password");

      // Load the driver class
      Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");

      // Establish a connection
      Connection con = DriverManager.getConnection("jdbc:odbc:mydsn");

      // Create a statement
      Statement stmt = con.createStatement();

      // Execute the query
      String sql = "INSERT INTO users (name, email, password) VALUES ('" + name + "', '" + email + "', '" + password + "')";
      int result = stmt.executeUpdate(sql);

      // Close the resources
      stmt.close();
      con.close();
    %>
    ```

  - Create a session object that will store the user information and track the user activity across the website. A session is a way of maintaining the state of a user between multiple requests. To use session, we need to import the required package, create a session object, set the attributes, and get the attributes. For example:

    ```jsp
    <%@ page import="javax.servlet.http.*" %>
    <%
      // Create a session object
      HttpSession session = request.getSession();

      // Set the attributes
      session.setAttribute("name", name);
      session.setAttribute("email", email);

      // Get the attributes
      String name = (String) session.getAttribute("name");
      String email = (String) session.getAttribute("email");
    %>
    ```

  - Display a confirmation message to the user after the registration is successful. For example:

    ```html
    <p>Thank you for registering, <%= name %>!</p>
    <p>Your email is <%= email %>.</p>
    ```



# Authenticate the user when he submits the login form using the user name and password from the database for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To authenticate the user when he submits the login form using the user name and password from the database, we need to use JDBC (Java Database Connectivity) and ODBC (Open Database Connectivity) drivers to connect to the database and execute SQL queries to verify the user credentials.
- JDBC is an API that allows Java applications to interact with various types of databases using a standard interface. ODBC is a standard that allows applications to access data from different database management systems using a common set of functions.
- Session tracking is a mechanism that allows a web server to maintain the state of a user across multiple requests. Session tracking can be implemented using various methods, such as cookies, URL rewriting, hidden form fields, or servlet API.
- The steps to authenticate the user using JDBC, ODBC and session tracking are as follows:

  1. Create a login form in HTML or JSP that accepts the user name and password from the user and submits them to a servlet.
  2. Load the JDBC driver class and register it with the DriverManager class. For example, Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
  3. Establish a connection to the database using the DriverManager.getConnection() method. For example, Connection con = DriverManager.getConnection("jdbc:odbc:mydb","username","password");
  4. Create a PreparedStatement object to execute a parameterized SQL query that selects the user name and password from the database table. For example, PreparedStatement ps = con.prepareStatement("select username,password from users where username = ?");
  5. Set the value of the parameter in the query using the ps.setString() method. For example, ps.setString(1, request.getParameter("username"));
  6. Execute the query using the ps.executeQuery() method and store the result in a ResultSet object. For example, ResultSet rs = ps.executeQuery();
  7. Check if the ResultSet object contains any row using the rs.next() method. If it does, compare the password from the ResultSet object with the password from the request object using the rs.getString() and request.getParameter() methods. For example, if(rs.next() && rs.getString("password").equals(request.getParameter("password")))
  8. If the passwords match, create a session object using the request.getSession() method and store the user name in the session object using the session.setAttribute() method. For example, HttpSession session = request.getSession(); session.setAttribute("username", request.getParameter("username"));
  9. Redirect the user to a welcome page or a home page using the response.sendRedirect() method. For example, response.sendRedirect("welcome.jsp");
  10. If the passwords do not match, display an error message to the user using the response.getWriter() method. For example, response.getWriter().println("Invalid user name or password");
  11. Close the ResultSet, PreparedStatement, and Connection objects using the rs.close(), ps.close(), and con.close() methods. For example, rs.close(); ps.close(); con.close();



# Design and implement a simple shopping cart example with session tracking API

- A shopping cart is a web application that allows users to browse, select, and purchase items from an online store.
- A session tracking API is a mechanism that enables the web server to identify and maintain the conversational state of each user across multiple requests.
- Session tracking is needed for shopping cart applications because the server should know which items belong to which user's cart, and how to handle actions such as adding, removing, or checking out items.
- There are different methods for session tracking, such as cookies, URL rewriting, hidden form fields, and HTTP session objects.
- Cookies are small pieces of data that are stored on the client's browser and sent to the server with every request. Cookies can store information such as user ID, cart ID, or item IDs.
- URL rewriting is a technique that appends session information to the end of every URL in the web application. For example, /cart?sessionID=1234. This method does not rely on the client's browser settings, but it can make the URLs longer and less user-friendly.
- Hidden form fields are input elements that are not visible to the user, but can store session information and send it to the server when a form is submitted. For example, <input type="hidden" name="sessionID" value="1234">. This method only works for requests that use the POST method, and it can increase the size of the HTML pages.
- HTTP session objects are server-side objects that store session information in memory or in a database. Each session object is associated with a unique session ID that is sent to the client as a cookie or a URL parameter. The server can retrieve the session object by using the session ID and access the session attributes. For example, session.getAttribute("cart").
- A simple shopping cart example with session tracking API can be designed and implemented as follows:

  - Create a web page that displays the available items for sale, along with their prices and an option to add them to the cart.
  - Create a servlet that handles the requests for adding items to the cart. The servlet should check if the user has a valid session ID, and if not, create a new session object and send the session ID to the client as a cookie or a URL parameter. The servlet should also add the selected item ID to the session object as an attribute, and redirect the user to the cart page.
  - Create a web page that displays the items in the user's cart, along with their prices and the total amount. The page should also provide options to remove items from the cart, or to proceed to checkout.
  - Create a servlet that handles the requests for removing items from the cart. The servlet should retrieve the session object by using the session ID from the cookie or the URL parameter, and remove the item ID from the session attribute. The servlet should then redirect the user to the cart page.
  - Create a servlet that handles the requests for checking out. The servlet should retrieve the session object by using the session ID from the cookie or the URL parameter, and process the payment and order details. The servlet should also invalidate the session object and redirect the user to a confirmation page.

