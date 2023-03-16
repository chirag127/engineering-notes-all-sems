### Random number generation for the notes of the Unit 2 - CRYPTOGRAPHIC FUNDAMENTALS FOR IOT in the subject of PRIVACY AND SECURITY IN IOT

- Random number generation is a process by which, a sequence of numbers or symbols that cannot be reasonably predicted better than by a random chance, is produced.
- Random numbers are essential for cryptography, as they are used for various purposes such as generating keys, challenges, nonces, padding bits, and initialization vectors.
- However, generating true random numbers is difficult, especially on a finite state machine such as a computer, which follows deterministic rules.
- Therefore, cryptographic applications typically use algorithmic techniques for random number generation, which are also called pseudo-random number generators (PRNGs).
- PRNGs are deterministic algorithms that produce sequences of numbers that are not statistically random, but appear to be random for practical purposes.
- A good PRNG should satisfy two main properties: unpredictability and uniformity.
- Unpredictability means that it is computationally infeasible to guess the next output of the PRNG given its previous outputs, or to distinguish the output from a truly random sequence.
- Uniformity means that the output of the PRNG follows a uniform distribution, where each possible value has an equal probability of occurring.
- A PRNG that satisfies these properties is called a cryptographically secure PRNG (CSPRNG).
- A CSPRNG is a PRNG that can withstand serious attacks from an adversary who has access to some or all of its outputs, and who tries to recover its internal state or predict its future outputs.
- A CSPRNG can be constructed from various cryptographic primitives, such as block ciphers, hash functions, stream ciphers, or digital signatures.
- A CSPRNG should also be periodically reseeded with fresh entropy, which is a measure of the randomness or unpredictability of a source of data.
- Entropy can be obtained from various physical or environmental sources, such as user input, mouse movements, keyboard timings, disk access timings, network traffic, or hardware devices that exploit quantum phenomena  .
- A physical random number generator (PRNG) is a device that produces random numbers based on a physical process that is inherently random, such as radioactive decay, thermal noise, or quantum tunneling.
- A PRNG can provide true randomness, but it may be too slow, expensive, or unreliable for some applications.
- Therefore, a hybrid approach that combines a PRNG and a CSPRNG is often used, where the PRNG provides entropy to the CSPRNG, and the CSPRNG produces fast and secure random numbers.