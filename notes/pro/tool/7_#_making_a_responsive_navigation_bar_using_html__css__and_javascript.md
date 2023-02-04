# making A Responsive Navigation Bar using HTML, CSS, and JavaScript

Sure! Here's an example of a responsive navigation bar using HTML, CSS, and JavaScript:

```
<!DOCTYPE html>
<html>
  <head>
    <style>
      /* Add styles for the navigation bar */
      .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px;
        background-color: #333;
        color: #fff;
      }
      .navbar a {
        color: #fff;
        text-decoration: none;
        margin-right: 20px;
      }
      /* Show and hide the navigation menu on small screens */
      .navbar .menu-icon {
        display: none;
      }
      @media (max-width: 600px) {
        .navbar a:not(:first-child) {
          display: none;
        }
        .navbar .menu-icon {
          display: block;
          cursor: pointer;
        }
      }
      /* Show and hide the navigation links on click */
      .navbar .menu-icon:hover .navbar-menu {
        display: block;
      }
    </style>
  </head>
  <body>
    <header class="navbar">
      <a href="#">Home</a>
      <a href="#">About</a>
      <a href="#">Services</a>
      <a href="#">Contact</a>
      <div class="menu-icon">
        <i class="fa fa-bars"></i>
      </div>
    </header>
    <script>
      // Add JavaScript to toggle the navigation menu on small screens
      const menuIcon = document.querySelector(".menu-icon");
      menuIcon.addEventListener("click", () => {
        const navbarMenu = document.querySelector(".navbar-menu");
        navbarMenu.classList.toggle("show");
      });
    </script>
  </body>
</html>
```

This code creates a navigation bar with four links (Home, About, Services, and Contact) and a menu icon that appears on small screens. The navigation bar is styled with CSS to look professional and have a consistent appearance. The JavaScript code toggles the navigation links on and off when the menu icon is clicked, making the navigation bar responsive to different screen sizes.
