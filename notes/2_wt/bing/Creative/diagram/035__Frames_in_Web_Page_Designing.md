Frames in Web Page Designing are a way of dividing the browser window into multiple sections, each of which can load a separate HTML document. Frames can be used to create a consistent layout for a website, such as a navigation menu that stays in place while the main content changes. Frames can also be used to display different types of information side by side, such as a map and a list of directions.

To create a frameset, you need to use the `<frameset>` tag instead of the `<body>` tag in your HTML document. The `<frameset>` tag defines how to split the window into rows and columns using the `rows` and `cols` attributes. For example, `<frameset rows="25%,75%">` means that the window will be divided into two horizontal frames, the first one taking 25% of the height and the second one taking 75%. Similarly, `<frameset cols="33%,67%">` means that the window will be divided into two vertical frames, the first one taking 33% of the width and the second one taking 67%.

Inside the `<frameset>` tag, you need to use the `<frame>` tag to specify the source of each frame. The `<frame>` tag has a `src` attribute that points to the URL of the HTML document that will be loaded in that frame. For example, `<frame src="menu.html">` means that the frame will load the menu.html document. You can also use the `name` attribute to give each frame a unique name, which can be used to target links to that frame. For example, `<frame src="menu.html" name="menu">` means that the frame will load the menu.html document and will be named "menu".

Here is an example of a frameset that divides the window into three frames: a top frame that takes 20% of the height, a left frame that takes 30% of the width, and a main frame that takes the remaining space. The top frame loads the header.html document, the left frame loads the menu.html document, and the main frame loads the home.html document. The menu.html document contains links that target the main frame, so that when the user clicks on a link, the main frame will change accordingly.

### Frames in Web Page Designing

```
<html>
<head>
  <title>Frames Example</title>
</head>
<frameset rows="20%,*">
  <frame src="header.html" name="header">
  <frameset cols="30%,*">
    <frame src="menu.html" name="menu">
    <frame src="home.html" name="main">
  </frameset>
</frameset>
</html>
```

The following diagram illustrates the basic layout of the frameset:

```
+------------------------------------+
|             header.html            |
|                                    |
+----------------+-------------------+
|                |                   |
|   menu.html    |    home.html      |
|                |                   |
|                |                   |
|                |                   |
|                |                   |
|                |                   |
|                |                   |
|                |                   |
+----------------+-------------------+
```