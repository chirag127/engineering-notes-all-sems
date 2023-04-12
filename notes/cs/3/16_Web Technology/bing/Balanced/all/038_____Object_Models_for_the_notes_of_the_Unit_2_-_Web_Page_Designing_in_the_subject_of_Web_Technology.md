# Object Models for Web Page Designing

- Object models are design patterns that help in creating and maintaining web UI elements and interactions in a structured and reusable way.
- One of the most popular object models in web page designing is the **Page Object Model (POM)**, which is widely used in test automation frameworks such as Selenium.
- In POM, each web page of an application is represented by a corresponding **Page Class**, which contains the **locators** and **methods** for all the web elements and actions on that page.
- The locators are the identifiers that help in finding the web elements on the page, such as id, name, class, xpath, css selector, etc.
- The methods are the functions that perform the interactions with the web elements, such as clicking, typing, selecting, etc.
- The Page Classes are stored in a separate package or folder, which acts as an **Object Repository** for the web UI elements.
- The advantage of POM is that it reduces code duplication and improves test maintenance, as any change in the web page can be easily reflected in the Page Class, without affecting the test scripts that use the Page Class.
- Another advantage of POM is that it enhances the readability and reusability of the test scripts, as they can use the Page Class methods to perform the actions on the web page, instead of writing the locators and interactions in the test scripts.
- An example of a Page Class for a login page is:

```java
public class LoginPage {

  //Locators for web elements
  private static By username = By.id("username");
  private static By password = By.id("password");
  private static By loginButton = By.id("login");

  //Method to enter username
  public static void enterUsername(WebDriver driver, String user) {
    driver.findElement(username).sendKeys(user);
  }

  //Method to enter password
  public static void enterPassword(WebDriver driver, String pass) {
    driver.findElement(password).sendKeys(pass);
  }

  //Method to click login button
  public static void clickLoginButton(WebDriver driver) {
    driver.findElement(loginButton).click();
  }
}
```

- An example of a test script that uses the Page Class is:

```java
public class LoginTest {

  //Create a WebDriver object
  WebDriver driver = new ChromeDriver();

  //Navigate to the login page
  driver.get("https://example.com/login");

  //Use the Page Class methods to perform actions on the web page
  LoginPage.enterUsername(driver, "testuser");
  LoginPage.enterPassword(driver, "testpass");
  LoginPage.clickLoginButton(driver);

  //Verify the login result
  //...

  //Close the browser
  driver.quit();
}
```

- A variation of POM is the **Page Factory**, which is a way of initializing the web elements using annotations, instead of locators.
- The Page Factory uses the `@FindBy` annotation to locate the web elements, and the `PageFactory.initElements()` method to initialize them.
- The advantage of Page Factory is that it simplifies the Page Class code and avoids the use of `driver.findElement()` method for each web element.
- An example of a Page Class using Page Factory is:

```java
public class LoginPage {

  //Initialize the web elements using @FindBy annotation
  @FindBy(id = "username")
  private WebElement username;

  @FindBy(id = "password")
  private WebElement password;

  @FindBy(id = "login")
  private WebElement loginButton;

  //Constructor to initialize the web elements using PageFactory
  public LoginPage(WebDriver driver) {
    PageFactory.initElements(driver, this);
  }

  //Method to enter username
  public void enterUsername(String user) {
    username.sendKeys(user);
  }

  //Method to enter password
  public void enterPassword(String pass) {
    password.sendKeys(pass);
  }

  //Method to click login button
  public void clickLoginButton() {
    loginButton.click();
  }
}
```

- An example of a test script that uses the Page Class with Page Factory is:

```java
public class LoginTest {

  //Create a WebDriver object
  WebDriver driver = new ChromeDriver();

  //Navigate to the login page
  driver.get("https://example.com/login");

  //Create a Page Class object and initialize the web elements
  LoginPage loginPage = new LoginPage(driver);

  //Use the Page Class methods to perform actions on the web page
  loginPage.enterUsername("testuser");
  loginPage.enterPassword("testpass");
  loginPage.clickLoginButton();

  //

```
