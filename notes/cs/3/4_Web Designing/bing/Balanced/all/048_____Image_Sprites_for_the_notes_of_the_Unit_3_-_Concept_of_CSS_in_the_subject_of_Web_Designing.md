# Image Sprites

- An image sprite is a collection of multiple images combined into one single image file.
- The advantage of using image sprites is that it reduces the number of HTTP requests and improves the loading speed of web pages.
- To display a specific part of the image sprite on a web page, we can use the CSS `background-image`, `background-position`, and `background-repeat` properties.
- For example, suppose we have an image sprite that contains four icons: home, search, settings, and help.

![Image sprite example](https://www.w3schools.com/css/img_navsprites.gif)

- To display the home icon on a web page, we can use the following CSS code:

```css
.home {
  width: 46px;
  height: 44px;
  background-image: url("img_navsprites.gif");
  background-position: 0 0;
  background-repeat: no-repeat;
}
```

- The `background-position` property specifies the horizontal and vertical position of the image sprite relative to the element. The value `0 0` means that the top-left corner of the image sprite is aligned with the top-left corner of the element.
- To display the other icons, we can change the `background-position` value accordingly. For example, to display the search icon, we can use `-47px 0`, which means that the image sprite is shifted 47 pixels to the left.

```css
.search {
  width: 46px;
  height: 44px;
  background-image: url("img_navsprites.gif");
  background-position: -47px 0;
  background-repeat: no-repeat;
}
```

- To display the settings icon, we can use `-94px 0`, and to display the help icon, we can use `-141px 0`.
- Alternatively, we can use percentage values to specify the `background-position`. For example, to display the home icon, we can use `0% 0%`, which means that the image sprite is aligned with the left and top edges of the element. To display the search icon, we can use `25% 0%`, which means that the image sprite is shifted 25% of its width to the left. To display the settings icon, we can use `50% 0%`, and to display the help icon, we can use `75% 0%`.
- We can also use image sprites for creating hover effects on buttons or links. For example, suppose we have an image sprite that contains two states of a button: normal and hover.

![Image sprite hover example](https://www.w3schools.com/css/img_button.gif)

- To display the normal state of the button, we can use the following CSS code:

```css
.button {
  width: 194px;
  height: 66px;
  background-image: url("img_button.gif");
  background-position: 0 0;
  background-repeat: no-repeat;
}
```

- To display the hover state of the button, we can use the `:hover` pseudo-class and change the `background-position` value to `0 -66px`, which means that the image sprite is shifted 66 pixels to the top.

```css
.button:hover {
  background-position: 0 -66px;
}
```

- This way, we can create a button that changes its appearance when the mouse cursor moves over it.