### Write programs using JavaScript for Web Page to display browsers information

JavaScript is a scripting language that can run in a web browser and manipulate the HTML elements and events. JavaScript can also access some information about the browser and the operating system of the user through the `window.navigator` object. This object has various properties and methods that can be used to get browser details, such as the name, version, platform, user agent, cookies, etc.

Here are some examples of JavaScript programs that can display browser information on a web page:

- To display the browser name and version, we can use the `navigator.appName` and `navigator.appVersion` properties. For example:

```javascript
// Get the browser name and version
var browserName = navigator.appName;
var browserVersion = navigator.appVersion;

// Display the browser name and version on the web page
document.write("Browser name: " + browserName + "<br>");
document.write("Browser version: " + browserVersion + "<br>");
```

- To display the browser code name, we can use the `navigator.appCodeName` property. For example:

```javascript
// Get the browser code name
var browserCodeName = navigator.appCodeName;

// Display the browser code name on the web page
document.write("Browser code name: " + browserCodeName + "<br>");
```

- To display the browser user agent, we can use the `navigator.userAgent` property. This property contains a string that identifies the browser, the operating system, and other information. For example:

```javascript
// Get the browser user agent
var browserUserAgent = navigator.userAgent;

// Display the browser user agent on the web page
document.write("Browser user agent: " + browserUserAgent + "<br>");
```

- To display the browser platform, we can use the `navigator.platform` property. This property returns the operating system or the device that the browser is running on. For example:

```javascript
// Get the browser platform
var browserPlatform = navigator.platform;

// Display the browser platform on the web page
document.write("Browser platform: " + browserPlatform + "<br>");
```

- To display the browser cookie status, we can use the `navigator.cookieEnabled` property. This property returns a boolean value that indicates whether the browser supports cookies or not. For example:

```javascript
// Get the browser cookie status
var browserCookieEnabled = navigator.cookieEnabled;

// Display the browser cookie status on the web page
document.write("Browser cookie enabled: " + browserCookieEnabled + "<br>");
```

These are some of the basic programs that can display browser information using JavaScript. There are more properties and methods in the `window.navigator` object that can be used to get more details about the browser, such as the language, the online status, the geolocation, etc. You can refer to the following sources for more information:

: How to Get browser details through JavaScript - PHPTPOINT
: How to detect browser in JavaScript [Chrome, Firefox ... - Codepedia
: JavaScript Window Navigator - W3Schools
: How to detect my browser version and operating system using JavaScript ... - Stack Overflow