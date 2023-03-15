# Write programs using JavaScript for Web Page to display browsers information

JavaScript is a scripting or programming language that allows you to implement complex features on web pages. To display browser information, such as the name, version, platform, and user agent, we can use the `window.navigator` object. This object contains properties that help to identify a web browser. Here are some examples of JavaScript programs to display browser information on a web page:

## Example 1: Display browser name and version

```javascript
// Get the browser name and version from the navigator object
var browserName = navigator.appName;
var browserVersion = navigator.appVersion;

// Display the browser name and version on the web page
document.write("Browser name: " + browserName + "<br>");
document.write("Browser version: " + browserVersion + "<br>");
```

## Example 2: Display browser platform and user agent

```javascript
// Get the browser platform and user agent from the navigator object
var browserPlatform = navigator.platform;
var browserUserAgent = navigator.userAgent;

// Display the browser platform and user agent on the web page
document.write("Browser platform: " + browserPlatform + "<br>");
document.write("Browser user agent: " + browserUserAgent + "<br>");
```

## Example 3: Display browser cookies and online status

```javascript
// Get the browser cookies and online status from the navigator object
var browserCookies = navigator.cookieEnabled;
var browserOnline = navigator.onLine;

// Display the browser cookies and online status on the web page
document.write("Browser cookies: " + browserCookies + "<br>");
document.write("Browser online: " + browserOnline + "<br>");
```

These are some of the basic programs to display browser information using JavaScript. You can also use other properties and methods of the `window.navigator` object to get more information about the browser, such as the language, the geolocation, the device memory, etc. You can find more information and examples on the following websites:

: https://phptpoint.com/how-to-get-browser-details-through-javascript/
: http://www.alanwood.net/demos/browserinfo.html
: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript
: https://www.w3schools.com/js/js_window_navigator.asp
: https://www.w3schools.com/js/js_ex_browser.asp
: https://stackoverflow.com/questions/11219582/how-to-detect-my-browser-version-and-operating-system-using-javascript