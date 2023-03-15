### Write programs using JavaScript for Web Page to display browsers information for the notes of the Unit 2 - Develop Java programs for window/web-based applications in the subject of Web Technology Lab

1. One way to display browser information using JavaScript is to use the `navigator` object, which contains information about the browser and the operating system.

```javascript
document.write("Browser CodeName: " + navigator.appCodeName + "<br>");
document.write("Browser Name: " + navigator.appName + "<br>");
document.write("Browser Version: " + navigator.appVersion + "<br>");
document.write("Cookies Enabled: " + navigator.cookieEnabled + "<br>");
document.write("Platform: " + navigator.platform + "<br>");
document.write("User-agent header: " + navigator.userAgent + "<br>");
```

2. Another way to display browser information is to use the `screen` object, which contains information about the user's screen.

```javascript
document.write("Screen Width: " + screen.width + "<br>");
document.write("Screen Height: " + screen.height + "<br>");
document.write("Available Screen Width: " + screen.availWidth + "<br>");
document.write("Available Screen Height: " + screen.availHeight + "<br>");
document.write("Color Depth: " + screen.colorDepth + "<br>");
document.write("Pixel Depth: " + screen.pixelDepth + "<br>");
```

3. It is also possible to display information about the user's location using the `geolocation` object.

```javascript
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
} else {
    document.write("Geolocation is not supported by this browser.<br>");
}

function showPosition(position) {
    document.write("Latitude: " + position.coords.latitude + "<br>");
    document.write("Longitude: " + position.coords.longitude + "<br>");
}
```
