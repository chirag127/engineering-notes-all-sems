### Image Sprites

- An image sprite is a collection of multiple images combined into one single image file.
- The advantage of using image sprites is that it reduces the number of HTTP requests and improves the loading speed of web pages.
- To display a specific part of the image sprite, we can use the CSS `background-image`, `background-position`, and `background-repeat` properties.
- For example, suppose we have an image sprite that contains four icons: home, search, settings, and help.

![Image sprite](https://i.imgur.com/2QbLl4w.png)

- To display the home icon, we can use the following CSS code:

```css
.home {
  width: 50px;
  height: 50px;
  background-image: url("sprite.png");
  background-position: 0 0;
  background-repeat: no-repeat;
}
```

- To display the search icon, we can use the following CSS code:

```css
.search {
  width: 50px;
  height: 50px;
  background-image: url("sprite.png");
  background-position: -50px 0;
  background-repeat: no-repeat;
}
```

- Similarly, we can display the other icons by changing the `background-position` values accordingly.
- We can also use image sprites for creating hover effects, such as changing the color or appearance of an icon when the mouse cursor moves over it.
- To do this, we can use the CSS `:hover` pseudo-class and modify the `background-position` property.
- For example, suppose we have an image sprite that contains two versions of each icon: normal and hover.

![Image sprite hover](https://i.imgur.com/0z0Z0Xs.png)

- To display the normal home icon, we can use the same CSS code as before:

```css
.home {
  width: 50px;
  height: 50px;
  background-image: url("sprite-hover.png");
  background-position: 0 0;
  background-repeat: no-repeat;
}
```

- To display the hover home icon, we can use the following CSS code:

```css
.home:hover {
  background-position: 0 -50px;
}
```

- This will shift the background image by 50 pixels vertically when the mouse cursor moves over the home icon, thus showing the hover version of the icon.
- Similarly, we can create hover effects for the other icons by changing the `background-position` values accordingly.