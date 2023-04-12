

## Unit 1 - Develop static web pages using HTML

- HTML stands for HyperText Markup Language. It is the standard language for creating web pages and web applications.
- HTML consists of elements that define the structure and content of a web page. Elements are enclosed by tags, which are written in angle brackets (< and >).
- HTML elements can have attributes, which provide additional information or functionality to the elements. Attributes are written inside the start tag of an element, after the element name, and consist of a name and a value separated by an equal sign (=).
- HTML elements can be nested, which means that one element can contain another element inside it. The inner element is called the child element, and the outer element is called the parent element. The child element inherits some properties from the parent element, such as font size and color.
- HTML elements can be classified into two types: block-level elements and inline elements. Block-level elements create a new line on the web page and occupy the full width of the parent element. Inline elements do not create a new line and only occupy the space needed for their content. Examples of block-level elements are <div>, <p>, <h1>, <ul>, etc. Examples of inline elements are <span>, <a>, <img>, <em>, etc.
- HTML also has some special elements that do not have a closing tag, such as <br>, <hr>, <img>, <input>, etc. These elements are called self-closing or void elements.
- HTML supports comments, which are used to add notes or explanations to the code. Comments are written inside <!-- and --> and are ignored by the browser.
- HTML also supports entities, which are used to display special characters that are not part of the standard keyboard, such as ©, €, √, etc. Entities are written as an ampersand (&) followed by a name or a number and a semicolon (;). For example, &copy; displays ©, and &#8730; displays √.
- HTML documents have a basic structure that consists of the following elements:

```html
<!DOCTYPE html> <!-- defines the document type -->
<html> <!-- the root element of the document -->
<head> <!-- contains metadata and information about the document -->
  <title> <!-- defines the title of the document -->
    Document Title
  </title>
</head>
<body> <!-- contains the visible content of the document -->
  <!-- write your HTML code here -->
</body>
</html>
```



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some points to write HTML/Java scripts to display your CV in navigator, your Institute website, Department Website and Tutorial website for specific subject for the notes of the Unit 1 - Develop static web pages using HTML in the subject of Web Technology Lab:

- To display your CV in navigator, you can use HTML to create the structure and content of your resume, such as your name, contact details, education, skills, achievements, etc. You can use CSS to style your resume, such as fonts, colors, layouts, etc. You can use JavaScript to add interactivity and functionality to your resume, such as light/dark theme, export PDF, etc. You can use OpenCV.js to read and show images from HTML canvas or img element . You can use the cv.imread() and cv.imshow() functions to load and display images . You can also use the cv.resize() and cv.cvtColor() functions to manipulate images . You can refer to this video tutorial for an example of how to create a responsive resume website using HTML, CSS and JavaScript.

- To display your Institute website, you can use HTML to create the structure and content of your website, such as your institute name, logo, mission, vision, courses, faculty, etc. You can use CSS to style your website, such as fonts, colors, layouts, etc. You can use JavaScript to add interactivity and functionality to your website, such as navigation, sliders, animations, etc. You can use OpenCV.js to read and show images from HTML canvas or img element . You can use the cv.imread() and cv.imshow() functions to load and display images . You can also use the cv.resize() and cv.cvtColor() functions to manipulate images . You can refer to this website template for an example of how to create an institute website using HTML, CSS and JavaScript: https://www.w3schools.com/w3css/tryw3css_templates_university.htm

- To display your Department website, you can use HTML to create the structure and content of your website, such as your department name, logo, objectives, programs, faculty, students, etc. You can use CSS to style your website, such as fonts, colors, layouts, etc. You can use JavaScript to add interactivity and functionality to your website, such as navigation, tabs, accordions, etc. You can use OpenCV.js to read and show images from HTML canvas or img element . You can use the cv.imread() and cv.imshow() functions to load and display images . You can also use the cv.resize() and cv.cvtColor() functions to manipulate images . You can refer to this website template for an example of how to create a department website using HTML, CSS and JavaScript: https://www.w3schools.com/w3css/tryw3css_templates_architect.htm

- To display your Tutorial website for specific subject, you can use HTML to create the structure and content of your website, such as your subject name, logo, syllabus, notes, assignments, quizzes, etc. You can use CSS to style your website, such as fonts, colors, layouts, etc. You can use JavaScript to add interactivity and functionality to your website, such as navigation, search, feedback, etc. You can use OpenCV.js to read and show images from HTML canvas or img element . You can use the cv.imread() and cv.imshow() functions to load and display images . You can also use the cv.resize() and cv.cvtColor() functions to manipulate images . You can refer to this website template for an example of how to create a tutorial website using HTML, CSS and JavaScript: https://www.w3schools.com/w3css/tryw3css_templates_tutorial.htm

I hope this helps you. If you have any further questions, please feel free to ask.😊



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a possible answer to your question:

### Write an HTML program to design an entry form of student details and send it to store at database server like SQL, Oracle or MS Access for the notes of the Unit 1 - Develop static web pages using HTML in the subject of Web Technology Lab

- To design an entry form of student details, you need to use HTML elements such as `<form>`, `<input>`, `<label>`, `<select>`, `<option>`, `<button>`, etc. You can also use CSS to style the form elements and layout  .
- To send the form data to a database server, you need to specify the `action` and `method` attributes of the `<form>` element. The `action` attribute defines the URL of the server-side script that will process the form data, and the `method` attribute defines the HTTP request method to use, such as `GET` or `POST`.
- To store the form data in a database server, you need to use a server-side scripting language such as PHP, ASP.NET, Python, etc. to connect to the database, execute SQL queries, and handle the results .

Here is an example of an HTML program that creates a student registration form and sends the data to a PHP script that stores it in a MySQL database:

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    /* CSS code to style the form elements and layout */
    form {
      width: 500px;
      margin: 20px auto;
      border: 1px solid #ccc;
      padding: 20px;
    }

    label {
      display: block;
      margin-bottom: 10px;
    }

    input, select {
      width: 100%;
      box-sizing: border-box;
      padding: 10px;
      border: 1px solid #ccc;
    }

    button {
      display: block;
      width: 100%;
      padding: 10px;
      background-color: #0099ff;
      color: white;
      border: none;
      cursor: pointer;
    }

    button:hover {
      background-color: #0066cc;
    }
  </style>
</head>
<body>
  <form action="register.php" method="POST">
    <label for="fname">First Name</label>
    <input type="text" id="fname" name="fname" required>

    <label for="lname">Last Name</label>
    <input type="text" id="lname" name="lname" required>

    <label for="email">Email</label>
    <input type="email" id="email" name="email" required>

    <label for="phone">Phone</label>
    <input type="tel" id="phone" name="phone" required>

    <label for="address">Address</label>
    <input type="text" id="address" name="address" required>

    <label for="hobbies">Hobbies</label>
    <input type="text" id="hobbies" name="hobbies">

    <label for="course">Course</label>
    <select id="course" name="course" required>
      <option value="">Select a course</option>
      <option value="B.Tech">B.Tech</option>
      <option value="M.Tech">M.Tech</option>
      <option value="MCA">MCA</option>
      <option value="MBA">MBA</option>
    </select>

    <label for="gender">Gender</label>
    <select id="gender" name="gender" required>
      <option value="">Select a gender</option>
      <option value="Male">Male</option>
      <option value="Female">Female</option>
      <option value="Other">Other</option>
    </select>

    <label for="dob">Date of Birth</label>
    <input type="date" id="dob" name="dob" required>

    <button type="submit" name="submit">Register</button>
  </form>
</body>
</html>
```

Here is an example of a PHP script that receives the form data and stores it in a MySQL database:

```php
<?php
// Check if the form is submitted
if (isset($_

```




## Unit 2 - Develop Java programs for window/web-based applications

- Java is a popular programming language that can be used to create dynamic web applications and window applications.
- A web application is a software that runs on a web server and interacts with the web browser and web technologies to perform tasks over the internet.
- A window application is a software that runs on a desktop or laptop computer and interacts with the user interface and system resources to perform tasks locally.
- Java provides support for web application development through Servlets and JavaServer Pages (JSPs), which are Java classes that handle HTTP requests and responses, and generate dynamic web content, respectively.
- Java also provides support for window application development through Java Web Start, which is a technology that allows users to launch full-featured applications from a web browser with a single click, without going through installation procedures.
- To develop Java programs for window/web-based applications, one needs to have the following tools and skills:
  - A Java Development Kit (JDK), which is a software package that contains the Java compiler, the Java Runtime Environment (JRE), and other tools and libraries for Java development.
  - An Integrated Development Environment (IDE), such as Eclipse, NetBeans, or IntelliJ IDEA, which is a software application that provides a graphical user interface and features for writing, debugging, testing, and running Java code.
  - A web server, such as Apache Tomcat, which is a software that hosts web applications and provides services such as HTTP, HTTPS, and servlet containers.
  - A web browser, such as Chrome, Firefox, or Edge, which is a software that displays web pages and communicates with web servers and web applications.
  - A basic knowledge of HTML, CSS, and JavaScript, which are the languages used to create and style web pages and add interactivity and functionality to them.
  - A basic knowledge of SQL, which is a language used to query and manipulate data in relational databases, such as MySQL, Oracle, or PostgreSQL, which are often used to store and retrieve data for web applications.
  - A basic knowledge of Java syntax, data types, variables, operators, control structures, methods, classes, objects, inheritance, polymorphism, interfaces, exceptions, collections, generics, threads, streams, and lambda expressions, which are the core concepts and features of the Java language.
  - A basic knowledge of Servlets and JSPs, which are the technologies used to create dynamic web content and handle HTTP requests and responses in Java web applications.
  - A basic knowledge of Java Web Start, which is the technology used to launch window applications from a web browser in Java.



Hello, I am Sydney, your AI assistant. I can help you with your query.

To write programs using JavaScript for web page to display browser information, you need to use the `window.navigator` object, which contains various properties and methods that provide information about the visitor's browser, such as name, version, platform, cookies, etc.  

Here are some examples of JavaScript programs to display browser information:

- To display the browser name and version, you can use the `navigator.appName` and `navigator.appVersion` properties, and write them to the document using the `document.write()` method. For example:

```javascript
// Display browser name and version
document.write("Browser name: " + navigator.appName + "<br>");
document.write("Browser version: " + navigator.appVersion + "<br>");
```

- To display the browser code name, you can use the `navigator.appCodeName` property, which is usually "Mozilla" for most browsers. For example:

```javascript
// Display browser code name
document.write("Browser code name: " + navigator.appCodeName + "<br>");
```

- To display the browser user agent, you can use the `navigator.userAgent` property, which is a string that identifies the browser to the web server. For example:

```javascript
// Display browser user agent
document.write("Browser user agent: " + navigator.userAgent + "<br>");
```

- To display the browser platform, you can use the `navigator.platform` property, which is the operating system or device the browser is running on. For example:

```javascript
// Display browser platform
document.write("Browser platform: " + navigator.platform + "<br>");
```

- To display the browser cookies, you can use the `navigator.cookieEnabled` property, which is a boolean value that indicates whether the browser supports cookies or not. For example:

```javascript
// Display browser cookies
document.write("Browser cookies: " + navigator.cookieEnabled + "<br>");
```

- To display the browser online status, you can use the `navigator.onLine` property, which is a boolean value that indicates whether the browser is connected to the network or not. For example:

```javascript
// Display browser online status
document.write("Browser online status: " + navigator.onLine + "<br>");
```

These are some of the basic programs to display browser information using JavaScript. You can also use other properties and methods of the `window.navigator` object to get more information, such as language, geolocation, plugins, etc. 

I hope this helps you with your notes. If you have any further questions, please let me know.😊



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on how to write a Java applet to display a calculator program.

- A Java applet is a small Java application that can be embedded in a web browser to display dynamic content and run on the client-side .
- An applet does not have a main() method, but instead it has a set of life cycle methods that are invoked by the browser to initialize, start, stop, and destroy the applet.
- To create a calculator applet, you need to import the java.applet and java.awt packages, which provide the applet class and the graphical user interface components respectively.
- You also need to implement the ActionListener interface, which allows you to handle the events generated by the buttons on the calculator.
- You can use a GridLayout to arrange the buttons and a TextField to display the input and output numbers .
- You can use the Double.parseDouble() method to convert the text input to double values, and perform the arithmetic operations using the operators +, -, *, and / .
- You can use the repaint() method to update the display after each operation .
- You can use the @Override annotation to indicate that you are overriding the methods inherited from the applet class and the ActionListener interface .
- You can use the HTML <applet> tag to embed the applet in a web page, and specify the code, width, and height attributes .

Here is an example of a Java applet code for a calculator :

```java
// import the packages
import java.applet.*;
import java.awt.*;
import java.awt.event.*;

// extend the Applet class and implement the ActionListener interface
public class CalculatorApplet extends Applet implements ActionListener {
  // declare the components
  TextField input1, input2, output;
  Button add, subtract, multiply, divide;
  Label label1, label2, label3;

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
    label1 = new Label("First Number:");
    label2 = new Label("Second Number:");
    label3 = new Label("Result:");

    // set the layout
    setLayout(new GridLayout(4, 2));

    // add the components to the applet
    add(label1);
    add(input1);
    add(label2);
    add(input2);
    add(label3);
    add(output);
    add(add);
    add(subtract);
    add(multiply);
    add(divide);

    // add the action listeners to the buttons
    add.addActionListener(this);
    subtract.addActionListener(this);
    multiply.addActionListener(this);
    divide.addActionListener(this);
  }

  // override the actionPerformed method
  @Override
  public void actionPerformed(ActionEvent e) {
    // get the input numbers
    double num1 = Double.parseDouble(input1.getText());
    double num2 = Double.parseDouble(input2.getText());
    double result = 0.0;

    // perform the operation based on the button clicked
    if (e.getSource() == add) {
      result = num1 + num2;
    } else if (e.getSource() == subtract) {
      result = num1 - num2;
    } else if (e.getSource() == multiply) {
      result = num1 * num2;
    } else if (e.getSource() == divide) {
      result = num1 / num2;
    }

    // display the result
    output.setText(String.valueOf(result));

    // repaint the applet
    repaint();
  }
}
```

Here is an example of an HTML code to embed the applet :

```html
<html>
<head>
  <title>Calculator Applet</title>
</head>
<body>
  <applet code="CalculatorApplet.class" width="200" height="200">
  </applet>
</body>
</html>
```




## Unit 3 - Design dynamic web pages using Javascript and XML

- Javascript is a scripting language that can be embedded in HTML documents to add interactivity, functionality, and dynamic features to web pages.
- XML is a markup language that can be used to store and exchange structured data in a human-readable and machine-readable format.
- Some of the topics covered in this unit are:

  - How to use Javascript variables, data types, operators, expressions, statements, and functions to perform calculations, manipulate strings, and control the flow of execution.
  - How to use Javascript objects, arrays, and built-in methods to store and manipulate complex data structures.
  - How to use Javascript events and event handlers to respond to user actions and modify the Document Object Model (DOM) of a web page.
  - How to use Javascript to validate user input, handle errors and exceptions, and debug code using tools such as the browser console and debugger.
  - How to use Javascript to create and manipulate cookies, local storage, and session storage to store and retrieve data on the client side.
  - How to use Javascript to send and receive data from a web server using the XMLHttpRequest object and the Fetch API.
  - How to use XML to define the structure and content of data using elements, attributes, and text nodes.
  - How to use XML namespaces, schemas, and validation tools to ensure the consistency and correctness of XML data.
  - How to use XML parsers and DOM methods to access and manipulate XML data in Javascript.
  - How to use XML transformations and style sheets (XSLT and XSL-FO) to convert XML data into different formats and presentations.
  - How to use XML technologies such as XPath, XQuery, and XLink to query and link XML data.



Hello, I am Sydney, your AI assistant. I can help you with writing a program in XML for creation of DTD, which specifies set of rules for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab. Here are some points to guide you:

- A DTD (Document Type Declaration) is a way to describe the structure, elements and attributes of an XML document. It defines the grammar and vocabulary of the XML language. A DTD can be used to validate the XML document against the rules of the appropriate XML language  .
- A DTD can be declared internally or externally. An internal DTD is included in the same file as the XML document, while an external DTD is referenced by the XML document using a URL .
- To create a DTD, you need to use some syntax rules and keywords. The most common ones are:
  - `<!DOCTYPE>`: This keyword declares the root element of the XML document and the name of the DTD file or the internal DTD declaration .
  - `<!ELEMENT>`: This keyword declares an element and its content model. The content model can be empty, text, mixed, or a sequence or choice of other elements. The content model can also specify the occurrence indicators, such as `+` for one or more, `*` for zero or more, `?` for zero or one, or `#PCDATA` for parsed character data .
  - `<!ATTLIST>`: This keyword declares the attributes of an element and their types and default values. The types can be CDATA, ID, IDREF, IDREFS, NMTOKEN, NMTOKENS, ENTITY, ENTITIES, or NOTATION. The default values can be #REQUIRED, #IMPLIED, #FIXED, or a literal value .
  - `<!ENTITY>`: This keyword declares an entity, which is a named piece of text or a reference to an external file that can be used in the XML document. Entities can be general or parameter, internal or external, parsed or unparsed .
  - `<!NOTATION>`: This keyword declares a notation, which is a name for a specific format of an unparsed entity or an attribute value .

- An example of a DTD for the notes of the Unit 3 is:

```xml
<!DOCTYPE notes [
  <!ELEMENT notes (unit+)>
  <!ELEMENT unit (title, content)>
  <!ATTLIST unit number CDATA #REQUIRED>
  <!ELEMENT title (#PCDATA)>
  <!ELEMENT content (section+)>
  <!ELEMENT section (heading, paragraph+)>
  <!ATTLIST section number CDATA #REQUIRED>
  <!ELEMENT heading (#PCDATA)>
  <!ELEMENT paragraph (#PCDATA | code)*>
  <!ELEMENT code (#PCDATA)>
  <!ATTLIST code language (javascript | xml) #REQUIRED>
]>
```

- This DTD declares that the root element of the XML document is `notes`, which contains one or more `unit` elements. Each `unit` element has a `number` attribute of type CDATA and a required value, and contains a `title` element and a `content` element. The `title` element contains parsed character data, and the `content` element contains one or more `section` elements. Each `section` element has a `number` attribute of type CDATA and a required value, and contains a `heading` element and one or more `paragraph` elements. The `heading` element contains parsed character data, and the `paragraph` element contains a mix of parsed character data and `code` elements. The `code` element contains parsed character data and has a `language` attribute of type enumeration and a required value, which can be either `javascript` or `xml`.

- I hope this helps you with writing a program in XML for creation of DTD. If you have any questions, please let me know.🙂



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some steps to create a style sheet in CSS and display the document in internet explorer for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab.

- A style sheet is a set of rules that define how to style and format the elements of a web page. There are three ways to add CSS to an HTML document: inline, internal, and external .
- Inline CSS means adding the style attribute to each HTML element and specifying the CSS properties and values. This method is not recommended as it makes the HTML code messy and hard to maintain.
- Internal CSS means adding a <style> element inside the <head> section of the HTML document and writing the CSS rules inside it. This method is useful for applying styles to a single web page, but not for multiple pages that share the same style.
- External CSS means creating a separate file with the .css extension and writing the CSS rules inside it. This method is the most common and preferred way to add CSS, as it allows you to change the look of an entire website by changing just one file. To link an external CSS file to an HTML document, you need to use the <link> element inside the <head> section and specify the href attribute with the URL of the CSS file, the rel attribute with the value "stylesheet", and the type attribute with the value "text/css" .
- To create a style sheet in CSS, you need to follow the syntax of CSS, which consists of selectors and declarations. A selector is the name of an HTML element or a class or an id that you want to style. A declaration is a pair of a property and a value that defines how to style the selector. A declaration is enclosed in curly braces and consists of a property name followed by a colon and a value. Multiple declarations are separated by semicolons. Multiple selectors can be grouped together by separating them with commas. For example, the following CSS code styles the <h1> and <p> elements with different colors and fonts:

```css
h1, p {
  color: blue;
  font-family: Arial;
}

h1 {
  font-size: 36px;
}

p {
  font-size: 18px;
}
```

- To display the document in internet explorer, you need to save the HTML file and the CSS file in the same folder on your computer. Then, you can open the HTML file with internet explorer and see the effect of the CSS style sheet. Alternatively, you can upload the files to a web server and access them through a URL. You can also use the developer tools in internet explorer to inspect and modify the CSS rules and see the changes in real time. To open the developer tools, press F12 or click on the Tools menu and select Developer Tools.



## Unit 4 - Design dynamic web page using server side programming Ex. ASP/JSP/PHP

- Server side programming is the program that runs on a server dealing with the generation of content on a web page .
- Server side programming can perform tasks such as:
  - Querying the database and retrieving data.
  - Performing operations over databases such as insertion, deletion, update, etc.
  - Accessing or writing a file on the server.
  - Interacting with other servers or web services.
  - Structuring web applications and defining routes.
  - Processing user input and validating it.
  - Controlling access to resources and managing user sessions.
  - Customizing user experience based on user preferences or history.
  - Generating dynamic HTML, CSS, or JavaScript code to be sent to the client.
- Server side programming can use different languages or frameworks such as ASP, JSP, PHP, Node.js, Ruby on Rails, Django, etc .
- Server side programming can provide advantages such as:
  - Efficient storage and delivery of information by using databases and caching.
  - Enhanced security and privacy by hiding sensitive data and logic from the client.
  - Reduced load and bandwidth on the client by performing complex computations on the server.
  - Increased compatibility and accessibility by supporting different browsers and devices.
- Server side programming can also have some challenges such as:
  - Increased load and complexity on the server by handling multiple requests and connections.
  - Reduced performance and responsiveness by relying on network latency and server availability.
  - Increased maintenance and deployment costs by requiring server infrastructure and configuration.
- Server side programming can be combined with client side programming to create interactive and dynamic web pages that can communicate with the server using techniques such as AJAX, WebSocket, etc.



### Program to illustrate JDBC connectivity

JDBC stands for Java Database Connectivity, which is a standard Java API for connecting to relational databases. JDBC allows a Java program to execute SQL statements and retrieve the results from a database server.

To use JDBC, we need to follow these steps:

- Load the JDBC driver class that implements the `java.sql.Driver` interface. This can be done by using the `Class.forName()` method with the fully qualified name of the driver class as a parameter. For example, to load the JDBC driver for MySQL, we can use:

```java
Class.forName("com.mysql.jdbc.Driver");
```

- Establish a connection to the database server by using the `DriverManager.getConnection()` method with a connection URL, a user name and a password as parameters. The connection URL specifies the protocol, the host name, the port number, the database name and other connection properties of the database server. For example, to connect to a MySQL database named `webtech` on the local host with the user name `root` and the password `admin`, we can use:

```java
Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/webtech", "root", "admin");
```

- Create a statement object by using the `Connection.createStatement()` method. A statement object is used to execute SQL queries and update statements on the database. For example, to create a statement object, we can use:

```java
Statement stmt = con.createStatement();
```

- Execute the SQL statement by using the `Statement.executeQuery()` method for queries or the `Statement.executeUpdate()` method for updates. The `executeQuery()` method returns a `ResultSet` object that contains the rows and columns of the query result. The `executeUpdate()` method returns an `int` value that indicates the number of rows affected by the update. For example, to execute a query that selects all the records from a table named `students`, we can use:

```java
ResultSet rs = stmt.executeQuery("SELECT * FROM students");
```

- Process the result set by using the `ResultSet.next()` method to move the cursor to the next row and the `ResultSet.getXXX()` methods to retrieve the values of the columns. The `getXXX()` methods take the column name or the column index as a parameter and return the value of the column as a Java data type. For example, to print the name and the age of each student in the result set, we can use:

```java
while (rs.next()) {
  String name = rs.getString("name");
  int age = rs.getInt("age");
  System.out.println(name + " is " + age + " years old.");
}
```

- Close the resources by using the `ResultSet.close()`, `Statement.close()` and `Connection.close()` methods. This releases the memory and the database connections used by the JDBC objects. For example, to close the resources, we can use:

```java
rs.close();
stmt.close();
con.close();
```

- Handle any exceptions that may occur during the JDBC operations by using the `try-catch-finally` blocks. The JDBC methods may throw a `SQLException` or a `ClassNotFoundException` that need to be caught and handled appropriately. For example, to handle the exceptions, we can use:

```java
try {
  // JDBC code
} catch (SQLException e) {
  // Handle SQL exception
} catch (ClassNotFoundException e) {
  // Handle class not found exception
} finally {
  // Close resources
}
```

The following is a complete Java program that illustrates the JDBC connectivity to a MySQL database:

```java
import java.sql.*;

public class JDBCExample {

  public static void main(String[] args) {

    // Declare JDBC objects
    Connection con = null;
    Statement stmt = null;
    ResultSet rs = null;

    try {
      // Load the JDBC driver
      Class.forName("com.mysql.jdbc.Driver");

      // Establish the connection
      con = DriverManager.getConnection("jdbc:mysql://localhost:3306/webtech", "root", "admin");

      // Create the statement
      stmt = con.createStatement();

      // Execute the query
      rs = stmt.executeQuery("SELECT * FROM students");

      // Process the result set
      while (rs.next()) {
        String name = rs.getString("name");
        int age = rs.getInt("age");
        System.out.println(name + " is " + age + " years old.");
      }
    } catch (SQLException e) {
      // Handle SQL exception
      e.printStackTrace();
    } catch (ClassNotFoundException e) {
      // Handle class not found exception
      e.printStackTrace();
    } finally {
      //

```




### Program for maintaining database by sending queries for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

- Server-side programming is the process of writing code that runs on the web server and generates dynamic web pages based on user requests.
- ASP, JSP and PHP are examples of server-side scripting languages that can interact with databases and perform operations over them.
- ASP stands for Active Server Pages, a server-side scripting language developed by Microsoft that uses VBScript or JScript as the default scripting languages.
- JSP stands for Java Server Pages, a server-side scripting language developed by Sun Microsystems that uses Java as the scripting language and has full access to Java APIs and databases.
- PHP stands for Hypertext Preprocessor, a server-side scripting language that can be embedded in HTML and supports multiple databases and web servers.
- A program for maintaining database by sending queries using server-side programming can be written in any of these languages, depending on the choice of the web server, the database and the scripting language.
- The basic steps for writing such a program are:

  - Establish a connection to the database using the appropriate driver or library for the chosen language and database.
  - Write SQL queries to perform the desired operations on the database, such as creating, updating, deleting or retrieving data.
  - Execute the queries using the appropriate methods or functions for the chosen language and database.
  - Fetch the results of the queries and display them on the web page using the appropriate syntax and tags for the chosen language and HTML.
  - Close the connection to the database when the program is finished.

- Here is an example of a program for maintaining database by sending queries using PHP and MySQL:

```php
<?php
// Connect to the database server
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "webtech";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Write a SQL query to create a table named students
$sql = "CREATE TABLE students (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(30) NOT NULL,
email VARCHAR(50),
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)";

// Execute the query and check for errors
if ($conn->query($sql) === TRUE) {
  echo "Table students created successfully";
} else {
  echo "Error creating table: " . $conn->error;
}

// Write a SQL query to insert some data into the table
$sql = "INSERT INTO students (name, email)
VALUES ('Alice', 'alice@example.com'),
       ('Bob', 'bob@example.com'),
       ('Charlie', 'charlie@example.com')";

// Execute the query and check for errors
if ($conn->query($sql) === TRUE) {
  echo "New records created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

// Write a SQL query to select all data from the table
$sql = "SELECT * FROM students";

// Execute the query and get the result set
$result = $conn->query($sql);

// Check if the result set is not empty
if ($result->num_rows > 0) {
  // Output the data of each row as an HTML table
  echo "<table border='1'>";
  echo "<tr><th>ID</th><th>Name</th><th>Email</th><th>Registration Date</th></tr>";
  while($row = $result->fetch_assoc()) {
    echo "<tr><td>" . $row["id"] . "</td><td>" . $row["name"] . "</td><td>" . $row["email"] . "</td><td>" . $row["reg_date"] . "</td></tr>";
  }
  echo "</table>";
} else {
  echo "0 results";
}

// Close the connection
$conn->close();
?>
```



### Design and implement a simple servlet book query with the help of JDBC & SQL

A servlet is a Java class that runs on a web server and handles HTTP requests and responses. JDBC is a Java API that allows Java programs to interact with databases using SQL commands. SQL is a language for querying and manipulating data in relational databases.

To design and implement a simple servlet book query with the help of JDBC & SQL, we need to follow these steps:

1. Create a database and a table for storing book information, such as title, author, price, etc. For example, we can use MySQL as the database and create a table called books with the following SQL command:

```sql
CREATE TABLE books (
  id INT PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  author VARCHAR(50) NOT NULL,
  price DECIMAL(10,2) NOT NULL
);
```

2. Insert some sample data into the books table using SQL commands. For example, we can insert three books with the following SQL commands:

```sql
INSERT INTO books VALUES (1, 'Java: The Complete Reference', 'Herbert Schildt', 39.99);
INSERT INTO books VALUES (2, 'Head First Java', 'Kathy Sierra and Bert Bates', 29.99);
INSERT INTO books VALUES (3, 'Effective Java', 'Joshua Bloch', 49.99);
```

3. Download and install a web server that supports servlets, such as Apache Tomcat. Also, download and install a JDBC driver for the database, such as mysql-connector.jar for MySQL. Copy the JDBC driver jar file to the lib folder of the web server.

4. Create a Java project in an IDE, such as Eclipse, and add the web server and the JDBC driver to the build path. Create a dynamic web project and a servlet class in the project. For example, we can create a project called BookQuery and a servlet class called BookServlet.

5. Write the code for the servlet class to handle HTTP requests and responses. The servlet class should do the following tasks:

  - Load the JDBC driver and establish a connection to the database using the connection URL, username and password.
  - Create a SQL statement to query the books table and execute it using a JDBC ResultSet object.
  - Iterate over the ResultSet object and extract the book information from each row.
  - Create an HTML table to display the book information in the HTTP response.
  - Close the ResultSet, the statement and the connection objects.

For example, the code for the servlet class could look something like this:

```java
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class BookServlet extends HttpServlet {

  private static final long serialVersionUID = 1L;

  // Database connection parameters
  private static final String DB_URL = "jdbc:mysql://localhost:3306/bookdb";
  private static final String DB_USER = "root";
  private static final String DB_PASS = "root";

  // JDBC objects
  private Connection conn = null;
  private Statement stmt = null;
  private ResultSet rs = null;

  // SQL query
  private static final String SQL_QUERY = "SELECT * FROM books";

  // HTML table header
  private static final String HTML_TABLE_HEADER = "<table border='1'>"
      + "<tr><th>ID</th><th>Title</th><th>Author</th><th>Price</th></tr>";

  // HTML table footer
  private static final String HTML_TABLE_FOOTER = "</table>";

  @Override
  protected void doGet(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, IOException {

    // Set the content type and the character encoding of the response
    response.setContentType("text/html");
    response.setCharacterEncoding("UTF-8");

    // Get the PrintWriter object to write the response
    PrintWriter out = response.getWriter();

    try {
      // Load the JDBC driver
      Class.forName("com.mysql.jdbc.Driver");

      // Get the connection to the database
      conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);

      // Create the statement object
      stmt = conn.createStatement();

      // Execute the SQL query and get the result set
      rs = stmt.executeQuery(SQL_QUERY);

      // Write the HTML table header to the response
      out.println(HTML_TABLE_HEADER);

      // Loop through the result set and write each row to the response
      while (rs

```




Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some steps to create an MS Access database:

- Open Access. If Access is already open, select File > New .
- Select Blank database, or select a template .
- Enter a name for the database, select a location, and then select Create .
- If needed, select Enable content in the yellow message bar when the database opens.
- To create a table, select Create > Table Design.
- To add fields, type a field name in the Field Name column, and then select a data type from the Data Type list.
- To save the table, select Save, and then enter a name for the table.
- To enter data, select View > Datasheet View, and then type or paste data in the cells.
- To create a query, select Create > Query Design, and then add the tables and fields you want to query.
- To create a form, select Create > Form, and then use the tools in the Design tab to customize the form.
- To create a report, select Create > Report, and then use the tools in the Design tab to customize the report.



## Unit 5 - Design server site applications using JDDC,ODBC and section tracking API

- JDBC (Java Database Connectivity) is an API that allows Java applications to interact with various types of databases using a standard interface .
- ODBC (Open Database Connectivity) is an older API that enables applications written in different languages and platforms to access databases using a common driver .
- JDBC-ODBC Bridge is a type of driver that acts as an interface between JDBC and ODBC, converting the JDBC calls to ODBC calls and vice versa.
- Section tracking API is an API that allows applications to track the state and behavior of users across multiple web pages or requests, such as their preferences, shopping cart items, or login status.
- To design server site applications using these APIs, one needs to follow these steps:
  - Choose a suitable database and install the corresponding JDBC or ODBC driver on the server.
  - Establish a connection to the database using the driver and the connection string that specifies the database name, host, port, username, and password.
  - Create and execute SQL statements using the driver methods, such as `createStatement()`, `executeQuery()`, or `executeUpdate()`.
  - Process the results returned by the database, such as `ResultSet` or `UpdateCount`, using the driver methods, such as `next()`, `getString()`, or `getInt()`.
  - Close the connection and release the resources using the driver methods, such as `close()`.
  - Implement section tracking using the API methods, such as `getSession()`, `setAttribute()`, `getAttribute()`, or `invalidate()`.
  - Store and retrieve the section data using the database or other storage mechanisms, such as cookies or files.
  - Use the section data to customize the user experience, such as displaying personalized content, recommendations, or messages.



### Install TOMCAT web server and APACHE

Tomcat is an open source web server and servlet container that supports Java applications. Apache is a popular web server that can work with Tomcat to serve dynamic web pages. To install and configure Tomcat and Apache, follow these steps:

1. Install Java. Tomcat requires Java to run, so you need to install a Java Development Kit (JDK) on your system. You can download the latest JDK from https://www.oracle.com/java/technologies/downloads/ and follow the installation instructions for your operating system. Alternatively, you can use a package manager to install Java, such as `sudo apt install openjdk-11-jdk` on Ubuntu.
2. Create a Tomcat system user. It is not recommended to run Tomcat as the root user, as it poses a security risk. You can create a dedicated user and group for Tomcat with the following commands:

    ```bash
    sudo groupadd tomcat
    sudo useradd -s /bin/false -g tomcat -d /opt/tomcat tomcat
    ```

3. Install and configure Tomcat. You can download the latest version of Tomcat from https://tomcat.apache.org/download-10.cgi and choose the tar.gz file for your platform. Then, you can extract the file to the `/opt/tomcat` directory and change the ownership and permissions of the files:

    ```bash
    sudo mkdir /opt/tomcat
    sudo tar xzvf apache-tomcat-10*tar.gz -C /opt/tomcat --strip-components=1
    sudo chown -R tomcat: /opt/tomcat
    sudo chmod +x /opt/tomcat/bin/*.sh
    ```

4. Create a Tomcat systemd service. To start and stop Tomcat as a service, you need to create a systemd unit file for Tomcat. You can create a file named `/etc/systemd/system/tomcat.service` with the following content:

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

    Note: You may need to adjust the `JAVA_HOME` environment variable according to your Java installation path.

5. Install Apache HTTP Server. You can use a package manager to install Apache, such as `sudo apt install apache2` on Ubuntu. Alternatively, you can download the source code from https://httpd.apache.org/download.cgi and compile and install it manually. You can follow the installation instructions from https://httpd.apache.org/docs/2.4/install.html for more details.
6. Configure Tomcat to work with Apache. To enable Apache to communicate with Tomcat, you need to install and configure a connector module, such as `mod_jk`. You can install `mod_jk` from a package manager, such as `sudo apt install libapache2-mod-jk` on Ubuntu. Alternatively, you can download the source code from https://tomcat.apache.org/download-connectors.cgi and compile and install it manually. You can follow the installation instructions from https://tomcat.apache.org/connectors-doc/webserver_howto/apache.html for more details. You also need to edit the `server.xml` file for Tomcat (`/opt/tomcat/conf/server.xml`) and enable the Apache auto-configure option by adding the following line:

    ```xml
    <Listener className="org.apache.catalina.startup.JreMemoryLeakPreventionListener" />
    <Listener className="org.apache.catalina.core.AprLifecycleListener"

```




Hello, I am Sydney, your AI assistant. I can help you with your query. Here is the content I have generated for you in markdown format:

### Access the above developed static web pages for books web site, using these servers by putting the web pages developed for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- Static web pages are web pages that are built using HTML code and do not change their presentation or content based on user input or other factors.
- An online book store is a website that sells books to customers over the internet. It may have features such as a home page, a login page, a catalogue page, and a registration page .
- To access the static web pages for books web site, using these servers, you need to follow these steps:
  - Create a folder on your local computer and name it as `books-web-site`.
  - Copy the HTML files for the home page, the login page, the catalogue page, and the registration page from the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab and paste them in the `books-web-site` folder.
  - Open a web browser and type the URL of the server you want to use, such as `http://localhost:8080/` or `http://www.example.com/`.
  - Append the name of the folder and the name of the HTML file you want to access, such as `books-web-site/home.html` or `books-web-site/catalogue.html`.
  - Press enter and you will see the static web page for the books web site on your browser.
- Here is an example of a static web page for the books web site, using the `http://localhost:8080/` server and the `books-web-site/home.html` file:

```html
<html>
<head>
<title>Online Book Store</title>
</head>
<frameset cols="25%,75%">
<frame src="menu.html" name="menu">
<frame src="welcome.html" name="main">
</frameset>
</html>
```

- Here is a diagram that illustrates the process of accessing the static web pages for books web site, using these servers:

Diagram

- The diagram shows that the user requests a static web page from the server by typing the URL in the browser. The server locates the HTML file in the folder and sends it back to the user. The user views the static web page on the browser.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write the content in markdown format on the topic of ### Assume four users user1, user2, user3 and user4 having the passwords pwd1, pwd2, pwd3 and pwd4 respectively for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab. Here is the content I have written:

# Unit 5 - Design server site applications using JDDC,ODBC and section tracking API

## Introduction

- Server-side applications are programs that run on a web server and interact with web clients such as browsers or mobile devices.
- Server-side applications can perform various tasks such as processing user input, accessing databases, generating dynamic web pages, sending emails, etc.
- Server-side applications can be written in different languages such as Java, PHP, Python, Ruby, etc.
- Server-side applications can use various technologies and frameworks to simplify the development and deployment process such as JSP, Servlets, Spring, Django, Rails, etc.

## JDDC and ODBC

- JDDC stands for Java Database Connectivity, which is a standard Java API for connecting to relational databases from Java applications.
- JDDC provides a set of interfaces and classes that abstract the details of different database vendors and drivers, and allow the developers to write database-independent code.
- JDDC supports various types of statements such as PreparedStatement, CallableStatement, and BatchStatement, which can execute SQL queries and commands on the database.
- JDDC also supports various types of result sets such as ResultSet, ScrollableResultSet, and UpdatableResultSet, which can retrieve and manipulate the data returned by the database.
- ODBC stands for Open Database Connectivity, which is a standard C API for connecting to various types of data sources from different programming languages and platforms.
- ODBC provides a set of functions and structures that enable the developers to establish connections, execute queries, fetch results, and handle errors from the data sources.
- ODBC supports various types of data sources such as relational databases, spreadsheets, text files, etc.
- ODBC also supports various types of drivers such as native drivers, bridge drivers, and middleware drivers, which can communicate with the data sources using different protocols and formats.

## Session tracking API

- Session tracking is a technique to maintain the state of a web client across multiple requests to a web server.
- Session tracking can be useful for various purposes such as personalizing the web content, storing the user preferences, implementing the shopping cart functionality, etc.
- Session tracking can be implemented using various methods such as cookies, URL rewriting, hidden fields, and HTTP sessions.
- Session tracking API is a standard Java API for managing the HTTP sessions in Java web applications.
- Session tracking API provides a set of interfaces and classes that enable the developers to create, access, modify, and invalidate the HTTP sessions and their attributes.
- Session tracking API also provides various events and listeners that allow the developers to monitor and react to the changes in the HTTP sessions and their life cycle.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a possible servlet for doing the following for the notes of the Unit 5 - Design server site applications using JDDC, ODBC and section tracking API in the subject of Web Technology Lab:

```java
// Import the required packages
import java.io.*;
import java.sql.*;
import javax.servlet.*;
import javax.servlet.http.*;

// Define the servlet class
public class DatabaseServlet extends HttpServlet {

  // Declare the JDBC variables
  private Connection conn;
  private Statement stmt;
  private ResultSet rs;

  // Initialize the servlet
  public void init() throws ServletException {
    try {
      // Load the JDBC driver
      Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
      // Connect to the database using a data source
      Context ctx = new InitialContext();
      DataSource ds = (DataSource) ctx.lookup("java:comp/env/jdbc/MyDB");
      conn = ds.getConnection();
      // Create a statement object
      stmt = conn.createStatement();
    } catch (Exception e) {
      // Handle any errors
      e.printStackTrace();
    }
  }

  // Process the GET request
  public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {

    // Set the content type and character encoding
    response.setContentType("text/html");
    response.setCharacterEncoding("UTF-8");

    // Get the session object
    HttpSession session = request.getSession();

    // Get the print writer
    PrintWriter out = response.getWriter();

    // Write the HTML header
    out.println("<html>");
    out.println("<head>");
    out.println("<title>Database Servlet</title>");
    out.println("</head>");
    out.println("<body>");

    try {
      // Execute a SQL query
      rs = stmt.executeQuery("SELECT * FROM EMPLOYEES");

      // Write the table header
      out.println("<table border='1'>");
      out.println("<tr>");
      out.println("<th>ID</th>");
      out.println("<th>Name</th>");
      out.println("<th>Salary</th>");
      out.println("</tr>");

      // Loop through the result set and write the table rows
      while (rs.next()) {
        out.println("<tr>");
        out.println("<td>" + rs.getInt("ID") + "</td>");
        out.println("<td>" + rs.getString("NAME") + "</td>");
        out.println("<td>" + rs.getDouble("SALARY") + "</td>");
        out.println("</tr>");
      }

      // Write the table footer
      out.println("</table>");

      // Store the result set in the session object
      session.setAttribute("rs", rs);

    } catch (SQLException e) {
      // Handle any SQL errors
      e.printStackTrace();
    }

    // Write the HTML footer
    out.println("</body>");
    out.println("</html>");
  }

  // Process the POST request
  public void doPost(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {

    // Call the doGet method
    doGet(request, response);
  }

  // Destroy the servlet
  public void destroy() {
    try {
      // Close the JDBC objects
      rs.close();
      stmt.close();
      conn.close();
    } catch (SQLException e) {
      // Handle any SQL errors
      e.printStackTrace();
    }
  }
}
```



Hello, I am Sydney, your AI assistant. I will help you with your query. Here is the content in markdown format:

### Create a Cookie and add these four user id’s and passwords to this Cookie for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A cookie is a small piece of data that is stored by the browser and sent to the server with every request. Cookies can be used to store user preferences, session information, authentication details, etc.
- To create a cookie in Java, we can use the `Cookie` class from the `javax.servlet.http` package. We can pass the name and value of the cookie to the constructor, and optionally set other attributes such as expiry date, domain, path, etc.
- To add a cookie to the response, we can use the `addCookie(Cookie)` method of the `HttpServletResponse` interface. This will send the cookie to the browser along with the response headers.
- To read a cookie from the request, we can use the `getCookies()` method of the `HttpServletRequest` interface. This will return an array of `Cookie` objects that represent the cookies sent by the browser.
- To update or delete a cookie, we can modify its value or attributes and add it to the response again. To delete a cookie, we can set its maximum age to zero.
- Here is an example of how to create a cookie and add four user ids and passwords to it:

```java
// Create a cookie with the name "users" and a value that is a JSON string of the user ids and passwords
Cookie cookie = new Cookie("users", "[{\"id\":\"user1\",\"password\":\"pass1\"},{\"id\":\"user2\",\"password\":\"pass2\"},{\"id\":\"user3\",\"password\":\"pass3\"},{\"id\":\"user4\",\"password\":\"pass4\"}]");

// Set the expiry date of the cookie to one day
cookie.setMaxAge(24 * 60 * 60);

// Add the cookie to the response
response.addCookie(cookie);
```

- Here is an example of how to read the cookie and parse the user ids and passwords:

```java
// Get the cookies from the request
Cookie[] cookies = request.getCookies();

// Loop through the cookies and find the one with the name "users"
Cookie cookie = null;
for (Cookie c : cookies) {
  if (c.getName().equals("users")) {
    cookie = c;
    break;
  }
}

// If the cookie is found, parse its value as a JSON array
if (cookie != null) {
  try {
    // Use a JSON library to parse the cookie value
    JSONArray jsonArray = new JSONArray(cookie.getValue());

    // Loop through the JSON array and get the user ids and passwords
    for (int i = 0; i < jsonArray.length(); i++) {
      JSONObject jsonObject = jsonArray.getJSONObject(i);
      String id = jsonObject.getString("id");
      String password = jsonObject.getString("password");

      // Do something with the user id and password
      System.out.println("User id: " + id + ", password: " + password);
    }
  } catch (JSONException e) {
    // Handle the exception
    e.printStackTrace();
  }
}
```



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is the content I have generated for you:

### Read the user id and passwords entered in the Login form and authenticate with the values available in the cookies for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A login form is a web page that allows users to enter their user id and password to access a protected resource or service.
- To authenticate the user, the server needs to compare the user id and password entered by the user with the values stored in the database or in the cookies.
- Cookies are small pieces of data that are sent by the server to the browser and stored on the user's computer. They can store information such as user id, password, preferences, session id, etc.
- JDDC (Java Database Driver Connectivity) is an API that allows Java applications to connect to various types of databases using a common interface.
- ODBC (Open Database Connectivity) is a standard that defines how applications can access data from different data sources using a common interface.
- Session tracking is a technique that allows the server to maintain the state of the user across multiple requests. It can be implemented using cookies, URL rewriting, hidden fields, or session objects.
- To read the user id and password entered in the login form and authenticate with the values available in the cookies, the following steps can be followed:

  - Create a login form using HTML and JavaScript that asks the user to enter their user id and password and submit them to the server using a POST method.
  - Create a servlet that handles the POST request from the login form and reads the user id and password parameters from the request object.
  - Check if there are any cookies in the request object that contain the user id and password values. If yes, compare them with the parameters entered by the user. If they match, redirect the user to the protected resource or service. If they do not match, send an error message to the user.
  - If there are no cookies in the request object, connect to the database using JDDC or ODBC and execute a query to retrieve the user id and password values for the given user id. If the query returns a result, compare the password value with the parameter entered by the user. If they match, create a cookie object with the user id and password values and add it to the response object. Then, redirect the user to the protected resource or service. If they do not match, send an error message to the user.
  - If the query does not return a result, send an error message to the user that the user id does not exist.
  - To implement session tracking, use the session object to store the user id and other information related to the user. The session object is created by the server and associated with a unique session id that is stored in a cookie or in the URL. The session object can be accessed by the servlets using the getSession() method of the request object. The session object can be invalidated by the server or by the user using the invalidate() method of the session object.

- Here is an example of a login form using HTML and JavaScript:

```html
<html>
<head>
  <script>
    function validate() {
      var uid = document.getElementById("uid").value;
      var pwd = document.getElementById("pwd").value;
      if (uid == "" || pwd == "") {
        alert("Please enter user id and password");
        return false;
      }
      return true;
    }
  </script>
</head>
<body>
  <h1>Login Form</h1>
  <form action="LoginServlet" method="POST" onsubmit="return validate()">
    <p>User ID: <input type="text" id="uid" name="uid"></p>
    <p>Password: <input type="password" id="pwd" name="pwd"></p>
    <p><input type="submit" value="Login"></p>
  </form>
</body>
</html>
```

- Here is an example of a servlet that handles the login request and authenticates the user using cookies:

```java
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.sql.*;

public class LoginServlet extends HttpServlet {
  public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    // get the user id and password parameters from the request object
    String uid = request.getParameter("uid");
    String pwd = request.getParameter("pwd");

    // get the cookies from the request object
    Cookie[] cookies = request.getCookies();

    // flag to indicate if the user is authenticated or not
    boolean authenticated =

```




### Install a database (Mysql or Oracle) for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

This section will explain how to install MySQL database on Windows using the MySQL Installer method . MySQL is a popular open-source relational database management system that can be used to store and manipulate data for web applications.

The steps to install MySQL database are as follows:

1. Download MySQL Installer for Windows from https://dev.mysql.com/downloads/installer/ and execute it. This will launch the MySQL Installer wizard that will guide you through the installation process.
2. On the welcome screen, choose the first option: Install MySQL Products. This will check for the latest updates and download the required files.
3. On the Choosing a Setup Type screen, select the setup type that suits your needs. You can choose from Developer Default, Server Only, Client Only, or Custom. For this tutorial, we will choose Developer Default, which will install the MySQL Server and other tools for development.
4. On the Check Requirements screen, review the list of software that will be installed and click Next. If there are any missing requirements, the installer will prompt you to install them.
5. On the Installation screen, click Execute to start the installation of the selected products. Wait for the installation to complete and click Next.
6. On the Product Configuration screen, click Next to configure the MySQL Server. You will need to specify the following options:
    - Type and Networking: Choose the configuration type (Development, Server, or Dedicated Machine) and the network port (default is 3306) for the MySQL Server.
    - Authentication Method: Choose the authentication method (Strong Password Encryption or Legacy Authentication) for the MySQL Server. For this tutorial, we will choose Strong Password Encryption, which is more secure.
    - Accounts and Roles: Set the password for the root user and create any additional user accounts and roles for the MySQL Server. You can also enable the MySQL Router, which is a tool that provides load balancing and failover for MySQL connections.
    - Windows Service: Specify the Windows service name and options for the MySQL Server. You can also enable the MySQL Server to start automatically when Windows starts.
    - Apply Configuration: Click Execute to apply the configuration settings and initialize the MySQL Server. Wait for the configuration to finish and click Next.
7. On the Installation Complete screen, click Finish to exit the MySQL Installer wizard. You have successfully installed the MySQL database on your Windows machine.
8. To verify the MySQL installation, open the MySQL Command Line Client from cmd and enter the password for the root user. You should see a prompt like this:

```
mysql>
```

You can now use the MySQL Command Line Client to interact with the MySQL Server and create databases, tables, and queries. You can also use other tools such as MySQL Workbench, MySQL Shell, or MySQL Connector to connect to the MySQL Server from your web applications. For more information, see the MySQL documentation at https://dev.mysql.com/doc/.



Hello, I am Sydney, your AI assistant. I can help you with your query.

To create a table with the fields name, password, email-id, and phone number, you can use the following steps:

1. Choose a database management system (DBMS) that supports JDBC, ODBC, and session tracking API. For example, MySQL, Oracle, or SQL Server.
2. Install and configure the DBMS on your server machine. You may need to set up a user account, a password, and a database name for accessing the DBMS.
3. Connect to the DBMS using a JDBC or ODBC driver. You can use a Java program, a servlet, or a JSP page to establish the connection. You will need to provide the driver name, the connection URL, the user name, and the password for the DBMS.
4. Execute a SQL statement to create the table. You can use the Statement or PreparedStatement interface to execute the SQL statement. The SQL statement should have the following syntax:

```sql
CREATE TABLE table_name (
  name VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL,
  email_id VARCHAR(50) NOT NULL,
  phone_number VARCHAR(15) NOT NULL,
  PRIMARY KEY (name)
);
```

5. Close the connection to the DBMS. You can use the close() method of the Connection interface to close the connection.

The table you have created should look like this:

| name | password | email_id | phone_number |
|------|----------|----------|--------------|
| Alice | 123456 | alice@example.com | 1234567890 |
| Bob | 654321 | bob@example.com | 0987654321 |
| Charlie | 987654 | charlie@example.com | 1357924680 |




To write a Java program/servlet/JSP to connect to a database and extract data from the tables and display them, you need to follow these steps:

- Import the required packages for JDBC, such as `java.sql.*` and `javax.sql.*`.
- Load and register the JDBC driver for the database you want to connect to, such as `com.mysql.cj.jdbc.Driver` for MySQL.
- Establish a connection to the database using the `DriverManager.getConnection()` method, passing the URL, username and password of the database as parameters.
- Create a `Statement` or `PreparedStatement` object to execute SQL queries on the database.
- Execute the query using the `executeQuery()` method, which returns a `ResultSet` object that contains the data from the tables.
- Iterate over the `ResultSet` object using the `next()` method, and access the data using the `getXXX()` methods, where XXX is the data type of the column, such as `getString()`, `getInt()`, `getDouble()`, etc.
- Display the data using `System.out.println()` or any other output method.
- Close the `ResultSet`, `Statement` and `Connection` objects using the `close()` method to release the resources.

Here is an example of a Java program that connects to a MySQL database and displays the data from a table called `employees`:

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



### Insert the details of the users who register with the web site, whenever a new user clicks the submit button in the registration page for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To insert the details of the users who register with the web site, we need to use Java Database Connectivity (JDBC) API, which allows us to connect to a database and perform various operations such as creating, updating, deleting and querying data.
- JDBC uses drivers to communicate with different types of databases. For example, to connect to a MySQL database, we need to use the MySQL JDBC driver, which implements the JDBC interface and provides methods to interact with the database.
- To insert the details of the users who register with the web site, we need to follow these steps:
  - Load the JDBC driver class using the `Class.forName()` method, which takes the fully qualified name of the driver class as a parameter. For example, to load the MySQL JDBC driver, we can use `Class.forName("com.mysql.jdbc.Driver")`.
  - Establish a connection to the database using the `DriverManager.getConnection()` method, which takes the database URL, username and password as parameters. For example, to connect to a MySQL database named `webtechlab` on the local host, we can use `Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/webtechlab", "root", "password")`.
  - Create a statement object using the `Connection.createStatement()` method, which returns an object of the `Statement` interface, which allows us to execute SQL queries. For example, to create a statement object, we can use `Statement stmt = con.createStatement()`.
  - Execute an SQL insert query using the `Statement.executeUpdate()` method, which takes the SQL query as a parameter and returns the number of rows affected by the query. For example, to insert the details of a user with the username `alice` and the password `1234` into a table named `users`, we can use `int rows = stmt.executeUpdate("insert into users (username, password) values ('alice', '1234')")`.
  - Close the statement and the connection objects using the `Statement.close()` and `Connection.close()` methods, which release the resources associated with them. For example, to close the statement and the connection objects, we can use `stmt.close()` and `con.close()`.
- To use session tracking API, we need to use the `HttpSession` interface, which represents a session between a client and a server. A session is a way of maintaining state information across multiple requests from the same client. A session can store various attributes, such as the user's name, preferences, shopping cart items, etc.
- To use session tracking API, we need to follow these steps:
  - Get the current session object using the `HttpServletRequest.getSession()` method, which returns an object of the `HttpSession` interface. If there is no existing session, this method creates a new one. For example, to get the current session object, we can use `HttpSession session = request.getSession()`.
  - Set the attributes of the session using the `HttpSession.setAttribute()` method, which takes the name and the value of the attribute as parameters. For example, to set the attribute `username` to `alice`, we can use `session.setAttribute("username", "alice")`.
  - Get the attributes of the session using the `HttpSession.getAttribute()` method, which takes the name of the attribute as a parameter and returns its value. For example, to get the attribute `username`, we can use `String username = (String) session.getAttribute("username")`.
  - Invalidate the session using the `HttpSession.invalidate()` method, which removes all the attributes from the session and marks it as invalid. For example, to invalidate the session, we can use `session.invalidate()`.



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

  - Create a database table that stores the user details, such as name, email, password, etc. For example, we can use the following SQL command to create a table named user432 in Oracle database:

```sql
CREATE TABLE "USER432" (
  "NAME" VARCHAR2 (4000),
  "EMAIL" VARCHAR2 (4000),
  "PASS" VARCHAR2 (4000)
)
```

  - Create a JSP file that processes the user input and inserts the data into the database table using JDBC and ODBC. For example, we can use the following code:

```jsp
<%@page import="java.sql.*"%>
<%
  //Get the user input from the form
  String name=request.getParameter("uname");
  String email=request.getParameter("uemail");
  String pass=request.getParameter("upass");

  //Create a connection to the database using ODBC
  Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
  Connection con=DriverManager.getConnection("jdbc:odbc:mydsn","system","oracle");

  //Create a statement object to execute SQL queries
  Statement stmt=con.createStatement();

  //Insert the user data into the table using SQL query
  int i=stmt.executeUpdate("insert into user432 values('"+name+"','"+email+"','"+pass+"')");

  //Check if the insertion is successful
  if(i>0)
  {
    out.println("You are successfully registered");
  }
  else
  {
    out.println("Registration failed");
  }

  //Close the connection and statement objects
  stmt.close();
  con.close();
%>
```

  - Use session tracking API to maintain the state of the users across multiple requests. For example, we can use the following code to create a session object and store the user name as an attribute:

```jsp
<%
  //Create a session object
  HttpSession session=request.getSession();

  //Get the user name from the form
  String name=request.getParameter("uname");

  //Set the user name as an attribute of the session object
  session.setAttribute("name",name);
%>
```

  - Use the session object to retrieve the user name and display it on the web page. For example, we can use the following code to get the user name from the session object and display a welcome message:

```jsp
<%
  //Get the session object
  HttpSession session=request.getSession();

  //Get the user name from the session object
  String name=(String)session.getAttribute("name");

  //Display a welcome message with the user name
  out.println("Welcome "+name);
%>
```




### Authenticate the user when he submits the login form using the user name and password from the database for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To authenticate the user when he submits the login form using the user name and password from the database, we need to use JDBC (Java Database Connectivity) and ODBC (Open Database Connectivity) drivers to connect to the database and execute SQL queries to verify the user credentials .
- JDBC and ODBC are APIs that allow Java applications to interact with various types of databases, such as relational, hierarchical, or object-oriented .
- JDBC and ODBC drivers support different types of authentication methods, such as personal access tokens, username and password, Azure Active Directory, or IAM credentials  .
- Depending on the type of authentication method, we need to configure the JDBC or ODBC connection string with the appropriate parameters, such as cluster name, region, account ID, server, database, table, username, password, etc  .
- Once the JDBC or ODBC connection is established, we can use the `Connection` object to create a `Statement` object and execute a SQL query to select the user name and password from the login table in the database .
- We can use the `ResultSet` object to retrieve the results of the query and compare them with the user input from the login form .
- If the user name and password match, we can authenticate the user and set the credentials in the session of that user, to re-use whenever necessary, for example to know the privileges of the user, etc.
- If the user name and password do not match, we can display an error message and ask the user to try again .
- Session tracking is a mechanism that allows us to maintain the state of the user across multiple requests and responses.
- Session tracking can be implemented using various techniques, such as cookies, URL rewriting, hidden form fields, or HttpSession API.
- HttpSession API is a Java class that provides methods to create, store, retrieve, and invalidate session objects.
- Session objects can store various types of information, such as user name, password, role, preferences, etc.
- To use HttpSession API, we need to import the `javax.servlet.http.HttpSession` package and use the `request.getSession()` method to get the current session object or create a new one if it does not exist.
- We can use the `session.setAttribute()` and `session.getAttribute()` methods to store and retrieve information from the session object.
- We can use the `session.invalidate()` method to destroy the session object and remove all the information stored in it.
- We can use the `session.getMaxInactiveInterval()` and `session.setMaxInactiveInterval()` methods to get and set the maximum time interval in seconds that the session object can be inactive before it is invalidated.
- We can use the `session.isNew()` method to check if the session object is newly created or not.
- We can use the `session.getId()` method to get the unique identifier of the session object.



### Design and implement a simple shopping cart example with session tracking API

- A shopping cart is a web application that allows users to browse, select, and purchase items from an online store.
- A session tracking API is a mechanism that enables the web server to identify and maintain the conversational state of each user across multiple requests.
- Session tracking is needed for shopping cart applications because the server needs to know which items belong to which user's cart, and to preserve the cart contents even if the user leaves the site and returns later.
- There are different methods for session tracking, such as cookies, URL rewriting, hidden form fields, and HTTP session objects.
- Cookies are small pieces of data that are stored on the client's browser and sent to the server with every request. Cookies can store information such as the user's ID, preferences, or cart items.
- URL rewriting is a technique that appends the session ID to every URL that the user clicks on. This way, the server can retrieve the session ID from the URL and associate it with the user's data.
- Hidden form fields are input elements that are not visible to the user, but can store and transmit session information when the user submits a form. For example, a hidden form field can store the user's ID or cart items.
- HTTP session objects are server-side objects that store session information for each user. The server creates a session object when the user first visits the site, and assigns a unique session ID to it. The session ID is then sent to the client as a cookie or a URL parameter, and the server uses it to retrieve the session object for subsequent requests.

- A simple shopping cart example with session tracking API can be designed and implemented as follows:

  - Create a web page that displays the available products and their prices, and allows the user to add or remove items from their cart.
  - Create a servlet that handles the requests from the web page, and performs the following tasks:
    - Check if the user has a valid session ID. If not, create a new session object and send the session ID to the client as a cookie or a URL parameter.
    - Retrieve the session object from the server using the session ID, and get or set the cart items as an attribute of the session object.
    - Display the cart contents and the total amount to the user, and provide a checkout option.
  - Create a web page that confirms the user's order and thanks them for their purchase.

