### Cross-Site Request Forgery (CSRF)

Cross-Site Request Forgery (CSRF) is a type of attack that occurs when a malicious website, email, or program causes a user's web browser to perform an unwanted action on a trusted site for which the user is currently authenticated.

- CSRF attacks specifically target state-changing requests, not theft of data, since the attacker has no way to see the response to the forged request.
- CSRF vulnerabilities are commonly found in web applications that do not verify the origin of a request before performing an action.
- To prevent CSRF attacks, it is important to include a unique token in each request that is verified by the server before performing the action. This token should be unpredictable and tied to the user's session.
- Another way to prevent CSRF attacks is to use the "SameSite" attribute for cookies, which prevents the browser from sending the cookie along with cross-site requests.
- It is also important to use proper HTTP methods (e.g. GET for retrieving data, POST for changing data) and to properly validate and sanitize user input.
