### Images and Multimedia

- Images and multimedia are essential elements of web design that can enhance the appearance and functionality of web pages.
- Images can be used to display logos, icons, photos, diagrams, charts, graphs, etc. Multimedia can be used to embed audio, video, animation, etc.
- HTML provides several tags and attributes to insert and manipulate images and multimedia on web pages.

#### Images

- The `<img>` tag is used to insert an image on a web page. It is an empty tag, meaning it does not have a closing tag.
- The `<img>` tag has two required attributes: `src` and `alt`.
  - The `src` attribute specifies the URL (Uniform Resource Locator) of the image file. The URL can be absolute or relative.
  - The `alt` attribute specifies the alternative text that is displayed if the image cannot be loaded or viewed. The alternative text should describe the content or purpose of the image.
- Example:

```html
<img src="logo.png" alt="Company logo">
```

- The `<img>` tag can also have some optional attributes to modify the appearance and behavior of the image, such as:
  - The `width` and `height` attributes specify the dimensions of the image in pixels. If only one of them is specified, the other one is adjusted proportionally.
  - The `align` attribute specifies the alignment of the image relative to the surrounding text. The possible values are `left`, `right`, `top`, `middle`, and `bottom`.
  - The `border` attribute specifies the width of the border around the image in pixels. The default value is 0, meaning no border.
  - The `hspace` and `vspace` attributes specify the horizontal and vertical space around the image in pixels. They create a margin between the image and the surrounding text or elements.
- Example:

```html
<img src="photo.jpg" alt="A photo of a person" width="200" height="300" align="right" border="5" hspace="10" vspace="10">
```

#### Multimedia

- Multimedia refers to any content that contains more than one type of media, such as audio, video, animation, etc.
- HTML provides several tags and attributes to embed and control multimedia on web pages, such as:
  - The `<audio>` tag is used to embed an audio file on a web page. It can have several attributes, such as:
    - The `src` attribute specifies the URL of the audio file. The URL can be absolute or relative.
    - The `controls` attribute specifies that the browser should display the default audio controls, such as play, pause, volume, etc.
    - The `autoplay` attribute specifies that the audio should start playing as soon as it is loaded. This attribute should be used with caution, as it can be annoying or intrusive for the users.
    - The `loop` attribute specifies that the audio should be played repeatedly.
    - The `muted` attribute specifies that the audio should be muted by default.
  - Example:

  ```html
  <audio src="song.mp3" controls autoplay loop muted></audio>
  ```

  - The `<video>` tag is used to embed a video file on a web page. It can have several attributes, such as:
    - The `src` attribute specifies the URL of the video file. The URL can be absolute or relative.
    - The `controls` attribute specifies that the browser should display the default video controls, such as play, pause, volume, etc.
    - The `autoplay` attribute specifies that the video should start playing as soon as it is loaded. This attribute should be used with caution, as it can be annoying or intrusive for the users.
    - The `loop` attribute specifies that the video should be played repeatedly.
    - The `muted` attribute specifies that the video should be muted by default.
    - The `width` and `height` attributes specify the dimensions of the video in pixels. If only one of them is specified, the other one is adjusted proportionally.
    - The `poster` attribute specifies the URL of an image that is displayed before the video is loaded or played. The URL can be absolute or relative.
  - Example:

  ```html
  <video src="movie.mp4" controls autoplay loop muted width="400" height="300" poster="poster.jpg"></video>
  ```

  - The `<embed>` tag is used to embed any other type of multimedia content on a web page, such as Flash, Java, etc. It can have several attributes, such as:
    - The `src` attribute specifies the URL of the multimedia file. The URL can be