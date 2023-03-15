# Write programs using JavaScript for Web Page to display browsers information

JavaScript is a scripting language that can be used to create dynamic and interactive web pages. One of the features of JavaScript is that it can access and manipulate the information about the visitor's browser, such as the name, version, platform, cookies, etc. This information can be useful for various purposes, such as customizing the web page content, detecting the browser compatibility, or collecting statistics.

To access the browser information, we can use the `window.navigator` object, which has several properties and methods that provide different details about the browser. Some of the common properties are:

- `navigator.appName`: The name of the browser, such as Netscape, Microsoft Internet Explorer, Opera, etc.
- `navigator.appVersion`: The version of the browser, such as 5.0, 4.0, etc.
- `navigator.userAgent`: The user agent string that identifies the browser, the operating system, and other information.
- `navigator.platform`: The platform on which the browser is running, such as Win32, Linux, Mac68K, etc.
- `navigator.cookieEnabled`: A boolean value that indicates whether the browser supports cookies or not.

To display the browser information on a web page, we can use the `document.write()` method, which writes a string of text to the document. For example, the following program displays the browser name and version on a web page:

```javascript
// Get the browser name and version
var browserName = navigator.appName;
var browserVersion = navigator.appVersion;

// Display the browser name and version on the web page
document.write("You are using " + browserName + " version " + browserVersion + ".");
```

The output of this program may look something like this:

You are using Netscape version 5.0 (Windows).

However, the `navigator.appName` and `navigator.appVersion` properties may not always give accurate or consistent results, as different browsers may use different names or versions for themselves. For example, most browsers use the internal code name Mozilla, and some browsers may append additional information to the version string. Therefore, a more reliable way to detect the browser name and version is to use the `navigator.userAgent` property, which contains a unique string that identifies the browser and other details.

To parse the user agent string and extract the browser name and version, we can use the `indexOf()` and `substring()` methods of the string object, which allow us to search and extract a part of a string. For example, the following program detects the browser name and version from the user agent string and displays them on a web page:

```javascript
// Get the user agent string
var userAgent = navigator.userAgent;

// Initialize the browser name and version variables
var browserName = "";
var browserVersion = "";

// Detect the browser name and version from the user agent string
if (userAgent.indexOf("Opera") != -1) {
  // Opera browser
  browserName = "Opera";
  browserVersion = userAgent.substring(userAgent.indexOf("OPR") + 4);
} else if (userAgent.indexOf("Edg") != -1) {
  // Edge browser
  browserName = "Microsoft Edge";
  browserVersion = userAgent.substring(userAgent.indexOf("Edg") + 4);
} else if (userAgent.indexOf("Chrome") != -1) {
  // Chrome browser
  browserName = "Google Chrome";
  browserVersion = userAgent.substring(userAgent.indexOf("Chrome") + 7);
} else if (userAgent.indexOf("Safari") != -1) {
  // Safari browser
  browserName = "Safari";
  browserVersion = userAgent.substring(userAgent.indexOf("Version") + 8);
} else if (userAgent.indexOf("Firefox") != -1) {
  // Firefox browser
  browserName = "Mozilla Firefox";
  browserVersion = userAgent.substring(userAgent.indexOf("Firefox") + 8);
} else if (userAgent.indexOf("MSIE") != -1) {
  // Internet Explorer browser
  browserName = "Microsoft Internet Explorer";
  browserVersion = userAgent.substring(userAgent.indexOf("MSIE") + 5);
} else {
  // Other browser
  browserName = "Unknown";
  browserVersion = "Unknown";
}

// Display the browser name and version on the web page
document.write("You are using " + browserName + " version " + browserVersion + ".");
```

The output of this program may look something like this:

You are using Google Chrome version 96.0.4664.110.

To display