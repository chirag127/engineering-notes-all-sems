### Object Models in Web Page Designing

- Object models in web page designing are a way of organizing and representing the web elements and their interactions on a web page using classes and methods.
- One of the most popular object models in web page designing is the **Page Object Model (POM)**, which is widely used in test automation frameworks such as Selenium  .
- The main idea of POM is to create a separate class for each web page in the application, and store all the web elements and their methods in that class. This way, the test scripts can access the web elements and their actions through the page objects, without directly interacting with the HTML code of the web page.
- The advantages of POM are:
  - It reduces code duplication and improves code reusability.
  - It makes the test scripts more readable and maintainable.
  - It enhances the modularity and scalability of the test framework.
  - It facilitates parallel testing and cross-browser testing.
  - It supports the separation of concerns principle, where the test logic is separated from the web page structure.
- The disadvantages of POM are:
  - It requires more effort and time to design and implement the page objects.
  - It may increase the complexity of the test framework if not designed properly.
  - It may not be suitable for dynamic web pages that change frequently.
- An example of POM in Selenium and Java is:

```java
// LoginPage.java
// This class represents the login page of the application
public class LoginPage {

  // Declare the web elements as private variables
  private WebDriver driver;
  private By username = By.id("username");
  private By password = By.id("password");
  private By loginButton = By.id("login");

  // Create a constructor that takes the driver as a parameter
  public LoginPage(WebDriver driver) {
    this.driver = driver;
  }

  // Define the methods to interact with the web elements
  public void enterUsername(String user) {
    driver.findElement(username).sendKeys(user);
  }

  public void enterPassword(String pass) {
    driver.findElement(password).sendKeys(pass);
  }

  public HomePage clickLoginButton() {
    driver.findElement(loginButton).click();
    return new HomePage(driver);
  }
}

// HomePage.java
// This class represents the home page of the application
public class HomePage {

  // Declare the web elements as private variables
  private WebDriver driver;
  private By welcomeMessage = By.id("welcome");
  private By logoutButton = By.id("logout");

  // Create a constructor that takes the driver as a parameter
  public HomePage(WebDriver driver) {
    this.driver = driver;
  }

  // Define the methods to interact with the web elements
  public String getWelcomeMessage() {
    return driver.findElement(welcomeMessage).getText();
  }

  public LoginPage clickLogoutButton() {
    driver.findElement(logoutButton).click();
    return new LoginPage(driver);
  }
}

// LoginTest.java
// This class contains the test scripts that use the page objects
public class LoginTest {

  // Declare the driver and the page objects as private variables
  private WebDriver driver;
  private LoginPage loginPage;
  private HomePage homePage;

  // Initialize the driver and the page objects before each test
  @BeforeMethod
  public void setUp() {
    driver = new ChromeDriver();
    driver.get("https://example.com/login");
    loginPage = new LoginPage(driver);
  }

  // Write the test cases using the page objects and their methods
  @Test
  public void testLoginSuccess() {
    loginPage.enterUsername("testuser");
    loginPage.enterPassword("testpass");
    homePage = loginPage.clickLoginButton();
    Assert.assertEquals(homePage.getWelcomeMessage(), "Welcome, testuser!");
  }

  @Test
  public void testLogoutSuccess() {
    loginPage.enterUsername("testuser");
    loginPage.enterPassword("testpass");
    homePage = loginPage.clickLoginButton();
    loginPage = homePage.clickLogoutButton();
    Assert.assertTrue(driver.getTitle().contains("Login"));
  }

  // Quit the driver after each test
  @AfterMethod
  public void tearDown() {
    driver.quit();
  }
}
```

- Another way of implementing POM is using the **Page Factory** pattern, which is a built-in feature of Selenium that helps to initialize the web elements using annotations .
- The advantages of Page Factory are:
  - It simplifies the declaration and initialization of the web elements using the @