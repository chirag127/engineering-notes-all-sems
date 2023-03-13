Frames in Web Page Designing are a way of dividing the browser window into multiple sections, each of which can display a different web page or another frameset. Frames can be useful for creating navigation menus, headers, footers, sidebars, etc. Frames can also be nested, meaning that a frame can contain another frameset.

### Frames in Web Page Designing

The following is an example of a frameset that divides the browser window into four frames: a top frame, a left frame, a right frame, and a bottom frame. The frameset uses the <frameset> tag with the rows and cols attributes to specify the size and position of each frame. The <frame> tag inside the <frameset> tag specifies the source of the web page to be displayed in each frame. The name attribute of the <frame> tag can be used to refer to the frame from other web pages or links.

```
<frameset rows="10%,*,10%">
  <frame src="top.html" name="topframe">
  <frameset cols="20%,*">
    <frame src="left.html" name="leftframe">
    <frame src="right.html" name="rightframe">
  </frameset>
  <frame src="bottom.html" name="bottomframe">
</frameset>
```

The following is an ASCII diagram of the frameset:

```
+-----------------------------------+
|             topframe              |
|-----------------------------------|
| leftframe  |       rightframe     |
|            |                      |
|            |                      |
|            |                      |
|            |                      |
|            |                      |
|            |                      |
|            |                      |
|            |                      |
|-----------------------------------|
|            bottomframe            |
+-----------------------------------+
```