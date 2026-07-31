### Cookies, frames and frame busting

- Cookies are small pieces of data that are stored by a web browser on a user's device. They are used to store information such as preferences, authentication, session state, etc. 
- Frames are HTML elements that allow a web page to display content from another source, such as an image, a video, or another web page. Frames can be nested inside each other, creating a hierarchy of frames. 
- Frame busting is a technique that prevents a web page from being loaded inside a frame by another web page. This is done to protect the web page from clickjacking attacks, which are a type of user interface redress attack that trick the user into clicking on something they did not intend to. 
- Frame busting can be implemented in different ways, such as:
  - Using the `X-Frame-Options` or `Content-Security-Policy` HTTP headers to instruct the browser to not load the web page in a frame. 
  - Using the `SameSite` cookie attribute to prevent session cookies from being included when the web page is loaded in a frame. This can prevent the web page from being authenticated or authorized by the server. 
  - Using JavaScript code to check the `window.top` or `window.parent` properties and redirect the web page to the top frame or the original URL if it is not the same as the current web page. 
- Frame busting is not a foolproof solution, as there are ways to bypass it, such as:
  - Using `sandbox` or `allow-top-navigation` attributes on the frame element to disable the frame busting script or the redirection. 
  - Using drag-and-drop or pointer events to manipulate the content of the frame or extract information from it. 
  - Using CSS filters or opacity to hide the frame or make it transparent. 
- Frame busting should be used in combination with other security measures, such as HTTPS, CSRF tokens, and user confirmation, to protect the web page from clickjacking attacks.