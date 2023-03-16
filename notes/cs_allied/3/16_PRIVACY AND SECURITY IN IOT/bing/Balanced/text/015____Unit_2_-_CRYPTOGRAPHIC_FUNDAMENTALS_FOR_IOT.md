## Unit 2 - Cryptographic Fundamentals for IoT

- Cryptography is the science of securing information by transforming it into a form that only the intended recipients can understand.
- Cryptography is essential for IoT devices, which often communicate over wireless networks and store sensitive data on cloud servers or edge devices.
- Cryptography can provide the following security services for IoT devices:
  - Confidentiality: preventing unauthorized access to the information.
  - Integrity: ensuring that the information is not modified or corrupted during transmission or storage.
  - Authentication: verifying the identity of the sender or receiver of the information.
  - Non-repudiation: preventing the sender or receiver from denying their involvement in the communication.
  - Access control: restricting the access to the information based on predefined rules or policies.
- Cryptography can be classified into two main types: symmetric and asymmetric.
  - Symmetric cryptography uses the same key for both encryption and decryption. The key must be shared securely between the communicating parties. Symmetric cryptography is fast and efficient, but it requires a large number of keys for a large network of devices.
  - Asymmetric cryptography uses different keys for encryption and decryption. The encryption key is public and can be shared with anyone, while the decryption key is private and must be kept secret. Asymmetric cryptography is more secure and scalable, but it is slower and more computationally intensive than symmetric cryptography.
- Cryptography can also be classified into two main categories: conventional and quantum.
  - Conventional cryptography relies on mathematical problems that are hard to solve, such as factoring large numbers or finding discrete logarithms. Conventional cryptography is widely used and standardized, but it is vulnerable to attacks by quantum computers, which can solve these problems faster than classical computers.
  - Quantum cryptography relies on the principles of quantum physics, such as superposition, entanglement, and uncertainty. Quantum cryptography can provide unconditional security, which means that no attacker, even with a quantum computer, can break the encryption. Quantum cryptography is still in its infancy and faces many challenges, such as high cost, low speed, and limited distance.