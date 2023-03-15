### Cookies, frames and frame busting

- Cookies are small pieces of data that are stored by a web browser on a user's device. They are used to store information such as preferences, authentication, session state, etc. 
- Frames are HTML elements that allow a web page to display content from another source, such as an image, a video, or another web page. Frames can be nested inside each other, creating a hierarchy of frames. 
- Clickjacking is a type of attack that tricks a user into clicking on a hidden or disguised element on a web page, such as a button, a link, or a form. Clickjacking can be used to perform malicious actions on behalf of the user, such as stealing their credentials, transferring funds, or posting messages. 
- Frame busting is a technique that prevents a web page from being loaded inside a frame, usually by using JavaScript code that checks the window location or the window parent and redirects the page to the original source if it is framed. Frame busting is a common defense against clickjacking attacks.  
- However, frame busting is not a foolproof solution, as there are ways to bypass it, such as using nested frames, using CSS properties to hide or modify the frame content, or using drag-and-drop to extract or inject data into frames. 
- Therefore, it is recommended to use other methods to protect a web page from clickjacking, such as:
  - Using the X-Frame-Options or Content Security Policy (frame-ancestors) HTTP headers, which instruct the browser to not load the page in a frame or only allow frames from certain origins. 
  - Using the SameSite cookie attribute, which prevents session cookies from being included when the page is loaded in a frame, thus preventing authentication bypass. 
  - Using user interaction or confirmation, such as CAPTCHA, re-authentication, or confirmation dialogs, to verify the user's intention before performing sensitive actions.