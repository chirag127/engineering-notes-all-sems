### Images and Multimedia

- Images and multimedia are essential elements of web design that can enhance the appearance and functionality of web pages.
- Images can be used to display logos, icons, photos, diagrams, charts, graphs, etc. Multimedia can be used to embed audio, video, animation, etc.
- HTML provides several tags and attributes to insert and manipulate images and multimedia on web pages.

#### Images

- To insert an image on a web page, the `<img>` tag is used. The `<img>` tag is an empty tag, meaning it does not have a closing tag.
- The `<img>` tag requires the `src` attribute, which specifies the URL or path of the image file. The `src` attribute can be an absolute URL (starting with http:// or https://) or a relative URL (relative to the current web page).
- The `<img>` tag also supports the following optional attributes:
  - `alt`: provides alternative text for the image, which is displayed when the image cannot be loaded or for accessibility purposes.
  - `width`: sets the width of the image in pixels or percentage.
  - `height`: sets the height of the image in pixels or percentage.
  - `title`: provides a tooltip text for the image, which is displayed when the mouse hovers over the image.
  - `align`: aligns the image horizontally with respect to the surrounding text. The possible values are `left`, `right`, `top`, `middle`, `bottom`.
  - `border`: sets the border width of the image in pixels.
- Example of using the `<img>` tag:

```html
<img src="logo.png" alt="Logo" width="100" height="50" title="This is the logo" align="left" border="1">
```

#### Multimedia

- To embed multimedia content on a web page, such as audio, video, animation, etc., the `<object>` tag is used. The `<object>` tag is a container tag, meaning it has a closing tag.
- The `<object>` tag requires the `data` attribute, which specifies the URL or path of the multimedia file. The `data` attribute can be an absolute URL (starting with http:// or https://) or a relative URL (relative to the current web page).
- The `<object>` tag also supports the following optional attributes:
  - `type`: specifies the MIME type of the multimedia file, such as `audio/mpeg`, `video/mp4`, `application/x-shockwave-flash`, etc.
  - `width`: sets the width of the multimedia object in pixels or percentage.
  - `height`: sets the height of the multimedia object in pixels or percentage.
  - `align`: aligns the multimedia object horizontally with respect to the surrounding text. The possible values are `left`, `right`, `top`, `middle`, `bottom`.
  - `border`: sets the border width of the multimedia object in pixels.
- The `<object>` tag can also contain nested `<param>` tags, which provide additional parameters for the multimedia object, such as `autoplay`, `loop`, `controls`, etc. The `<param>` tag is an empty tag, meaning it does not have a closing tag. The `<param>` tag requires the `name` and `value` attributes, which specify the name and value of the parameter.
- The `<object>` tag can also contain alternative content, which is displayed when the multimedia object cannot be loaded or for accessibility purposes.
- Example of using the `<object>` tag:

```html
<object data="video.mp4" type="video/mp4" width="320" height="240" align="center" border="1">
  <param name="autoplay" value="true">
  <param name="loop" value="false">
  <param name="controls" value="true">
  <p>This is a video.</p>
</object>
```