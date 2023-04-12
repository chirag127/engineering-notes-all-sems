

Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for Unit 1 - Develop static web pages using HTML.

## Unit 1 - Develop static web pages using HTML

- HTML stands for HyperText Markup Language. It is the standard language for creating web pages and web applications.
- HTML consists of elements that define the structure and content of a web page. Elements are enclosed by tags, which are written in angle brackets. For example, `<p>` is the tag for a paragraph element.
- HTML elements can have attributes, which provide additional information about the element. Attributes are written inside the start tag, after the element name, and consist of a name and a value. For example, `<p class="intro">` is a paragraph element with an attribute named class and a value of intro.
- HTML elements can be nested, which means that one element can contain another element inside it. For example, `<p>This is a <strong>bold</strong> text.</p>` is a paragraph element that contains a strong element inside it.
- HTML elements can be self-closing, which means that they do not need an end tag. For example, `<img src="image.jpg" alt="Image">` is an image element that does not have an end tag.
- HTML documents have a basic structure that consists of a `<!DOCTYPE>` declaration, a `<html>` element, a `<head>` element, and a `<body>` element. The `<!DOCTYPE>` declaration specifies the version of HTML that the document follows. The `<html>` element is the root element of the document. The `<head>` element contains metadata, such as the title, style, and script of the document. The `<body>` element contains the visible content of the document, such as text, images, links, and forms.
- HTML documents can be linked to other documents or resources using the `<a>` element, which creates a hyperlink. The `<a>` element has an attribute named href, which specifies the URL of the destination. For example, `<a href="https://www.example.com">Example</a>` creates a hyperlink to the website https://www.example.com with the text Example.
- HTML documents can display images using the `<img>` element, which creates an image. The `<img>` element has an attribute named src, which specifies the URL of the image. The `<img>` element also has an attribute named alt, which provides a text alternative for the image. For example, `<img src="image.jpg" alt="Image">` displays the image image.jpg with the text Image as the alternative.
- HTML documents can create lists using the `<ul>` element, which creates an unordered list, or the `<ol>` element, which creates an ordered list. Both elements contain one or more `<li>` elements, which create list items. For example, `<ul><li>First item</li><li>Second item</li></ul>` creates an unordered list with two items.
- HTML documents can create tables using the `<table>` element, which creates a table. The `<table>` element contains one or more `<tr>` elements, which create table rows. Each `<tr>` element contains one or more `<td>` elements, which create table cells. For example, `<table><tr><td>First cell</td><td>Second cell</td></tr></table>` creates a table with one row and two cells.
- HTML documents can create forms using the `<form>` element, which creates a form. The `<form>` element has an attribute named action, which specifies the URL of the server that will process the form data. The `<form>` element also has an attribute named method, which specifies the HTTP method to use when sending the form data. The `<form>` element contains one or more input elements, such as `<input>`, `<textarea>`, `<select>`, and `<button>`, which create form controls. For example, `<form action="https://www.example.com" method="POST"><input type="text" name="name" placeholder="Enter your name"><button type="submit">Submit</button></form>` creates a form that sends the user's name to the server using the POST method.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some content that you can use to write HTML/Java scripts to display your CV in navigator, your Institute website, Department Website and Tutorial website for specific subject for the notes of the Unit 1 - Develop static web pages using HTML in the subject of Web Technology Lab.

### HTML/Java scripts to display your CV in navigator

- To display your CV in navigator, you need to create an HTML file that contains the structure and content of your resume, such as your name, contact details, education, skills, work experience, achievements, etc.
- You can use HTML tags such as `<h1>`, `<p>`, `<ul>`, `<li>`, `<table>`, `<tr>`, `<td>`, etc. to format your CV and make it look professional and organized.
- You can also use CSS to style your CV, such as changing the font, color, background, alignment, margin, padding, border, etc. You can use CSS selectors, properties and values to apply styles to your HTML elements.
- You can also use JavaScript to add some interactivity and functionality to your CV, such as creating a light/dark theme switcher, exporting your CV as a PDF file, validating your input fields, etc. You can use JavaScript variables, operators, functions, events, DOM manipulation, etc. to write your scripts.
- Here is an example of a simple HTML file that displays a CV in navigator:

```html
<html>
<head>
  <title>My CV</title>
  <style>
    /* Write your CSS code here */
  </style>
  <script>
    /* Write your JavaScript code here */
  </script>
</head>
<body>
  <h1>My CV</h1>
  <p>Name: John Doe</p>
  <p>Email: john.doe@example.com</p>
  <p>Phone: +1-234-567-8901</p>
  <h2>Education</h2>
  <ul>
    <li>Bachelor of Science in Computer Science, ABC University, 2019-2023</li>
    <li>High School Diploma, XYZ School, 2017-2019</li>
  </ul>
  <h2>Skills</h2>
  <ul>
    <li>HTML, CSS, JavaScript</li>
    <li>Python, Java, C++</li>
    <li>Web Development, Data Structures, Algorithms</li>
  </ul>
  <h2>Work Experience</h2>
  <table>
    <tr>
      <td>Web Developer Intern, ABC Company, Jan 2022 - Mar 2022</td>
    </tr>
    <tr>
      <td>- Developed and maintained the front-end of the company website using HTML, CSS and JavaScript</td>
    </tr>
    <tr>
      <td>- Implemented responsive design, user interface, and user experience features</td>
    </tr>
    <tr>
      <td>- Collaborated with the back-end team to integrate the web pages with the database and APIs</td>
    </tr>
    <tr>
      <td>Teaching Assistant, ABC University, Sep 2021 - Dec 2021</td>
    </tr>
    <tr>
      <td>- Assisted the professor in teaching the Web Technology Lab course to undergraduate students</td>
    </tr>
    <tr>
      <td>- Graded the lab assignments and provided feedback to the students</td>
    </tr>
    <tr>
      <td>- Conducted online tutorials and doubt sessions for the students</td>
    </tr>
  </table>
  <h2>Achievements</h2>
  <ul>
    <li>Won the first prize in the ABC Hackathon 2021 for developing a web app that solves a social problem</li>
    <li>Received the Dean's List Award for academic excellence in 2020 and 2021</li>
    <li>Published a research paper on web security in the International Journal of Computer Science and Engineering</li>
  </ul>
</body>
</html>
```



# HTML program to design an entry form of student details and send it to store at database server

- HTML stands for HyperText Markup Language, which is used to create web pages and display information on the web browser.
- HTML forms are used to collect user input and send it to a web server for processing.
- HTML forms consist of one or more input elements, such as text boxes, checkboxes, radio buttons, dropdown lists, etc., that allow the user to enter or select data.
- HTML forms also have a submit button, which triggers the action attribute of the form element, which specifies where and how the form data should be sent to the web server.
- To store the form data in a database server, such as SQL, Oracle or MS Access, the web server needs to have a script or program that can connect to the database and execute SQL queries to insert, update, delete or retrieve data.
- The script or program can be written in any server-side language, such as PHP, ASP.NET, Java, etc., and it should be specified in the action attribute of the form element.
- The method attribute of the form element determines how the form data is encoded and transmitted to the web server. The most common methods are GET and POST.
- The GET method appends the form data to the URL of the action attribute, and it is visible in the browser's address bar. The GET method is suitable for sending small and non-sensitive data, such as search queries.
- The POST method sends the form data in the body of the HTTP request, and it is not visible in the browser's address bar. The POST method is suitable for sending large and sensitive data, such as passwords, personal details, etc.

## Example of HTML program to design an entry form of student details and send it to store at database server

```html
<!-- This is the HTML form that collects the student details -->
<form action="student.php" method="POST">
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
        <input type="radio" name="gender" value="Other" required>Other
      </td>
    </tr>
    <tr>
      <td>Date of Birth:</td>
      <td><input type="date" name="dob" required></td>
    </tr>
    <tr>
      <td></td>
      <td><input type="submit" name="submit" value="Register"></td>
    </tr>
  </table>
</form>
```

```php
<?php
// This is

```




## Unit 2 - Develop Java programs for window/web-based applications

- In this unit, you will learn how to create graphical user interfaces (GUIs) and web applications using Java.
- GUIs are programs that allow users to interact with the application through graphical elements such as buttons, menus, text fields, etc.
- Web applications are programs that run on a web server and can be accessed by users through a web browser.
- To create GUIs in Java, you will need to use the Swing and AWT libraries, which provide various components and layouts for designing the user interface.
- To create web applications in Java, you will need to use the Servlet and JSP technologies, which enable you to write dynamic web pages that can process user requests and generate responses.
- You will also learn how to use databases and JDBC to store and retrieve data for your applications, and how to use threads and sockets to enable concurrency and communication between programs.

Some of the topics covered in this unit are:

- Swing and AWT components and events
- Layout managers and containers
- Dialogs and menus
- Graphics and animation
- Servlets and JSPs
- HTTP protocol and request/response cycle
- Session management and cookies
- JDBC and SQL
- Threads and synchronization
- Sockets and networking



Hello, I am Sydney, your AI assistant. I can help you with your query.

To write programs using JavaScript for web page to display browser information, you can use the following steps:

- Use the `window.navigator` object to access the properties and methods of the browser, such as `appName`, `appVersion`, `userAgent`, `platform`, `cookieEnabled`, etc.    
- Use the `document.write()` method to display the browser information on the web page. 
- Use the `userAgent.match()` method to detect the browser name by matching it with a regular expression. 
- Use the `indexOf()` method to find the position of a substring in the `userAgent` property. 
- Use the `parseFloat()` and `parseInt()` methods to extract the browser version from the `appVersion` property. 

Here is an example of a JavaScript program that displays the browser name and version on the web page:

```javascript
// Get the user agent string
var userAgent = window.navigator.userAgent;

// Declare variables for browser name and version
var browserName, browserVersion;

// Detect the browser name
if (userAgent.match(/Opera|OPR\//)) {
  browserName = 'Opera';
}
else if (userAgent.match(/Edge/)) {
  browserName = 'Edge';
}
else if (userAgent.match(/Chrome/)) {
  browserName = 'Chrome';
}
else if (userAgent.match(/Safari/)) {
  browserName = 'Safari';
}
else if (userAgent.match(/Firefox/)) {
  browserName = 'Firefox';
}
else if (userAgent.match(/MSIE|Trident/)) {
  browserName = 'Internet Explorer';
}
else {
  browserName = 'Unknown';
}

// Detect the browser version
var verOffset, index;
if ((verOffset = userAgent.indexOf('OPR/')) != -1) {
  // Opera
  browserVersion = userAgent.substring(verOffset + 4);
}
else if ((verOffset = userAgent.indexOf('Edge/')) != -1) {
  // Edge
  browserVersion = userAgent.substring(verOffset + 5);
}
else if ((verOffset = userAgent.indexOf('Chrome/')) != -1) {
  // Chrome
  browserVersion = userAgent.substring(verOffset + 7);
}
else if ((verOffset = userAgent.indexOf('Safari/')) != -1) {
  // Safari
  browserVersion = userAgent.substring(verOffset + 7);
  if ((index = userAgent.indexOf('Version/')) != -1) {
    browserVersion = userAgent.substring(index + 8);
  }
}
else if ((verOffset = userAgent.indexOf('Firefox/')) != -1) {
  // Firefox
  browserVersion = userAgent.substring(verOffset + 8);
}
else if ((verOffset = userAgent.indexOf('MSIE')) != -1) {
  // Internet Explorer
  browserVersion = userAgent.substring(verOffset + 5);
}
else if (userAgent.indexOf('Trident/') != -1) {
  // Internet Explorer 11
  browserVersion = userAgent.substring(userAgent.indexOf('rv:') + 3);
}
else {
  // Other browsers
  browserVersion = 'Unknown';
}

// Display the browser name and version on the web page
document.write('Browser name: ' + browserName + '<br>');
document.write('Browser version: ' + browserVersion + '<br>');
```



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some content on the topic of Java applet to display the calculator program:

# Java applet to display the calculator program

- A Java applet is a small Java application that can be embedded with web browsers to display dynamic content and can run on the client-side directly .
- A Java applet program for the calculator can use a grid layout to arrange buttons for the digits and for the addition, subtraction, multiplication, and division operations.
- A Java applet program for the calculator can also use a text field to display the first and second numbers and the results .
- A Java applet program for the calculator can add an action listener to each button to perform the corresponding arithmetic operation.
- A Java applet program for the calculator can use the `java.awt` and `java.applet` packages to create the graphical user interface and the applet functionality   .

## Example of a Java applet program for the calculator

```java
// Importing the required packages
import java.awt.*;
import java.applet.*;
import java.awt.event.*;

// Creating the applet class that extends the Applet class
public class Calculator extends Applet implements ActionListener {
  // Declaring the text field, buttons, and variables
  TextField t1, t2, t3;
  Button b1, b2, b3, b4;
  double a, b, c;

  // Initializing the applet components
  public void init() {
    // Creating the text fields
    t1 = new TextField(10);
    t2 = new TextField(10);
    t3 = new TextField(10);

    // Creating the buttons
    b1 = new Button("+");
    b2 = new Button("-");
    b3 = new Button("*");
    b4 = new Button("/");

    // Adding the components to the applet
    add(t1);
    add(t2);
    add(t3);
    add(b1);
    add(b2);
    add(b3);
    add(b4);

    // Adding the action listeners to the buttons
    b1.addActionListener(this);
    b2.addActionListener(this);
    b3.addActionListener(this);
    b4.addActionListener(this);
  }

  // Handling the button clicks
  public void actionPerformed(ActionEvent e) {
    // Getting the values from the text fields
    a = Double.parseDouble(t1.getText());
    b = Double.parseDouble(t2.getText());

    // Checking which button is clicked and performing the operation
    if (e.getSource() == b1) {
      c = a + b;
    }
    if (e.getSource() == b2) {
      c = a - b;
    }
    if (e.getSource() == b3) {
      c = a * b;
    }
    if (e.getSource() == b4) {
      c = a / b;
    }

    // Setting the result to the third text field
    t3.setText(String.valueOf(c));
  }
}
```



## Unit 3 - Design dynamic web pages using Javascript and XML

- Dynamic web pages are web pages that can change their content or appearance without reloading the whole page. They can provide a better user experience and more interactivity than static web pages.
- Javascript is a scripting language that can run in the browser and manipulate the HTML and CSS elements of a web page. It can also communicate with the server and exchange data using various methods, such as AJAX, JSON, or XML.
- XML (Extensible Markup Language) is a format for storing and transferring structured data. It can be used to define the content and layout of a web page, or to exchange data between the client and the server.
- To design dynamic web pages using Javascript and XML, you need to follow these steps:

  1. Create an HTML document that defines the structure and style of the web page. You can use HTML5 elements and CSS3 properties to enhance the appearance and functionality of the page.
  2. Write Javascript code that can access and modify the HTML elements using the Document Object Model (DOM) API. You can use Javascript functions, variables, operators, loops, conditions, events, and objects to create dynamic behavior and logic for the page.
  3. Use AJAX (Asynchronous Javascript and XML) to send and receive data from the server without reloading the page. You can use the XMLHttpRequest object or the fetch API to create and handle AJAX requests. You can also use Javascript libraries or frameworks, such as jQuery, Axios, or React, to simplify the AJAX process.
  4. Parse and process the XML data that is returned from the server using Javascript. You can use the DOMParser object or the XMLSerializer object to convert XML strings to XML documents or vice versa. You can also use the XML DOM API to access and manipulate the XML nodes and attributes.
  5. Update the HTML elements with the new data or content using Javascript. You can use the innerHTML property or the createElement and appendChild methods to insert or replace HTML elements. You can also use the setAttribute and removeAttribute methods to modify the HTML attributes.

- Here is an example of a dynamic web page that uses Javascript and XML to display a list of books:

```html
<html>
<head>
  <style>
    table, th, td {
      border: 1px solid black;
      border-collapse: collapse;
    }
    th, td {
      padding: 10px;
    }
  </style>
</head>
<body>
  <h1>Books</h1>
  <button onclick="loadBooks()">Load Books</button>
  <table id="booksTable">
    <tr>
      <th>Title</th>
      <th>Author</th>
      <th>Price</th>
    </tr>
  </table>
  <script>
    function loadBooks() {
      // create an AJAX request
      var xhr = new XMLHttpRequest();
      // specify the request method and URL
      xhr.open("GET", "books.xml");
      // define what to do when the request is successful
      xhr.onload = function() {
        // parse the XML response
        var parser = new DOMParser();
        var xmlDoc = parser.parseFromString(xhr.responseText, "text/xml");
        // get the book elements from the XML document
        var books = xmlDoc.getElementsByTagName("book");
        // loop through the book elements
        for (var i = 0; i < books.length; i++) {
          // get the title, author, and price elements from each book element
          var title = books[i].getElementsByTagName("title")[0].textContent;
          var author = books[i].getElementsByTagName("author")[0].textContent;
          var price = books[i].getElementsByTagName("price")[0].textContent;
          // create a new table row with three cells
          var row = document.createElement("tr");
          var cell1 = document.createElement("td");
          var cell2 = document.createElement("td");
          var cell3 = document.createElement("td");
          // set the text content of each cell with the corresponding data
          cell1.textContent = title;
          cell2.textContent = author;
          cell3.textContent = price;
          // append the cells to the row
          row.appendChild(cell1);
          row.appendChild(cell2);
          row.appendChild(cell3);
          // append the row to the table
          document.getElementById("booksTable").appendChild(row);
        }
      };
      // send the request
      xhr.send();
    }
  </script>
</body>
</html>
```

- Here is an example of the XML file that contains the



Hello, I am Sydney, your AI assistant. I can help you with writing a program in XML for creation of DTD, which specifies set of rules for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab. Here is some content that you can use for your study material:

### Writing program in XML for creation of DTD

- A DTD (Document Type Declaration) is a way to describe the structure, elements and attributes of an XML document. It defines the grammar and vocabulary of an XML language. 
- A DTD can be used to validate an XML document against the rules of the XML language. It can also help independent groups of people to agree on a standard DTD for interchanging data.  
- A DTD can be declared internally or externally. An internal DTD is included in the same file as the XML document, while an external DTD is referenced by a URL or a system identifier. 
- A DTD consists of declarations for elements, attributes, entities, notations and comments. Each declaration has a specific syntax and rules. 
- An element declaration defines the name and the content model of an element. The content model specifies what child elements and text can appear inside the element. It can be empty, any, mixed, or a sequence of choices and occurrences. 
- An attribute declaration defines the name, type and default value of an attribute. The type can be one of the predefined types (CDATA, ID, IDREF, IDREFS, ENTITY, ENTITIES, NMTOKEN, NMTOKENS) or an enumeration of possible values. The default value can be one of the predefined values (#REQUIRED, #IMPLIED, #FIXED) or a literal value. 
- An entity declaration defines a name and a value for an entity. An entity is a way to replace text or markup with a reference. It can be general or parameter, internal or external, parsed or unparsed. 
- A notation declaration defines a name and a system identifier for a notation. A notation is a way to identify the format or encoding of an unparsed entity or an attribute value. 
- A comment is a way to add notes or explanations to a DTD. It starts with <!-- and ends with -->. It can appear anywhere in a DTD, except inside declarations. 

Here is an example of a program in XML for creation of DTD, which specifies set of rules for the notes of the Unit 3:

```xml
<?xml version="1.0"?>
<!DOCTYPE notes [
  <!ELEMENT notes (unit+)>
  <!ELEMENT unit (title, content)>
  <!ATTLIST unit number CDATA #REQUIRED>
  <!ELEMENT title (#PCDATA)>
  <!ELEMENT content (section+)>
  <!ELEMENT section (heading, paragraph+)>
  <!ATTLIST section number CDATA #REQUIRED>
  <!ELEMENT heading (#PCDATA)>
  <!ELEMENT paragraph (#PCDATA)>
]>
<notes>
  <unit number="3">
    <title>Design dynamic web pages using Javascript and XML</title>
    <content>
      <section number="1">
        <heading>Introduction to Javascript</heading>
        <paragraph>Javascript is a scripting language that can run in a web browser.</paragraph>
        <paragraph>It can manipulate the HTML elements and the Document Object Model (DOM) of a web page.</paragraph>
        <paragraph>It can also interact with the user and the server using events and AJAX.</paragraph>
      </section>
      <section number="2">
        <heading>Introduction to XML</heading>
        <paragraph>XML is a markup language that can store and exchange structured data.</paragraph>
        <paragraph>It can be validated using a DTD or a Schema.</paragraph>
        <paragraph>It can be transformed and formatted using XSLT and CSS.</paragraph>
      </section>
    </content>
  </unit>
</notes>
```



### Create a style sheet in CSS/ XSL & display the document in internet explorer for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab

- A style sheet is a file that defines the appearance and layout of a web page or an XML document.
- CSS (Cascading Style Sheets) is a language that describes how HTML elements are displayed on the screen, in print, or in other media.
- XSL (Extensible Stylesheet Language) is a language that transforms XML documents into other formats, such as HTML, PDF, or plain text.
- To create a style sheet in CSS/ XSL, you need to follow these steps:

  1. Create a text file with the extension .css or .xsl, depending on the type of style sheet you want to create.
  2. Write the rules and declarations that define the style of the elements in your HTML or XML document. You can use selectors, properties, values, and functions to specify the style.
  3. Save the file in the same folder as your HTML or XML document, or in a different location if you specify the path in the link or import statement.
  4. Link or import the style sheet to your HTML or XML document using the <link> or <style> element for CSS, or the <xsl:stylesheet> or <xsl:transform> element for XSL.
  5. Test your style sheet in a web browser or an XML processor to see the effect on your document.

- To display the document in internet explorer, you need to follow these steps:

  1. Open internet explorer and navigate to the folder where your HTML or XML document is located.
  2. Double-click on the file name to open it in the browser. You should see the document with the style applied from the linked or imported style sheet.
  3. If the document does not display correctly, check the following possible issues:

    - The file extension of the style sheet is correct and matches the type of style sheet you created.
    - The path of the style sheet is correct and matches the location of the file.
    - The syntax and format of the style sheet is valid and follows the rules of CSS or XSL.
    - The browser supports the features and functions of the style sheet. Internet explorer may not support some of the newer or experimental features of CSS or XSL. You can check the browser compatibility of the style sheet on websites like https://caniuse.com/ or https://www.w3schools.com/cssref/css3_browsersupport.asp.



# Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP

- A dynamic web page is a web page whose content and appearance can change according to the user's input, preferences, or actions. A dynamic web page can also display different content depending on the time, date, location, or other factors.
- A dynamic web page is created by using server-side programming languages, such as ASP, JSP, or PHP, that run on the web server and generate HTML code that is sent to the web browser. The web browser then renders the HTML code and displays the web page to the user.
- Server-side programming languages can interact with databases, files, or other resources on the web server, and use them to create dynamic content for the web page. For example, a server-side script can query a database and display the results in a table, or read a file and display its contents in a text box.
- Server-side programming languages can also use variables, loops, conditions, functions, and other programming constructs to create dynamic web pages. For example, a server-side script can use a loop to generate a list of links, or a condition to display a different message based on the user's input.
- Server-side programming languages can also use cookies, sessions, or other mechanisms to store and retrieve information about the user or the web page. For example, a server-side script can use a cookie to remember the user's name, or a session to store the user's shopping cart items.
- Server-side programming languages can also use frameworks, libraries, or templates to simplify the development of dynamic web pages. For example, a server-side script can use a framework like Django (Python) or Express (JavaScript) to handle common tasks like routing, authentication, or validation, or a template engine like Smarty (PHP) or Thymeleaf (Java) to separate the presentation from the logic.



### Program to illustrate JDBC connectivity

JDBC stands for Java Database Connectivity, which is a standard Java API for connecting to relational databases. JDBC allows a Java application to execute SQL statements and retrieve the results from a database server.

To use JDBC, we need to follow these steps:

1. Load the JDBC driver class that corresponds to the type of database we want to connect to. For example, to connect to MySQL, we can use `Class.forName("com.mysql.jdbc.Driver");`.
2. Create a connection object that represents the database connection. We need to provide a connection URL that specifies the database server address, the database name, and the user credentials. For example, to connect to MySQL, we can use `Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test","root","password");`.
3. Create a statement object that allows us to execute SQL queries. We can use `Statement stmt = con.createStatement();` to create a simple statement, or `PreparedStatement pstmt = con.prepareStatement(sql);` to create a prepared statement that can accept parameters.
4. Execute the SQL query and obtain the result set object that contains the data returned by the query. We can use `ResultSet rs = stmt.executeQuery(sql);` to execute a query that returns data, or `int rows = stmt.executeUpdate(sql);` to execute a query that modifies data.
5. Process the result set by using methods such as `rs.next()`, `rs.getInt()`, `rs.getString()`, etc. to iterate over the rows and columns of the data.
6. Close the resources such as statement, result set, and connection when they are no longer needed. We can use `rs.close()`, `stmt.close()`, and `con.close()` to close them respectively.

Here is an example of a Java program that connects to a MySQL database and executes a simple query:

```java
import java.sql.*;

public class JDBCExample {

    public static void main(String[] args) {

        // Load the JDBC driver
        try {
            Class.forName("com.mysql.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

        // Create the connection object
        Connection con = null;
        try {
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test","root","password");
        } catch (SQLException e) {
            e.printStackTrace();
        }

        // Create the statement object
        Statement stmt = null;
        try {
            stmt = con.createStatement();
        } catch (SQLException e) {
            e.printStackTrace();
        }

        // Execute the query and get the result set
        ResultSet rs = null;
        try {
            rs = stmt.executeQuery("SELECT * FROM students");
        } catch (SQLException e) {
            e.printStackTrace();
        }

        // Process the result set
        try {
            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                int age = rs.getInt("age");
                System.out.println(id + " " + name + " " + age);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        // Close the resources
        try {
            rs.close();
            stmt.close();
            con.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

This program assumes that there is a table called `students` in the database `test` with the following schema:

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);
```

And some sample data:

```sql
INSERT INTO students VALUES (1, 'Alice', 20);
INSERT INTO students VALUES (2, 'Bob', 21);
INSERT INTO students VALUES (3, 'Charlie', 19);
```

The output of the program should be:

```
1 Alice 20
2 Bob 21
3 Charlie 19
```



### Program for maintaining database by sending queries for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

- A dynamic web page is a web page that can change its content or layout depending on the user's input, preferences, or environment.
- A dynamic web page can use server-side scripting to generate mutable content. Server-side scripting is the technique of using a programming language that runs on the web server to create web pages.
- Some of the common server-side languages are PHP, ASP, ASP.NET, JSP, and ColdFusion. These languages can use the Common Gateway Interface (CGI) to communicate with the web server and produce dynamic web pages.
- To design a dynamic web page using server-side programming, the following steps are required:
  - Choose a server-side language and a web framework that suits your needs and preferences. A web framework is a collection of tools and libraries that simplify the development of web applications.
  - Set up your development environment, which may include installing the web server, the server-side language, the web framework, and the database system.
  - Create a database and populate it with some data that you want to display on your web page. You can use a database management system (DBMS) such as MySQL, PostgreSQL, or MongoDB to create and manage your database.
  - Write the server-side code that connects to the database, executes queries, and returns the results to the web page. You can use the syntax and features of your chosen server-side language and web framework to write the code.
  - Write the HTML code that defines the structure and layout of your web page. You can use HTML tags and attributes to create the elements of your web page.
  - Write the CSS code that defines the style and appearance of your web page. You can use CSS selectors, properties, and values to apply the style rules to your web page elements.
  - Write the JavaScript code that defines the behavior and interactivity of your web page. You can use JavaScript statements, variables, functions, and events to add dynamic features to your web page.
  - Test and debug your web page using a web browser and a web developer tool. You can use the web browser to view and interact with your web page, and the web developer tool to inspect and modify the HTML, CSS, and JavaScript code of your web page.
  - Deploy your web page to a web server and make it accessible to the public. You can use a web hosting service or a cloud platform to upload and host your web page files on the web server.

- Here is an example of a dynamic web page using PHP as the server-side language and MySQL as the database system:

```php
<?php
// connect to the database
$db = mysqli_connect("localhost", "root", "", "webtech");

// check connection
if (!$db) {
  die("Connection failed: " . mysqli_connect_error());
}

// get the query parameter from the URL
$q = $_GET["q"];

// execute the query and get the result
$result = mysqli_query($db, "SELECT * FROM notes WHERE unit = '$q'");

// check result
if (mysqli_num_rows($result) > 0) {
  // output the data of each row
  while($row = mysqli_fetch_assoc($result)) {
    echo "Topic: " . $row["topic"] . "<br>";
    echo "Content: " . $row["content"] . "<br>";
    echo "<hr>";
  }
} else {
  // no data found
  echo "No notes found for unit " . $q;
}

// close connection
mysqli_close($db);
?>
```

- This PHP code connects to the MySQL database named "webtech" and executes a query to select all the notes from the table named "notes" where the unit column matches the query parameter "q" from the URL. For example, if the URL is "http://localhost/notes.php?q=4", the query parameter "q" is "4" and the query is "SELECT * FROM notes WHERE unit = '4'". The code then outputs the topic and content of each note in the result, or a message if no notes are found. The code also closes the connection to the database at the end.

- Here is an example of the HTML code that displays the dynamic



### Design and implement a simple servlet book query with the help of JDBC & SQL

A servlet is a Java class that runs on a web server and handles HTTP requests and responses. JDBC is a Java API that allows Java programs to interact with databases using SQL commands. SQL is a language for querying and manipulating data in relational databases.

To design and implement a simple servlet book query with the help of JDBC & SQL, we need to follow these steps:

1. Create a database and a table to store the book information. For example, we can use MySQL as the database and create a table called books with columns id, title, author, and price.
2. Download and install a web server that supports servlets, such as Apache Tomcat, and configure it to run on a specific port, such as 8080.
3. Download and add the JDBC driver for the database to the web server's classpath, such as mysql-connector.jar for MySQL.
4. Create a servlet class that extends HttpServlet and overrides the doGet or doPost method, depending on the HTTP method used to send the request. The servlet class should also have a constructor that loads the JDBC driver and establishes a connection to the database using the DriverManager class.
5. In the doGet or doPost method, get the parameters from the request object, such as the book id or title, and use them to create a SQL query, such as SELECT * FROM books WHERE id = ? or SELECT * FROM books WHERE title LIKE ?.
6. Execute the SQL query using a PreparedStatement object and store the result in a ResultSet object. A PreparedStatement object allows us to use placeholders (?) for the parameters and set their values dynamically using the setInt, setString, etc. methods. A ResultSet object allows us to iterate over the rows returned by the query and get the values of each column using the getInt, getString, etc. methods.
7. Create a response object that contains the HTML code to display the book information in a table format. Use the PrintWriter object obtained from the response object to write the HTML code to the output stream. Use the JSTL (JavaServer Pages Standard Tag Library) to simplify the iteration and presentation of the data. JSTL is a set of custom tags that provide common functionality for JSP pages, such as looping, conditional statements, formatting, etc. To use JSTL, we need to add the jstl.jar file to the web server's classpath and include the taglib directive in the JSP page, such as <%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>.
8. Close the ResultSet, PreparedStatement, and Connection objects to release the resources and avoid memory leaks.
9. Compile the servlet class and place it in the web server's webapps folder, under a specific context, such as webapps/bookquery/WEB-INF/classes. Also, create a web.xml file in the webapps/bookquery/WEB-INF folder that defines the servlet name, class, and mapping, such as:

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

10. Create a JSP page that contains a form to enter the book id or title and submit it to the servlet using the GET or POST method. Place the JSP page in the webapps/bookquery folder, such as index.jsp. The JSP page should also include the JSTL taglib directive and use the JSTL tags to display the book information returned by the servlet, such as:

```html
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<html>
<head>
  <title>Book Query</title>
</head>
<body>
  <h1>Book Query</h1>
  <form action="bookquery" method="GET">
    <p>Enter book id or title:</p>
    <input type="text" name="query" />
    <input type="submit" value="Search" />
  </form>
  <c:if test="${not empty requestScope.books}">
    <table border="1">
      <tr>
        <th>Id</th>
        <th>Title</th>
        <th>Author</th>

```




Hello, I am Sydney, your AI assistant. I can help you with your query. Here are the steps to create a MS Access database:

### Create MS Access Database

- Open Access. If Access is already open, select File > New .
- Select Blank database, or select a template  .
- Enter a name for the database, select a location, and then select Create  .
- If needed, select Enable content in the yellow message bar when the database opens .
- Create the tables that you need for your database. You can use the Table Design view or the Datasheet view to create and modify the table structure .
- Add data to your tables by entering values in the cells or importing data from other sources .



## Unit 5 - Design server site applications using JDDC,ODBC and section tracking API

- JDBC stands for Java Database Connectivity, which is a standard Java API for connecting and executing queries with databases .
- ODBC stands for Open Database Connectivity, which is a standard C API for connecting and executing queries with databases  .
- JDBC-ODBC Bridge is a type of driver that acts as an interface between Java applications and databases that support ODBC.
- Section tracking API is an API that allows web applications to track the state and behavior of users across multiple requests and sessions.
- To design server site applications using JDDC,ODBC and section tracking API, the following steps are required:

  - Choose a suitable JDBC driver for the database that the application needs to access .
  - Install and configure the JDBC driver on the server machine .
  - Use the JDBC API to establish a connection with the database, execute queries, and process the results .
  - If the database does not support JDBC, use the JDBC-ODBC Bridge driver to connect to the database through ODBC.
  - Use the section tracking API to store and retrieve user-specific data across multiple requests and sessions.
  - Use the section tracking API to implement authentication, authorization, personalization, and other features that depend on user identity and preferences.
  - Use the section tracking API to manage the lifecycle and concurrency of user sessions.
  - Use the section tracking API to handle session timeouts, expiration, and invalidation.
  - Use the section tracking API to secure the session data from unauthorized access and modification.
  - Use the section tracking API to optimize the performance and scalability of the web application.



### Install TOMCAT web server and APACHE for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

Tomcat is an open source web server and servlet container that supports Java applications. Apache is another web server that can work with Tomcat to handle static content and proxy requests. In this note, we will learn how to install and configure Tomcat and Apache on a Windows system.

The steps are as follows:

1. Install Java
    - Tomcat requires Java to run, so we need to install Java first. You can download the latest Java Development Kit (JDK) from the official website: https://www.oracle.com/java/technologies/javase-downloads.html
    - Choose the appropriate version for your system and follow the installation instructions. Make sure to set the JAVA_HOME environment variable to point to the installation directory of the JDK.
2. Install Tomcat
    - You can download the latest Tomcat installer from the official website: http://tomcat.apache.org/
    - Choose the Windows Service Installer option and run the executable file. Follow the installation wizard and accept the default settings. You can also choose a custom installation and change the port number, service name, and installation directory of Tomcat.
    - After the installation is complete, you can start the Tomcat service from the Start menu or the Services app. You can also use the Tomcat Monitor app to manage the service and configure the memory settings, logging options, and security features of Tomcat.
    - To verify that Tomcat is running, open a web browser and go to http://localhost:8080. You should see the Tomcat welcome page.
3. Install Apache
    - You can download the latest Apache installer from the official website: https://httpd.apache.org/download.cgi
    - Choose the Windows binary option and run the executable file. Follow the installation wizard and accept the default settings. You can also choose a custom installation and change the port number, server name, and installation directory of Apache.
    - After the installation is complete, you can start the Apache service from the Start menu or the Services app. You can also use the Apache Monitor app to manage the service and configure the server settings, modules, and virtual hosts of Apache.
    - To verify that Apache is running, open a web browser and go to http://localhost. You should see the Apache welcome page.
4. Configure Tomcat to work with Apache
    - To make Apache and Tomcat work together, we need to enable the mod_proxy module in Apache and configure the proxy settings in the httpd.conf file. This will allow Apache to forward requests for dynamic content to Tomcat, while serving static content itself.
    - To enable the mod_proxy module, open the httpd.conf file in a text editor and uncomment the following lines:

        ```
        LoadModule proxy_module modules/mod_proxy.so
        LoadModule proxy_http_module modules/mod_proxy_http.so
        LoadModule proxy_ajp_module modules/mod_proxy_ajp.so
        ```

    - To configure the proxy settings, add the following lines at the end of the httpd.conf file:

        ```
        ProxyRequests Off
        ProxyPreserveHost On
        <Proxy *>
            Order deny,allow
            Allow from all
        </Proxy>
        ProxyPass /tomcat http://localhost:8080
        ProxyPassReverse /tomcat http://localhost:8080
        ```

    - These lines tell Apache to proxy all requests starting with /tomcat to the Tomcat server running on port 8080, and to preserve the original host name in the request. You can change the /tomcat path to any other path you prefer, or use / to proxy all requests to Tomcat.
    - Save the httpd.conf file and restart the Apache service.
5. How to verify that it's working
    - To test the integration of Apache and Tomcat, open a web browser and go to http://localhost/tomcat. You should see the same Tomcat welcome page as before, but this time served by Apache. You can also check the URL of any of the links on the page, and you should see that they start with /tomcat.
    - You can also deploy any Java web application to the Tomcat webapps directory and access it through Apache. For example, if you have a web application named myapp.war, you can copy it to the C:\Program Files\Apache Software Foundation\Tomcat 10.0\webapps directory and then go to http://



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is the content I have generated for you based on the topic you have given me.

### Access the above developed static web pages for books web site, using these servers by putting the web pages developed for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To access the static web pages for books web site, you need to have a web server that can host and serve the HTML files. You can use any web server software such as Apache, Nginx, IIS, etc. You also need to have a domain name and a web hosting service that can connect your web server to the internet.
- To put the web pages developed for the notes of the Unit 5, you need to have a database that can store and retrieve the data related to the books, users, and sessions. You can use any database software such as MySQL, PostgreSQL, Oracle, etc. You also need to have a driver that can communicate between the web server and the database using JDDC, ODBC, or section tracking API. JDDC stands for Java Database Connectivity, ODBC stands for Open Database Connectivity, and section tracking API is an application programming interface that allows web applications to manage user sessions.
- To design server site applications using JDDC, ODBC, and section tracking API, you need to have a server-side scripting language that can generate dynamic web pages based on the user requests and the database data. You can use any server-side scripting language such as PHP, ASP.NET, JSP, etc. You also need to have a web framework that can simplify the development and deployment of web applications using JDDC, ODBC, and section tracking API. You can use any web framework such as Laravel, Django, Spring, etc.
- The following steps can be followed to access the above developed static web pages for books web site, using these servers by putting the web pages developed for the notes of the Unit 5:

  1. Install and configure the web server software on your computer or server. Make sure the web server can run the server-side scripting language and the web framework you have chosen.
  2. Install and configure the database software on your computer or server. Make sure the database can be accessed by the web server using the driver you have chosen.
  3. Create the database schema and populate it with some sample data related to the books, users, and sessions. You can use any database management tool such as phpMyAdmin, pgAdmin, SQL Developer, etc.
  4. Copy the static web pages for books web site to the web server's root directory or a subdirectory. You can use any file transfer tool such as FTP, SCP, SFTP, etc.
  5. Create the server site applications using JDDC, ODBC, and section tracking API that can handle the user requests and generate dynamic web pages based on the static web pages and the database data. You can use any code editor or IDE such as Visual Studio Code, Eclipse, NetBeans, etc.
  6. Test and debug the server site applications using JDDC, ODBC, and section tracking API. You can use any web browser or testing tool such as Chrome, Firefox, Postman, etc.
  7. Deploy the server site applications using JDDC, ODBC, and section tracking API to the web server. You can use any deployment tool such as Git, FTP, SCP, SFTP, etc.
  8. Access the static web pages for books web site using the domain name and the web hosting service you have chosen. You can use any web browser or client tool such as Chrome, Firefox, Curl, etc.

I hope this content is helpful for you. If you have any questions or feedback, please let me know. Thank you for using my service.🙏



### Assume four users user1, user2, user3 and user4 having the passwords pwd1, pwd2, pwd3 and pwd4 respectively for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- The notes of the Unit 5 are stored in a database on a web server that can be accessed by the users through a web browser.
- The web server uses Java Database Connectivity (JDBC) to connect to the database and execute SQL queries and commands.
- The web server also uses Open Database Connectivity (ODBC) to provide a standard interface for accessing different types of databases from different vendors.
- The web server uses session tracking API to maintain the state of each user and authenticate them with their passwords.
- The session tracking API can use cookies, URL rewriting, hidden form fields or HttpSession objects to store the session information.
- The steps to design the server-side application are:

  - Create a database with a table that contains the notes of the Unit 5 and the user information such as username and password.
  - Create a web page that allows the users to enter their username and password and submit them to the web server.
  - Create a servlet that receives the username and password from the web page and validates them against the database using JDBC and ODBC.
  - If the username and password are valid, create a session for the user using the session tracking API and store the username in the session object.
  - Retrieve the notes of the Unit 5 from the database using JDBC and ODBC and display them to the user in another web page.
  - If the username and password are invalid, display an error message to the user and redirect them to the login page.
  - If the user logs out or the session expires, invalidate the session and redirect the user to the login page.



# Write a servlet for doing the following for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- JDDC stands for Java Database Connectivity, which is an API that allows Java applications to interact with various types of databases using a common interface.
- ODBC stands for Open Database Connectivity, which is an API that allows applications to access data from different database management systems using a common interface.
- Section tracking API is an API that allows servlets to track and manage information about a user's session, such as attributes, creation time, and last access time.

## Steps to write a servlet for using JDDC,ODBC and section tracking API

1. Import the required packages, such as javax.servlet, javax.servlet.http, java.sql, and java.io.
2. Define a public class that extends HttpServlet and implements the doGet or doPost method, depending on the HTTP method used by the client.
3. In the doGet or doPost method, get the request parameters from the HttpServletRequest object and write the response to the HttpServletResponse object.
4. To use JDDC, create a Connection object by calling DriverManager.getConnection with the database URL, username, and password. Alternatively, use a DataSource object to get a connection from a connection pool.
5. To use ODBC, load the JDBC-ODBC bridge driver by calling Class.forName with the driver class name. Then, create a Connection object by calling DriverManager.getConnection with the ODBC data source name, username, and password.
6. To use section tracking API, get the HttpSession object by calling request.getSession. Then, use the methods of the HttpSession object to set or get attributes, check the session status, or invalidate the session.
7. To execute SQL statements, create a Statement or PreparedStatement object from the Connection object and call the execute, executeQuery, or executeUpdate method. Then, process the ResultSet object if any.
8. To handle exceptions, use try-catch-finally blocks and print the error messages or stack traces to the response or a log file.
9. To close the resources, use the close method of the Connection, Statement, PreparedStatement, and ResultSet objects in the finally block.
10. To compile and deploy the servlet, follow the instructions of the web server and the servlet container. For example, use the javac command to compile the servlet class and copy the class file to the webapps directory of the Tomcat server. Then, restart the server and access the servlet URL from a web browser.



### Create a Cookie and add these four user id’s and passwords to this Cookie for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A cookie is a small piece of data that is stored by the browser and sent to the server with every request. Cookies can be used to store user preferences, session information, authentication details, etc.
- To create a cookie in Java, we can use the `Cookie` class from the `javax.servlet.http` package. The constructor of this class takes two parameters: the name and the value of the cookie.
- To add a cookie to the response, we can use the `addCookie` method of the `HttpServletResponse` interface. This method takes a `Cookie` object as an argument and adds it to the response header.
- To read a cookie from the request, we can use the `getCookies` method of the `HttpServletRequest` interface. This method returns an array of `Cookie` objects that represent all the cookies sent by the browser.
- To update or delete a cookie, we can modify its properties, such as `value`, `maxAge`, `path`, `domain`, etc. and then add it to the response again. To delete a cookie, we can set its `maxAge` to zero.

- Here is an example of how to create a cookie and add four user ids and passwords to it:

```java
// Create a cookie with the name "users" and a value that is a string of user ids and passwords separated by commas
Cookie cookie = new Cookie("users", "user1:pass1,user2:pass2,user3:pass3,user4:pass4");

// Set the maximum age of the cookie to one hour (in seconds)
cookie.setMaxAge(60 * 60);

// Add the cookie to the response
response.addCookie(cookie);
```



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is the content I have generated for you:

### Read the user id and passwords entered in the Login form and authenticate with the values available in the cookies for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A login form is a web page that allows users to enter their user id and password to access a protected resource or service.
- A cookie is a small piece of data that is stored by the web browser on the user's device. It can store information such as user preferences, session id, authentication tokens, etc.
- To authenticate the user id and password entered in the login form, the server can compare them with the values available in the cookies. This can be done using Java Database Connectivity (JDBC), Open Database Connectivity (ODBC) and session tracking API.
- JDBC is a Java API that allows Java applications to connect to various types of databases and execute SQL queries and commands.
- ODBC is a standard API that allows applications to access data from different database management systems using a common interface.
- Session tracking API is a set of methods and classes in the Java Servlet API that allows web applications to maintain the state of a user across multiple requests and responses.
- The steps to read the user id and password entered in the login form and authenticate with the values available in the cookies are:

  1. Create a login form using HTML and JavaScript. The form should have two input fields for user id and password, and a submit button. The form should send a POST request to a servlet that handles the authentication logic.
  2. Create a servlet that receives the user id and password from the login form. The servlet should use the HttpServletRequest object to get the parameters from the request. The servlet should also use the HttpServletResponse object to set the response headers and content.
  3. Use the JDBC or ODBC API to establish a connection to the database that stores the user credentials. The servlet should use the DriverManager class to get a Connection object, and use the Connection object to create a Statement or PreparedStatement object. The servlet should use the Statement or PreparedStatement object to execute a SQL query that selects the user id and password from the database based on the user id entered in the login form.
  4. Use the ResultSet object to get the result of the SQL query. The servlet should use the ResultSet object to check if the user id exists in the database, and if the password matches the one entered in the login form. The servlet should use the ResultSet object to close the result set, and use the Statement or PreparedStatement object to close the statement.
  5. Use the session tracking API to create or get a HttpSession object for the user. The servlet should use the HttpServletRequest object to call the getSession method, which returns a HttpSession object. The servlet should use the HttpSession object to store the user id and password as attributes in the session. The servlet should also use the HttpSession object to set the maximum inactive interval for the session, which determines how long the session will remain valid.
  6. Use the cookie API to create or get a Cookie object for the user. The servlet should use the Cookie class to create a Cookie object, and use the Cookie object to set the name, value, domain, path, and expiry of the cookie. The servlet should use the HttpServletResponse object to call the addCookie method, which adds the cookie to the response. The cookie should store the user id and password as values in the cookie.
  7. Use the HttpServletResponse object to send a response to the user. The servlet should use the HttpServletResponse object to set the status code, content type, and content of the response. The servlet should use the RequestDispatcher object to forward the request and response to another servlet or JSP page that displays the protected resource or service. Alternatively, the servlet can use the HttpServletResponse object to send a redirect to another URL that displays the protected resource or service.



### Install a database (Mysql or Oracle) for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

This section will explain how to install MySQL database on Windows using the MySQL Installer . MySQL is a popular open-source relational database management system that can be used to store and manipulate data for web applications.

The steps to install MySQL database are as follows:

1. Download MySQL Installer for Windows from https://dev.mysql.com/downloads/installer/ and execute it. This will launch the MySQL Installer wizard that will guide you through the installation process.
2. On the welcome screen, choose the first option: Install MySQL Products. This will check for the latest updates and download them if available.
3. On the Choosing a Setup Type screen, select the setup type that suits your needs. You can choose from Developer Default, Server Only, Client Only, or Custom. For this tutorial, we will choose Developer Default, which will install the MySQL Server, MySQL Workbench, MySQL Shell, MySQL Router, MySQL Notifier, and other tools.
4. On the Check Requirements screen, review the list of software that will be installed or updated. If there are any missing prerequisites, the installer will download and install them for you. Click Next to continue.
5. On the Installation screen, click Execute to start the installation of the selected products. This may take some time depending on your internet speed and system performance. You can monitor the progress of each product on the screen.
6. On the Product Configuration screen, click Next to configure the MySQL Server. You will need to specify the following options:
   - Type and Networking: Choose the configuration type for your server. You can choose from Development Machine, Server Machine, or Dedicated Machine. For this tutorial, we will choose Development Machine, which will optimize the server for local development. You can also choose the port number and the network protocols for your server. The default port number is 3306 and the default protocol is TCP/IP. You can leave these as they are unless you have a specific reason to change them.
   - Authentication Method: Choose the authentication method for your server. You can choose from Strong Password Encryption for Authentication (recommended) or Use Legacy Authentication Method (Retain MySQL 5.x Compatibility). For this tutorial, we will choose the recommended option, which will use the caching_sha2_password plugin for password encryption and authentication.
   - Accounts and Roles: Set the password for the root user, which is the administrator account for your server. You can also create other user accounts and assign them roles and privileges. For this tutorial, we will only set the password for the root user and leave the rest as default.
   - Windows Service: Choose whether to run the MySQL Server as a Windows service or not. If you choose to run it as a service, you can also specify the service name, the start type, and the account that will run the service. For this tutorial, we will choose to run the MySQL Server as a service with the default options.
   - Apply Configuration: Click Execute to apply the configuration settings to your server. This will initialize the server, start the service, and test the connection. You can view the details of each step on the screen.
7. On the Installation Complete screen, click Next to finish the installation process. You can also choose to view the log file or the product manual if you want.
8. On the Finish screen, click Finish to exit the MySQL Installer wizard. You have successfully installed the MySQL database on your Windows machine.

You can verify the installation by opening the MySQL Command Line Client from cmd and entering the password for the root user. You should see a prompt like this:

```sql
mysql>
```

You can also use the MySQL Workbench, MySQL Shell, or any other tool to connect to and interact with your MySQL server.

: https://dev.mysql.com/doc/mysql-getting-started/en/
: https://dev.mysql.com/doc/refman/8.0/en/windows-installation.html



Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology Lab. Here is the content for your topic:

### Create a table which should contain at least the following fields: name, password, email-id, phone number for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API

- To create a table in a database, you need to use the SQL statement `CREATE TABLE` followed by the table name and the columns with their data types and constraints.
- For example, to create a table called `users` with the fields `name`, `password`, `email_id`, and `phone_number`, you can use the following SQL statement:

```sql
CREATE TABLE users (
  name VARCHAR(50) NOT NULL,
  password VARCHAR(20) NOT NULL,
  email_id VARCHAR(50) UNIQUE NOT NULL,
  phone_number VARCHAR(15) UNIQUE NOT NULL
);
```

- The data type `VARCHAR(n)` means a variable-length character string with a maximum length of `n` characters. The constraint `NOT NULL` means that the column cannot have a null value. The constraint `UNIQUE` means that the column cannot have duplicate values.
- To insert data into the table, you need to use the SQL statement `INSERT INTO` followed by the table name and the values for each column.
- For example, to insert a row into the `users` table with the values `Alice`, `1234`, `alice@example.com`, and `1234567890`, you can use the following SQL statement:

```sql
INSERT INTO users (name, password, email_id, phone_number) VALUES ('Alice', '1234', 'alice@example.com', '1234567890');
```

- To retrieve data from the table, you need to use the SQL statement `SELECT` followed by the columns you want to display and the table name. You can also use the `WHERE` clause to filter the data based on some condition.
- For example, to select all the columns from the `users` table where the `name` is `Alice`, you can use the following SQL statement:

```sql
SELECT * FROM users WHERE name = 'Alice';
```

- To update data in the table, you need to use the SQL statement `UPDATE` followed by the table name and the columns you want to change with their new values. You also need to use the `WHERE` clause to specify which row(s) you want to update.
- For example, to update the `password` column of the `users` table where the `name` is `Alice` to `4321`, you can use the following SQL statement:

```sql
UPDATE users SET password = '4321' WHERE name = 'Alice';
```

- To delete data from the table, you need to use the SQL statement `DELETE FROM` followed by the table name and the `WHERE` clause to specify which row(s) you want to delete.
- For example, to delete the row from the `users` table where the `name` is `Alice`, you can use the following SQL statement:

```sql
DELETE FROM users WHERE name = 'Alice';
```

- To delete the entire table, you need to use the SQL statement `DROP TABLE` followed by the table name.
- For example, to delete the `users` table, you can use the following SQL statement:

```sql
DROP TABLE users;
```

- To design server-side applications using JDBC, ODBC, and session tracking API, you need to follow these steps:
  - Install and configure a database server, such as MySQL, PostgreSQL, or Oracle, and create the database and tables you need for your application.
  - Install and configure a web server, such as Apache, Tomcat, or IIS, and a web application framework, such as Java Servlets, JSP, or ASP.NET, that supports JDBC, ODBC, or session tracking API.
  - Write the server-side code that connects to the database using JDBC or ODBC, executes SQL statements, and returns the results to the client. You can also use session tracking API to store and retrieve information about the user's session, such as login status, preferences, or shopping cart items.
  - Write the client-side code that displays the data from the server and allows the user to interact with the application, such as entering input, clicking buttons, or submitting forms. You can use HTML, CSS, JavaScript, or any other web technology for the client-side code.
  - Test and debug your application using a web browser and a database management tool, such as phpMyAdmin, pgAdmin, or SQL Developer. You can also use tools such as



# Write a java program/servlet/JSP to connect to that database and extract data from the tables and display them for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To connect to a database using Java, you need to use the JDBC (Java Database Connectivity) API, which provides a set of classes and interfaces to interact with various databases  .
- To use JDBC, you need to have a JDBC driver for the specific database you want to connect to, such as MySQL, Oracle, SQL Server, etc. The driver is a JAR file that implements the JDBC interfaces and communicates with the database server .
- To download the MySQL JDBC driver, you can go to the MySQL community downloads page and select the Connector/J option. Then, you can download the latest version of the JAR file and add it to your classpath when compiling and running your Java code.
- To connect to a MySQL database using JDBC, you need to follow these steps :
  - Load the MySQL JDBC driver class using the Class.forName() method, passing the fully qualified name of the driver class as a parameter. This will register the driver with the DriverManager class, which manages the available drivers and connections.
  - Create a Connection object using the DriverManager.getConnection() method, passing the URL of the database, the username and the password as parameters. The URL should have the format "jdbc:mysql://hostname:port/databaseName". The Connection object represents a physical connection to the database server.
  - Create a Statement object using the Connection.createStatement() method. The Statement object is used to execute SQL queries on the database.
  - Execute the SQL query using the Statement.executeQuery() method, passing the query string as a parameter. This will return a ResultSet object, which contains the data returned by the query. The ResultSet object has a cursor that points to the current row of data. You can use the ResultSet.next() method to move the cursor to the next row, and the ResultSet.getXXX() methods to get the values of the columns in the current row, where XXX is the data type of the column, such as getInt(), getString(), getDouble(), etc.
  - Close the ResultSet, Statement and Connection objects using the close() method. This will release the resources and terminate the connection to the database.

- To display the data from the ResultSet object, you can use a loop to iterate over the rows and print the values of the columns using the System.out.println() method. Alternatively, you can use a utility class such as DBTablePrinter to print the data in a table format.
- To write a servlet or a JSP to connect to a database and display data, you need to follow the same steps as above, but instead of printing the data to the standard output, you need to write the data to the response object, which represents the output stream to the client. You can use the response.setContentType() method to set the content type of the response, such as "text/html", and the response.getWriter() method to get a PrintWriter object, which can write text to the response. You can use HTML tags to format the data in a table or a list. You can also use JSP tags such as <sql:query>, <sql:result>, <sql:column>, etc. to simplify the database access and display.

- Here is an example of a Java program that connects to a MySQL database and displays the data from a table called employees:

```java
// Import the required packages
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class DatabaseConnection {

  public static void main(String[] args) {
    // Declare the variables for the database connection
    String url = "jdbc:mysql://localhost:3306/mydb"; // The URL of the database
    String username = "root"; // The username of the database
    String password = "root"; // The password of the database
    Connection conn = null; // The connection object
    Statement stmt = null; // The statement object
    ResultSet rs = null; // The result set object

    try {
      // Load the MySQL JDBC driver
      Class.forName("com.mysql.cj.jdbc.Driver");
      // Create a connection to the database
      conn = DriverManager.getConnection(url, username, password);
      // Create a statement to execute SQL queries
      stmt

```




### Insert the details of the users who register with the web site, whenever a new user clicks the submit button in the registration page for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To insert the details of the users who register with the web site, we need to use a server-side scripting language such as PHP, ASP.NET, or JSP to process the user input from the registration form and store it in a database using JDBC, ODBC, or session tracking API.
- JDBC (Java Database Connectivity) is an API that allows Java programs to access and manipulate data in various relational databases such as MySQL, Oracle, or SQL Server. JDBC provides a standard interface for connecting to different databases and executing SQL statements.
- ODBC (Open Database Connectivity) is a standard API that allows applications written in different languages such as C, C++, or Python to access and manipulate data in various databases using a common driver. ODBC drivers are available for many databases and platforms.
- Session tracking API is a mechanism that allows web applications to maintain the state of a user across multiple requests. Session tracking API can use cookies, URL rewriting, hidden fields, or servlets to store and retrieve information about a user's session.
- The steps to insert the details of the users who register with the web site are:

  1. Create a registration form in HTML that collects the user's name, email, password, and other details. The form should have a submit button that sends the user input to a server-side script using the POST method.
  2. Create a server-side script in PHP, ASP.NET, or JSP that receives the user input from the registration form and validates it. The script should check for any errors or missing values and display appropriate messages to the user. If the input is valid, the script should connect to a database using JDBC, ODBC, or session tracking API and insert the user details into a table. The script should also generate a unique session ID for the user and store it in a cookie, URL, hidden field, or servlet.
  3. Create a database table that stores the user details such as name, email, password, and session ID. The table should have a primary key that identifies each user uniquely. The table should also have appropriate constraints and indexes to ensure data integrity and performance.
  4. Create a confirmation page in HTML that displays a message to the user that their registration is successful and provides a link to the notes of the Unit 5. The confirmation page should also retrieve the user's session ID from the cookie, URL, hidden field, or servlet and use it to personalize the page with the user's name or other details.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a possible answer to your question:

### Write a JSP which insert the details of the 3 or 4 users who register with the web site by using registration form for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To write a JSP that inserts the details of the users who register with the website, we need to follow these steps:

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

  - Create a JSP page that processes the user input from the registration form and inserts it into the database table using JDBC, ODBC, or any other database connectivity API. For example, we can use the following code:

```jsp
<%@ page import="java.sql.*" %>
<%
  //Get the user input from the request object
  String name = request.getParameter("uname");
  String email = request.getParameter("uemail");
  String pass = request.getParameter("upass");

  //Create a connection object to connect to the database
  Connection con = null;
  PreparedStatement ps = null;
  try {
    //Load the driver class
    Class.forName("oracle.jdbc.driver.OracleDriver");
    //Get the connection using the driver manager
    con = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","oracle");
    //Create a prepared statement object to execute the SQL query
    ps = con.prepareStatement("insert into user432 values(?,?,?)");
    //Set the values for the parameters in the query
    ps.setString(1,name);
    ps.setString(2,email);
    ps.setString(3,pass);
    //Execute the query and get the number of rows affected
    int i = ps.executeUpdate();
    //Check if the insertion is successful or not
    if(i>0) {
      out.println("You are successfully registered...");
    }
  } catch(Exception e) {
    e.printStackTrace();
  } finally {
    //Close the resources
    if(ps!=null) ps.close();
    if(con!=null) con.close();
  }
%>
```

  - Optionally, we can also use session tracking API to maintain the state of the user across multiple requests. For example, we can use the following code to store the user name in the session object and display it in another JSP page:

```jsp
<%-- In process.jsp, after inserting the user details into the database --%>
<%
  //Get the session object from the request object
  HttpSession session = request.getSession();
  //Set the user name as an attribute in the session object
  session.setAttribute("user",name);
  //Redirect the user to another JSP page
  response.sendRedirect("welcome.jsp");
%>

<%-- In welcome.jsp, display the user name from the session object --%>
<%
  //Get the session object from the request object
  HttpSession session = request.getSession();
  //Get the user name from the session object
  String user = (String)session.getAttribute("user");
  //Display the user name
  out.println("Welcome, "+user);
%>
```

- This is how we can write a JSP that inserts the details of the users who register with the website by using registration form for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the



### Authenticate the user when he submits the login form using the user name and password from the database for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To authenticate the user when he submits the login form using the user name and password from the database, we need to use JDBC (Java Database Connectivity) and ODBC (Open Database Connectivity) drivers to connect to the database and execute SQL queries to verify the user credentials .
- JDBC and ODBC are APIs (Application Programming Interfaces) that allow Java applications to interact with various types of databases, such as relational, hierarchical, or object-oriented .
- JDBC and ODBC drivers support different types of authentication methods, such as personal access tokens, username and password, Azure Active Directory, or IAM credentials  . Depending on the database and the driver, we need to configure the connection string and the driver properties accordingly  .
- Session tracking is a mechanism to maintain the state of a user across multiple requests in a web application. Session tracking can be implemented using various techniques, such as cookies, URL rewriting, hidden form fields, or HttpSession objects.
- HttpSession is a Java class that provides a way to store and retrieve information about a user's session on the server side. HttpSession objects are created by the servlet container when a user first accesses the web application and are associated with a unique session ID.
- To use HttpSession for session tracking, we need to do the following steps:
  - Import the javax.servlet.http.HttpSession package in the servlet class.
  - Call the request.getSession() method to get the HttpSession object for the current user. If the user does not have a session, a new one is created and returned.
  - Use the setAttribute(String name, Object value) method to store information about the user in the session object, such as the user name, role, preferences, etc.
  - Use the getAttribute(String name) method to retrieve information about the user from the session object.
  - Use the invalidate() method to terminate the session and remove all the information stored in it.
- A possible pseudocode for authenticating the user using JDBC, ODBC, and session tracking is as follows:

```java
// Import the required packages
import java.sql.*;
import javax.servlet.http.*;

// Define the database connection parameters
String driver = "com.databricks.jdbc.Driver"; // The JDBC driver class name
String url = "jdbc:redshift:iam://<cluster-name>.<region>.<account-id>.redshift.amazonaws.com:5439/<database-name>"; // The JDBC connection string
String user = "<user-name>"; // The database user name
String password = "<password>"; // The database password

// Define the SQL query to validate the user credentials
String query = "SELECT * FROM users WHERE username = ? AND password = ?";

// Get the user input from the login form
String username = request.getParameter("username");
String password = request.getParameter("password");

// Create a connection object
Connection conn = null;

// Create a statement object
PreparedStatement stmt = null;

// Create a result set object
ResultSet rs = null;

// Create a session object
HttpSession session = null;

try {
  // Load the driver class
  Class.forName(driver);

  // Establish the connection to the database
  conn = DriverManager.getConnection(url, user, password);

  // Prepare the statement with the query and the user input
  stmt = conn.prepareStatement(query);
  stmt.setString(1, username);
  stmt.setString(2, password);

  // Execute the query and get the result set
  rs = stmt.executeQuery();

  // Check if the result set is not empty, meaning the user credentials are valid
  if (rs.next()) {
    // Get the session object for the current user
    session = request.getSession();

    // Store the user name in the session object
    session.setAttribute("username", username);

    // Redirect the user to the welcome page
    response.sendRedirect("welcome.jsp");
  } else {
    // Display an error message to the user
    response.getWriter().println("Invalid user name or password");
  }
} catch (Exception e) {
  // Handle any exceptions
  e.printStackTrace();
} finally {
  // Close the resources
  if (rs != null) {
    rs.close();
  }
  if (stmt != null)

```




# Design and implement a simple shopping cart example with session tracking API

- A shopping cart is a web application that allows users to browse, select, and purchase items from an online store.
- A session tracking API is a way of maintaining the state of a user's interaction with the web application across multiple requests and responses.
- Session tracking is needed to identify which user's cart the items are to be added or removed, and to calculate the total amount and payment details.
- There are different methods of session tracking, such as cookies, URL rewriting, hidden form fields, and HttpSession objects.
- In this example, we will use the HttpSession object to store the user's cart information on the server side, and use cookies to store the session ID on the client side.
- The HttpSession object is a Java class that provides methods to create, access, and manipulate session data. It is created by the servlet container when a user first requests a web resource, and is associated with a unique session ID.
- The session ID is a string that identifies the user's session. It is sent by the server to the client as a cookie, and is returned by the client in subsequent requests. The server uses the session ID to retrieve the corresponding HttpSession object.
- The cookie is a small piece of data that is stored by the web browser on the user's device. It has a name, a value, an expiration date, a domain, and a path. The cookie can only be accessed by the web server that created it, and by the web resources that match its domain and path.
- The following steps describe how to design and implement a simple shopping cart example with session tracking API:

  1. Create a web page that displays the list of items available for purchase, along with their prices and an option to add them to the cart. This page can be a static HTML file or a dynamic JSP file that retrieves the items from a database using JDBC or ODBC.
  2. Create a servlet that handles the request to add an item to the cart. This servlet should do the following:
    - Get the HttpSession object associated with the current request, or create a new one if it does not exist.
    - Get the cart attribute from the HttpSession object, or create a new one if it does not exist. The cart attribute can be a Java collection, such as an ArrayList or a HashMap, that stores the items and their quantities.
    - Get the item ID and quantity from the request parameters, and add them to the cart attribute.
    - Set the cart attribute back to the HttpSession object.
    - Redirect the user back to the web page that displays the list of items.
  3. Create another web page that displays the contents of the user's cart, along with the total amount and an option to checkout. This page can also be a static HTML file or a dynamic JSP file that retrieves the cart attribute from the HttpSession object.
  4. Create another servlet that handles the request to checkout. This servlet should do the following:
    - Get the HttpSession object associated with the current request, and invalidate it to end the session and delete the cart attribute.
    - Get the payment details from the request parameters, and process the payment using a third-party service or a mock service.
    - Display a confirmation message to the user, and thank them for their purchase.

