# making An Image/Photo Gallery using html css and js

Sure, I can help you with that. 

An Image/Photo Gallery is a collection of images displayed in a grid or a list format. It is a great way to showcase your images and make them easily accessible to your visitors. 

Here's how you can create an Image/Photo Gallery using HTML, CSS, and JavaScript:

1. HTML: Start by creating a basic HTML structure for your page. You can use the following code to create the structure:

```
<!DOCTYPE html>
<html>
  <head>
    <title>Image Gallery</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1>Image Gallery</h1>
    <div class="container">
      <!-- Add your images here -->
    </div>
  </body>
</html>
```

2. CSS: Next, you'll need to style the page using CSS. You can use the following code to create a basic CSS style for your Image Gallery:

```
.container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.container img {
  width: 300px;
  height: 200px;
  margin: 10px;
}
```

3. JavaScript: Finally, you can use JavaScript to add interactivity to your Image Gallery. For example, you can add a lightbox effect to your images so that when a user clicks on an image, it opens up in a larger view. You can use the following code to add a lightbox effect to your Image Gallery:

```
const images = document.querySelectorAll('.container img');
const lightbox = document.createElement('div');
lightbox.id = 'lightbox';
document.body.appendChild(lightbox);

images.forEach(image => {
  image.addEventListener('click', e => {
    lightbox.classList.add('active');
    const img = document.createElement('img');
    img.src = image.src;
    while (lightbox.firstChild) {
      lightbox.removeChild(lightbox.firstChild);
    }
    lightbox.appendChild(img);
  });
});

lightbox.addEventListener('click', e => {
  if (e.target !== e.currentTarget) return;
  lightbox.classList.remove('active');
});
```

And that's it! You have now created an Image/Photo Gallery using HTML, CSS, and JavaScript. You can now add your images to the `.container` div in the HTML and style it further to match your needs.
