### Floating

- Floating is a CSS property that allows an element to be placed on the left or right side of its container, letting text and inline elements wrap around it.
- Floating removes the element from the normal flow of the page, but it still remains a part of the flow, unlike absolute positioning.
- Floating can be used for positioning and layout of web pages, such as letting an image float to one side and letting text wrap around it.
- Floating can also be used to create multi-column layouts, by floating the columns to the left or right.
- The syntax for floating is `float: value;`, where the value can be one of the following :
  - `left`: The element floats to the left of its container.
  - `right`: The element floats to the right of its container.
  - `none`: The element does not float, and is displayed where it occurs in the text. This is the default value.
  - `inherit`: The element inherits the float value from its parent element.
- The `clear` property can be used to specify what elements can float beside the cleared element and on which side.
- The syntax for clearing is `clear: value;`, where the value can be one of the following:
  - `left`: No floating elements allowed on the left side of the cleared element.
  - `right`: No floating elements allowed on the right side of the cleared element.
  - `both`: No floating elements allowed on either side of the cleared element.
  - `none`: The element is not affected by the floating elements. This is the default value.
  - `inherit`: The element inherits the clear value from its parent element.
- Here is an example of floating an image with a caption to the right, and letting the text wrap around it:

```html
<style>
  .img-container {
    float: right;
    margin: 10px;
  }

  .img-container img {
    display: block;
    width: 200px;
    height: auto;
  }

  .img-container p {
    text-align: center;
    font-style: italic;
  }
</style>

<h2>Floating Example</h2>
<div class="img-container">
  <img src="img_flower.jpg" alt="Flower">
  <p>A beautiful flower</p>
</div>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus quis lectus metus, at posuere neque. Sed pharetra nibh eget orci convallis at posuere leo convallis. Sed blandit augue vitae augue scelerisque bibendum. Vivamus sit amet libero turpis, non venenatis urna. In blandit, odio convallis suscipit venenatis, ante ipsum cursus augue.</p>
<p>Et mollis nunc diam eget sapien. Nulla facilisi. Etiam feugiat imperdiet rhoncus. Sed suscipit bibendum enim, sed volutpat tortor malesuada non. Morbi fringilla dui non purus porttitor mattis. Suspendisse quis vulputate risus. Phasellus erat velit, sagittis sed varius volutpat, placerat nec urna. Nam eu metus vitae dolor fringilla feugiat. Nulla.</p>
<p>Facilisi. Etiam enim metus, luctus in adipiscing at, consectetur quis sapien. Duis imperdiet egestas ligula, quis hendrerit ipsum ullamcorper et. Phasellus id tristique orci. Proin consequat mi at felis scelerisque ullamcorper. Etiam tempus, felis vel eleifend porta, velit nunc mattis urna, at ullamcorper erat diam dignissim ante. Pellentesque justo risus.</p>
```