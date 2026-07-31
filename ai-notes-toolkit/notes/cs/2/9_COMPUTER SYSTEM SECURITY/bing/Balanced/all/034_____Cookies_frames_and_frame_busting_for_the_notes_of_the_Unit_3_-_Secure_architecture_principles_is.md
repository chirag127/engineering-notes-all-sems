# Cookies, Frames and Frame Busting

- Cookies are small pieces of data that are stored by a web browser on a user's device. They are used to store information such as preferences, authentication, session state, and tracking.
- Frames are HTML elements that allow a web page to display content from another source, such as an image, a video, or another web page. Frames can be nested inside each other, creating a hierarchy of frames.
- Frame busting is a technique that prevents a web page from being loaded inside a frame by another web page. Frame busting is used to defend against clickjacking attacks, which trick users into clicking on hidden or disguised elements in a framed web page.
- Clickjacking attacks can be used to perform actions on behalf of the user, such as liking a page, sending a message, or transferring money, without their consent or knowledge.
- Frame busting can be implemented in different ways, such as:

  - Using the `X-Frame-Options` or `Content-Security-Policy` HTTP headers to instruct the browser to not load the page in a frame, or only allow frames from the same origin or a trusted source.
  - Using the `SameSite` cookie attribute to prevent session cookies from being included when the page is loaded in a frame, which can prevent authentication bypass or CSRF attacks.
  - Using JavaScript code to check the `window.top` or `window.parent` properties and redirect the page to the original URL or display an error message if the page is framed.
  - Using CSS properties to hide or obscure the framed content, such as `display:none`, `opacity:0`, or `pointer-events:none`.

- Frame busting is not a foolproof solution, as some browsers may not support the HTTP headers or the JavaScript code, or the attacker may use techniques to bypass or disable the frame busting code, such as:

  - Using a proxy server to modify or remove the HTTP headers or the JavaScript code from the framed page.
  - Using the `sandbox` attribute on the `iframe` element to restrict the JavaScript execution or navigation of the framed page.
  - Using the `allow-top-navigation-by-user-activation` feature policy to allow the framed page to navigate the top page only with user interaction.
  - Using drag-and-drop or clipboard events to extract or inject data into the framed page.

- Therefore, frame busting should be used as a defense-in-depth measure, and not as the sole protection against clickjacking attacks. Other security best practices, such as using HTTPS, validating user input, and implementing CSRF tokens, should also be applied.