### Random number generation

- Random number generation is a process by which a sequence of numbers or symbols that cannot be reasonably predicted better than by random chance is generated.
- Random numbers are useful for many applications, such as cryptography, simulation, gaming, statistical sampling, and scientific experiments.
- There are two main types of random number generators: hardware-based and pseudo-random.
- Hardware-based random number generators use physical devices or phenomena, such as dice, coins, quantum effects, or radioactive decay, to produce random outcomes .
- Pseudo-random number generators use mathematical algorithms or functions, such as linear congruential generators, Mersenne Twister, or Blum Blum Shub, to produce sequences of numbers that appear random but are actually deterministic and reproducible .
- Pseudo-random number generators have advantages over hardware-based ones, such as speed, portability, and scalability, but they also have limitations, such as periodicity, correlation, and predictability .
- Pseudo-random number generators require an initial value or seed to start the sequence, which can be chosen randomly or based on some external input .
- The quality of a pseudo-random number generator can be measured by various statistical tests, such as frequency, runs, autocorrelation, or chi-square tests, that check how well the generated sequence matches the expected properties of a true random sequence .
- Some applications require true random numbers, which can be obtained from hardware-based generators or online services, such as RANDOM.ORG, that use atmospheric noise or other sources of randomness to generate numbers.
- Some applications require cryptographically secure random numbers, which can be obtained from hardware-based generators or special pseudo-random number generators, such as Yarrow, Fortuna, or NIST SP 800-90A, that use cryptographic techniques to ensure the unpredictability and secrecy of the generated numbers .