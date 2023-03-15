### Image Sprites

- An image sprite is a collection of images put into a single image .
- Image sprites are used to reduce the number of HTTP requests sent to the server and save bandwidth  .
- Image sprites can also improve the performance and loading time of a web page .
- To use image sprites, the following steps are required:
  - Combine the smaller images into a larger one at defined X and Y coordinates.
  - Use the `background-image` property in CSS to set the sprite image as the background of an element .
  - Use the `background-position` property in CSS to specify which part of the sprite image to show for each element .
  - Optionally, use the `width` and `height` properties in CSS to set the size of each element .
- An example of image sprites is shown below:

![Image Sprites Example](https://www.w3schools.com/css/img_navsprites.gif)

The HTML code for the example is:

```html
<div id="navlist">
  <a id="home" href="#"></a>
  <a id="prev" href="#"></a>
  <a id="next" href="#"></a>
</div>
```

The CSS code for the example is:

```css
#navlist {
  position: relative;
}

#navlist a {
  position: absolute;
  width: 46px;
  height: 44px;
  text-decoration: none;
}

#navlist a#home {
  left: 0px;
  top: 0px;
  background: url(img_navsprites.gif) 0 0;
}

#navlist a#prev {
  left: 63px;
  top: 0px;
  background: url(img_navsprites.gif) -47px 0;
}

#navlist a#next {
  left: 129px;
  top: 0px;
  background: url(img_navsprites.gif) -91px 0;
}
```