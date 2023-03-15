Hello, I am Sydney, your AI assistant. I can help you with your query.

To write programs using JavaScript for web page to display browser information, you need to use the `window.navigator` object, which contains various properties and methods that provide information about the visitor's browser, such as name, version, platform, cookies, etc.  

Here are some examples of JavaScript programs to display browser information:

- To display the browser name and version, you can use the `navigator.appName` and `navigator.appVersion` properties, and write them to the document using the `document.write()` method. For example:

```javascript
// Display browser name and version
document.write("Browser name: " + navigator.appName + "<br>");
document.write("Browser version: " + navigator.appVersion + "<br>");
```

- To display the browser code name, you can use the `navigator.appCodeName` property, which is usually "Mozilla" for most browsers. For example:

```javascript
// Display browser code name
document.write("Browser code name: " + navigator.appCodeName + "<br>");
```

- To display the browser user agent, you can use the `navigator.userAgent` property, which is a string that identifies the browser to the web server. For example:

```javascript
// Display browser user agent
document.write("Browser user agent: " + navigator.userAgent + "<br>");
```

- To display the browser platform, you can use the `navigator.platform` property, which is the operating system or device the browser is running on. For example:

```javascript
// Display browser platform
document.write("Browser platform: " + navigator.platform + "<br>");
```

- To display the browser cookies, you can use the `navigator.cookieEnabled` property, which is a boolean value that indicates whether the browser supports cookies or not. For example:

```javascript
// Display browser cookies
document.write("Browser cookies: " + navigator.cookieEnabled + "<br>");
```

- To display the browser online status, you can use the `navigator.onLine` property, which is a boolean value that indicates whether the browser is connected to the network or not. For example:

```javascript
// Display browser online status
document.write("Browser online status: " + navigator.onLine + "<br>");
```

These are some of the basic programs to display browser information using JavaScript. You can also use other properties and methods of the `window.navigator` object to get more information, such as language, geolocation, plugins, etc. 

I hope this helps you with your notes. If you have any further questions, please let me know.😊