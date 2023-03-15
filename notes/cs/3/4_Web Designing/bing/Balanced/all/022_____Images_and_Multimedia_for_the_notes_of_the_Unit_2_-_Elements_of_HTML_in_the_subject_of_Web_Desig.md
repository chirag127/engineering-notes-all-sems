# Images and Multimedia

- Images and multimedia are essential elements of web design that can enhance the appearance and functionality of web pages.
- Images can be used to display logos, icons, photos, diagrams, charts, graphs, etc. Multimedia can be used to embed audio, video, animation, etc.
- HTML provides several tags and attributes to insert and manipulate images and multimedia on web pages.

## Images

- To insert an image on a web page, the `<img>` tag is used. The `<img>` tag is an empty tag, which means it does not have a closing tag.
- The `<img>` tag has two required attributes: `src` and `alt`. The `src` attribute specifies the URL (Uniform Resource Locator) of the image file. The `alt` attribute specifies the alternative text that is displayed if the image cannot be loaded or viewed.
- Example: `<img src="logo.png" alt="Company Logo">`
- The `<img>` tag can also have some optional attributes, such as `width`, `height`, `title`, `align`, etc. The `width` and `height` attributes specify the dimensions of the image in pixels. The `title` attribute specifies the text that is shown when the mouse pointer hovers over the image. The `align` attribute specifies the alignment of the image relative to the surrounding text and elements. The possible values for the `align` attribute are `left`, `right`, `top`, `middle`, `bottom`, and `baseline`.
- Example: `<img src="logo.png" alt="Company Logo" width="200" height="100" title="This is our logo" align="right">`
- To create an image map, which is an image that contains clickable areas that link to different web pages, the `<map>` and `<area>` tags are used. The `<map>` tag defines the name and shape of the image map. The `<area>` tag defines the coordinates and URL of each clickable area. The `<area>` tag is an empty tag and has three required attributes: `shape`, `coords`, and `href`. The `shape` attribute specifies the shape of the clickable area. The possible values for the `shape` attribute are `rect` (rectangle), `circle`, `poly` (polygon), and `default` (the entire image). The `coords` attribute specifies the coordinates of the clickable area in pixels. The `href` attribute specifies the URL of the web page that is linked to the clickable area.
- Example: `<img src="map.png" alt="Image Map" usemap="#mymap"> <map name="mymap"> <area shape="rect" coords="50,50,150,150" href="page1.html" alt="Page 1"> <area shape="circle" coords="250,250,50" href="page2.html" alt="Page 2"> <area shape="poly" coords="350,50,450,150,350,250,250,150" href="page3.html" alt="Page 3"> <area shape="default" href="page4.html" alt="Page 4"> </map>`

## Multimedia

- To embed multimedia content on a web page, such as audio, video, animation, etc., the `<object>` tag is used. The `<object>` tag defines the type and data of the multimedia content. The `<object>` tag has two required attributes: `type` and `data`. The `type` attribute specifies the MIME (Multipurpose Internet Mail Extensions) type of the multimedia content. The `data` attribute specifies the URL of the multimedia file. The `<object>` tag can also have some optional attributes, such as `width`, `height`, `name`, `classid`, `codebase`, etc. The `width` and `height` attributes specify the dimensions of the multimedia content in pixels. The `name` attribute specifies the name of the multimedia object. The `classid` attribute specifies the identifier of the object class that can handle the multimedia content. The `codebase` attribute specifies the URL of the codebase that contains the object class.
- Example: `<object type="application/x-shockwave-flash" data="animation.swf" width="300" height="200"> <param name="quality" value="high"> </object>`
- The `<param>` tag is used to specify the parameters for the multimedia object. The `<param>` tag is an empty tag and has two required attributes: `name` and `value`. The `name` attribute specifies the name of the parameter. The `value` attribute specifies the value of the parameter.
- Example: `<param name="quality" value="high">`
-