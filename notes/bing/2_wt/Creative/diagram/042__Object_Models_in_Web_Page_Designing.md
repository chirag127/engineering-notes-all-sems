Object Models in Web Page Designing are a way of representing the web elements and interactions of a web page as classes, variables and methods. They are used to create an object repository and to improve the reusability and maintainability of the code. One of the most common design patterns for Object Models in Web Page Designing is the Page Object Model (POM), which divides the application into modules or pages and abstracts the web elements and actions of each page as a separate class.

The following diagram illustrates the basic architecture of a Page Object Model in Web Page Designing using ASCII art:

### Object Models in Web Page Designing

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Test Case    |----->|   Page Class   |----->|   Web Page     |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
| - Test Steps   |      | - Web Elements |      | - HTML Elements|
| - Test Data    |      | - Page Methods |      | - CSS Styles   |
| - Assertions   |      |                |      | - JavaScript   |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```