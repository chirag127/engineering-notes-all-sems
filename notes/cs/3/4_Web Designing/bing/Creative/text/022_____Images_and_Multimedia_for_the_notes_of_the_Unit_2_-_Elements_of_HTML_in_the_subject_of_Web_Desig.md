### Images and Multimedia

- Images and multimedia are elements that can be used to enhance the appearance and functionality of a web page.
- Images and multimedia can include text, graphics, audio, video, animation, and other types of media.
- Images and multimedia can be embedded in a web page using different HTML tags and attributes, depending on the format and type of the media.
- Some of the common HTML tags and attributes for images and multimedia are:

  - `<img>`: This tag is used to embed a simple image in a web page. It has the following attributes:
    - `src`: This attribute specifies the URL of the image file to be displayed.
    - `alt`: This attribute provides an alternative text for the image, in case it cannot be loaded or displayed. This is useful for accessibility and SEO purposes.
    - `width` and `height`: These attributes specify the dimensions of the image in pixels. They can be used to resize or crop the image, but it is recommended to use CSS for better control and performance.
    - `title`: This attribute provides a tooltip text for the image, which appears when the mouse cursor hovers over the image.
  - `<figure>` and `<figcaption>`: These tags are used to annotate an image with a caption or a description. The `<figure>` tag wraps around the `<img>` tag and the `<figcaption>` tag, which contains the caption text. For example:

    ```html
    <figure>
      <img src="images/dinosaur.jpg" alt="Dinosaur" />
      <figcaption>A dinosaur skeleton at the museum.</figcaption>
    </figure>
    ```

  - `<embed>`: This tag is used to embed multimedia elements of various formats and types, such as audio, video, flash, etc. It has the following attributes:
    - `src`: This attribute specifies the URL of the media file to be embedded.
    - `type`: This attribute specifies the MIME type of the media file, such as `audio/mpeg`, `video/mp4`, `application/x-shockwave-flash`, etc. This helps the browser to identify the appropriate plugin or player to use for the media.
    - `width` and `height`: These attributes specify the dimensions of the media in pixels. They can be used to resize or crop the media, but it is recommended to use CSS for better control and performance.
  - `<audio>` and `<video>`: These tags are used to embed audio and video elements in a web page, respectively. They have the following attributes:
    - `src`: This attribute specifies the URL of the audio or video file to be embedded.
    - `controls`: This attribute enables the default controls for the audio or video, such as play, pause, volume, etc.
    - `autoplay`: This attribute makes the audio or video start playing automatically when the page loads. This is not recommended for user experience and accessibility reasons.
    - `loop`: This attribute makes the audio or video repeat indefinitely when it reaches the end.
    - `muted`: This attribute mutes the audio or video by default.
    - `poster`: This attribute specifies the URL of an image to be shown before the video starts playing or when the video is not available.
    - `preload`: This attribute specifies how much of the audio or video should be loaded when the page loads. It can have the following values: `none`, `metadata`, or `auto`.
  - `<source>`: This tag is used to provide multiple sources for the `<audio>` or `<video>` tags, in case the browser does not support the default source. It has the following attributes:
    - `src`: This attribute specifies the URL of the alternative audio or video file to be embedded.
    - `type`: This attribute specifies the MIME type of the alternative audio or video file, such as `audio/mpeg`, `video/mp4`, etc. This helps the browser to select the best source for the media.
  - `<track>`: This tag is used to provide subtitles or captions for the `<audio>` or `<video>` tags. It has the following attributes:
    - `src`: This attribute specifies the URL of the file that contains the subtitles or captions, usually in WebVTT format.
    - `kind`: This attribute specifies the kind of the track, such as `subtitles`, `captions`, `descriptions`, `chapters`, or `metadata`.
    - `srclang`: This attribute specifies the language of the track, using a valid BCP 47 language tag, such as `en`, `fr`, `zh`, etc.