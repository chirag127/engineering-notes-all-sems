### Write programs using JavaScript for Web Page to display browsers information

JavaScript is a powerful scripting language that can be used to create dynamic and interactive web pages. One of the ways to use JavaScript is to display information about the user's browser. Here are some examples of how to do this:

1. **Display the name and version of the browser:** You can use the `navigator` object to access information about the user's browser. The `navigator.appName` property returns the name of the browser, while the `navigator.appVersion` property returns the version of the browser. Here is an example of how to display this information on a web page:

```javascript
document.write("Browser name: " + navigator.appName + "<br>");
document.write("Browser version: " + navigator.appVersion);
```

2. **Display the user's screen resolution:** You can use the `screen` object to access information about the user's screen. The `screen.width` and `screen.height` properties return the width and height of the screen, respectively. Here is an example of how to display this information on a web page:

```javascript
document.write("Screen resolution: " + screen.width + "x" + screen.height);
```

3. **Display the user's operating system:** You can use the `navigator` object to access information about the user's operating system. The `navigator.platform` property returns the name of the user's operating system. Here is an example of how to display this information on a web page:

```javascript
document.write("Operating system: " + navigator.platform);
```

These are just a few examples of how to use JavaScript to display information about the user's browser on a web page. You can use these techniques to create dynamic and interactive web pages that provide useful information to the user.