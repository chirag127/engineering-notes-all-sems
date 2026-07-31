### Write programs using JavaScript for Web Page to display browsers information

#### Introduction
JavaScript is a programming language that is commonly used in web development. It can be used to create interactive elements on web pages, such as displaying information about the user's browser.

#### Displaying Browser Information
One way to display information about the user's browser is to use the `navigator` object. This object contains information about the browser and the user's operating system.

Here is an example of how to display the name and version of the user's browser using JavaScript:

```javascript
var browserName = navigator.appName;
var browserVersion = navigator.appVersion;

document.write("Browser name: " + browserName + "<br>");
document.write("Browser version: " + browserVersion);
```

This code uses the `appName` and `appVersion` properties of the `navigator` object to get the name and version of the user's browser. It then uses the `document.write()` method to display this information on the web page.

#### Conclusion
In conclusion, JavaScript can be used to display information about the user's browser on a web page. The `navigator` object provides access to this information, and its properties can be used to get specific details about the browser and the user's operating system. This can be useful for web developers who want to create web pages that are tailored to the user's browser and operating system.