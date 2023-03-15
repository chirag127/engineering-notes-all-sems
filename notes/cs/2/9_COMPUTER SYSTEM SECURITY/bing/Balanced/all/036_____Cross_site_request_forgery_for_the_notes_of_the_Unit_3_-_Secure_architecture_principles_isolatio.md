# Cross Site Request Forgery

- Cross Site Request Forgery (CSRF) is a type of web attack that exploits the trust between a web application and a user's browser.
- CSRF occurs when an attacker tricks a user into performing an action on a web application that the user is already logged into, without the user's consent or knowledge.
- For example, an attacker can send a malicious link to a user via email or chat, and if the user clicks on the link, the user's browser will send a request to the web application that the user is authenticated with, such as transferring money, changing password, or deleting account.
- CSRF can cause serious damage to the user and the web application, such as financial loss, identity theft, or data breach.
- CSRF can be prevented by using various techniques, such as:
  - Using a secret token or nonce that is unique for each request and session, and validating it on the server side.
  - Using the SameSite attribute on cookies to prevent them from being sent along with cross-site requests.
  - Using the Origin or Referer headers to check the source of the request and reject it if it is not from the same origin as the web application.
  - Using anti-CSRF frameworks or libraries that provide built-in protection against CSRF attacks.