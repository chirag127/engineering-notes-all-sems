# Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab

### Write programs using JavaScript for Web Page to display browsers information

1. One way to display browser information using JavaScript is by accessing the `navigator` object. This object contains information about the user's browser and operating system.

```javascript
document.write("Browser CodeName: " + navigator.appCodeName);
document.write("<br>");
document.write("Browser Name: " + navigator.appName);
document.write("<br>");
document.write("Browser Version: " + navigator.appVersion);
document.write("<br>");
document.write("Cookies Enabled: " + navigator.cookieEnabled);
document.write("<br>");
document.write("Platform: " + navigator.platform);
document.write("<br>");
document.write("User-agent header: " + navigator.userAgent);
```

2. Another way to display browser information is by using the `screen` object. This object contains information about the user's screen, such as its width, height, and color depth.

```javascript
document.write("Screen Width: " + screen.width);
document.write("<br>");
document.write("Screen Height: " + screen.height);
document.write("<br>");
document.write("Screen Color Depth: " + screen.colorDepth);
document.write("<br>");
document.write("Screen Pixel Depth: " + screen.pixelDepth);
```

These are just two examples of how you can use JavaScript to display browser information on a web page. There are many other properties and methods available in the `navigator` and `screen` objects that you can use to gather and display information about the user's browser and screen.