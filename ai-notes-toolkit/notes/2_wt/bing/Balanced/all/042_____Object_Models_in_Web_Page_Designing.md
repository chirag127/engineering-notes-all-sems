### Object Models in Web Page Designing

- Object models in web page designing are a way of organizing and representing the web elements and their interactions on a web page using classes and methods.
- One of the most popular object models in web page designing is the **Page Object Model (POM)**, which is a design pattern used in test automation frameworks such as Selenium  .
- In POM, each web page of an application is represented by a corresponding class, which contains the web elements as variables and the interactions as methods.
- For example, consider a web page that has a login form with username, password and submit button. The corresponding class for this web page could look something like this:

```java
public class LoginPage {

  // Web elements as variables
  private WebElement username;
  private WebElement password;
  private WebElement submit;

  // Constructor to initialize the web elements
  public LoginPage(WebDriver driver) {
    username = driver.findElement(By.id("username"));
    password = driver.findElement(By.id("password"));
    submit = driver.findElement(By.id("submit"));
  }

  // Methods to interact with the web elements
  public void enterUsername(String user) {
    username.sendKeys(user);
  }

  public void enterPassword(String pass) {
    password.sendKeys(pass);
  }

  public void clickSubmit() {
    submit.click();
  }

  public HomePage login(String user, String pass) {
    enterUsername(user);
    enterPassword(pass);
    clickSubmit();
    return new HomePage(driver);
  }
}
```

- The advantage of using POM is that it reduces code duplication and improves test maintenance by separating the test logic from the web elements. If there is any change in the web page, only the corresponding class needs to be updated, not the test cases.
- Another advantage of using POM is that it makes the test cases more readable and understandable by using meaningful method names and parameters.
- A variation of POM is the **Page Factory** pattern, which is a way of initializing the web elements using annotations instead of explicit findElement() calls .
- For example, the same login page class could be written using Page Factory as follows:

```java
public class LoginPage {

  // Web elements as variables with annotations
  @FindBy(id = "username")
  private WebElement username;

  @FindBy(id = "password")
  private WebElement password;

  @FindBy(id = "submit")
  private WebElement submit;

  // Constructor to initialize the web elements using Page Factory
  public LoginPage(WebDriver driver) {
    PageFactory.initElements(driver, this);
  }

  // Methods to interact with the web elements
  public void enterUsername(String user) {
    username.sendKeys(user);
  }

  public void enterPassword(String pass) {
    password.sendKeys(pass);
  }

  public void clickSubmit() {
    submit.click();
  }

  public HomePage login(String user, String pass) {
    enterUsername(user);
    enterPassword(pass);
    clickSubmit();
    return new HomePage(driver);
  }
}
```

- The advantage of using Page Factory is that it simplifies the code and avoids the risk of stale element references by initializing the web elements when they are accessed.
- A disadvantage of using Page Factory is that it may slow down the execution time by initializing all the web elements at once, even if they are not needed.
- A mnemonic to remember the difference between POM and Page Factory is: **POM** uses **P**lain **O**ld **M**ethods to find web elements, while **Page Factory** uses **F**ancy **A**nnotations to initialize web elements.