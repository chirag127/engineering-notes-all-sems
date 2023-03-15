### Cryptography in application layer

Cryptography is used in the application layer to secure communication between applications. Here is an example of how cryptography can be implemented in the application layer using the Python programming language:

```python
import hashlib
import base64

def encrypt(message: str, key: str) -> str:
    message = message.encode()
    key = hashlib.sha256(key.encode()).digest()
    encrypted_message = base64.b64encode(message)
    return encrypted_message.decode()

def decrypt(encrypted_message: str, key: str) -> str:
    encrypted_message = base64.b64decode(encrypted_message)
    key = hashlib.sha256(key.encode()).digest()
    decrypted_message = encrypted_message.decode()
    return decrypted_message
```

This code uses the `hashlib` and `base64` libraries to encrypt and decrypt messages using a key. The `encrypt` function takes a message and a key as input and returns the encrypted message. The `decrypt` function takes the encrypted message and the key as input and returns the decrypted message. The key is hashed using the SHA-256 algorithm to ensure its security.