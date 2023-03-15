### Cookies, frames and frame busting

- Cookies are small pieces of data that are stored by a web browser on a user's device. They are used to store information such as preferences, authentication, session state, etc. 
- Frames are HTML elements that allow a web page to display another web page within a rectangular region. They are often used to embed content from different sources or domains. 
- Frame busting is a technique that prevents a web page from being loaded inside a frame. It is used to defend against clickjacking attacks, which trick users into clicking on hidden or disguised elements in a framed page.   

Some key points about cookies, frames and frame busting are:

- Cookies can have attributes that control their scope, expiration, and security. For example, the `SameSite` attribute prevents cookies from being sent along with cross-site requests, which can mitigate some types of clickjacking attacks. 
- Frames can have attributes that control their appearance, size, and scrolling. For example, the `frameborder` attribute specifies whether or not to display a border around the frame. 
- Frame busting can be implemented using various methods, such as checking the `window.top` or `window.parent` properties, using the `X-Frame-Options` or `Content-Security-Policy` HTTP headers, or using JavaScript to redirect or break out of the frame.   
- Frame busting is not a foolproof solution, as some methods can be bypassed by attackers using techniques such as nested frames, proxies, or drag-and-drop.