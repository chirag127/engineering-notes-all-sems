### Write programs using JavaScript for Web Page to display browsers information

- JavaScript is a scripting language that can be used to create dynamic and interactive web pages.
- JavaScript can access the browser's information through the `window.navigator` object, which contains properties and methods related to the browser and the user agent.
- The `window.navigator` object can provide information such as the browser name, version, platform, language, online status, and more.
- However, the `window.navigator` object is not reliable for browser detection, as different browsers may use the same name, change the user agent data, or misidentify themselves to bypass site tests.
- Therefore, it is recommended to use other methods for browser detection, such as:
  - Extracting information from the user agent string and checking if it contains the browser's name. For example, to check for Chrome browsers:

  ```javascript
  if (navigator.userAgent.indexOf("Chrome") != -1) {
    // code for Chrome browser
  }
  ```

  - Using a detection library such as Bowser, which can parse the user agent string and return a detailed object with browser name, version, engine, platform, and more.
  - Detecting the CSS vendor prefix, which is a prefix added to some CSS properties to indicate the browser or engine that supports them. For example, to check for WebKit browsers:

  ```javascript
  if ("WebkitAppearance" in document.documentElement.style) {
    // code for WebKit browsers
  }
  ```

  - Browser duck typing, which is a technique of checking for unique features that each browser has. For example, to check for Internet Explorer browsers:

  ```javascript
  if ("ActiveXObject" in window) {
    // code for IE browsers
  }
  ```

- Here is an example of a simple web page that displays some browser information using the `window.navigator` object:

  ```html
  <html>
    <head>
      <title>Browser Information</title>
      <script>
        // function to display browser information
        function displayBrowserInfo() {
          // get the browser information elements
          var browserName = document.getElementById("browserName");
          var browserVersion = document.getElementById("browserVersion");
          var browserPlatform = document.getElementById("browserPlatform");
          var browserLanguage = document.getElementById("browserLanguage");
          var browserOnline = document.getElementById("browserOnline");

          // set the browser information elements
          browserName.textContent = navigator.appName;
          browserVersion.textContent = navigator.appVersion;
          browserPlatform.textContent = navigator.platform;
          browserLanguage.textContent = navigator.language;
          browserOnline.textContent = navigator.onLine ? "Yes" : "No";
        }
      </script>
    </head>
    <body onload="displayBrowserInfo()">
      <h1>Browser Information</h1>
      <p>
        Browser Name: <span id="browserName"></span>
      </p>
      <p>
        Browser Version: <span id="browserVersion"></span>
      </p>
      <p>
        Browser Platform: <span id="browserPlatform"></span>
      </p>
      <p>
        Browser Language: <span id="browserLanguage"></span>
      </p>
      <p>
        Browser Online: <span id="browserOnline"></span>
      </p>
    </body>
  </html>
  ```