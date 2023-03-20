 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Hijacking & Defense

1. Session Hijacking: An attacker takes over a user's session to gain unauthorized access to a computer system.
- Predicting session ID: The attacker predicts the session ID of a valid user to take over the session.
- Sniffing: The attacker sniffs the network to steal the session ID of an active session.
- Cross-site Scripting (XSS): The attacker injects a malicious script into a website to steal cookies and session IDs of users.

Defense:
- Use strong session IDs that are difficult to predict.
- Use encrypted sessions and HTTPS.
- Sanitize user input to prevent XSS.

2. Man-in-the-Middle (MITM) Attack: An attacker secretly relays and modifies the communication between two parties to steal data or credentials.
- ARP Poisoning: The attacker sends spoofed ARP messages to associate the attacker's MAC address with the IP address of the target server or router. This allows the attacker to intercept traffic.
- DNS Spoofing: The attacker spoofs DNS responses to redirect users to a malicious server to steal data or login credentials.

Defense:
- Use encryption and certificate pinning to authenticate endpoints.
- Use DNS security extensions (DNSSEC) to authenticate DNS data.
- Be cautious of unsecured Wi-Fi networks.

3. Phishing & Social Engineering: The attacker tricks users into providing login credentials or sensitive information or downloading malware by impersonating a trustworthy entity.
- Emails with malicious links or attachments
- Fake login pages
- Impersonation over the phone

Defense:
- User education and awareness about such threats.
- Carefully verify the authenticity of requests for sensitive data.
- Use two-factor authentication whenever possible.