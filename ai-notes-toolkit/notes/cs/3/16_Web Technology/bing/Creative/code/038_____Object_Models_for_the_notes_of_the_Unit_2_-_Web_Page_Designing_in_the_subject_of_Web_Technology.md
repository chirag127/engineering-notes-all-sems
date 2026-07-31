### Object Models for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

- An object model is a visual representation of a system's objects, actions, and associated attributes.
- An object model can be used, in conjunction with a design system, to create a consistent and intuitive user interface for web pages.
- One of the most popular object models in web page designing is the Page Object Model (POM), which is a design pattern used in test automation that creates an object repository for web UI elements  .
- In POM, each web page in the application is represented by a corresponding page class, which contains the web elements and the methods or functions to interact with them.
- The advantages of POM are:
  - It reduces code duplication and improves test maintenance by separating the test logic from the UI elements.
  - It enhances readability and reusability of the test code by using descriptive names for the web elements and methods.
  - It facilitates the implementation of the Page Factory pattern, which is a way of initializing the web elements using annotations.
- The disadvantages of POM are:
  - It requires more effort and time to create and maintain the page classes and the object repository.
  - It may not be suitable for dynamic web pages that change frequently or have complex UI elements.
  - It may not cover all the aspects of the web page functionality, such as navigation, validation, or error handling.