### Object Models in Web Page Designing

An object model is a way of representing the components and interactions of a web page or application in a structured and reusable manner. An object model can help to improve the maintainability, readability, and reliability of the code that interacts with the web page or application.

One of the most common object models used in web page designing is the Page Object Model (POM). The POM is a design pattern that creates an object repository for all the web UI elements and their corresponding actions and attributes. The POM separates the test logic from the UI elements, making the code more modular and easier to update.

The POM consists of two main components: the page classes and the test classes. The page classes are responsible for storing the web elements and their methods for each web page in the application. The test classes are responsible for performing the test scenarios using the web elements and methods from the page classes.

An example of a page class in JavaScript using Selenium WebDriver is:

```javascript
// Page class for the home page of a website
class HomePage {
  // Constructor to initialize the web driver and the web elements
  constructor(driver) {
    this.driver = driver;
    this.searchBox = driver.findElement(By.id("search-box"));
    this.searchButton = driver.findElement(By.id("search-button"));
    this.logo = driver.findElement(By.id("logo"));
  }

  // Method to enter a search query in the search box
  enterSearchQuery(query) {
    this.searchBox.sendKeys(query);
  }

  // Method to click on the search button
  clickSearchButton() {
    this.searchButton.click();
  }

  // Method to verify that the logo is displayed
  verifyLogo() {
    return this.logo.isDisplayed();
  }
}
```

An example of a test class in JavaScript using Mocha and Chai is:

```javascript
// Test class for the home page of a website
const { expect } = require("chai");
const { Builder } = require("selenium-webdriver");
const HomePage = require("./HomePage");

describe("Home page tests", function () {
  // Initialize the web driver and the home page object before each test
  beforeEach(async function () {
    this.driver = await new Builder().forBrowser("chrome").build();
    this.homePage = new HomePage(this.driver);
    await this.driver.get("https://www.example.com");
  });

  // Close the web driver after each test
  afterEach(async function () {
    await this.driver.quit();
  });

  // Test case to verify that the logo is displayed on the home page
  it("should display the logo on the home page", async function () {
    const logoDisplayed = await this.homePage.verifyLogo();
    expect(logoDisplayed).to.be.true;
  });

  // Test case to verify that the search functionality works on the home page
  it("should perform a search on the home page", async function () {
    await this.homePage.enterSearchQuery("selenium");
    await this.homePage.clickSearchButton();
    const currentUrl = await this.driver.getCurrentUrl();
    expect(currentUrl).to.contain("selenium");
  });
});
```

The POM is not the only object model that can be used in web page designing. There are other design patterns and frameworks that can also help to create robust and scalable code for web UI automation. Some of them are:

- ScreenPlay Model: This is a design pattern that uses actors, tasks, abilities, and questions to model the interactions between the user and the web page or application. The ScreenPlay Model aims to overcome some of the limitations of the POM, such as code duplication and high coupling.
- Page Factory: This is a framework that provides a way to initialize the web elements of a page class using annotations. The Page Factory helps to reduce the boilerplate code and improve the readability of the page classes.
- Robot Framework: This is a generic test automation framework that supports keyword-driven, data-driven, and behavior-driven approaches. The Robot Framework can be used to create high-level test cases using keywords that abstract the low-level details of the web UI elements and actions.