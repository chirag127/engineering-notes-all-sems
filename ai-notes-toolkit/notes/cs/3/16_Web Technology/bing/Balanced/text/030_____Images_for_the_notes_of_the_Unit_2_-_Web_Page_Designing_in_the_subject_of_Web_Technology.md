### Images for the notes of the Unit 2 - Web Page Designing in the subject of Web Technology

- Web page designing is the process of creating and arranging the elements of a web page, such as text, images, links, layout, colors, fonts, etc.
- Web page designing can be done using various tools and languages, such as HTML, CSS, JavaScript, Photoshop, Dreamweaver, etc.
- Web page designing involves the following steps:

  - Planning: Define the purpose, audience, content, and structure of the web page.
  - Designing: Choose the layout, colors, fonts, images, and other elements of the web page.
  - Coding: Write the HTML, CSS, and JavaScript code for the web page.
  - Testing: Check the web page for errors, compatibility, accessibility, and usability.
  - Publishing: Upload the web page to a web server and make it available online.

- Web page designing can be done using two approaches:

  - Static web page designing: The web page does not change its content or appearance based on user input or interaction. The web page is the same for every user and every request. Static web pages are created using only HTML and CSS.
  - Dynamic web page designing: The web page changes its content or appearance based on user input or interaction. The web page can be customized for different users and different requests. Dynamic web pages are created using HTML, CSS, and JavaScript, as well as server-side languages and databases.

- The following images illustrate some examples of web page designing:

  - A static web page example:

  ```
  <html>
  <head>
  <title>Static Web Page Example</title>
  <style>
  body {
    font-family: Arial, sans-serif;
    background-color: lightblue;
  }
  h1 {
    color: white;
    text-align: center;
  }
  p {
    color: black;
    text-align: justify;
  }
  </style>
  </head>
  <body>
  <h1>Static Web Page Example</h1>
  <p>This is a static web page example. It does not change its content or appearance based on user input or interaction. It is the same for every user and every request. It is created using only HTML and CSS.</p>
  </body>
  </html>
  ```

  ![Static Web Page Example](https://i.imgur.com/0i5k9XN.png)

  - A dynamic web page example:

  ```
  <html>
  <head>
  <title>Dynamic Web Page Example</title>
  <style>
  body {
    font-family: Arial, sans-serif;
    background-color: lightblue;
  }
  h1 {
    color: white;
    text-align: center;
  }
  p {
    color: black;
    text-align: justify;
  }
  button {
    display: block;
    margin: auto;
  }
  </style>
  <script>
  function changeColor() {
    var colors = ["red", "green", "blue", "yellow", "pink", "purple"];
    var random = Math.floor(Math.random() * colors.length);
    document.body.style.backgroundColor = colors[random];
  }
  </script>
  </head>
  <body>
  <h1>Dynamic Web Page Example</h1>
  <p>This is a dynamic web page example. It changes its content or appearance based on user input or interaction. It can be customized for different users and different requests. It is created using HTML, CSS, and JavaScript.</p>
  <button onclick="changeColor()">Change Background Color</button>
  </body>
  </html>
  ```

  ![Dynamic Web Page Example](https://i.imgur.com/4wQ7sQg.png)

  ![Dynamic Web Page Example After Clicking the Button](https://i.imgur.com/6wQZ6w0.png)