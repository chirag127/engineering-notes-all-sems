### Write programs using Java script for Web Page to display browsers information for the notes of the Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab.

Web pages are viewed on a variety of web browsers, each with their own unique features and capabilities. As a web developer, it is important to be able to retrieve and display the browser information of visitors to your web page. This can be achieved using JavaScript, a popular programming language used for creating dynamic and interactive web pages. Here are some programs that can be used to display browser information on a web page:

1. Browser Name and Version:

```javascript
document.write("Browser name: " + navigator.appName + "<br>");
document.write("Browser version: " + navigator.appVersion + "<br>");
```

This program uses the `navigator` object in JavaScript to retrieve the name and version of the user's web browser. The information is then displayed on the web page using the `document.write()` method.

2. Browser Language:

```javascript
document.write("Browser language: " + navigator.language + "<br>");
```

This program retrieves the language of the user's web browser using the `navigator.language` property. The language information is then displayed on the web page using the `document.write()` method.

3. Operating System:

```javascript
document.write("Operating system: " + navigator.platform + "<br>");
```

This program retrieves the user's operating system using the `navigator.platform` property. The operating system information is then displayed on the web page using the `document.write()` method.

4. Screen Resolution:

```javascript
document.write("Screen resolution: " + screen.width + " x " + screen.height + "<br>");
```

This program retrieves the user's screen resolution using the `screen.width` and `screen.height` properties. The screen resolution information is then displayed on the web page using the `document.write()` method.

By using these programs, web developers can display browser information on their web pages, which can be useful for debugging and optimizing their web applications. It is important to note that these programs may not work on all web browsers, as some may not support certain properties and methods.