### Object Models for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

- An object model is a visual representation of a system's objects, actions, and associated attributes.
- An object model can help to create a consistent and intuitive user interface for web pages, by defining the elements and interactions of each page.
- One of the most popular object models in web page designing is the Page Object Model (POM), which is a design pattern used in test automation that creates an object repository for web UI elements  .
- The advantages of the POM are that it reduces code duplication, improves test maintenance, enhances readability, and facilitates reusability  .
- The basic idea of the POM is to divide the application into modules/pages/panels as needed and abstracts object identification and user actions into methods or functions of the corresponding class .
- For example, consider a web page that has a login form with two input fields (username and password) and a submit button. The POM for this page would look something like this:

```python
# Page class for the login page
class LoginPage:

    # Constructor that takes a driver object as an argument
    def __init__(self, driver):
        self.driver = driver

        # Web elements of the login page
        self.username = driver.find_element_by_id("username")
        self.password = driver.find_element_by_id("password")
        self.submit = driver.find_element_by_id("submit")

    # Methods or functions that perform user actions on the web elements
    def enter_username(self, user):
        self.username.send_keys(user)

    def enter_password(self, pwd):
        self.password.send_keys(pwd)

    def click_submit(self):
        self.submit.click()
```

- The POM can be further enhanced by using the Page Factory, which is a way of initializing the web elements using annotations or decorators .
- The Page Factory can help to avoid using the `find_element` methods repeatedly and make the code more concise and elegant .
- For example, using the Page Factory, the POM for the login page would look something like this:

```python
# Page class for the login page with Page Factory
class LoginPage:

    # Constructor that takes a driver object as an argument
    def __init__(self, driver):
        self.driver = driver
        PageFactory.init_elements(driver, self)

        # Web elements of the login page with annotations
        @FindBy(id = "username")
        self.username = None

        @FindBy(id = "password")
        self.password = None

        @FindBy(id = "submit")
        self.submit = None

    # Methods or functions that perform user actions on the web elements
    def enter_username(self, user):
        self.username.send_keys(user)

    def enter_password(self, pwd):
        self.password.send_keys(pwd)

    def click_submit(self):
        self.submit.click()
```

- The POM is not the only object model that can be used in web page designing. There are other design patterns and components that can be applied, such as the ScreenPlay Model, the Page Component Model, the Data Driven Model, etc.
- The choice of the object model depends on the complexity, scalability, and maintainability of the web application and the testing framework.
- The object model is a powerful tool that can help to design and test web pages more efficiently and effectively.