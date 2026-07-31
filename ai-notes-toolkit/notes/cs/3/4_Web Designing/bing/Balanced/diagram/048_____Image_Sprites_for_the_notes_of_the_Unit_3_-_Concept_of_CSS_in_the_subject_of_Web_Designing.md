### Image Sprites

- An image sprite is a collection of multiple images combined into one single image file.
- The advantage of using image sprites is that it reduces the number of HTTP requests and improves the loading speed of web pages.
- To display a specific part of the image sprite on a web page, the CSS properties `background-image`, `background-position` and `background-repeat` are used.
- The `background-image` property specifies the URL of the image sprite file.
- The `background-position` property specifies the horizontal and vertical offset of the image sprite relative to the element's top-left corner.
- The `background-repeat` property specifies how the image sprite is repeated or tiled in the element's background.
- Example: Suppose we have an image sprite file called `icons.png` that contains four icons: home, search, settings and logout. To display the home icon on a web page, we can use the following CSS code:

```css
.home {
  width: 50px; /* the width of the icon */
  height: 50px; /* the height of the icon */
  background-image: url("icons.png"); /* the URL of the image sprite file */
  background-position: 0 0; /* the offset of the home icon in the image sprite file */
  background-repeat: no-repeat; /* the image sprite is not repeated */
}
```

- To display the other icons, we can change the `background-position` property accordingly. For example, to display the search icon, we can use `background-position: -50px 0;`, which means shifting the image sprite 50 pixels to the left. Similarly, to display the settings icon, we can use `background-position: 0 -50px;`, which means shifting the image sprite 50 pixels to the top. To display the logout icon, we can use `background-position: -50px -50px;`, which means shifting the image sprite 50 pixels to the left and 50 pixels to the top.