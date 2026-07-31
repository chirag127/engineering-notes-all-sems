### Creating page layout and site designs with CSS

- CSS stands for Cascading Style Sheets and is a code language that allows you to control the appearance of your web page.
- CSS can be used to create different layouts and designs for your web page, such as headers, navigation bars, content sections, footers, and responsive layouts  .
- A layout is the way the elements of a web page are arranged and aligned on the screen.
- A design is the overall look and feel of a web page, such as colors, fonts, images, and animations.
- To create a layout and a design with CSS, you need to use the following steps:
  - Define the HTML structure of your web page, using semantic elements such as `<header>`, `<nav>`, `<section>`, `<footer>`, etc .
  - Link a CSS file to your HTML file, using the `<link>` element in the `<head>` section .
  - Use CSS selectors to target the HTML elements you want to style, such as element selectors, class selectors, id selectors, etc .
  - Use CSS properties and values to specify the style rules for the selected elements, such as `display`, `width`, `height`, `margin`, `padding`, `border`, `color`, `font`, `background`, etc .
  - Use CSS layout techniques to position and align the elements on the web page, such as normal flow, floats, flexbox, grid, etc .
  - Use CSS media queries to make your web page responsive and adapt to different screen sizes and devices .
  - Use CSS transitions, animations, and transforms to add interactivity and effects to your web page .
- Here is an example of a simple web page layout and design with CSS:

```html
<html>
<head>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>My Website</h1>
    <nav>
      <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
  </header>
  <section>
    <h2>Welcome to my website</h2>
    <p>This is some content for my website.</p>
  </section>
  <footer>
    <p>© 2023 by My Website. All rights reserved.</p>
  </footer>
</body>
</html>
```

```css
/* style.css */

/* Define the layout of the web page */
header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: lightblue;
  padding: 10px;
}

nav {
  display: flex;
}

nav ul {
  display: flex;
  list-style: none;
}

nav li {
  margin: 10px;
}

section {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 20px;
}

footer {
  display: flex;
  justify-content: center;
  background-color: lightgray;
  padding: 10px;
}

/* Define the design of the web page */
h1 {
  color: white;
  font-family: Arial, sans-serif;
}

nav a {
  color: black;
  font-family: Arial, sans-serif;
  text-decoration: none;
}

nav a:hover {
  color: white;
  transition: 0.5s;
}

h2 {
  color: darkblue;
  font-family: Arial, sans-serif;
}

p {
  color: black;
  font-family: Arial, sans-serif;
}

/* Make the web page responsive */
@media (max-width: 600px) {
  header {
    flex-direction: column;
  }

  nav {
    flex-direction: column;
  }

  nav li {
    margin: 5px;
  }
}
```

- The result of the above code is shown below:

![Web page layout and design with CSS](https://i.imgur.com/7s1wZ4x.png)

- You can learn more about CSS layout and design by reading the