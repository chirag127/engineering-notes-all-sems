# Cross-Site Request Forgery (CSRF)

Cross-Site Request Forgery (CSRF) is a type of attack that occurs when a malicious website, email, or program causes a user's web browser to perform an unwanted action on a trusted site for which the user is currently authenticated.

## How CSRF attacks work

1. The attacker creates a malicious link or form that is designed to perform an action on a target website.
2. The attacker sends the link or form to the victim, often through email or social media.
3. The victim clicks on the link or submits the form, which sends a request to the target website.
4. If the victim is currently authenticated on the target website, the request will be processed as if it was sent by the victim.

## Prevention of CSRF attacks

There are several methods to prevent CSRF attacks:

1. **Use of anti-CSRF tokens**: A unique token is generated for each user session and included in all forms and links that can perform state-changing actions. The server checks the token before processing the request, and if it does not match the token stored in the user's session, the request is rejected.
2. **Same-Site Cookies**: Cookies can be set with the `SameSite` attribute, which prevents the browser from sending the cookie along with cross-site requests. This can prevent CSRF attacks that rely on the user being authenticated on the target website.
3. **Re-authentication**: For sensitive actions, the user can be required to re-enter their password or perform another form of authentication before the action is processed.
