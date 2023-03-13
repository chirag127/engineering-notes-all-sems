### Introduction to security attacks

- A security attack is a method used by hackers to target cryptographic solutions like ciphertext, encryption keys, etc. These attacks aim to retrieve the plaintext from the ciphertext or decode the encrypted data.
- A security attack goal is to compromise one or more of the five major security requirements: Confidentiality, Availability, Authentication, Integrity, and Nonrepudiation.
- Depending on the type of cryptographic system in place and the information available to the attacker, these attacks can be broadly classified into six types:
  - Brute force attack: The attacker tries all possible combinations of the secret key until the correct one is found.
  - Ciphertext-only attack: The attacker gains access to a collection of ciphertext and tries to infer the plaintext or the key.
  - Chosen plaintext attack: The attacker chooses some plaintext and obtains the corresponding ciphertext, and then tries to find the key or the algorithm.
  - Chosen ciphertext attack: The attacker chooses some ciphertext and obtains the corresponding plaintext, and then tries to find the key or the algorithm.
  - Known plaintext attack: The attacker knows some pairs of plaintext and ciphertext and tries to find the key or the algorithm.
  - Key and algorithm attack: The attacker knows or guesses the algorithm and tries to find the key or a weakness in the algorithm.
- To prevent or resist these attacks, cryptographic systems should use strong encryption algorithms, secure key generation and distribution methods, and proper implementation and testing of the systems.