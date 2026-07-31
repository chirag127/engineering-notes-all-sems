Hello, I am Sydney, your AI assistant. I can help you with your notes for the Unit 2 - Web Page Designing in the subject of Web Technology. Here are some frames for the notes:

### Frames
- Frames are a way of dividing a web page into multiple sections, each with its own independent content and scroll bars.
- Frames can be used to create layouts that are more flexible and dynamic than using tables or CSS grids.
- Frames are created using the `<frameset>` tag, which replaces the `<body>` tag in the HTML document.
- The `<frameset>` tag can have one or more `<frame>` tags as its children, which specify the source, name, size, and border of each frame.
- The `<frameset>` tag can also have nested `<frameset>` tags to create more complex layouts with rows and columns of frames.
- The `<noframes>` tag can be used to provide alternative content for browsers that do not support frames or have frames disabled.
- Frames can be linked to each other using the `target` attribute in the `<a>` tag, which specifies the name of the frame where the link should open.
- Frames can also be accessed and manipulated using JavaScript, using the `window.frames` collection and the `frameElement` property.

Some examples of frames are:

- A web page with a header, a navigation bar, and a main content area:

```
<frameset rows="10%,*,10%">
  <frame src="header.html" name="header" scrolling="no" noresize>
  <frameset cols="20%,*">
    <frame src="nav.html" name="nav" scrolling="auto" noresize>
    <frame src="main.html" name="main" scrolling="auto" noresize>
  </frameset>
  <frame src="footer.html" name="footer" scrolling="no" noresize>
</frameset>
<noframes>
  <body>
    <p>This page uses frames, but your browser does not support them.</p>
  </body>
</noframes>
```

- A web page with a left sidebar and a right content area that can be resized by the user:

```
<frameset cols="25%,*">
  <frame src="sidebar.html" name="sidebar" scrolling="auto" noresize>
  <frame src="content.html" name="content" scrolling="auto" resize>
</frameset>
<noframes>
  <body>
    <p>This page uses frames, but your browser does not support them.</p>
  </body>
</noframes>
```

- A web page with a 3x3 grid of frames, each with a different background color:

```
<frameset rows="*,*,*">
  <frameset cols="*,*,*">
    <frame src="red.html" name="red" scrolling="no" noresize>
    <frame src="green.html" name="green" scrolling="no" noresize>
    <frame src="blue.html" name="blue" scrolling="no" noresize>
  </frameset>
  <frameset cols="*,*,*">
    <frame src="yellow.html" name="yellow" scrolling="no" noresize>
    <frame src="cyan.html" name="cyan" scrolling="no" noresize>
    <frame src="magenta.html" name="magenta" scrolling="no" noresize>
  </frameset>
  <frameset cols="*,*,*">
    <frame src="black.html" name="black" scrolling="no" noresize>
    <frame src="white.html" name="white" scrolling="no" noresize>
    <frame src="gray.html" name="gray" scrolling="no" noresize>
  </frameset>
</frameset>
<noframes>
  <body>
    <p>This page uses frames, but your browser does not support them.</p>
  </body>
</noframes>
```
