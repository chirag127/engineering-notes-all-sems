Hello, I am Sydney, your AI assistant. I can help you with your query.

Object Models in Web Page Designing are a way of representing the structure and behavior of web pages using classes, objects, methods, and attributes. They are used to create an object repository for all web UI elements and to reduce code duplication and improve test maintenance.

One of the most common Object Models in Web Page Designing is the Page Object Model (POM), which is a design pattern in Selenium that creates a corresponding page class for each web page in the application. The page class contains all the web elements and page methods of that web page.

Here is an example of a Page Object Model for a login page:

### Object Models in Web Page Designing

```
+---------------------+       +---------------------+
|                     |       |                     |
|   LoginPage         |       |   HomePage          |
|                     |       |                     |
+---------------------+       +---------------------+
|                     |       |                     |
| - username          |       | - welcomeMessage    |
| - password          |       | - logoutButton      |
| - loginButton       |       |                     |
|                     |       |                     |
+---------------------+       +---------------------+
|                     |       |                     |
| + enterUsername()   |       | + verifyWelcome()   |
| + enterPassword()   |       | + clickLogout()     |
| + clickLogin()      |       |                     |
|                     |       |                     |
+---------------------+       +---------------------+
```

The LoginPage class has three web elements: username, password, and loginButton. It also has three page methods: enterUsername(), enterPassword(), and clickLogin(). These methods are used to interact with the web elements and perform actions on the login page.

The HomePage class has two web elements: welcomeMessage and logoutButton. It also has two page methods: verifyWelcome() and clickLogout(). These methods are used to verify the welcome message and click the logout button on the home page.

The Page Object Model helps to separate the test logic from the web UI elements and makes the code more readable and maintainable. It also allows to reuse the same web elements and page methods across different test cases and scenarios.