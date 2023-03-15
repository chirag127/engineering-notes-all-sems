### Object Models in Web Page Designing

Object models are used in web page designing to represent the structure and behavior of the objects within a web page. An object model is a conceptual representation of the objects and their relationships within a system. In web page designing, object models are used to define the structure of the web page and the interactions between the different elements on the page.

Here is an example of how an object model can be used in web page designing:

```javascript
// Define a "Page" object
function Page(title, content) {
  this.title = title;
  this.content = content;
}

// Define a "Header" object
function Header(title) {
  this.title = title;
}

// Define a "Footer" object
function Footer(content) {
  this.content = content;
}

// Create a new "Page" object
var myPage = new Page("My Web Page", "Welcome to my web page!");

// Create a new "Header" object
var myHeader = new Header("My Web Page");

// Create a new "Footer" object
var myFooter = new Footer("Copyright 2023");

// Add the "Header" and "Footer" objects to the "Page" object
myPage.header = myHeader;
myPage.footer = myFooter;
```

In this example, we have defined three objects: `Page`, `Header`, and `Footer`. These objects represent the different elements of a web page. We have also created instances of these objects and added them to the `myPage` object to represent the structure of the web page.

This is just one way that object models can be used in web page designing. There are many other ways that object models can be used to represent the structure and behavior of web pages.