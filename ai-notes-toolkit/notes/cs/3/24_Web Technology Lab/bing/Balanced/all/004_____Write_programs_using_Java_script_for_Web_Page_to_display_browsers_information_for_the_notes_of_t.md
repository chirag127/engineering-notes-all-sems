# Write programs using JavaScript for Web Page to display browsers information

JavaScript is a scripting language that can be used to create dynamic and interactive web pages. JavaScript can access the browser's information through the `window.navigator` object, which contains properties and methods that provide information about the browser and the operating system.

Some of the common properties of the `window.navigator` object are:

- `navigator.appName`: The name of the browser application, such as "Netscape" or "Microsoft Internet Explorer".
- `navigator.appVersion`: The version of the browser application, such as "5.0" or "4.0".
- `navigator.userAgent`: The user agent string that identifies the browser and the operating system, such as "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36".
- `navigator.platform`: The platform on which the browser is running, such as "Win32" or "Linux x86_64".
- `navigator.language`: The preferred language of the user, such as "en-US" or "fr-FR".
- `navigator.cookieEnabled`: A boolean value that indicates whether cookies are enabled in the browser or not.

To display the browser's information on a web page, we can use the `document.write()` method, which writes HTML expressions or JavaScript code to a document. For example, the following program displays the browser's name, version, user agent, platform, language, and cookie status on a web page:

```javascript
// Get the browser's information from the window.navigator object
var name = navigator.appName;
var version = navigator.appVersion;
var userAgent = navigator.userAgent;
var platform = navigator.platform;
var language = navigator.language;
var cookieEnabled = navigator.cookieEnabled;

// Write the browser's information to the document
document.write("<h1>Browser Information</h1>");
document.write("<p>Name: " + name + "</p>");
document.write("<p>Version: " + version + "</p>");
document.write("<p>User Agent: " + userAgent + "</p>");
document.write("<p>Platform: " + platform + "</p>");
document.write("<p>Language: " + language + "</p>");
document.write("<p>Cookies Enabled: " + cookieEnabled + "</p>");
```

The output of the program may look something like this:

![Browser Information](https://i.imgur.com/0w0yR8c.png)

Note that the information from the `window.navigator` object can be misleading or inaccurate, as different browsers may use the same name, change the data, or misidentify themselves to bypass site tests. Therefore, it is not recommended to use the `window.navigator` object to detect browser versions or features. Instead, it is better to use a detection library such as Bowser, or check for the support of specific features using feature detection techniques.