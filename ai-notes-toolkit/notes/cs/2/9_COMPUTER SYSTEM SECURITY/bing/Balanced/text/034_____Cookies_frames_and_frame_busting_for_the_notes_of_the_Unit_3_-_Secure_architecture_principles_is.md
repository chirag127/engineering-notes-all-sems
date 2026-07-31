### Cookies, frames and frame busting

- Cookies are small pieces of data that are stored by a web browser on a user's device. They are used to store information such as preferences, authentication, session state, etc. 
- Frames are HTML elements that allow a web page to display content from another source, such as an image, a video, or another web page. Frames can be nested inside each other, creating a hierarchy of frames. 
- Frame busting is a technique that prevents a web page from being loaded inside a frame by another web page. This is done to prevent attacks such as clickjacking, where a malicious web page overlays a transparent frame over a legitimate web page and tricks the user into clicking on something they did not intend to. 
- Frame busting can be implemented in different ways, such as:
  - Using the `X-Frame-Options` or `Content-Security-Policy` HTTP headers to instruct the browser to not load the page in a frame. 
  - Using the `SameSite` cookie attribute to prevent session cookies from being included when the page is loaded in a frame. 
  - Using JavaScript code to check the `window.top` or `window.parent` properties and redirect the page to the original URL if it is not the top-level frame. 
- Frame busting is not a foolproof defense, as there are ways to bypass it, such as:
  - Using a proxy server to modify the HTTP headers or the JavaScript code of the framed page. 
  - Using drag-and-drop or other HTML5 features to manipulate the content of the frames. 
  - Using CSS or JavaScript tricks to hide or disguise the frame borders or the cursor.