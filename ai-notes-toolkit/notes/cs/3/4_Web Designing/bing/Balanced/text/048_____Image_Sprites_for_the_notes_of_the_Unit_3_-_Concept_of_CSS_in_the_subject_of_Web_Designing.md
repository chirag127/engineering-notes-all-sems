### Image Sprites

- An image sprite is a collection of multiple images combined into one single image file.
- Image sprites are used to reduce the number of HTTP requests and improve the loading speed of web pages.
- Image sprites can also create dynamic effects such as hover, active, and focus states for buttons and links.
- To use image sprites, the following steps are required:
  - Create a single image file that contains all the images you want to use as sprites.
  - Use CSS properties such as `background-image`, `background-position`, and `background-repeat` to display the desired part of the sprite image on an HTML element.
  - Adjust the width and height of the HTML element to match the size of the sprite image part.
  - Use CSS pseudo-classes such as `:hover`, `:active`, and `:focus` to change the `background-position` of the sprite image and create dynamic effects.
- Example of an image sprite file:

![Image sprite file](https://www.w3schools.com/css/img_navsprites.gif)

- Example of HTML and CSS code to use the image sprite file:

```html
<html>
<head>
<style>
#navlist {
  position: relative;
}

#navlist li {
  margin: 0;
  padding: 0;
  list-style: none;
  position: absolute;
  top: 0;
}

#navlist li, #navlist a {
  height: 44px;
  display: block;
}

#home {
  left: 0px;
  width: 46px;
}

#prev {
  left: 63px;
  width: 43px;
}

#next {
  left: 129px;
  width: 43px;
}

#navlist a {
  background-image: url(https://www.w3schools.com/css/img_navsprites.gif);
  background-repeat: no-repeat;
}

#home a {
  background-position: 0px 0px;
}

#prev a {
  background-position: -47px 0px;
}

#next a {
  background-position: -91px 0px;
}

#home a:hover {
  background-position: 0px -45px;
}

#prev a:hover {
  background-position: -47px -45px;
}

#next a:hover {
  background-position: -91px -45px;
}
</style>
</head>
<body>
<ul id="navlist">
  <li id="home"><a href="#"></a></li>
  <li id="prev"><a href="#"></a></li>
  <li id="next"><a href="#"></a></li>
</ul>
</body>
</html>
```

- Example of the output of the HTML and CSS code:

![Output of the HTML and CSS code](https://www.w3schools.com/css/navsprites.gif)