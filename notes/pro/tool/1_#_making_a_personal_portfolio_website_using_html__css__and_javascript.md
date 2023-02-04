# making A Personal Portfolio Website using HTML, CSS, and JavaScript

Sure, here is an example of how you could create a personal portfolio website using HTML, CSS, and JavaScript:

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>My Personal Portfolio</title>
    <style>
      /* Add your CSS styles here */
      body {
        font-family: Arial, sans-serif;
        background-color: #f2f2f2;
      }
      header {
        text-align: center;
        padding: 50px 0;
      }
      h1 {
        font-size: 42px;
        margin-bottom: 20px;
      }
      section {
        display: flex;
        justify-content: center;
        align-items: center;
        height: calc(100vh - 100px);
      }
      .card {
        background-color: white;
        box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
        width: 50%;
        padding: 40px;
        text-align: center;
      }
      .card h2 {
        font-size: 32px;
        margin-bottom: 20px;
      }
      .card p {
        font-size: 18px;
        margin-bottom: 20px;
        line-height: 1.5;
      }
      .card a {
        display: inline-block;
        padding: 10px 20px;
        background-color: #333;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        font-size: 18px;
      }
    </style>
  </head>
  <body>
    <header>
      <h1>My Personal Portfolio</h1>
    </header>
    <section>
      <div class="card">
        <h2>About Me</h2>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer
          malesuada bibendum massa, eu commodo mi congue id. Nulla facilisi.
        </p>
        <a href="#">Learn More</a>
      </div>
    </section>
    <script>
      // Add your JavaScript code here
      const card = document.querySelector('.card');
      card.addEventListener('mouseenter', () => {
        card.style.transform = 'scale(1.1)';
        card.style.transition = 'all 0.5s ease-in-out';
      });
      card.addEventListener('mouseleave', () => {
        card.style.transform = 'scale(1)';
        card.style.transition = 'all 0.5s ease-in-out';
      });
    </script>
  </body>
</html>
```

This code creates a simple personal portfolio website with a header, a section containing an about me card, and some basic styling using CSS. The JavaScript code adds a hover effect to the card, making it scale up slightly when the user's mouse enters the card, and scale back down when the mouse leaves.

Of course, this is just a starting point, and you can customize and build upon this code to create the exact website you have in mind.
