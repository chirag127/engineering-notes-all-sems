# Cookies, Frames and Frame Busting

## Cookies
- Cookies are small pieces of data that are stored by the browser on the user's device, usually to store preferences, authentication tokens, session IDs, etc.
- Cookies can be set by the server using the `Set-Cookie` HTTP header, or by the client using JavaScript.
- Cookies have attributes that control their scope, duration, and security, such as `domain`, `path`, `expires`, `max-age`, `secure`, `httponly`, and `samesite`.
- Cookies can be accessed by the server using the `Cookie` HTTP header, or by the client using `document.cookie`.
- Cookies can be used for various purposes, such as personalization, tracking, state management, etc.

## Frames
- Frames are HTML elements that allow embedding another document within the current document, such as `<iframe>`, `<frame>`, and `<frameset>`.
- Frames can be used for various purposes, such as navigation, content aggregation, advertising, etc.
- Frames can also pose security risks, such as clickjacking, cross-site scripting, cross-frame scripting, etc.

## Frame Busting
- Frame busting is a technique that prevents a web page from being loaded inside a frame, usually to protect against clickjacking attacks.
- Clickjacking is an attack that tricks the user into clicking on a hidden or disguised element on a framed page, such as a button, a link, or a form, that performs an unwanted action on behalf of the user, such as logging out, transferring money, posting a message, etc.
- Frame busting can be implemented using various methods, such as:
  - Checking the `window.top` or `window.parent` properties and redirecting or breaking out of the frame if they are not the same as the current window.
  - Setting the `X-Frame-Options` HTTP header to `DENY`, `SAMEORIGIN`, or `ALLOW-FROM` to instruct the browser to block or allow the framing of the page.
  - Setting the `Content-Security-Policy` HTTP header with the `frame-ancestors` directive to specify the origins that are allowed to frame the page.
  - Setting the `SameSite` cookie attribute to `Strict` or `Lax` to prevent the inclusion of cookies when the page is loaded in a cross-site frame.