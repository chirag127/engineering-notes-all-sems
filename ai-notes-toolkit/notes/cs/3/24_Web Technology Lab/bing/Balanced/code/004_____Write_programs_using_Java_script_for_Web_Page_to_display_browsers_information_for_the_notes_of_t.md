# Write programs using JavaScript for Web Page to display browsers information

JavaScript is a scripting language that can be used to create dynamic and interactive web pages. One of the features of JavaScript is that it can access the information about the visitor's browser, such as the name, version, platform, and user agent. This information can be useful for various purposes, such as customizing the web page content, detecting browser compatibility, or performing analytics.

There are different ways to write programs using JavaScript for web page to display browsers information. Here are some of the common methods:

- **Using the window.navigator object**: The window.navigator object is a built-in object that contains the information about the visitor's browser. Some of the properties of this object are:

  - `navigator.appName`: The name of the browser, such as Netscape or Microsoft Internet Explorer.
  - `navigator.appVersion`: The version of the browser, such as 5.0 or 11.0.
  - `navigator.platform`: The operating system of the browser, such as Win32 or Linux.
  - `navigator.userAgent`: The user agent string of the browser, which contains more detailed information about the browser and its features.

  To use the window.navigator object, we can write a simple HTML page with a script tag that displays the browser information in an alert box or on the web page itself. For example:

  ```html
  <html>
  <head>
    <title>Browser Information</title>
  </head>
  <body>
    <script>
      // Display the browser information in an alert box
      alert(
        "Browser Name: " +
          navigator.appName +
          "\n" +
          "Browser Version: " +
          navigator.appVersion +
          "\n" +
          "Browser Platform: " +
          navigator.platform +
          "\n" +
          "Browser User Agent: " +
          navigator.userAgent
      );

      // Display the browser information on the web page
      document.write(
        "<h1>Browser Information</h1>" +
          "<p>Browser Name: " +
          navigator.appName +
          "</p>" +
          "<p>Browser Version: " +
          navigator.appVersion +
          "</p>" +
          "<p>Browser Platform: " +
          navigator.platform +
          "</p>" +
          "<p>Browser User Agent: " +
          navigator.userAgent +
          "</p>"
      );
    </script>
  </body>
  </html>
  ```

  However, using the window.navigator object has some limitations and drawbacks. For instance:

  - Different browsers can use the same name, such as Netscape or Mozilla, which can cause confusion or false detection.
  - The navigator data can be changed by the browser owner or the user, which can make it unreliable or inaccurate.
  - Some browsers misidentify themselves to bypass site tests or to mimic other browsers, which can lead to incorrect results.

- **Using a detection library**: A detection library is a third-party JavaScript library that can help to detect the browser and its features more accurately and reliably. One of the popular detection libraries is Bowser, which can parse the user agent string and provide a simple and consistent API to access the browser information. To use Bowser, we need to include the library in our HTML page and then use its methods and properties to get the browser information. For example:

  ```html
  <html>
  <head>
    <title>Browser Information</title>
    <!-- Include the Bowser library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bowser/2.11.0/bowser.min.js"></script>
  </head>
  <body>
    <script>
      // Get the browser information using Bowser
      var browser = bowser.getParser(window.navigator.userAgent);

      // Display the browser information in an alert box
      alert(
        "Browser Name: " +
          browser.getBrowserName() +
          "\n" +
          "Browser Version: " +
          browser.getBrowserVersion() +
          "\n" +
          "Browser Platform: " +
          browser.getOSName() +
          "\n" +
          "Browser User Agent: " +
          browser.getUA()
      );

      // Display the browser information on the web page
      document.write(
        "<h1>Browser Information</h1>" +
          "<p>Browser Name: " +
          browser.getBrowserName() +
          "</p>" +
          "<p>Browser Version: " +
          browser.getBrowserVersion() +
          "</p>" +
          "<p

```
