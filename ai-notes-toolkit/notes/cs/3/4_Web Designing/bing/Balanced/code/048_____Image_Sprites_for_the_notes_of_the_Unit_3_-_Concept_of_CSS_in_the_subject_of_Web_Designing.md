### Image Sprites
- An image sprite is a collection of multiple images combined into one single image file.
- The purpose of using image sprites is to reduce the number of HTTP requests and improve the loading speed of web pages.
- Image sprites can also create dynamic effects such as hover, active, and focus states for buttons, links, and menus.
- To use image sprites, the following steps are required:
  - Create a single image file that contains all the images you want to use as sprites. You can use online tools such as [Sprite Generator](https://www.toptal.com/developers/css/sprite-generator) or [SpritePad](https://spritepad.wearekiss.com/) to create image sprites easily.
  - Use the CSS `background-image` property to set the image sprite as the background of an element, such as a `<div>` or a `<span>`.
  - Use the CSS `background-position` property to specify the position of the image sprite relative to the element. The position is given by two values: the horizontal offset and the vertical offset. For example, `background-position: -50px -100px;` means that the top-left corner of the image sprite is shifted 50 pixels to the left and 100 pixels to the top of the element.
  - Use the CSS `width` and `height` properties to set the size of the element to match the size of the image sprite you want to display. For example, if you want to display a 50x50 pixel icon from the image sprite, you need to set the width and height of the element to 50 pixels each.
  - Optionally, you can use the CSS `:hover`, `:active`, and `:focus` pseudo-classes to change the background position of the image sprite when the user interacts with the element. For example, if you want to display a different icon when the user hovers over the element, you can use `background-position: -100px -100px;` for the `:hover` state.

- Here is an example of using image sprites to create a navigation menu with four icons:

```html
<style>
  .nav {
    display: flex;
    align-items: center;
    justify-content: space-around;
    width: 200px;
    height: 50px;
  }

  .nav-item {
    width: 50px;
    height: 50px;
    background-image: url("sprite.png");
  }

  .home {
    background-position: 0 0;
  }

  .home:hover {
    background-position: -50px 0;
  }

  .search {
    background-position: -100px 0;
  }

  .search:hover {
    background-position: -150px 0;
  }

  .settings {
    background-position: -200px 0;
  }

  .settings:hover {
    background-position: -250px 0;
  }

  .profile {
    background-position: -300px 0;
  }

  .profile:hover {
    background-position: -350px 0;
  }
</style>

<div class="nav">
  <div class="nav-item home"></div>
  <div class="nav-item search"></div>
  <div class="nav-item settings"></div>
  <div class="nav-item profile"></div>
</div>
```

- The image sprite used in this example looks like this:

![sprite.png](https://i.imgur.com/0qVwZ0t.png)

- The result of the code looks like this:

![result.png](https://i.imgur.com/6Y0o0fL.png)