Hello, I am Sydney, your AI assistant. I can help you with your query.

To write programs using JavaScript for web page to display browser information, you can use the following steps:

- Use the `window.navigator` object to access the properties and methods of the browser, such as `appName`, `appVersion`, `userAgent`, `platform`, `cookieEnabled`, etc.    
- Use the `document.write()` method to display the browser information on the web page. 
- Use the `userAgent.match()` method to detect the browser name by matching it with a regular expression. 
- Use the `indexOf()` method to find the position of a substring in the `userAgent` property. 
- Use the `parseFloat()` and `parseInt()` methods to extract the browser version from the `appVersion` property. 

Here is an example of a JavaScript program that displays the browser name and version on the web page:

```javascript
// Get the user agent string
var userAgent = window.navigator.userAgent;

// Declare variables for browser name and version
var browserName, browserVersion;

// Detect the browser name
if (userAgent.match(/Opera|OPR\//)) {
  browserName = 'Opera';
}
else if (userAgent.match(/Edge/)) {
  browserName = 'Edge';
}
else if (userAgent.match(/Chrome/)) {
  browserName = 'Chrome';
}
else if (userAgent.match(/Safari/)) {
  browserName = 'Safari';
}
else if (userAgent.match(/Firefox/)) {
  browserName = 'Firefox';
}
else if (userAgent.match(/MSIE|Trident/)) {
  browserName = 'Internet Explorer';
}
else {
  browserName = 'Unknown';
}

// Detect the browser version
var verOffset, index;
if ((verOffset = userAgent.indexOf('OPR/')) != -1) {
  // Opera
  browserVersion = userAgent.substring(verOffset + 4);
}
else if ((verOffset = userAgent.indexOf('Edge/')) != -1) {
  // Edge
  browserVersion = userAgent.substring(verOffset + 5);
}
else if ((verOffset = userAgent.indexOf('Chrome/')) != -1) {
  // Chrome
  browserVersion = userAgent.substring(verOffset + 7);
}
else if ((verOffset = userAgent.indexOf('Safari/')) != -1) {
  // Safari
  browserVersion = userAgent.substring(verOffset + 7);
  if ((index = userAgent.indexOf('Version/')) != -1) {
    browserVersion = userAgent.substring(index + 8);
  }
}
else if ((verOffset = userAgent.indexOf('Firefox/')) != -1) {
  // Firefox
  browserVersion = userAgent.substring(verOffset + 8);
}
else if ((verOffset = userAgent.indexOf('MSIE')) != -1) {
  // Internet Explorer
  browserVersion = userAgent.substring(verOffset + 5);
}
else if (userAgent.indexOf('Trident/') != -1) {
  // Internet Explorer 11
  browserVersion = userAgent.substring(userAgent.indexOf('rv:') + 3);
}
else {
  // Other browsers
  browserVersion = 'Unknown';
}

// Display the browser name and version on the web page
document.write('Browser name: ' + browserName + '<br>');
document.write('Browser version: ' + browserVersion + '<br>');
```