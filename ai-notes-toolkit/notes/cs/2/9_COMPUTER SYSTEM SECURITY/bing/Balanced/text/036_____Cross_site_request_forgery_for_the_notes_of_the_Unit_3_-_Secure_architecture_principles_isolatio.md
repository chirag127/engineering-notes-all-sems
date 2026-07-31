### Cross site request forgery

- Cross site request forgery (CSRF) is a type of web attack that exploits the trust between a web application and a user's browser.
- CSRF occurs when an attacker tricks a user into performing an action on a web application that the user is already logged into, without the user's consent or knowledge.
- For example, an attacker can send a malicious link to a user via email or chat, and if the user clicks on the link, the user's browser will send a request to the web application that the user is authenticated with, such as transferring money, changing password, or deleting account.
- CSRF can cause serious damage to the user and the web application, such as financial loss, identity theft, or data breach.
- CSRF can be prevented by using various techniques, such as:
  - Validating the origin and the referer of the request, to ensure that the request is coming from a legitimate source.
  - Generating and verifying a unique token for each request, to ensure that the request is authorized by the user.
  - Implementing the same-site cookie attribute, to prevent the browser from sending cookies to cross-origin requests.
  - Using anti-CSRF frameworks or libraries, to simplify the implementation of CSRF protection.