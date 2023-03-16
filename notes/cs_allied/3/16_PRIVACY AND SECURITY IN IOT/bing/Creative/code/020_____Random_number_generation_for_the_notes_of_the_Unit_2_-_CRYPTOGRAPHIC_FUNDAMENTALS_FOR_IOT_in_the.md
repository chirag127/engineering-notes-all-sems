### Random number generation for the notes of the Unit 2 - CRYPTOGRAPHIC FUNDAMENTALS FOR IOT in the subject of PRIVACY AND SECURITY IN IOT

- Random number generation is a process by which, a sequence of numbers or symbols that cannot be reasonably predicted better than by a random chance, is produced.
- Random numbers are essential for cryptography, as they are used for generating keys, challenges, nonces, padding bits, and initialization vectors in cryptographic algorithms and protocols.
- However, generating true random numbers is difficult, especially on a finite state machine such as a computer, which follows deterministic rules.
- Therefore, cryptographic applications typically use algorithmic techniques for random number generation, which are called pseudo-random number generators (PRNGs).
- PRNGs are deterministic algorithms that produce sequences of numbers that appear to be random, but are actually derived from a secret seed value.
- PRNGs must satisfy two main properties to be considered cryptographically secure:
  - Unpredictability: Given any part of the sequence, it should be computationally infeasible to predict the next number or the seed value.
  - Non-repeatability: The same sequence should not be generated again, even if the PRNG is reinitialized with the same seed value.
- Some examples of PRNGs are linear congruential generators, linear feedback shift registers, Blum-Blum-Shub, and Yarrow.
- Some sources of randomness that can be used to generate seed values for PRNGs are physical phenomena, such as atmospheric noise, thermal noise, radioactive decay, or quantum effects. These are called physical random number generators (PRNGs).
- PRNGs are usually slower and more expensive than PRNGs, but they can provide true randomness that is not dependent on any algorithm or assumption.