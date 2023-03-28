
### Cross Site Request Forgery

- Cross Site Request Forgery (CSRF) is a type of attack that occurs when a malicious website, email, or program causes a user’s web browser to perform an unwanted action on a trusted site for which the user is currently authenticated.
- CSRF attacks are often used to steal the user’s identity, hijack their session, or to perform malicious actions on the user’s behalf.
- To prevent CSRF attacks, web applications should implement a security mechanism such as a CSRF token or a form token.
- A CSRF token is a random, unique string of characters that is generated for each request. The token is then included in the request header or in the form data.
- The server-side application then checks to make sure the token matches the one it generated for the request. If the token does not match, the request is rejected.
- Form tokens are similar to CSRF tokens, but they are used to validate the authenticity of the form data. Form tokens are generated for each form submission and are included in the form data.
- The server-side application then checks to make sure the token matches the one it generated for the form. If the token does not match, the request is rejected.
- To further protect against CSRF attacks, web applications should also implement other security measures such as same-site cookies, HTTP referer checks, and content security policy (CSP).