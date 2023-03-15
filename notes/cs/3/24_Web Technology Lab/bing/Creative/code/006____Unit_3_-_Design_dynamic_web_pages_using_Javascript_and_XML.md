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