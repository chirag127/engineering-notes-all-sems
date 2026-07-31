### Image Sprites

- An image sprite is a collection of images put into a single image .
- Image sprites are used to reduce the number of HTTP requests sent to the server and save bandwidth  .
- Image sprites can also improve the performance and loading time of a web page .
- To use image sprites, we need to specify the background-image property and the background-position property in CSS .
- The background-image property sets the source of the sprite image file .
- The background-position property sets the x and y coordinates of the sprite image to display the desired part of the image .
- For example, if we have a sprite image that contains four icons, we can use the following CSS code to display each icon:

```css
/* Set the sprite image as the background image */
.sprite {
  background-image: url("sprite.png");
}

/* Display the first icon by setting the top left corner of the sprite image */
.icon1 {
  width: 50px;
  height: 50px;
  background-position: 0 0;
}

/* Display the second icon by setting the top right corner of the sprite image */
.icon2 {
  width: 50px;
  height: 50px;
  background-position: -50px 0;
}

/* Display the third icon by setting the bottom left corner of the sprite image */
.icon3 {
  width: 50px;
  height: 50px;
  background-position: 0 -50px;
}

/* Display the fourth icon by setting the bottom right corner of the sprite image */
.icon4 {
  width: 50px;
  height: 50px;
  background-position: -50px -50px;
}
```

- The sprite image file looks like this:

![sprite.png](https://www.w3schools.com/css/img_navsprites.gif)

- The output of the CSS code looks like this:

![output.png](https://www.w3schools.com/css/navsprites.gif)

- Image sprites can also be used for creating hover effects, animations, and responsive images.