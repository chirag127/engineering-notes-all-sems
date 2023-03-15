Object Models in Web Page Designing are a way of representing the structure and behavior of web pages using classes, objects, methods, and attributes. They help to create an object repository for all web UI elements and reduce code duplication and improve test maintenance. One of the most common design patterns for Object Models in Web Page Designing is the Page Object Model (POM), which creates a separate class for each web page and defines the web elements and methods for that page. Here is a possible ascii diagram for the Page Object Model:

### Object Models in Web Page Designing

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  HomePage       |       |  LoginPage      |       |  ProfilePage    |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
| - homeLink      |       | - usernameField |       | - profilePic    |
| - loginLink     |       | - passwordField |       | - editButton    |
| - searchField   |       | - loginButton   |       | - logoutButton  |
| - searchButton  |       |                 |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
| + openHomePage()|       | + openLoginPage()|      | + openProfilePage()|
| + clickLoginLink()|     | + enterUsername()|      | + clickEditButton()|
| + enterSearchText()|    | + enterPassword()|      | + clickLogoutButton()|
| + clickSearchButton()|  | + clickLoginButton()|   |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```