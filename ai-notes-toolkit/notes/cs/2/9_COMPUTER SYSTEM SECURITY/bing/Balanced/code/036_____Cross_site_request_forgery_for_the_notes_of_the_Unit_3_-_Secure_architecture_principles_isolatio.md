### Cross site request forgery

- Cross site request forgery (CSRF) is a type of web attack that exploits the trust between a web application and a user's browser.
- CSRF occurs when an attacker tricks a user into performing an action on a web application that the user is already logged into, such as transferring money, changing password, or deleting an account.
- CSRF can be performed by embedding malicious links or forms in emails, chat messages, or web pages that the user visits, or by exploiting vulnerabilities in the web application or browser.
- CSRF can be prevented by using anti-CSRF tokens, which are unique and unpredictable values that are sent along with every request from the web application to the server, and verified by the server before processing the request.
- CSRF can also be mitigated by using the same-site cookie attribute, which prevents cookies from being sent to cross-origin requests, or by using the origin or referer headers, which indicate the source of the request.